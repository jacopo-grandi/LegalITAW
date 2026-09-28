"""Application services for the stable ``legalita-v2`` workflow CLI."""

from __future__ import annotations

import base64
import hashlib
import json
import re
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence

from legalitaw.benchmark.agentic_run import (
    estimate_batched_single_cost,
    estimate_paired_consensus_cost,
    estimate_targeted_audit_cost,
    materialize_run_source,
)
from legalitaw.evaluation.agentic_run import aggregate_agentic_run
from legalitaw.agentic.models import LoadedWorkflowTask, WorkflowSubmission
from legalitaw.agentic.submissions import (
    SUPPORTED_EXTERNAL_ARTIFACT_SUFFIXES,
    import_submission,
)
from legalitaw.artifacts import write_json_atomic
from legalitaw.config import AGENTIC_RESULTS_DIR, JudgeRuntimeConfig
from legalitaw.modeling.runtime import is_non_retryable_model_error


RUN_MANIFEST_SCHEMA = "legalita_v2_run_manifest_v1"
SCORE_MANIFEST_SCHEMA = "legalita_v2_score_manifest_v1"
PREFLIGHT_SCHEMA = "legalita_v2_preflight_v1"
CHECKPOINT_SCHEMA = "legalita_v2_score_checkpoint_v1"
EVALUATION_CONTRACT = "legalita_v2_evaluation_v1"
TASK_ID_PATTERN = re.compile(r"^(WF2-\d{3})(?:_.+)?$")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _timestamp_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")


def _safe_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-") or "unknown"


def _failure_is_non_retryable(exc: BaseException) -> bool:
    """Inspect wrapped provider failures without depending on one SDK."""
    seen: set[int] = set()
    current: BaseException | None = exc
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        if isinstance(current, Exception) and is_non_retryable_model_error(current):
            return True
        current = current.__cause__ or current.__context__
    return False


def _json_sha256(value: Any) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"oggetto JSON atteso in {path}")
    return payload


def _parse_timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def submission_sha256(submission: WorkflowSubmission) -> str:
    """Hash only the work product, independent of directory and provenance."""
    artifacts: dict[str, str] = {}
    for artifact in submission.artifacts:
        raw = (
            base64.b64decode(artifact.binary_base64, validate=True)
            if artifact.binary_base64 is not None
            else artifact.content.encode("utf-8")
        )
        artifacts[artifact.path] = hashlib.sha256(raw).hexdigest()
    return _json_sha256({"task_id": submission.task_id, "artifacts": artifacts})


@dataclass
class ResolvedAttempt:
    task_id: str
    directory: Path
    status: str
    created_at: str | None
    timestamp: datetime | None
    has_submission_json: bool
    submission: WorkflowSubmission | None = None
    submission_sha256: str | None = None
    manifest: dict[str, Any] = field(default_factory=dict)
    failure: dict[str, Any] | None = None
    error: str | None = None

    def relative_payload(self, root: Path) -> dict[str, Any]:
        try:
            directory = self.directory.relative_to(root).as_posix()
        except ValueError:
            directory = str(self.directory)
        return {
            "task_id": self.task_id,
            "directory": directory or ".",
            "status": self.status,
            "created_at": self.created_at,
            "has_submission_json": self.has_submission_json,
            "submission_sha256": self.submission_sha256,
            "error": self.error,
        }


@dataclass
class ResolvedRun:
    root: Path
    source_metadata: dict[str, Any]
    run_manifest: dict[str, Any] | None
    attempts: dict[str, list[ResolvedAttempt]]
    selected: dict[str, ResolvedAttempt]
    decisions: dict[str, str]
    requested_task_ids: list[str] | None
    model: str

    @property
    def completed_task_ids(self) -> list[str]:
        return sorted(
            task_id
            for task_id, attempt in self.selected.items()
            if attempt.status == "completed" and attempt.submission is not None
        )

    @property
    def failed_task_ids(self) -> list[str]:
        return sorted(
            task_id
            for task_id, attempt in self.selected.items()
            if attempt.status == "failed"
        )

    @property
    def submissions(self) -> dict[str, WorkflowSubmission]:
        return {
            task_id: attempt.submission
            for task_id, attempt in self.selected.items()
            if attempt.status == "completed" and attempt.submission is not None
        }


