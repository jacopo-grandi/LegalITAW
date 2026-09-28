"""Scoring di un task WF2: verdetti per criterio e aggregati all-pass.

Struttura adattata da Harvey LAB (MIT).
"""

import logging
from collections import Counter
from collections.abc import Mapping
from datetime import datetime, timezone
from typing import Any

from legalitaw.evaluation.judge import Judge
from legalitaw.schemas import ConsensusResult, CriterionResult, JudgeVote, TaskScore, WorkflowJudgeTask

log = logging.getLogger(__name__)



def criterion_result_from_judge_output(
    *,
    criterion_id: str,
    criterion_title: str,
    scoring_type: str,
    category: str,
    judge_output: Any,
) -> CriterionResult:
    """Converte output legacy o multi-judge nel modello pubblico CriterionResult."""
    verdict = "unresolved"
    reasoning = "Errore tecnico del judge: verdetto non disponibile."
    consensus_method: str | None = None
    supporting_judges: list[str] = []
    tie_breaker_used = False
    judge_votes: list[JudgeVote] = []

    if isinstance(judge_output, ConsensusResult):
        verdict = judge_output.verdict
        reasoning = judge_output.reasoning
        consensus_method = judge_output.consensus_method
        supporting_judges = list(judge_output.supporting_judges)
        tie_breaker_used = judge_output.tie_breaker_used
        judge_votes = list(judge_output.judge_votes)
    elif isinstance(judge_output, JudgeVote):
        judge_votes = [judge_output]
        if judge_output.status == "ok" and judge_output.verdict in ("pass", "fail"):
            verdict = judge_output.verdict
            reasoning = judge_output.reasoning or ""
            supporting_judges = [judge_output.judge_id]
        else:
            reasoning = "Errore tecnico del judge: verdetto non disponibile."
    elif isinstance(judge_output, Mapping):
        raw_verdict = str(judge_output.get("verdict", "")).lower().strip()
        if raw_verdict in ("pass", "fail", "unresolved"):
            verdict = raw_verdict
            reasoning = str(judge_output.get("reasoning") or "")
        consensus_method = judge_output.get("consensus_method")  # type: ignore[assignment]
        supporting_judges = list(judge_output.get("supporting_judges") or [])
        tie_breaker_used = bool(judge_output.get("tie_breaker_used") or False)
        for item in judge_output.get("judge_votes") or []:
            try:
                judge_votes.append(
                    item if isinstance(item, JudgeVote) else JudgeVote.model_validate(item)
                )
            except Exception:
                log.debug("JudgeVote legacy non valido ignorato: %r", item)

    return CriterionResult(
        id=criterion_id,
        title=criterion_title,
        verdict=verdict,
        reasoning=reasoning,
        scoring_type=scoring_type,
        category=category,
        consensus_method=consensus_method,
        supporting_judges=supporting_judges,
        tie_breaker_used=tie_breaker_used,
        judge_votes=judge_votes,
    )




