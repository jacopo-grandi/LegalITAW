import unittest

from legalitaw.evaluation.judge import AdaptiveMajorityJudge
from legalitaw.schemas import JudgeVote


INPUTS = {
    "task_description": "Quesito giuridico",
    "agent_output": "Risposta del sistema",
    "criterion_title": "Criterio",
    "match_criteria": "PASS se corretto. FAIL se assente.",
    "citation_context": '{"summary": "nessuna citazione"}',
}


class FakeJudge:
    provider = "anthropic"

    def __init__(
        self,
        judge_id: str,
        verdict: str | None = "pass",
        *,
        status: str = "ok",
        reasoning: str | None = None,
    ) -> None:
        self.judge_id = judge_id
        self.model = f"fake-{judge_id}"
        self.verdict = verdict
        self.status = status
        self.reasoning = reasoning or f"reasoning-{judge_id}-{verdict}"
        self.calls: list[dict] = []

    def evaluate(self, **kwargs) -> JudgeVote:
        self.calls.append(kwargs)
        if self.status == "error":
            return JudgeVote(
                judge_id=self.judge_id,
                provider=self.provider,
                model=self.model,
                verdict=None,
                reasoning=None,
                status="error",
                error=f"error-{self.judge_id}",
                attempts=1,
                latency_ms=1,
            )
        return JudgeVote(
            judge_id=self.judge_id,
            provider=self.provider,
            model=self.model,
            verdict=self.verdict,
            reasoning=self.reasoning,
            status="ok",
            error=None,
            attempts=1,
            latency_ms=1,
        )


def run_case(a: FakeJudge, b: FakeJudge, c: FakeJudge):
    judge = AdaptiveMajorityJudge(a, b, c)
    return judge.evaluate(**INPUTS)


class AdaptiveMajorityJudgeTest(unittest.TestCase):
    def test_initial_pass_agreement_skips_c(self) -> None:
        a = FakeJudge("A", "pass")
        b = FakeJudge("B", "pass")
        c = FakeJudge("C", "fail")

        result = run_case(a, b, c)

        self.assertEqual(result.verdict, "pass")
        self.assertEqual(result.consensus_method, "initial_agreement")
        self.assertEqual(result.supporting_judges, ["A", "B"])
        self.assertFalse(result.tie_breaker_used)
        self.assertEqual(len(c.calls), 0)

    def test_initial_fail_agreement_skips_c(self) -> None:
        result = run_case(FakeJudge("A", "fail"), FakeJudge("B", "fail"), FakeJudge("C", "pass"))

        self.assertEqual(result.verdict, "fail")
        self.assertEqual(result.consensus_method, "initial_agreement")
        self.assertEqual(result.supporting_judges, ["A", "B"])
        self.assertEqual(len(result.judge_votes), 2)

    def test_tie_breaker_supports_a_and_c(self) -> None:
        c = FakeJudge("C", "pass")
        result = run_case(FakeJudge("A", "pass"), FakeJudge("B", "fail"), c)

        self.assertEqual(result.verdict, "pass")
        self.assertEqual(result.consensus_method, "tie_breaker")
        self.assertEqual(result.supporting_judges, ["A", "C"])
        self.assertTrue(result.tie_breaker_used)
        self.assertEqual(len(c.calls), 1)

    def test_tie_breaker_supports_b_and_c(self) -> None:
        result = run_case(FakeJudge("A", "pass"), FakeJudge("B", "fail"), FakeJudge("C", "fail"))

        self.assertEqual(result.verdict, "fail")
        self.assertEqual(result.consensus_method, "tie_breaker")
        self.assertEqual(result.supporting_judges, ["B", "C"])

    def test_recovery_agreement(self) -> None:
        result = run_case(
            FakeJudge("A", status="error"),
            FakeJudge("B", "pass"),
            FakeJudge("C", "pass"),
        )

        self.assertEqual(result.verdict, "pass")
        self.assertEqual(result.consensus_method, "recovery_agreement")
        self.assertEqual(result.supporting_judges, ["B", "C"])

    def test_recovery_disagreement_is_unresolved(self) -> None:
        result = run_case(
            FakeJudge("A", status="error"),
            FakeJudge("B", "pass"),
            FakeJudge("C", "fail"),
        )

        self.assertEqual(result.verdict, "unresolved")
        self.assertEqual(result.consensus_method, "unresolved")
        self.assertEqual(result.supporting_judges, [])

    def test_failed_tie_breaker_is_unresolved(self) -> None:
        result = run_case(
            FakeJudge("A", "pass"),
            FakeJudge("B", "fail"),
            FakeJudge("C", status="error"),
        )

        self.assertEqual(result.verdict, "unresolved")
        self.assertEqual(result.consensus_method, "unresolved")

    def test_two_initial_errors_skip_c(self) -> None:
        c = FakeJudge("C", "pass")
        result = run_case(FakeJudge("A", status="error"), FakeJudge("B", status="error"), c)

        self.assertEqual(result.verdict, "unresolved")
        self.assertEqual(len(c.calls), 0)
        self.assertEqual(len(result.judge_votes), 2)

    def test_c_receives_no_prior_votes_or_reasoning(self) -> None:
        a = FakeJudge("A", "pass", reasoning="SECRET_A_REASONING")
        b = FakeJudge("B", "fail", reasoning="SECRET_B_REASONING")
        c = FakeJudge("C", "pass")

        result = run_case(a, b, c)

        self.assertEqual(result.verdict, "pass")
        serialized_c_input = " ".join(str(value) for value in c.calls[0].values())
        self.assertNotIn("SECRET_A_REASONING", serialized_c_input)
        self.assertNotIn("SECRET_B_REASONING", serialized_c_input)
        self.assertNotIn("A=PASS", serialized_c_input)
        self.assertNotIn("B=FAIL", serialized_c_input)

    def test_a_and_b_receive_the_same_inputs(self) -> None:
        a = FakeJudge("A", "pass")
        b = FakeJudge("B", "pass")
        run_case(a, b, FakeJudge("C", "fail"))

        self.assertEqual(a.calls[0], b.calls[0])
        self.assertEqual(a.calls[0], INPUTS)

    def test_c_is_called_once_only_when_needed(self) -> None:
        c = FakeJudge("C", "pass")
        run_case(FakeJudge("A", "pass"), FakeJudge("B", "fail"), c)

        self.assertEqual(len(c.calls), 1)


if __name__ == "__main__":
    unittest.main()