def _candidate_directories(root: Path) -> list[Path]:
    candidates: set[Path] = set()
    for marker in ("submission.json", "failure.json", "run_manifest.json"):
        candidates.update(path.parent for path in root.rglob(marker))
    for directory in [root, *(path for path in root.rglob("*") if path.is_dir())]:
        if not TASK_ID_PATTERN.fullmatch(directory.name):
            continue
        if any(
            path.is_file()
            and path.suffix.casefold() in SUPPORTED_EXTERNAL_ARTIFACT_SUFFIXES
            for path in directory.rglob("*")
        ):
            candidates.add(directory)
    return sorted(candidates, key=lambda item: item.as_posix())


def _task_id_from_directory(directory: Path) -> str | None:
    match = TASK_ID_PATTERN.fullmatch(directory.name)
    return match.group(1) if match else None


def _load_attempt(
    directory: Path,
    *,
    tasks: Mapping[str, LoadedWorkflowTask],
    default_model: str,
) -> ResolvedAttempt | None:
    manifest_path = directory / "run_manifest.json"
    submission_path = directory / "submission.json"
    failure_path = directory / "failure.json"
    manifest: dict[str, Any] = {}
    failure: dict[str, Any] | None = None
    submission_task_id: str | None = None
    manifest_error: str | None = None

    if manifest_path.is_file():
        try:
            manifest = _read_object(manifest_path)
        except Exception as exc:
            manifest_error = f"run_manifest.json non valido: {exc}"
    if manifest.get("schema_version") == RUN_MANIFEST_SCHEMA:
        return None
    if failure_path.is_file():
        try:
            failure = _read_object(failure_path)
        except Exception as exc:
            failure = {"error": f"failure.json non valido: {exc}"}
    if submission_path.is_file():
        try:
            raw_submission = _read_object(submission_path)
            value = raw_submission.get("task_id")
            submission_task_id = str(value) if value else None
        except Exception:
            pass

    ids = {
        value
        for value in (
            str(manifest.get("task_id")) if manifest.get("task_id") else None,
            submission_task_id,
            _task_id_from_directory(directory),
        )
        if value
    }
    if not ids:
        return None
    if len(ids) != 1:
        raise ValueError(
            f"task_id incoerenti in {directory}: {', '.join(sorted(ids))}"
        )
    task_id = ids.pop()
    if task_id not in tasks:
        return None

    created_at = manifest.get("created_at")
    if created_at is None and failure is not None:
        created_at = failure.get("created_at")
    status = str(manifest.get("run_status") or "").strip().lower()
    if not status:
        status = "completed" if submission_path.is_file() else "failed" if failure else "candidate"

    attempt = ResolvedAttempt(
        task_id=task_id,
        directory=directory,
        status=status,
        created_at=str(created_at) if created_at else None,
        timestamp=_parse_timestamp(created_at),
        has_submission_json=submission_path.is_file(),
        manifest=manifest,
        failure=failure,
        error=manifest_error,
    )
    if status == "failed":
        return attempt

    try:
        source = submission_path if submission_path.is_file() else directory
        attempt.submission = import_submission(
            tasks[task_id],
            source=source,
            model=str(manifest.get("model") or default_model),
        )
        attempt.status = "completed"
        if submission_path.is_file():
            attempt.created_at = attempt.created_at or attempt.submission.created_at
        attempt.timestamp = attempt.timestamp or _parse_timestamp(attempt.created_at)
        attempt.submission_sha256 = submission_sha256(attempt.submission)
    except Exception as exc:
        attempt.status = "invalid"
        attempt.error = f"{type(exc).__name__}: {exc}"
    return attempt


