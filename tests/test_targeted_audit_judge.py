import unittest

from legalitaw.evaluation.judge import TargetedAuditJudge
from legalitaw.evaluation.scoring import score_task
from legalitaw.schemas import Criterion, JudgeVote, WorkflowJudgeTask


def criteria(count: int, *, category: str = "legal") -> list[Criterion]:
    return [
        Criterion(
            id=f"C-{index:03d}",
            title=f"Criterio {index}",
            match_criteria="PASS se presente. FAIL se assente.",
            category=category,
            criterion_logic="required_presence",
        )
        for index in range(1, count + 1)
    ]


class FakeBatchJudge:
    def __init__(
        self,
        judge_id: str,
        verdicts: dict[str, str] | None = None,
        *,
        status: str = "ok",
    ) -> None:
        self.judge_id = judge_id
        self.provider = "openai" if judge_id == "A" else "anthropic"
        self.model = "gpt-5.6-luna" if judge_id == "A" else "claude-sonnet-4-6"
        self.verdicts = verdicts or {}
        self.status = status
        self.calls: list[list[str]] = []

    def evaluate_batch(self, *, criteria, **kwargs):
        self.calls.append([item.id for item in criteria])
        votes = {}
        for item in criteria:
            if self.status == "error":
                votes[item.id] = JudgeVote(
                    judge_id=self.judge_id,
                    provider=self.provider,
                    model=self.model,
                    verdict=None,
                    reasoning=None,
                    status="error",
                    error="fake error",
                    attempts=1,
                )
                continue
            verdict = self.verdicts.get(item.id, "pass")
            votes[item.id] = JudgeVote(
                judge_id=self.judge_id,
                provider=self.provider,
                model=self.model,
                verdict=verdict,
                reasoning=f"{self.judge_id}-{verdict}",
                evidence_status="found" if verdict == "pass" else "not_found",
                evidence=["presente"] if verdict == "pass" else [],
                status="ok",
                attempts=1,
            )
        return votes


class TargetedAuditJudgeTest(unittest.TestCase):
    def test_batched_single_never_calls_reviewer(self) -> None:
        primary = FakeBatchJudge("A", {"C-001": "fail"})
        judge = TargetedAuditJudge(primary, None, batch_size=10)

        results = judge.evaluate_criteria(
            task_id="WF2-001",
            task_description="Q",
            agent_output="presente",
            criteria=criteria(11),
        )

        self.assertEqual(judge.strategy, "batched_single")
        self.assertEqual([len(call) for call in primary.calls], [10, 1])
        self.assertEqual(results["C-001"].verdict, "fail")
        self.assertEqual(judge.last_diagnostics["reviewer_api_calls"], 0)

    def test_score_task_uses_grouped_strategy_and_records_diagnostics(self) -> None:
        primary = FakeBatchJudge("A")
        reviewer = FakeBatchJudge("B")
        judge = TargetedAuditJudge(
            primary,
            reviewer,
            batch_size=10,
            audit_sample_rate=0,
        )
        task = WorkflowJudgeTask(
            task_id="WF2-001",
            query="Q",
            criteria=criteria(11),
        )

        score = score_task(
            task,
            "presente",
            "external-model",
            judge=judge,
        )

        self.assertEqual(score.required_pass_rate, 1.0)
        self.assertEqual(score.judge_strategy, "targeted_audit")
        self.assertEqual(score.judge_diagnostics["targeted_audit"]["primary_api_calls"], 2)

    def test_primary_is_batched_and_clean_passes_skip_reviewer(self) -> None:
        primary = FakeBatchJudge("A")
        reviewer = FakeBatchJudge("B")
        judge = TargetedAuditJudge(
            primary,
            reviewer,
            batch_size=10,
            audit_sample_rate=0,
        )

        results = judge.evaluate_criteria(
            task_id="WF2-001",
            task_description="Q",
            agent_output="presente",
            criteria=criteria(21),
        )

        self.assertEqual([len(call) for call in primary.calls], [10, 10, 1])
        self.assertEqual(reviewer.calls, [])
        self.assertTrue(all(item.consensus_method == "primary_only" for item in results.values()))

    def test_primary_fail_is_reviewed_and_sonnet_overrides(self) -> None:
        primary = FakeBatchJudge("A", {"C-001": "fail"})
        reviewer = FakeBatchJudge("B", {"C-001": "pass"})
        judge = TargetedAuditJudge(primary, reviewer, audit_sample_rate=0)

        result = judge.evaluate_criteria(
            task_id="WF2-001",
            task_description="Q",
            agent_output="presente",
            criteria=criteria(1),
        )["C-001"]

        self.assertEqual(result.verdict, "pass")
        self.assertEqual(result.consensus_method, "reviewer_override")
        self.assertEqual(result.supporting_judges, ["B"])

    def test_sample_is_ten_percent_and_stable_within_each_category(self) -> None:
        primary = FakeBatchJudge("A")
        reviewer = FakeBatchJudge("B")
        judge = TargetedAuditJudge(
            primary,
            reviewer,
            batch_size=10,
            audit_sample_rate=0.10,
        )
        mixed = criteria(20, category="legal") + [
            item.model_copy(update={"id": f"F-{index:03d}", "category": "format"})
            for index, item in enumerate(criteria(10), start=1)
        ]

        judge.evaluate_criteria(
            task_id="WF2-001",
            task_description="Q",
            agent_output="presente",
            criteria=mixed,
        )

        reviewed = {criterion_id for call in reviewer.calls for criterion_id in call}
        self.assertEqual(sum(item.startswith("C-") for item in reviewed), 2)
        self.assertEqual(sum(item.startswith("F-") for item in reviewed), 1)
        self.assertEqual(judge.last_diagnostics["sampled_audit_criteria"], 3)

    def test_reviewer_error_keeps_valid_primary_score(self) -> None:
        primary = FakeBatchJudge("A", {"C-001": "fail"})
        reviewer = FakeBatchJudge("B", status="error")
        judge = TargetedAuditJudge(primary, reviewer, audit_sample_rate=0)

        result = judge.evaluate_criteria(
            task_id="WF2-001",
            task_description="Q",
            agent_output="presente",
            criteria=criteria(1),
        )["C-001"]

        self.assertEqual(result.verdict, "fail")
        self.assertEqual(result.consensus_method, "audit_unavailable_primary_retained")


if __name__ == "__main__":
    unittest.main()
