"""Shared composition helpers for LegalITA command-line entry points."""

from __future__ import annotations

import argparse
import logging
from typing import Any


def configure_logging() -> None:
    """Configure process logging; library imports remain side-effect free."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
    )


def add_judge_arguments(
    parser: argparse.ArgumentParser,
    *,
    default_model: str | None,
) -> None:
    """Add the shared adaptive-judge options to a parser."""
    parser.add_argument(
        "--judge",
        default=default_model,
        help="Modello del Judge A (default: configurazione runtime).",
    )
    parser.add_argument(
        "--judge-strategy",
        choices=["single", "batched_single", "adaptive_majority", "targeted_audit", "paired_consensus"],
        default=None,
    )
    for judge_id in ("a", "b", "c"):
        parser.add_argument(
            f"--judge-{judge_id}-provider",
            choices=["anthropic", "openai", "novita", "gemini", "typesafe"],
            default=None,
        )
        parser.add_argument(f"--judge-{judge_id}-model", default=None)
    parser.add_argument("--judge-batch-size", type=int, default=None)
    parser.add_argument("--judge-audit-sample-rate", type=float, default=None)


def judge_overrides(args: argparse.Namespace) -> dict[str, Any]:
    """Translate parsed judge flags to workflow keyword arguments."""
    return {
        "judge_model": args.judge,
        "judge_strategy": args.judge_strategy,
        "judge_a_provider": args.judge_a_provider,
        "judge_a_model": args.judge_a_model,
        "judge_b_provider": args.judge_b_provider,
        "judge_b_model": args.judge_b_model,
        "judge_c_provider": args.judge_c_provider,
        "judge_c_model": args.judge_c_model,
        "batch_size": args.judge_batch_size,
        "audit_sample_rate": args.judge_audit_sample_rate,
    }