def _select_attempt(task_id: str, attempts: Sequence[ResolvedAttempt]) -> tuple[ResolvedAttempt, str]:
    completed = [item for item in attempts if item.status == "completed"]
    pool = completed or [item for item in attempts if item.status == "failed"]
    if not pool:
        errors = "; ".join(item.error or item.status for item in attempts)
        raise ValueError(f"{task_id}: nessun tentativo utilizzabile ({errors})")

    reason_parts: list[str] = []
    if completed and len(completed) != len(attempts):
        reason_parts.append("completed prevale su failed/invalid")
    if len(pool) > 1:
        dated = [item for item in pool if item.timestamp is not None]
        if dated:
            newest = max(item.timestamp for item in dated)
            pool = [item for item in dated if item.timestamp == newest]
            reason_parts.append("selezionato il tentativo più recente")
    if len(pool) > 1:
        explicit = [item for item in pool if item.has_submission_json]
        if explicit:
            pool = explicit
            reason_parts.append("submission.json valido prevale sull'inferenza")
    if len(pool) != 1:
        locations = ", ".join(str(item.directory) for item in pool)
        raise ValueError(f"{task_id}: tentativi indistinguibili: {locations}")
    if not reason_parts:
        reason_parts.append("unico tentativo utilizzabile")
    return pool[0], "; ".join(reason_parts)


def _find_v2_manifest(root: Path) -> dict[str, Any] | None:
    manifests: list[dict[str, Any]] = []
    for path in root.rglob("run_manifest.json"):
        try:
            payload = _read_object(path)
        except Exception:
            continue
        if payload.get("schema_version") == RUN_MANIFEST_SCHEMA:
            manifests.append(payload)
    if len(manifests) > 1:
        raise ValueError("più manifest legalita_v2_run_manifest_v1 nella sorgente")
    return manifests[0] if manifests else None


def resolve_run_directory(
    root: Path,
    *,
    tasks: Sequence[LoadedWorkflowTask],
    source_metadata: dict[str, Any],
    model: str | None = None,
) -> ResolvedRun:
    by_id = {task.spec.task_id: task for task in tasks}
    run_manifest = _find_v2_manifest(root)
    default_model = str(
        model
        or (run_manifest or {}).get("model")
        or Path(str(source_metadata.get("source") or root.name)).stem
        or "external"
    )
    attempts: dict[str, list[ResolvedAttempt]] = {}
    for directory in _candidate_directories(root):
        attempt = _load_attempt(
            directory,
            tasks=by_id,
            default_model=default_model,
        )
        if attempt is not None:
            attempts.setdefault(attempt.task_id, []).append(attempt)

    if not attempts:
        raise ValueError("nessuna submission o tentativo WF2 trovato nella sorgente")
    selected: dict[str, ResolvedAttempt] = {}
    decisions: dict[str, str] = {}
    for task_id, items in sorted(attempts.items()):
        selected[task_id], decisions[task_id] = _select_attempt(task_id, items)

    requested: list[str] | None = None
    if run_manifest is not None:
        raw_requested = run_manifest.get("requested_task_ids")
        if not isinstance(raw_requested, list) or not raw_requested:
            raise ValueError("manifest v2 senza requested_task_ids validi")
        requested = [str(item) for item in raw_requested]
        if len(requested) != len(set(requested)):
            raise ValueError("requested_task_ids contiene duplicati")
        unknown = sorted(set(requested) - set(by_id))
        if unknown:
            raise ValueError(f"manifest v2 riferisce task sconosciuti: {unknown}")

    selected_models = {
        item.submission.model
        for item in selected.values()
        if item.submission is not None
    }
    inferred_model = default_model
    if model is None and run_manifest is None and len(selected_models) == 1:
        inferred_model = next(iter(selected_models))
    return ResolvedRun(
        root=root,
        source_metadata=source_metadata,
        run_manifest=run_manifest,
        attempts=attempts,
        selected=selected,
        decisions=decisions,
        requested_task_ids=requested,
        model=inferred_model,
    )


@contextmanager
def resolved_run_source(
    source: Path,
    *,
    tasks: Sequence[LoadedWorkflowTask],
    model: str | None = None,
) -> Iterator[ResolvedRun]:
    with materialize_run_source(source) as (root, source_metadata):
        yield resolve_run_directory(
            root,
            tasks=tasks,
            source_metadata=source_metadata,
            model=model,
        )


