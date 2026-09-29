"""Batch ingestion and evaluation for external Workflow 2.0 runs."""

from __future__ import annotations

import hashlib
import json
import math
import re
import stat
import tempfile
import zipfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterator, Mapping, Sequence

from legalitaw.evaluation.agentic_run import aggregate_agentic_run
from legalitaw.agentic.models import LoadedWorkflowTask
from legalitaw.agentic.submissions import import_submission
from legalitaw.artifacts import write_json_atomic


TASK_DIRECTORY = re.compile(r"^WF2-\d{3}(?:_.+)?$")
MAX_ARCHIVE_UNCOMPRESSED_BYTES = 2 * 1024 * 1024 * 1024
ESTIMATED_CHARS_PER_TOKEN = 3.5
ESTIMATED_OUTPUT_TOKENS_PER_CRITERION = 400
JUDGE_TOKEN_PRICES_USD_PER_MTOK: dict[str, tuple[float, float]] = {
    "gpt-5.6-luna": (0.20, 1.20),
    "claude-sonnet-4-6": (3.00, 15.00),
    # Listino Anthropic al 25 set 2026 (platform.claude.com/docs/en/about-claude/pricing)
    "claude-opus-5-5": (4.00, 20.00),
    "claude-opus-5": (5.00, 25.00),
    "claude-sonnet-5": (2.00, 10.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    # Novita, fonte di terze parti al 25 set 2026: da verificare sul listino Novita
    "deepseek/deepseek-v4-pro": (1.60, 3.20),
    "deepseek/deepseek-v4-flash": (0.14, 0.28),
    "jev-latest": (0.042, 0.0),
    "jev-1.13.0": (0.042, 0.0),
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-") or "unknown"


def default_external_results_dir(results_root: Path, model: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return results_root / "external-agentic" / _safe_component(model) / timestamp


def _validate_archive(archive: zipfile.ZipFile) -> None:
    total_size = 0
    names: set[str] = set()
    for member in archive.infolist():
        if member.filename in names:
            raise ValueError(f"path duplicato nello ZIP: {member.filename!r}")
        names.add(member.filename)
        relative = PurePosixPath(member.filename)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"path non sicuro nello ZIP: {member.filename!r}")
        mode = member.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise ValueError(f"symlink non ammesso nello ZIP: {member.filename!r}")
        total_size += member.file_size
        if total_size > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
            raise ValueError(
                "ZIP troppo grande dopo decompressione: limite 2 GiB"
            )


def _task_directory_count(directory: Path) -> int:
    return sum(
        1
        for child in directory.iterdir()
        if child.is_dir() and TASK_DIRECTORY.fullmatch(child.name)
    )


def locate_external_run_root(directory: Path) -> Path:
    """Locate the directory whose immediate children are WF2 task folders."""
    candidates = [directory]
    candidates.extend(child for child in directory.iterdir() if child.is_dir())
    ranked = sorted(
        ((_task_directory_count(candidate), candidate) for candidate in candidates),
        key=lambda item: (-item[0], str(item[1])),
    )
    if not ranked or ranked[0][0] == 0:
        raise ValueError("nessuna cartella task WF2 trovata nella submission")
    best_count = ranked[0][0]
    best = [candidate for count, candidate in ranked if count == best_count]
    if len(best) != 1:
        raise ValueError(
            "radice della run ambigua: " + ", ".join(str(item) for item in best)
        )
    return best[0]


@contextmanager
def materialize_run_source(source: Path) -> Iterator[tuple[Path, dict[str, Any]]]:
    """Yield a directory source, safely extracting ZIP archives when needed."""
    source = source.resolve()
    if source.is_dir():
        yield source, {
            "source": str(source),
            "source_type": "directory",
            "source_sha256": None,
        }
        return
    if not source.is_file() or not zipfile.is_zipfile(source):
        raise ValueError("--submission deve essere una directory o un file ZIP valido")

    with tempfile.TemporaryDirectory(prefix="legalita-external-run-") as temporary:
        destination = Path(temporary)
        with zipfile.ZipFile(source) as archive:
            _validate_archive(archive)
            archive.extractall(destination)
        yield destination, {
            "source": str(source),
            "source_type": "zip",
            "source_sha256": _sha256(source),
        }


@contextmanager
def external_run_root(source: Path) -> Iterator[tuple[Path, dict[str, Any]]]:
    """Yield the legacy flat external-run root from a directory or ZIP."""
    with materialize_run_source(source) as (directory, source_manifest):
        yield locate_external_run_root(directory), source_manifest


def task_submission_directory(run_root: Path, task_id: str) -> Path:
    exact = run_root / task_id
    if exact.is_dir():
        return exact
    candidates = sorted(
        child
        for child in run_root.glob(f"{task_id}_*")
        if child.is_dir() and TASK_DIRECTORY.fullmatch(child.name)
    )
    if not candidates:
        return exact
    if len(candidates) > 1:
        raise ValueError(
            f"{task_id}: piu' cartelle candidate: "
            + ", ".join(item.name for item in candidates)
        )
    return candidates[0]


def preflight_external_run(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    run_root: Path,
    model: str,
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for task in tasks:
        task_id = task.spec.task_id
        directory = task_submission_directory(run_root, task_id)
        present = (
            sorted(
                item.relative_to(directory).as_posix()
                for item in directory.rglob("*")
                if item.is_file()
            )
            if directory.is_dir()
            else []
        )
        relative_directory = (
            directory.relative_to(run_root).as_posix()
            if directory.is_relative_to(run_root)
            else directory.name
        )
        try:
            submission = import_submission(task, source=directory, model=model)
        except Exception as exc:
            rows.append(
                {
                    "task_id": task_id,
                    "status": "error",
                    "directory": relative_directory,
                    "present_files": present,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
            continue
        rows.append(
            {
                "task_id": task_id,
                "status": "ready",
                "directory": relative_directory,
                "present_files": present,
                "imported_artifacts": [item.path for item in submission.artifacts],
                "error_type": None,
                "error": None,
            }
        )

    ready = sum(item["status"] == "ready" for item in rows)
    return {
        "schema_version": "external_agentic_preflight_v2",
        "submission_policy": "free_artifacts",
        "task_count": len(rows),
        "ready_count": ready,
        "error_count": len(rows) - ready,
        "all_ready": ready == len(rows),
        "tasks": rows,
    }


def estimate_targeted_audit_cost(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    run_root: Path | None = None,
    model: str,
    primary_model: str,
    reviewer_model: str,
    batch_size: int,
    audit_sample_rate: float,
    submissions: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Conservative pre-run estimate for the batched targeted-audit strategy."""
    from legalitaw.evaluation.agentic import judge_task
    from legalitaw.evaluation.judge import (
        JUDGE_SYSTEM,
        build_batch_judge_prompt,
        build_jev_request_payload,
    )
    from legalitaw.agentic.submissions import submission_text

    try:
        primary_prices = JUDGE_TOKEN_PRICES_USD_PER_MTOK[primary_model]
        reviewer_prices = JUDGE_TOKEN_PRICES_USD_PER_MTOK[reviewer_model]
    except KeyError as exc:
        raise ValueError(
            f"pricing judge non registrato per il cost guard: {exc.args[0]}"
        ) from exc

    primary_input_chars = 0
    primary_calls = 0
    sampled_reviewer_input_chars = 0
    sampled_reviewer_criteria = 0
    sampled_reviewer_calls = 0
    maximum_reviewer_input_chars = 0
    maximum_reviewer_calls = 0
    judge_criteria = 0

    for task in tasks:
        if submissions is not None:
            submission = submissions[task.spec.task_id]
        else:
            if run_root is None:
                raise ValueError("run_root richiesto senza submission risolte")
            directory = task_submission_directory(run_root, task.spec.task_id)
            submission = import_submission(task, source=directory, model=model)
        output = submission_text(submission)
        jt = judge_task(task)
        task_criteria = list(jt.criteria)
        judge_criteria += len(task_criteria)

        def request_chars(judge_model: str, batch: Sequence[Any]) -> int:
            if judge_model.startswith("jev-"):
                payload, _ = build_jev_request_payload(
                    model=judge_model,
                    task_description=jt.query,
                    agent_output=output,
                    criteria=batch,
                    citation_context=None,
                )
                return len(json.dumps(payload, ensure_ascii=False))
            return len(JUDGE_SYSTEM) + len(
                build_batch_judge_prompt(jt.query, output, batch, None)
            )

        for start in range(0, len(task_criteria), batch_size):
            batch = task_criteria[start : start + batch_size]
            primary_input_chars += request_chars(primary_model, batch)
            maximum_reviewer_input_chars += request_chars(reviewer_model, batch)
            primary_calls += 1
            maximum_reviewer_calls += 1

        strata: dict[str, list[Any]] = {}
        for criterion in task_criteria:
            strata.setdefault(criterion.category, []).append(criterion)
        sampled: list[Any] = []
        for items in strata.values():
            count = min(
                len(items),
                max(1, math.ceil(len(items) * audit_sample_rate)),
            ) if audit_sample_rate > 0 else 0
            sampled.extend(items[:count])
        sampled_reviewer_criteria += len(sampled)
        for start in range(0, len(sampled), batch_size):
            batch = sampled[start : start + batch_size]
            sampled_reviewer_input_chars += request_chars(reviewer_model, batch)
            sampled_reviewer_calls += 1

    def tokens(chars: int) -> int:
        return math.ceil(chars / ESTIMATED_CHARS_PER_TOKEN)

    def cost(
        *,
        input_chars: int,
        criteria_count: int,
        prices: tuple[float, float],
    ) -> dict[str, int | float]:
        input_tokens = tokens(input_chars)
        output_tokens = criteria_count * ESTIMATED_OUTPUT_TOKENS_PER_CRITERION
        amount = (
            input_tokens * prices[0] + output_tokens * prices[1]
        ) / 1_000_000
        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "estimated_cost_usd": round(amount, 4),
        }

    primary = cost(
        input_chars=primary_input_chars,
        criteria_count=judge_criteria,
        prices=primary_prices,
    )
    reviewer_sample = cost(
        input_chars=sampled_reviewer_input_chars,
        criteria_count=sampled_reviewer_criteria,
        prices=reviewer_prices,
    )
    reviewer_maximum = cost(
        input_chars=maximum_reviewer_input_chars,
        criteria_count=judge_criteria,
        prices=reviewer_prices,
    )
    minimum = float(primary["estimated_cost_usd"]) + float(
        reviewer_sample["estimated_cost_usd"]
    )
    conservative_maximum = float(primary["estimated_cost_usd"]) + float(
        reviewer_maximum["estimated_cost_usd"]
    )
    return {
        "schema_version": "targeted_audit_cost_estimate_v1",
        "currency": "USD",
        "pricing_as_of": "2026-09-21",
        "estimation_contract": "chars_per_token_plus_fixed_output_allowance",
        "chars_per_token": ESTIMATED_CHARS_PER_TOKEN,
        "output_tokens_per_criterion": ESTIMATED_OUTPUT_TOKENS_PER_CRITERION,
        "judge_criteria": judge_criteria,
        "batch_size": batch_size,
        "audit_sample_rate": audit_sample_rate,
        "primary_model": primary_model,
        "reviewer_model": reviewer_model,
        "primary_api_calls": primary_calls,
        "sample_only_reviewer_api_calls": sampled_reviewer_calls,
        "maximum_reviewer_api_calls": maximum_reviewer_calls,
        "sample_only_estimated_cost_usd": round(minimum, 2),
        "conservative_maximum_estimated_cost_usd": round(
            conservative_maximum,
            2,
        ),
        "retry_ceiling_estimated_cost_usd": round(
            conservative_maximum * 3,
            2,
        ),
        "primary": primary,
        "reviewer_sample_only": reviewer_sample,
        "reviewer_all_criteria": reviewer_maximum,
        "notes": [
            (
                "Il minimo include il campione stratificato ma non le review "
                "obbligatorie attivate da verdetto, evidenza o probabilità, "
                "non note prima della run."
            ),
            "Il massimo conservativo assume che il reviewer riveda tutti i criteri una volta.",
            "Il retry ceiling assume tre tentativi completi ed e un limite teorico, non una previsione.",
        ],
    }


def estimate_batched_single_cost(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    run_root: Path | None = None,
    model: str,
    primary_model: str,
    batch_size: int,
    submissions: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Pre-run estimate for a batched primary judge without reviewer calls."""
    projection = estimate_targeted_audit_cost(
        tasks,
        run_root=run_root,
        model=model,
        primary_model=primary_model,
        reviewer_model=primary_model,
        batch_size=batch_size,
        audit_sample_rate=0.0,
        submissions=submissions,
    )
    primary = projection["primary"]
    estimated_cost = float(primary["estimated_cost_usd"])
    return {
        "schema_version": "batched_single_cost_estimate_v1",
        "currency": projection["currency"],
        "pricing_as_of": projection["pricing_as_of"],
        "estimation_contract": projection["estimation_contract"],
        "chars_per_token": projection["chars_per_token"],
        "output_tokens_per_criterion": projection["output_tokens_per_criterion"],
        "judge_criteria": projection["judge_criteria"],
        "batch_size": batch_size,
        "primary_model": primary_model,
        "primary_api_calls": projection["primary_api_calls"],
        "estimated_cost_usd": round(estimated_cost, 2),
        "conservative_maximum_estimated_cost_usd": round(estimated_cost, 2),
        "retry_ceiling_estimated_cost_usd": round(estimated_cost * 3, 2),
        "primary": primary,
        "notes": [
            "La stima include esclusivamente il judge principale in batch.",
            "Nessuna chiamata a reviewer o tie-breaker viene effettuata.",
            "Il retry ceiling assume tre tentativi completi ed e un limite teorico.",
        ],
    }


def _load_resumable_score(path: Path, task_id: str) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("task_id") != task_id:
        raise ValueError(
            f"score resume {path}: task_id {payload.get('task_id')!r} != {task_id!r}"
        )
    return payload


def _summary_payload(
    scores: list[dict[str, Any]],
    failures: dict[str, Any],
    task_ids: list[str],
    *,
    model: str,
    run_status: str,
) -> dict[str, Any]:
    return {
        "schema_version": "external_agentic_run_summary_v1",
        "model": model,
        "run_status": run_status,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        **aggregate_agentic_run(
            scores,
            expected_task_ids=task_ids,
            technical_failures=failures,
        ),
    }


def evaluate_external_run(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    run_root: Path,
    model: str,
    out_dir: Path,
    judge: Any,
    evaluate_submission_fn: Any,
    evaluation_payload_fn: Any,
    resume: bool = False,
    fail_fast: bool = False,
) -> dict[str, Any]:
    """Evaluate every task, checkpoint scores, and return a 100-task aggregate."""
    out_dir.mkdir(parents=True, exist_ok=True)
    scores_dir = out_dir / "scores"
    errors_dir = out_dir / "errors"
    task_ids = [task.spec.task_id for task in tasks]
    scores: list[dict[str, Any]] = []
    failures: dict[str, Any] = {}

    for task in tasks:
        task_id = task.spec.task_id
        score_path = scores_dir / f"{task_id}.json"
        error_path = errors_dir / f"{task_id}.json"
        if resume and score_path.is_file():
            error_path.unlink(missing_ok=True)
            scores.append(_load_resumable_score(score_path, task_id))
            continue
        if resume and error_path.is_file():
            error_path.unlink()
        try:
            directory = task_submission_directory(run_root, task_id)
            submission = import_submission(task, source=directory, model=model)
            score = evaluate_submission_fn(task, submission, judge=judge)
            payload = evaluation_payload_fn(score)
            write_json_atomic(score_path, payload)
            scores.append(payload)
        except Exception as exc:
            failure = {
                "task_id": task_id,
                "error_type": type(exc).__name__,
                "error": str(exc),
            }
            failures[task_id] = failure
            write_json_atomic(error_path, failure)
            if fail_fast:
                write_json_atomic(
                    out_dir / "summary.json",
                    _summary_payload(
                        scores,
                        failures,
                        task_ids,
                        model=model,
                        run_status="failed",
                    ),
                )
                raise
        write_json_atomic(
            out_dir / "summary.json",
            _summary_payload(
                scores,
                failures,
                task_ids,
                model=model,
                run_status="running",
            ),
        )

    status = "completed" if len(scores) + len(failures) == len(tasks) else "incomplete"
    summary = _summary_payload(
        scores,
        failures,
        task_ids,
        model=model,
        run_status=status,
    )
    write_json_atomic(out_dir / "summary.json", summary)
    return summary


__all__ = [
    "default_external_results_dir",
    "evaluate_external_run",
    "external_run_root",
    "locate_external_run_root",
    "materialize_run_source",
    "preflight_external_run",
    "task_submission_directory",
]


# Quota di criteri attesa per l'arbitro: disaccordi (~15%), citazioni di B non
# ritrovate (~9%), audit (~4%), misurata sulla run Luna del 21 set 2026.
PAIRED_CONSENSUS_EXPECTED_ESCALATION_RATE = 0.30


def estimate_paired_consensus_cost(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    run_root: Path | None = None,
    model: str,
    judge_a_model: str,
    judge_b_model: str,
    judge_c_model: str,
    batch_size: int,
    submissions: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """A e B su tutti i criteri; C su una quota attesa e, nel massimo, su tutti."""
    common = dict(
        run_root=run_root,
        model=model,
        batch_size=batch_size,
        submissions=submissions,
    )
    a = estimate_batched_single_cost(tasks, primary_model=judge_a_model, **common)["primary"]
    b = estimate_batched_single_cost(tasks, primary_model=judge_b_model, **common)["primary"]
    c_all = estimate_batched_single_cost(tasks, primary_model=judge_c_model, **common)
    c = c_all["primary"]
    ab = float(a["estimated_cost_usd"]) + float(b["estimated_cost_usd"])
    c_full = float(c["estimated_cost_usd"])
    expected = ab + c_full * PAIRED_CONSENSUS_EXPECTED_ESCALATION_RATE
    maximum = ab + c_full
    return {
        "schema_version": "paired_consensus_cost_estimate_v1",
        "currency": "USD",
        "pricing_as_of": "2026-09-25",
        "estimation_contract": c_all["estimation_contract"],
        "chars_per_token": c_all["chars_per_token"],
        "output_tokens_per_criterion": c_all["output_tokens_per_criterion"],
        "judge_criteria": c_all["judge_criteria"],
        "batch_size": batch_size,
        "judge_models": {"A": judge_a_model, "B": judge_b_model, "C": judge_c_model},
        "expected_escalation_rate": PAIRED_CONSENSUS_EXPECTED_ESCALATION_RATE,
        "judge_a": a,
        "judge_b": b,
        "judge_c_all_criteria": c,
        "expected_estimated_cost_usd": round(expected, 2),
        "conservative_maximum_estimated_cost_usd": round(maximum, 2),
        "retry_ceiling_estimated_cost_usd": round(maximum * 3, 2),
        "notes": [
            "A e B valutano tutti i criteri; C solo i casi contesi e l'audit.",
            "Il valore atteso usa la quota di escalation misurata sulla run Luna del 21 set 2026.",
            "Il massimo conservativo assume che C valuti tutti i criteri.",
        ],
    }
