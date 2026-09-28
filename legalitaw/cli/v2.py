"""Stable operational CLI for LegalITA Workflow 2.0."""

from __future__ import annotations

import argparse
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
    _add_scoring_arguments(score)
    return parser


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
) -> Path:
    tasks = _selected_run_tasks(args)
    for task in tasks:
        validate_runtime_fn(task, profile=args.profile)
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
    elif args.command in {"score", "evaluate"}:
        _score_command(args, score_v2_source_fn=score_v2_source)
    else:  # pragma: no cover - argparse owns the choices
        raise RuntimeError(f"comando sconosciuto: {args.command}")


if __name__ == "__main__":
    main()
