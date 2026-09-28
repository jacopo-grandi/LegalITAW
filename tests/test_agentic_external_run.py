import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from legalitaw.benchmark.agentic_run import (
    estimate_batched_single_cost,
    estimate_targeted_audit_cost,
    evaluate_external_run,
    external_run_root,
    locate_external_run_root,
)
from legalitaw.schemas import Criterion


def fake_task(task_id: str) -> SimpleNamespace:
    return SimpleNamespace(spec=SimpleNamespace(task_id=task_id))


class AgenticExternalRunTest(unittest.TestCase):
    def test_batched_single_cost_contains_no_reviewer(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_root = Path(temporary)
            (run_root / "WF2-001").mkdir()
            task = fake_task("WF2-001")
            fake_criteria = [
                Criterion(id="C-001", title="C", match_criteria="PASS se presente")
            ]
            judge_projection = SimpleNamespace(query="Q", criteria=fake_criteria)
            with (
                patch("legalitaw.benchmark.agentic_run.import_submission", return_value=object()),
                patch("legalitaw.evaluation.agentic.judge_task", return_value=judge_projection),
                patch(
                    "legalitaw.agentic.submissions.submission_text",
                    return_value="Risposta",
                ),
            ):
                estimate = estimate_batched_single_cost(
                    [task],
                    run_root=run_root,
                    model="external-model",
                    primary_model="gpt-5.6-luna",
                    batch_size=10,
                )

        self.assertEqual(estimate["primary_api_calls"], 1)
        self.assertEqual(estimate["schema_version"], "batched_single_cost_estimate_v1")
        self.assertNotIn("reviewer_model", estimate)

    def test_targeted_cost_estimate_bounds_primary_and_full_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_root = Path(temporary)
            (run_root / "WF2-001").mkdir()
            task = fake_task("WF2-001")
            fake_criteria = [
                Criterion(
                    id=f"C-{index:03d}",
                    title="C",
                    match_criteria="PASS se presente",
                    category="legal" if index < 6 else "format",
                )
                for index in range(12)
            ]
            judge_projection = SimpleNamespace(query="Q", criteria=fake_criteria)
            with (
                patch("legalitaw.benchmark.agentic_run.import_submission", return_value=object()),
                patch("legalitaw.evaluation.agentic.judge_task", return_value=judge_projection),
                patch(
                    "legalitaw.agentic.submissions.submission_text",
                    return_value="Risposta",
                ),
            ):
                estimate = estimate_targeted_audit_cost(
                    [task],
                    run_root=run_root,
                    model="external-model",
                    primary_model="gpt-5.6-luna",
                    reviewer_model="claude-sonnet-4-6",
                    batch_size=10,
                    audit_sample_rate=0.10,
                )

        self.assertEqual(estimate["judge_criteria"], 12)
        self.assertEqual(estimate["primary_api_calls"], 2)
        self.assertEqual(estimate["maximum_reviewer_api_calls"], 2)
        self.assertEqual(estimate["sample_only_reviewer_api_calls"], 1)
        self.assertGreater(
            estimate["conservative_maximum_estimated_cost_usd"],
            estimate["sample_only_estimated_cost_usd"],
        )

    def test_locates_single_wrapped_run_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            wrapped = base / "risultati_modello"
            (wrapped / "WF2-001").mkdir(parents=True)
            (wrapped / "WF2-002").mkdir()

            self.assertEqual(locate_external_run_root(base), wrapped)

    def test_zip_path_traversal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "unsafe.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../escape.txt", "no")

            with self.assertRaisesRegex(ValueError, "path non sicuro"):
                with external_run_root(archive_path):
                    pass

    def test_batch_checkpoints_scores_and_fixed_denominator_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            run_root = base / "run"
            out_dir = base / "out"
            for task_id in ("WF2-001", "WF2-002"):
                (run_root / task_id).mkdir(parents=True)

            def evaluate(task, submission, *, judge):
                return {"task_id": task.spec.task_id}

            def payload(score):
                passed = 1 if score["task_id"] == "WF2-001" else 0
                return {
                    "task_id": score["task_id"],
                    "n_required": 1,
                    "n_required_passed": passed,
                    "n_required_unresolved": 0,
                    "all_pass": bool(passed),
                    "reasoning_scoring_status": "complete",
                }

            with patch(
                "legalitaw.benchmark.agentic_run.import_submission",
                side_effect=lambda task, source, model: {"task_id": task.spec.task_id},
            ):
                summary = evaluate_external_run(
                    [fake_task("WF2-001"), fake_task("WF2-002")],
                    run_root=run_root,
                    model="external-model",
                    out_dir=out_dir,
                    judge=object(),
                    evaluate_submission_fn=evaluate,
                    evaluation_payload_fn=payload,
                )

            self.assertEqual(summary["overall_score"], 0.5)
            self.assertEqual(summary["task_success_rate"], 0.5)
            self.assertTrue((out_dir / "scores" / "WF2-001.json").is_file())
            saved = json.loads((out_dir / "summary.json").read_text())
            self.assertEqual(saved["run_status"], "completed")


if __name__ == "__main__":
    unittest.main()
