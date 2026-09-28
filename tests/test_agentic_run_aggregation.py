import unittest

from legalitaw.evaluation.agentic_run import aggregate_agentic_run


def score(
    task_id: str,
    *,
    required: int,
    passed: int,
    unresolved: int = 0,
    all_pass: bool | None = None,
) -> dict:
    return {
        "task_id": task_id,
        "n_required": required,
        "n_required_passed": passed,
        "n_required_unresolved": unresolved,
        "all_pass": all_pass,
        "reasoning_scoring_status": (
            "incomplete" if unresolved else "complete"
        ),
    }


class AgenticRunAggregationTest(unittest.TestCase):
    def test_each_task_has_equal_weight_even_with_different_rubric_sizes(self) -> None:
        result = aggregate_agentic_run(
            [
                score("WF2-001", required=1, passed=1, all_pass=True),
                score("WF2-002", required=9, passed=0, all_pass=False),
            ],
            expected_task_ids=["WF2-001", "WF2-002"],
        )

        self.assertEqual(result["overall_score"], 0.5)
        self.assertEqual(
            result["required_criterion_micro_rate_lower_bound"], 0.1
        )
        self.assertEqual(result["task_success_rate"], 0.5)

    def test_missing_and_technical_failure_tasks_keep_fixed_denominator(self) -> None:
        result = aggregate_agentic_run(
            [score("WF2-001", required=4, passed=4, all_pass=True)],
            expected_task_ids=["WF2-001", "WF2-002", "WF2-003"],
            technical_failures={"WF2-002": {"error": "judge timeout"}},
        )

        self.assertAlmostEqual(result["overall_score"], 1 / 3)
        self.assertAlmostEqual(result["task_scoring_coverage"], 1 / 3)
        self.assertEqual(result["n_technical_failure_tasks"], 1)
        self.assertEqual(result["n_missing_tasks"], 1)
        self.assertEqual(
            [item["status"] for item in result["tasks"]],
            ["complete", "technical_failure", "missing"],
        )

    def test_unresolved_criteria_are_reported_as_explicit_bounds(self) -> None:
        result = aggregate_agentic_run(
            [score("WF2-001", required=4, passed=2, unresolved=1)],
            expected_task_ids=["WF2-001"],
        )

        self.assertEqual(result["overall_score"], 0.5)
        self.assertEqual(result["overall_score_upper_bound"], 0.75)
        self.assertEqual(result["required_criterion_resolution_coverage"], 0.75)
        self.assertEqual(result["required_criterion_resolved_pass_rate"], 2 / 3)
        self.assertEqual(result["n_incomplete_tasks"], 1)

    def test_duplicate_score_is_rejected(self) -> None:
        item = score("WF2-001", required=1, passed=1, all_pass=True)
        with self.assertRaisesRegex(ValueError, "score duplicato"):
            aggregate_agentic_run(
                [item, item],
                expected_task_ids=["WF2-001"],
            )


if __name__ == "__main__":
    unittest.main()