def summarize_consensus_diagnostics(criteria_results: list[CriterionResult]) -> dict[str, Any]:
    """Metriche diagnostiche del consenso multi-judge, senza toccare lo score primario."""
    total_criteria = len(criteria_results)
    method_counts: Counter[str] = Counter(
        result.consensus_method or "single" for result in criteria_results
    )
    c_calls = sum(
        1
        for result in criteria_results
        if any(vote.judge_id == "C" for vote in result.judge_votes)
    )
    individual_valid: dict[str, Counter[str]] = {
        "A": Counter(),
        "B": Counter(),
        "C": Counter(),
    }
    combination_counts: Counter[str] = Counter()
    ab_pairs: list[tuple[str, str]] = []

    for result in criteria_results:
        by_judge = {vote.judge_id: vote for vote in result.judge_votes}
        labels: list[str] = []
        for judge_id in ("A", "B", "C"):
            vote = by_judge.get(judge_id)
            labels.append(f"{judge_id}:{_vote_label(vote)}")
            if vote and vote.status == "ok" and vote.verdict in ("pass", "fail"):
                individual_valid[judge_id][vote.verdict] += 1
        if by_judge:
            combination_counts["|".join(labels)] += 1

        vote_a = by_judge.get("A")
        vote_b = by_judge.get("B")
        if (
            vote_a
            and vote_b
            and vote_a.status == "ok"
            and vote_b.status == "ok"
            and vote_a.verdict in ("pass", "fail")
            and vote_b.verdict in ("pass", "fail")
        ):
            ab_pairs.append((vote_a.verdict, vote_b.verdict))

    return {
        "criteria_evaluated": total_criteria,
        "initial_agreement_rate": _rate(method_counts["initial_agreement"], total_criteria),
        "tie_breaker_rate": _rate(method_counts["tie_breaker"], total_criteria),
        "recovery_rate": _rate(method_counts["recovery_agreement"], total_criteria),
        "primary_only_rate": _rate(method_counts["primary_only"], total_criteria),
        "targeted_audit_rate": _rate(
            sum(
                method_counts[name]
                for name in (
                    "audit_agreement",
                    "reviewer_override",
                    "audit_recovery",
                    "audit_unavailable_primary_retained",
                )
            ),
            total_criteria,
        ),
        "reviewer_override_rate": _rate(
            method_counts["reviewer_override"],
            total_criteria,
        ),
        "unresolved_rate": _rate(method_counts["unresolved"], total_criteria),
        "judge_c_evaluated_criteria": c_calls,
        "judge_call_counts": {
            judge_id: sum(
                1
                for result in criteria_results
                for vote in result.judge_votes
                if vote.judge_id == judge_id
            )
            for judge_id in ("A", "B", "C")
        },
        "individual_pass_rates": {
            judge_id: _rate(counts["pass"], counts["pass"] + counts["fail"])
            for judge_id, counts in individual_valid.items()
        },
        "vote_combination_matrix": dict(combination_counts),
        "cohen_kappa_ab": _cohen_kappa(ab_pairs),
    }




def _vote_label(vote: JudgeVote | None) -> str:
    if vote is None:
        return "not_called"
    if vote.status != "ok":
        return "error"
    return str(vote.verdict)


def _rate(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator > 0 else 0.0




def _cohen_kappa(pairs: list[tuple[str, str]]) -> float | None:
    n = len(pairs)
    if n == 0:
        return None

    observed = sum(1 for a, b in pairs if a == b) / n
    a_counts = Counter(a for a, _ in pairs)
    b_counts = Counter(b for _, b in pairs)
    expected = sum(
        (a_counts[label] / n) * (b_counts[label] / n)
        for label in ("pass", "fail")
    )
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1.0 - expected)




def _log_criterion_consensus(
    task_id: str,
    criterion_id: str,
    criterion_result: CriterionResult,
    *,
    position: int | None = None,
    total: int | None = None,
) -> None:
    progress = (
        f" [{position}/{total}]"
        if position is not None and total is not None
        else ""
    )
    if not criterion_result.judge_votes:
        log.info(
            "%s / %s%s - verdict=%s",
            task_id,
            criterion_id,
            progress,
            criterion_result.verdict.upper(),
        )
        return

    by_judge = {vote.judge_id: vote for vote in criterion_result.judge_votes}
    labels = []
    for judge_id in ("A", "B", "C"):
        vote = by_judge.get(judge_id)
        if vote is not None:
            labels.append(f"{judge_id}={_vote_label(vote).upper()}")
    method = criterion_result.consensus_method or "single"
    log.info(
        "%s / %s%s - %s - %s",
        task_id,
        criterion_id,
        progress,
        " ".join(labels),
        method,
    )




