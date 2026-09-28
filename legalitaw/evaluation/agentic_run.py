"""Aggregate complete Workflow 2.0 runs with equal task weight.

The aggregate is intentionally a *system* score: every expected task occupies
one fixed slot in the denominator.  A missing task or a task that could not be
scored therefore contributes zero instead of disappearing from the report.
Judge ``unresolved`` verdicts are exposed as lower/upper score bounds.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import Any


AGGREGATE_CONTRACT = "wf2_equal_task_weight_v1"


def _value(score: Any, name: str, default: Any = None) -> Any:
    if isinstance(score, Mapping):
        return score.get(name, default)
    return getattr(score, name, default)


def _count(score: Any, name: str) -> int:
    value = _value(score, name, 0)
    try:
        return int(value or 0)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} non e' un intero valido: {value!r}") from exc


def _rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def aggregate_agentic_run(
    scores: Iterable[Any],
    *,
    expected_task_ids: Sequence[str],
    technical_failures: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Return the overall score for one external or native agentic run.

    ``overall_score`` is the conservative lower bound.  For a scored task its
    contribution is ``required PASS / required total``; required unresolved
    criteria count as zero only in this explicitly labelled lower bound.  The
    upper bound assumes that those unresolved criteria would pass.  Missing
    tasks and technical failures contribute zero to both bounds because they
    are failures of the evaluated system, not judge uncertainty.

    The function accepts both ``TaskScore`` objects and their JSON mappings so
    the same contract can aggregate in-memory results and resumed score files.
    """
    expected = list(expected_task_ids)
    if not expected:
        raise ValueError("expected_task_ids non puo' essere vuoto")
    if len(expected) != len(set(expected)):
        raise ValueError("expected_task_ids contiene duplicati")

    failure_map = dict(technical_failures or {})
    unexpected_failures = sorted(set(failure_map) - set(expected))
    if unexpected_failures:
        raise ValueError(
            f"technical_failures contiene task inattesi: {unexpected_failures}"
        )

    by_task: dict[str, Any] = {}
    for score in scores:
        task_id = str(_value(score, "task_id", "")).strip()
        if not task_id:
            raise ValueError("score senza task_id")
        if task_id not in expected:
            raise ValueError(f"score per task inatteso: {task_id}")
        if task_id in by_task:
            raise ValueError(f"score duplicato per task: {task_id}")
        if task_id in failure_map:
            raise ValueError(
                f"{task_id} compare sia negli score sia nei technical_failures"
            )
        by_task[task_id] = score

    task_rows: list[dict[str, Any]] = []
    lower_sum = 0.0
    upper_sum = 0.0
    scored_lower: list[float] = []
    required_total = 0
    required_passed = 0
    required_unresolved = 0
    n_all_pass = 0
    n_complete = 0
    n_incomplete = 0

    for task_id in expected:
        score = by_task.get(task_id)
        if score is None:
            status = "technical_failure" if task_id in failure_map else "missing"
            task_rows.append(
                {
                    "task_id": task_id,
                    "status": status,
                    "criterion_rate_lower_bound": 0.0,
                    "criterion_rate_upper_bound": 0.0,
                    "all_pass": False,
                    "technical_failure": failure_map.get(task_id),
                }
            )
            continue

        n_required = _count(score, "n_required")
        n_passed = _count(score, "n_required_passed")
        n_unresolved = _count(score, "n_required_unresolved")
        if n_required <= 0:
            raise ValueError(f"{task_id}: n_required deve essere positivo")
        if n_passed + n_unresolved > n_required:
            raise ValueError(
                f"{task_id}: pass ({n_passed}) + unresolved ({n_unresolved}) "
                f"supera i required ({n_required})"
            )

        lower = n_passed / n_required
        upper = (n_passed + n_unresolved) / n_required
        lower_sum += lower
        upper_sum += upper
        scored_lower.append(lower)
        required_total += n_required
        required_passed += n_passed
        required_unresolved += n_unresolved

        all_pass = _value(score, "all_pass") is True
        if all_pass:
            n_all_pass += 1
        scoring_status = str(
            _value(score, "reasoning_scoring_status", None)
            or _value(score, "scoring_status", "")
        )
        if scoring_status == "complete" and n_unresolved == 0:
            n_complete += 1
        else:
            n_incomplete += 1
        task_status = (
            "complete"
            if scoring_status == "complete" and n_unresolved == 0
            else "incomplete"
        )
        task_rows.append(
            {
                "task_id": task_id,
                "status": task_status,
                "criterion_rate_lower_bound": lower,
                "criterion_rate_upper_bound": upper,
                "all_pass": all_pass,
                "n_required": n_required,
                "n_required_passed": n_passed,
                "n_required_unresolved": n_unresolved,
                "technical_failure": None,
            }
        )

    n_expected = len(expected)
    n_scored = len(by_task)
    n_technical_failures = len(failure_map)
    n_missing = n_expected - n_scored - n_technical_failures
    resolved_required = required_total - required_unresolved

    return {
        "aggregate_contract": AGGREGATE_CONTRACT,
        "score_unit": "task",
        "task_weight": 1 / n_expected,
        "denominator_policy": (
            "Ogni task atteso pesa uguale; task mancanti o in errore tecnico "
            "valgono zero. Gli unresolved definiscono i limiti inferiore e superiore."
        ),
        "overall_score": lower_sum / n_expected,
        "overall_score_lower_bound": lower_sum / n_expected,
        "overall_score_upper_bound": upper_sum / n_expected,
        "scored_tasks_macro_average": (
            sum(scored_lower) / len(scored_lower) if scored_lower else None
        ),
        "task_success_rate": n_all_pass / n_expected,
        "task_scoring_coverage": n_scored / n_expected,
        "task_completion_coverage": n_complete / n_expected,
        "required_criterion_micro_rate_lower_bound": _rate(
            required_passed, required_total
        ),
        "required_criterion_resolved_pass_rate": _rate(
            required_passed, resolved_required
        ),
        "required_criterion_resolution_coverage": _rate(
            resolved_required, required_total
        ),
        "n_expected_tasks": n_expected,
        "n_scored_tasks": n_scored,
        "n_complete_tasks": n_complete,
        "n_incomplete_tasks": n_incomplete,
        "n_technical_failure_tasks": n_technical_failures,
        "n_missing_tasks": n_missing,
        "n_all_pass_tasks": n_all_pass,
        "n_required_criteria": required_total,
        "n_required_passed": required_passed,
        "n_required_unresolved": required_unresolved,
        "tasks": task_rows,
    }


__all__ = ["AGGREGATE_CONTRACT", "aggregate_agentic_run"]