def _preflight_payload(resolved: ResolvedRun) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for task_id, attempts in sorted(resolved.attempts.items()):
        selected = resolved.selected[task_id]
        rows.append(
            {
                "task_id": task_id,
                "status": selected.status,
                "selected": selected.relative_payload(resolved.root),
                "attempt_count": len(attempts),
                "decision": resolved.decisions[task_id],
                "attempts": [item.relative_payload(resolved.root) for item in attempts],
            }
        )
    return {
        "schema_version": PREFLIGHT_SCHEMA,
        "source": resolved.source_metadata,
        "manifest_present": resolved.run_manifest is not None,
        "model": resolved.model,
        "discovered_task_count": len(rows),
        "completed_submission_count": len(resolved.completed_task_ids),
        "failed_generation_count": len(resolved.failed_task_ids),
        "tasks": rows,
    }


from legalitaw.evaluation.agentic import judge_context_mode  # noqa: E402


def _judge_payload(config: JudgeRuntimeConfig) -> dict[str, Any]:
    reviewer = (
        config.judge_b.__dict__
        if config.strategy in {"targeted_audit", "adaptive_majority", "paired_consensus"}
        else None
    )
    return {
        "strategy": config.strategy,
        "primary": config.judge_a.__dict__,
        "reviewer": reviewer,
        "tie_breaker": (
            config.judge_c.__dict__
            if config.strategy in {"adaptive_majority", "paired_consensus"}
            else None
        ),
        "batch_size": config.batch_size,
        "audit_sample_rate": (
            config.audit_sample_rate
            if config.strategy in {"targeted_audit", "paired_consensus"}
            else 0.0
        ),
        # Presente solo fuori dal default, cosi' i checkpoint gia' scritti con
        # il contesto completo restano validi.
        **(
            {"judge_context": judge_context_mode()}
            if judge_context_mode() != "full"
            else {}
        ),
    }


def _checkpoint_key(
    task: LoadedWorkflowTask,
    attempt: ResolvedAttempt,
    config: JudgeRuntimeConfig,
) -> dict[str, Any]:
    return {
        "schema_version": CHECKPOINT_SCHEMA,
        "submission_sha256": attempt.submission_sha256,
        "rubric_version": task.rubric.rubric_version,
        "rubric_sha256": _file_sha256(task.rubric_path),
        "methodology_version": task.spec.methodology_version,
        "judge": _judge_payload(config),
        "evaluation_contract": EVALUATION_CONTRACT,
    }


def _load_checkpoint(
    path: Path,
    *,
    task_id: str,
    expected_fingerprint: str,
) -> tuple[dict[str, Any] | None, str]:
    if not path.is_file():
        return None, "missing"
    try:
        payload = _read_object(path)
    except Exception as exc:
        return None, f"invalid_json:{type(exc).__name__}"
    if payload.get("task_id") != task_id:
        return None, "task_id_changed"
    checkpoint = payload.get("_checkpoint")
    if not isinstance(checkpoint, dict):
        return None, "checkpoint_metadata_missing"
    if checkpoint.get("fingerprint") != expected_fingerprint:
        return None, "fingerprint_changed"
    if _has_judge_errors(payload):
        # un giudice non ha risposto (credito, rete, output illeggibile): il task va rigiudicato,
        # altrimenti i criteri decisi senza quel voto restano nello score per sempre
        return None, "judge_errors"
    return payload, "reusable"


def _has_judge_errors(payload: dict[str, Any]) -> bool:
    for criterion in payload.get("criteria_results") or []:
        for vote in criterion.get("judge_votes") or []:
            if vote.get("status") not in (None, "ok"):
                return True
    return False


def default_v2_score_dir(source: Path) -> Path:
    identity = hashlib.sha256(str(source.resolve()).encode("utf-8")).hexdigest()[:10]
    stem = _safe_component(source.stem if source.is_file() else source.name)
    return AGENTIC_RESULTS_DIR / "v2-scores" / f"{stem}-{identity}"