def score_task(
        task: WorkflowJudgeTask,
        model_output: str,
        model: str,
        judge: Judge | None = None,
) -> TaskScore:
    """Valuta la risposta di un modello su un singolo task, criterio per criterio."""
    if judge is None:
        judge = Judge()

    criteria_results: list[CriterionResult] = []
    n_passed = 0
    n_unresolved = 0
    n_required = 0
    n_required_passed = 0
    n_required_unresolved = 0
    n_bonus = 0
    n_bonus_passed = 0
    n_bonus_unresolved = 0

    criterion_outputs: Mapping[str, Any] | None = None
    evaluate_criteria = getattr(judge, "evaluate_criteria", None)
    if callable(evaluate_criteria):
        criterion_outputs = evaluate_criteria(
            task_id=task.task_id,
            task_description=task.query,
            agent_output=model_output,
            criteria=task.criteria,
            citation_context=None,
        )

    for criterion_position, criterion in enumerate(task.criteria, start=1):
        result = (
            criterion_outputs.get(criterion.id)
            if criterion_outputs is not None
            else judge.evaluate(
                task_description=task.query,
                agent_output=model_output,
                criterion_title=criterion.title,
                match_criteria=criterion.match_criteria,
                citation_context=None,
            )
        )
        criterion_result = criterion_result_from_judge_output(
            criterion_id=criterion.id,
            criterion_title=criterion.title,
            scoring_type=criterion.scoring_type,
            category=criterion.category,
            judge_output=result,
        )
        verdict = criterion_result.verdict

        if verdict == "pass":
            n_passed += 1
        elif verdict == "unresolved":
            n_unresolved += 1

        if criterion.scoring_type == "required":
            n_required += 1
            if verdict == "pass":
                n_required_passed += 1
            elif verdict == "unresolved":
                n_required_unresolved += 1
        elif criterion.scoring_type == "bonus":
            n_bonus += 1
            if verdict == "pass":
                n_bonus_passed += 1
            elif verdict == "unresolved":
                n_bonus_unresolved += 1

        criteria_results.append(criterion_result)
        _log_criterion_consensus(
            task.task_id,
            criterion.id,
            criterion_result,
            position=criterion_position,
            total=len(task.criteria),
        )

    n_criteria = len(task.criteria)
    scoring_status = "incomplete" if n_required_unresolved > 0 else "complete"
    if scoring_status == "incomplete":
        content_all_pass = None
        reasoning_all_pass = None
        reasoning_score = None
        required_pass_rate = None
    else:
        content_all_pass = n_required > 0 and n_required_passed == n_required
        reasoning_all_pass = content_all_pass
        reasoning_score = 1.0 if reasoning_all_pass else 0.0
        required_pass_rate = n_required_passed / n_required if n_required > 0 else 0.0
    all_pass = reasoning_all_pass
    score = reasoning_score
    valid_bonus = n_bonus - n_bonus_unresolved
    bonus_pass_rate = n_bonus_passed / valid_bonus if valid_bonus > 0 else None
    unresolved_rate = n_unresolved / n_criteria if n_criteria > 0 else 0.0

    reasoning_parts = [
        f"Reasoning: {n_required_passed}/{n_required} criteri required superati.",
    ]
    if n_bonus > 0:
        reasoning_parts.append(f"Bonus: {n_bonus_passed}/{n_bonus} ottenuti.")
    if scoring_status == "incomplete":
        reasoning_parts.append(
            f"VALUTAZIONE INCOMPLETA: {n_required_unresolved} required unresolved."
        )
    elif n_required == 0:
        reasoning_parts.append("NESSUN CRITERIO REQUIRED. FAIL.")
    elif content_all_pass:
        reasoning_parts.append("ALL PASS.")
    else:
        reasoning_parts.append(
            f"FALLITI {n_required - n_required_passed} REQUIRED."
        )
    if n_unresolved:
        reasoning_parts.append(f"UNRESOLVED: {n_unresolved}/{n_criteria} criteri.")
    summary = " ".join(reasoning_parts)

    log.info(f"{task.task_id} [{model}] → {summary}")

    return TaskScore(
        task_id=task.task_id,
        model=model,
        model_output=model_output,
        evaluation_error=None,
        score=score,
        all_pass=all_pass,
        reasoning_score=reasoning_score,
        reasoning_all_pass=reasoning_all_pass,
        reasoning_scoring_status=scoring_status,  # type: ignore[arg-type]
        content_all_pass=content_all_pass,
        scoring_status=scoring_status,
        n_criteria=n_criteria,
        n_passed=n_passed,
        n_unresolved=n_unresolved,
        n_required=n_required,
        n_required_passed=n_required_passed,
        n_required_unresolved=n_required_unresolved,
        n_bonus=n_bonus,
        n_bonus_passed=n_bonus_passed,
        n_bonus_unresolved=n_bonus_unresolved,
        required_pass_rate=required_pass_rate,
        bonus_pass_rate=bonus_pass_rate,
        unresolved_rate=unresolved_rate,
        summary=summary,
        criteria_results=criteria_results,
        judge_model=getattr(judge, "model", "unknown"),
        judge_strategy=getattr(judge, "strategy", "single"),
        judge_models=getattr(
            judge,
            "judge_models",
            {"A": getattr(judge, "model", "unknown")},
        ),
        judge_diagnostics={
            **summarize_consensus_diagnostics(criteria_results),
            **(
                {"targeted_audit": dict(judge.last_diagnostics)}
                if getattr(judge, "last_diagnostics", None)
                else {}
            ),
        },
        scored_at=datetime.now(timezone.utc).isoformat(),
    )

