"""Stable operational CLI for LegalITA Workflow 2.0."""

from __future__ import annotations

import argparse
import os
import json
from pathlib import Path
from typing import Any, Sequence

from dotenv import load_dotenv

from legalitaw.agentic.generic_agent import validate_generic_agent_runtime
from legalitaw.agentic.loader import select_tasks
from legalitaw.config import (
    AGENTIC_RESULTS_DIR,
    WORKFLOW2_TASKS_DIR,
    build_judge_runtime_config,
)

from .common import add_judge_arguments, configure_logging, judge_overrides


def _add_scoring_arguments(parser: argparse.ArgumentParser) -> None:
    # Senza flag si usa la terna di default (legalitaw.config).
    add_judge_arguments(parser, default_model=None)
    parser.add_argument(
        "--reviewer",
        default=None,
        help="Abilita targeted_audit usando questo reviewer.",
    )
    parser.add_argument(
        "--reviewer-provider",
        choices=("anthropic", "openai", "novita", "gemini", "typesafe"),
        default="anthropic",
    )
    parser.add_argument(
        "--max-estimated-judge-cost-usd",
        type=float,
        default=75.0,
    )
    parser.add_argument("--allow-estimated-cost-overrun", action="store_true")
    parser.add_argument(
        "--judge-context",
        choices=("full", "compact"),
        default=None,
        help=(
            "Contesto dato al judge: compact = solo i file testuali della busta pubblica "
            "(incarico, reference pack, fonti; default), full = fascicolo pubblico completo."
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="legalitaw",
        description="Genera e valuta run LegalITA Workflow 2.0.",
    )
    parser.add_argument("--root", type=Path, default=WORKFLOW2_TASKS_DIR)
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Genera una run interna.")
    run.add_argument("--model", required=True)
    selectors = run.add_mutually_exclusive_group()
    selectors.add_argument("--tasks", nargs="+", default=None)
    selectors.add_argument("--limit", type=int, default=None)
    run.add_argument("--start-at", default=None)
    run.add_argument("--profile", choices=("bare", "production"), default="bare")
    run.add_argument("--score", action="store_true")
    run.add_argument("--results", type=Path, default=AGENTIC_RESULTS_DIR)
    run.add_argument("--max-agent-steps", type=int, default=150)
    run.add_argument("--timeout-seconds", type=int, default=3600)
    run.add_argument("--max-agent-cost-usd", type=float, default=None)
    run.add_argument("--max-task-attempts", type=int, default=1)
    run.add_argument("--score-out", type=Path, default=None)
    run.add_argument(
        "--parallel",
        type=int,
        default=None,
        metavar="N",
        help=(
            "Divide gli incarichi in N blocchi contigui lanciati in parallelo: "
            "un processo, una run e un log per blocco (es. 100 incarichi, N=4 -> 4 x 25)."
        ),
    )
    run.add_argument(
        "--log-dir",
        type=Path,
        default=None,
        help="Con --parallel: cartella dei log b1.log, b2.log... (default <results>/logs/<data-ora>).",
    )
    run.add_argument(
        "--skip-done",
        action="store_true",
        help=(
            "Salta gli incarichi che hanno già un esito (consegnato o fallito) per questo "
            "modello in --results: serve a riprendere una run interrotta."
        ),
    )
    run.add_argument(
        "--progress-every",
        type=int,
        default=60,
        metavar="SECONDI",
        help="Con --parallel: ogni quanto stampare l'avanzamento (default 60).",
    )
    _add_scoring_arguments(run)

    score = subparsers.add_parser(
        "score",
        aliases=["evaluate"],
        help="Valuta una directory, una run interna o uno ZIP.",
    )
    score.add_argument("source", type=Path)
    score.add_argument("--model", default=None)
    denominator = score.add_mutually_exclusive_group()
    denominator.add_argument("--expected", choices=("all",), default=None)
    denominator.add_argument("--completed-only", action="store_true")
    score.add_argument("--fresh", action="store_true")
    score.add_argument("--out", type=Path, default=None)
    score.add_argument("--preflight-only", action="store_true")
    score.add_argument("--fail-fast", action="store_true")
    score.add_argument(
        "--reuse-votes",
        type=Path,
        nargs="+",
        default=None,
        metavar="SCORE_DIR",
        help=(
            "Riusa i voti di Judge A e B già dati in score precedenti sulla stessa submission "
            "(stesso testo, criterio, provider e modello); l'arbitro C giudica sempre dal vivo."
        ),
    )
    score.add_argument(
        "--tie-breaker-scope",
        choices=("full", "disagreements"),
        default=None,
        help="paired_consensus: full (predefinito) o disagreements = arbitro solo su disaccordi e voti non validi.",
    )
    score.add_argument(
        "--reuse-jev-votes",
        type=Path,
        nargs="+",
        default=None,
        metavar="SCORE_DIR",
        help=(
            "Riusa i voti Jev di uno o più score precedenti sulle stesse submission "
            "(stesso testo, criterio e modello Jev); il resto viene giudicato di nuovo."
        ),
    )
    _add_scoring_arguments(score)

    lancia = subparsers.add_parser(
        "lancia",
        help="Lancia un modello su tutti i 100 incarichi, in 4 blocchi paralleli.",
        description=(
            "Scorciatoia per la run standard: ragionamento low, 4 blocchi paralleli, "
            "risultati in <risultati>/<nome>-wf2-100 e log in <risultati>/logs/<data>_<nome>."
        ),
    )
    lancia.add_argument("modello", help="id esatto del modello, es. gemini-4-neon")
    lancia.add_argument(
        "--ragionamento",
        default="low",
        help="Livello di ragionamento (AGENT_REASONING_EFFORT), default low.",
    )
    lancia.add_argument("--blocchi", type=int, default=4, help="Blocchi paralleli, default 4.")
    lancia.add_argument(
        "--nome",
        default=None,
        help="Nome breve della run (es. neon4-low); default <modello>-<ragionamento>.",
    )
    lancia.add_argument(
        "--risultati",
        type=Path,
        default=None,
        help=(
            "Cartella base dei risultati agentici; default LEGALITAW_RESULTS_DIR, "
            "poi ../legal-ITA-main/results/agentic se esiste, poi results/agentic del repo."
        ),
    )
    lancia.add_argument(
        "--riprendi",
        action="store_true",
        help="Rifà solo gli incarichi rimasti senza esito in una run interrotta.",
    )
    return parser


def _default_results_base() -> Path:
    configured = os.environ.get("LEGALITAW_RESULTS_DIR")
    if configured:
        return Path(configured).expanduser()
    sibling = WORKFLOW2_TASKS_DIR.parent.parent / "legal-ITA-main" / "results" / "agentic"
    if sibling.is_dir():
        return sibling
    return AGENTIC_RESULTS_DIR


def _slug(text: str) -> str:
    return "".join(ch if ch.isalnum() or ch in ".-_" else "-" for ch in text).strip("-")


def _lancia_run_argv(args: argparse.Namespace, *, today: str | None = None) -> list[str]:
    """Traduce `lancia` nella `run --parallel` equivalente."""
    import datetime as dt

    base = (args.risultati or _default_results_base()).expanduser()
    name = _slug(args.nome or f"{args.modello}-{args.ragionamento}")
    day = today or dt.date.today().isoformat()
    argv = [
        "--root",
        str(args.root),
        "run",
        "--model",
        args.modello,
        "--parallel",
        str(args.blocchi),
        "--results",
        str(base / f"{name}-wf2-100"),
        "--log-dir",
        str(base / "logs" / f"{day}_{name}"),
    ]
    if args.riprendi:
        argv.append("--skip-done")
    return argv


def _runtime_config(args: argparse.Namespace):
    options = judge_overrides(args)
    strategy = options["judge_strategy"]
    reviewer_model = options["judge_b_model"]
    reviewer_provider = options["judge_b_provider"]
    if args.reviewer:
        strategy = "targeted_audit"
        reviewer_model = args.reviewer
        reviewer_provider = args.reviewer_provider
    return build_judge_runtime_config(
        judge_strategy=strategy,
        judge_a_provider=options["judge_a_provider"],
        judge_a_model=options["judge_a_model"],
        judge_b_provider=reviewer_provider,
        judge_b_model=reviewer_model,
        judge_c_provider=options["judge_c_provider"],
        judge_c_model=options["judge_c_model"],
        legacy_judge_model=options["judge_model"],
        batch_size=options["batch_size"],
        audit_sample_rate=options["audit_sample_rate"],
    )


def _selected_run_tasks(args: argparse.Namespace):
    tasks = select_tasks(args.tasks or ["all"], root=args.root)
    if args.start_at is not None:
        indexes = [
            index
            for index, task in enumerate(tasks)
            if args.start_at in {task.short_id, task.spec.task_id, task.directory.name}
        ]
        if len(indexes) != 1:
            raise ValueError(
                f"--start-at {args.start_at!r}: atteso un match, trovati {len(indexes)}"
            )
        tasks = tasks[indexes[0] :]
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("--limit deve essere almeno 1")
        tasks = tasks[: args.limit]
    if not tasks:
        raise ValueError("nessun task selezionato")
    return tasks


def _run_command(
    args: argparse.Namespace,
    *,
    generate_v2_run_fn: Any,
    score_v2_source_fn: Any,
    validate_runtime_fn: Any = validate_generic_agent_runtime,
    run_parallel_fn: Any = None,
) -> Path:
    tasks = _selected_run_tasks(args)
    if getattr(args, "skip_done", False):
        from .parallel import done_task_ids

        done = done_task_ids(Path(args.results), model=args.model)
        skipped = [task for task in tasks if task.spec.task_id in done]
        tasks = [task for task in tasks if task.spec.task_id not in done]
        print(f"--skip-done: {len(skipped)} incarichi già fatti, {len(tasks)} da fare.")
        if not tasks:
            return Path(args.results)
    for task in tasks:
        validate_runtime_fn(task, profile=args.profile)
    parallel = getattr(args, "parallel", None)
    if parallel is not None:
        if parallel < 1:
            raise ValueError("--parallel deve essere almeno 1")
        if args.score:
            raise ValueError("--score non si usa con --parallel: valuta i blocchi a run finita")
        if run_parallel_fn is None:
            from .parallel import run_parallel as run_parallel_fn
        code = run_parallel_fn(args, tasks)
        if code:
            raise SystemExit(code)
        return Path(args.results)
    run_root = generate_v2_run_fn(
        tasks,
        model=args.model,
        results_root=args.results,
        profile=args.profile,
        max_steps=args.max_agent_steps,
        timeout_seconds=args.timeout_seconds,
        max_cost_usd=args.max_agent_cost_usd,
        max_task_attempts=args.max_task_attempts,
    )
    print(f"run: {run_root}")
    if args.score:
        all_tasks = select_tasks(["all"], root=args.root)
        summary = score_v2_source_fn(
            run_root,
            tasks=all_tasks,
            runtime_config=_runtime_config(args),
            model=args.model,
            out_dir=args.score_out or run_root / "score-run",
            max_estimated_judge_cost_usd=args.max_estimated_judge_cost_usd,
            allow_estimated_cost_overrun=args.allow_estimated_cost_overrun,
        )
        _print_summary(summary)
    return run_root


def _score_command(args: argparse.Namespace, *, score_v2_source_fn: Any) -> dict[str, Any]:
    if getattr(args, "reuse_votes", None):
        from legalitaw.evaluation.judge import VOTE_REPLAY_ENV

        os.environ[VOTE_REPLAY_ENV] = os.pathsep.join(str(path.expanduser()) for path in args.reuse_votes)
    if getattr(args, "tie_breaker_scope", None):
        os.environ["LEGALITA_TIE_BREAKER_SCOPE"] = args.tie_breaker_scope
    if getattr(args, "reuse_jev_votes", None):
        from legalitaw.evaluation.judge import JEV_REPLAY_ENV

        os.environ[JEV_REPLAY_ENV] = os.pathsep.join(str(path.expanduser()) for path in args.reuse_jev_votes)
    tasks = select_tasks(["all"], root=args.root)
    summary = score_v2_source_fn(
        args.source,
        tasks=tasks,
        runtime_config=_runtime_config(args),
        model=args.model,
        out_dir=args.out,
        expected_all=args.expected == "all",
        completed_only=args.completed_only,
        fresh=args.fresh,
        preflight_only=args.preflight_only,
        max_estimated_judge_cost_usd=args.max_estimated_judge_cost_usd,
        allow_estimated_cost_overrun=args.allow_estimated_cost_overrun,
        fail_fast=args.fail_fast,
    )
    if args.preflight_only:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        _print_summary(summary)
    return summary


def _print_summary(summary: dict[str, Any]) -> None:
    print(
        f"overall_score={summary['overall_score']:.6f} "
        f"task={summary['n_scored_tasks']}/{summary['n_expected_tasks']} "
        f"fallimenti={summary['n_technical_failure_tasks']} "
        f"mancanti={summary['n_missing_tasks']} "
        f"coverage={summary['task_scoring_coverage']:.1%} "
        f"unresolved={summary['n_required_unresolved']} "
        f"partial={str(summary['partial']).lower()} "
        f"-> {summary['out_dir']}"
    )


def main(argv: Sequence[str] | None = None) -> None:
    load_dotenv()
    configure_logging()
    args = build_parser().parse_args(argv)
    if getattr(args, "judge_context", None):
        import os

        os.environ["LEGALITA_JUDGE_CONTEXT"] = args.judge_context
    from legalitaw.benchmark.agentic_v2 import generate_v2_run, score_v2_source

    if args.command == "run":
        _run_command(
            args,
            generate_v2_run_fn=generate_v2_run,
            score_v2_source_fn=score_v2_source,
        )
    elif args.command == "lancia":
        os.environ["AGENT_REASONING_EFFORT"] = args.ragionamento
        run_args = build_parser().parse_args(_lancia_run_argv(args))
        print(
            f"{args.modello} · ragionamento {args.ragionamento} · {args.blocchi} blocchi\n"
            f"risultati: {run_args.results}\nlog: {run_args.log_dir}"
        )
        _run_command(
            run_args,
            generate_v2_run_fn=generate_v2_run,
            score_v2_source_fn=score_v2_source,
        )
    elif args.command in {"score", "evaluate"}:
        _score_command(args, score_v2_source_fn=score_v2_source)
    else:  # pragma: no cover - argparse owns the choices
        raise RuntimeError(f"comando sconosciuto: {args.command}")


if __name__ == "__main__":
    main()