def _summary(
    scores: list[dict[str, Any]],
    failures: dict[str, Any],
    expected_task_ids: list[str],
    *,
    model: str,
    denominator_source: str,
    partial: bool,
    run_status: str,
    completed_submission_count: int,
) -> dict[str, Any]:
    return {
        "schema_version": "legalita_v2_score_summary_v1",
        "model": model,
        "run_status": run_status,
        "partial": partial,
        "denominator_source": denominator_source,
        "completed_submission_count": completed_submission_count,
        "updated_at": _utc_now(),
        **aggregate_agentic_run(
            scores,
            expected_task_ids=expected_task_ids,
            technical_failures=failures,
        ),
        "judge_usage": _judge_usage(scores),
    }


def _judge_usage(scores: list[dict[str, Any]]) -> dict[str, Any]:
    """Somma dei token e del costo stimato dei giudici, dai diagnostici salvati per task.

    I task giudicati prima del 28 set 2026 non hanno il dato: sono contati in tasks_without_usage.
    """
    from legalitaw.benchmark.agentic_run import JUDGE_TOKEN_PRICES_USD_PER_MTOK as prices

    totals: dict[str, dict[str, Any]] = {}
    without = 0
    for score in scores:
        usage = ((score.get("judge_diagnostics") or {}).get("targeted_audit") or {}).get("usage")
        if not usage:
            without += 1
            continue
        for judge_id, item in usage.items():
            slot = totals.setdefault(judge_id, {"model": item.get("model"), "calls": 0, "input_tokens": 0,
                                                "cached_input_tokens": 0, "output_tokens": 0,
                                                "estimated_cost_usd": 0.0})
            for key in ("calls", "input_tokens", "cached_input_tokens", "output_tokens"):
                slot[key] += int(item.get(key) or 0)
            price = prices.get(item.get("model") or "")
            if price:  # input in cache stimato al 10% del prezzo pieno
                slot["estimated_cost_usd"] = round(slot["estimated_cost_usd"] + (
                    int(item.get("input_tokens") or 0) * price[0]
                    + int(item.get("cached_input_tokens") or 0) * price[0] * 0.1
                    + int(item.get("output_tokens") or 0) * price[1]) / 1_000_000, 6)
    return {
        "per_judge": totals,
        "estimated_cost_usd": round(sum(v["estimated_cost_usd"] for v in totals.values()), 4),
        "tasks_with_usage": len(scores) - without,
        "tasks_without_usage": without,
    }


