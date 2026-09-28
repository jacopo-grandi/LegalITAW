import unittest

from legalitaw.evaluation.scoring import score_task
from legalitaw.schemas import ConsensusResult, Criterion, JudgeVote, WorkflowJudgeTask


def make_task(task_id: str, *, include_bonus: bool = False) -> WorkflowJudgeTask:
    criteria = [
        {
            "id": "C-001",
            "title": "Required",
            "match_criteria": "PASS se risponde. FAIL se non risponde.",
            "scoring_type": "required",
        }
    ]
    if include_bonus:
        criteria.append(
            {
                "id": "C-002",
                "title": "Bonus",
                "match_criteria": "PASS se cita un dettaglio ulteriore. FAIL se no.",
                "scoring_type": "bonus",
            }
        )
    return WorkflowJudgeTask(
        task_id=task_id,
        query="Q",
        criteria=[Criterion.model_validate(item) for item in criteria],
    )


def vote(judge_id: str, verdict: str) -> JudgeVote:
    return JudgeVote(
        judge_id=judge_id,
        provider="anthropic",
        model=f"fake-{judge_id}",
        verdict=verdict,
        reasoning=f"{verdict}-{judge_id}",
        status="ok",
        error=None,
        attempts=1,
        latency_ms=1,
    )


def consensus(verdict: str) -> ConsensusResult:
    if verdict == "unresolved":
        return ConsensusResult(
            verdict="unresolved",
            reasoning="Verdetto UNRESOLVED: non esistono due voti validi concordi.",
            consensus_method="unresolved",
            supporting_judges=[],
            tie_breaker_used=False,
            judge_votes=[
                vote("A", "pass"),
                vote("B", "fail"),
            ],
        )
    return ConsensusResult(
        verdict=verdict,
        reasoning=f"Verdetto {verdict.upper()} sostenuto da Judge A e Judge B.",
        consensus_method="initial_agreement",
        supporting_judges=["A", "B"],
        tie_breaker_used=False,
        judge_votes=[vote("A", verdict), vote("B", verdict)],
    )


class SequenceJudge:
    model = "fake-adaptive"
    strategy = "adaptive_majority"
    judge_models = {"A": "fake-A", "B": "fake-B", "C": "fake-C"}

    def __init__(self, verdicts: list[str]) -> None:
        self.results = [consensus(verdict) for verdict in verdicts]

    def evaluate(self, **kwargs) -> ConsensusResult:
        return self.results.pop(0)


class AdaptiveScoringTest(unittest.TestCase):
    def test_required_unresolved_makes_task_incomplete_not_failed(self) -> None:
        score = score_task(
            task=make_task("diritto_civile/0001"),
            model_output="A",
            model="fake-model",
            judge=SequenceJudge(["unresolved"]),
        )

        self.assertEqual(score.scoring_status, "incomplete")
        self.assertIsNone(score.score)
        self.assertIsNone(score.all_pass)
        self.assertIsNone(score.required_pass_rate)
        self.assertEqual(score.n_passed, 0)
        self.assertEqual(score.n_required_passed, 0)
        self.assertEqual(score.n_required_unresolved, 1)
        self.assertEqual(score.criteria_results[0].verdict, "unresolved")


    def test_bonus_unresolved_does_not_change_required_all_pass(self) -> None:
        score = score_task(
            task=make_task("diritto_civile/0001", include_bonus=True),
            model_output="A",
            model="fake-model",
            judge=SequenceJudge(["pass", "unresolved"]),
        )

        self.assertEqual(score.scoring_status, "complete")
        self.assertEqual(score.score, 1.0)
        self.assertTrue(score.all_pass)
        self.assertEqual(score.n_bonus_unresolved, 1)
        self.assertIsNone(score.bonus_pass_rate)


if __name__ == "__main__":
    unittest.main()