def score_v2_source(
    source: Path,
    *,
    tasks: Sequence[LoadedWorkflowTask],
    runtime_config: JudgeRuntimeConfig,
    model: str | None = None,
    out_dir: Path | None = None,
    expected_all: bool = False,
    completed_only: bool = False,
    fresh: bool = False,
    preflight_only: bool = False,
    max_estimated_judge_cost_usd: float = 75.0,
    allow_estimated_cost_overrun: bool = False,
    fail_fast: bool = False,
    create_judge_fn: Any = None,
    evaluate_submission_fn: Any = None,
    evaluation_payload_fn: Any = None,
) -> dict[str, Any]:
    """Resolve, preflight, checkpoint and score any supported run source."""
    if expected_all and completed_only:
        raise ValueError("--expected all e --completed-only sono incompatibili")
    task_by_id = {task.spec.task_id: task for task in tasks}
    with resolved_run_source(source, tasks=tasks, model=model) as resolved:
        if expected_all:
            expected_ids = [task.spec.task_id for task in tasks]
            denominator_source = "corpus_all"
            partial = False
        elif completed_only:
            expected_ids = resolved.completed_task_ids
            denominator_source = "completed_only"
            partial = True
        elif resolved.requested_task_ids is not None:
            expected_ids = list(resolved.requested_task_ids)
            denominator_source = "run_manifest"
            partial = False
        else:
            expected_ids = sorted(resolved.selected)
            denominator_source = "discovered_inferred"
            partial = True
        if not expected_ids:
            raise ValueError("nessun task nel denominatore dello scoring")

        base_out = out_dir or default_v2_score_dir(source)
        score_out = base_out / _timestamp_id() if fresh else base_out
        score_out.mkdir(parents=True, exist_ok=True)
        scores_dir = score_out / "scores"
        errors_dir = score_out / "errors"

        judge_payload = _judge_payload(runtime_config)
        preflight = _preflight_payload(resolved)
        preflight.update(
            {
                "expected_task_ids": expected_ids,
                "denominator_source": denominator_source,
                "partial": partial,
                "judge": judge_payload,
            }
        )

        ready_tasks: list[LoadedWorkflowTask] = []
        submissions: dict[str, WorkflowSubmission] = {}
        reusable_scores: dict[str, dict[str, Any]] = {}
        checkpoint_states: dict[str, str] = {}
        checkpoint_keys: dict[str, dict[str, Any]] = {}
        for task_id in expected_ids:
            attempt = resolved.selected.get(task_id)
            if attempt is None or attempt.submission is None:
                continue
            task = task_by_id[task_id]
            ready_tasks.append(task)
            submissions[task_id] = attempt.submission
            key = _checkpoint_key(task, attempt, runtime_config)
            checkpoint_keys[task_id] = key
            fingerprint = _json_sha256(key)
            if fresh:
                checkpoint_states[task_id] = "fresh_requested"
                continue
            payload, state = _load_checkpoint(
                scores_dir / f"{task_id}.json",
                task_id=task_id,
                expected_fingerprint=fingerprint,
            )
            checkpoint_states[task_id] = state
            if payload is not None:
                reusable_scores[task_id] = payload
        preflight["checkpoints"] = {
            "reusable_count": len(reusable_scores),
            "states": checkpoint_states,
        }
        write_json_atomic(score_out / "preflight.json", preflight)

        pending_ids = [
            task.spec.task_id
            for task in ready_tasks
            if task.spec.task_id not in reusable_scores
        ]
        pending_tasks = [task_by_id[task_id] for task_id in pending_ids]
        pending_submissions = {
            task_id: submissions[task_id] for task_id in pending_ids
        }
        if runtime_config.strategy == "targeted_audit":
            cost_estimate = estimate_targeted_audit_cost(
                pending_tasks,
                model=resolved.model,
                primary_model=runtime_config.judge_a.model,
                reviewer_model=runtime_config.judge_b.model,
                batch_size=runtime_config.batch_size,
                audit_sample_rate=runtime_config.audit_sample_rate,
                submissions=pending_submissions,
            )
        elif runtime_config.strategy == "paired_consensus":
            cost_estimate = estimate_paired_consensus_cost(
                pending_tasks,
                model=resolved.model,
                judge_a_model=runtime_config.judge_a.model,
                judge_b_model=runtime_config.judge_b.model,
                judge_c_model=runtime_config.judge_c.model,
                batch_size=runtime_config.batch_size,
                submissions=pending_submissions,
            )
        elif runtime_config.strategy == "batched_single":
            cost_estimate = estimate_batched_single_cost(
                pending_tasks,
                model=resolved.model,
                primary_model=runtime_config.judge_a.model,
                batch_size=runtime_config.batch_size,
                submissions=pending_submissions,
            )
        else:
            cost_estimate = {
                "schema_version": "judge_cost_estimate_unavailable_v1",
                "strategy": runtime_config.strategy,
                "conservative_maximum_estimated_cost_usd": None,
                "reason": "stima disponibile soltanto per strategie batch",
            }
        write_json_atomic(score_out / "cost_estimate.json", cost_estimate)
        write_json_atomic(
            score_out / "run_manifest.json",
            {
                "schema_version": SCORE_MANIFEST_SCHEMA,
                "created_at": _utc_now(),
                "source": resolved.source_metadata,
                "source_run_id": (resolved.run_manifest or {}).get("run_id"),
                "model": resolved.model,
                "expected_task_ids": expected_ids,
                "denominator_source": denominator_source,
                "partial": partial,
                "judge": judge_payload,
                "cost_guard_usd": max_estimated_judge_cost_usd,
                "reviewer_enabled": judge_payload["reviewer"] is not None,
            },
        )
        if preflight_only:
            return {
                "out_dir": str(score_out),
                "preflight": preflight,
                "cost_estimate": cost_estimate,
            }

        ceiling = cost_estimate.get("conservative_maximum_estimated_cost_usd")
        if (
            isinstance(ceiling, (int, float))
            and ceiling > max_estimated_judge_cost_usd
            and not allow_estimated_cost_overrun
        ):
            raise RuntimeError(
                f"cost guard: stima ${ceiling:.2f} > soglia "
                f"${max_estimated_judge_cost_usd:.2f}"
            )

        if create_judge_fn is None or evaluate_submission_fn is None or evaluation_payload_fn is None:
            from legalitaw.benchmark.agentic_service import create_judge as create_judge_fn
            from legalitaw.evaluation.agentic import evaluate_submission as evaluate_submission_fn
            from legalitaw.evaluation.agentic import evaluation_payload as evaluation_payload_fn

        judge = create_judge_fn(runtime_config) if pending_ids else None
        scores = list(reusable_scores.values())
        failures: dict[str, Any] = {}
        for task_id in expected_ids:
            attempt = resolved.selected.get(task_id)
            if attempt is not None and attempt.status == "failed":
                failures[task_id] = {
                    "task_id": task_id,
                    "stage": "generation",
                    "error": (attempt.failure or {}).get("message") or "generazione fallita",
                }
                write_json_atomic(
                    errors_dir / f"{task_id}.json",
                    failures[task_id],
                )

        for task_id in pending_ids:
            task = task_by_id[task_id]
            score_path = scores_dir / f"{task_id}.json"
            error_path = errors_dir / f"{task_id}.json"
            try:
                score = evaluate_submission_fn(task, submissions[task_id], judge=judge)
                payload = evaluation_payload_fn(score)
                key = checkpoint_keys[task_id]
                payload["_checkpoint"] = {
                    "schema_version": CHECKPOINT_SCHEMA,
                    "fingerprint": _json_sha256(key),
                    "key": key,
                }
                write_json_atomic(score_path, payload)
                error_path.unlink(missing_ok=True)
                scores.append(payload)
            except Exception as exc:
                from legalitaw.evaluation.judge import JudgeProviderFatalError

                failure = {
                    "task_id": task_id,
                    "stage": "scoring",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
                fatal = isinstance(exc, JudgeProviderFatalError)
                failures[task_id] = failure
                write_json_atomic(error_path, failure)
                if fail_fast or fatal:
                    write_json_atomic(
                        score_out / "summary.json",
                        _summary(
                            scores,
                            failures,
                            expected_ids,
                            model=resolved.model,
                            denominator_source=denominator_source,
                            partial=partial,
                            run_status="failed",
                            completed_submission_count=len(resolved.completed_task_ids),
                        ),
                    )
                    raise
            write_json_atomic(
                score_out / "summary.json",
                _summary(
                    scores,
                    failures,
                    expected_ids,
                    model=resolved.model,
                    denominator_source=denominator_source,
                    partial=partial,
                    run_status="running",
                    completed_submission_count=len(resolved.completed_task_ids),
                ),
            )

        summary = _summary(
            scores,
            failures,
            expected_ids,
            model=resolved.model,
            denominator_source=denominator_source,
            partial=partial,
            run_status="completed",
            completed_submission_count=len(resolved.completed_task_ids),
        )
        summary["out_dir"] = str(score_out)
        summary["checkpoint_reused_count"] = len(reusable_scores)
        write_json_atomic(score_out / "summary.json", summary)
        return summary


class _UnexpectedFailure(RuntimeError):
    def __init__(self, task: LoadedWorkflowTask, model: str, exc: Exception) -> None:
        super().__init__(str(exc))
        self.task_id = task.spec.task_id
        self.model = model
        self.error_type = type(exc).__name__
        self.artifacts: list[Any] = []
        self.tool_trace: list[dict[str, Any]] = []
        self.agent_transcript: list[dict[str, Any]] = []
        self.decision_log: list[Any] = []
        self.workspace_manifest = {
            "run_status": "failed",
            "private_envelope_mounted": False,
            "shell_available": False,
            "workspace_network_available": False,
            "document_coverage": None,
        }
        self.model_call_metrics: dict[str, Any] = {}
        self.raw_response = None
        self.execution_mode = "generic_agent"
        self.created_at = _utc_now()


def generate_v2_run(
    tasks: Sequence[LoadedWorkflowTask],
    *,
    model: str,
    results_root: Path,
    profile: str = "bare",
    max_steps: int = 150,
    timeout_seconds: int = 3600,
    max_cost_usd: float | None = None,
    max_task_attempts: int = 1,
    generate_submission_fn: Any = None,
    persist_run_fn: Any = None,
    persist_failed_run_fn: Any = None,
) -> Path:
    """Generate one v2 run and maintain its top-level manifest atomically."""
    if not tasks:
        raise ValueError("nessun task selezionato")
    if max_task_attempts < 1:
        raise ValueError("--max-task-attempts deve essere almeno 1")
    if generate_submission_fn is None or persist_run_fn is None or persist_failed_run_fn is None:
        from legalitaw.benchmark.agentic_service import generate_generic_submission
        from legalitaw.benchmark.agentic_service import persist_failed_run, persist_run

        generate_submission_fn = generate_generic_submission
        persist_run_fn = persist_run
        persist_failed_run_fn = persist_failed_run

    run_id = f"{_timestamp_id()}-{_safe_component(model)}"
    run_root = results_root / "v2-runs" / run_id
    attempts_root = run_root / "attempts"
    task_ids = [task.spec.task_id for task in tasks]
    manifest: dict[str, Any] = {
        "schema_version": RUN_MANIFEST_SCHEMA,
        "run_id": run_id,
        "model": model,
        "corpus": "task_workflow2.0",
        "execution_mode": "generic_agent",
        "profile": profile,
        "run_status": "running",
        "created_at": _utc_now(),
        "requested_task_ids": task_ids,
        "completed_task_ids": [],
        "failed_task_ids": [],
        "attempts": {task_id: [] for task_id in task_ids},
    }
    manifest_path = run_root / "run_manifest.json"
    write_json_atomic(manifest_path, manifest)

    completed: set[str] = set()
    failed: set[str] = set()
    try:
        for task in tasks:
            task_id = task.spec.task_id
            for attempt_number in range(1, max_task_attempts + 1):
                caught: Exception | None = None
                try:
                    submission = generate_submission_fn(
                        task,
                        model=model,
                        max_steps=max_steps,
                        timeout_seconds=timeout_seconds,
                        profile=profile,
                        max_cost_usd=max_cost_usd,
                    )
                    directory = persist_run_fn(
                        task,
                        submission,
                        results_root=attempts_root,
                    )
                    completed.add(task_id)
                    failed.discard(task_id)
                except Exception as exc:
                    caught = exc
                    failure = (
                        exc
                        if hasattr(exc, "workspace_manifest")
                        else _UnexpectedFailure(task, model, exc)
                    )
                    directory = persist_failed_run_fn(
                        task,
                        failure,
                        results_root=attempts_root,
                    )
                    failed.add(task_id)
                manifest["attempts"][task_id].append(
                    directory.relative_to(run_root).as_posix()
                )
                manifest["completed_task_ids"] = sorted(completed)
                manifest["failed_task_ids"] = sorted(failed)
                manifest["updated_at"] = _utc_now()
                write_json_atomic(manifest_path, manifest)
                if caught is not None and _failure_is_non_retryable(caught):
                    manifest.update(
                        {
                            "run_status": "aborted",
                            "aborted_at": _utc_now(),
                            "aborted_task_id": task_id,
                            "aborted_error_type": type(caught).__name__,
                            "aborted_reason": str(caught),
                        }
                    )
                    write_json_atomic(manifest_path, manifest)
                    raise caught
                if task_id in completed:
                    break
                if attempt_number == max_task_attempts:
                    break
    except KeyboardInterrupt:
        manifest.update(
            {
                "run_status": "interrupted",
                "interrupted_at": _utc_now(),
                "completed_task_ids": sorted(completed),
                "failed_task_ids": sorted(failed),
            }
        )
        write_json_atomic(manifest_path, manifest)
        raise

    manifest["run_status"] = "completed" if not failed else "completed_with_failures"
    manifest["completed_at"] = _utc_now()
    write_json_atomic(manifest_path, manifest)
    return run_root


__all__ = [
    "ResolvedAttempt",
    "ResolvedRun",
    "default_v2_score_dir",
    "generate_v2_run",
    "resolve_run_directory",
    "resolved_run_source",
    "score_v2_source",
    "submission_sha256",
]
