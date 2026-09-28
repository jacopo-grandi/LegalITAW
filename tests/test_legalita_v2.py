import json
import os
import tempfile
import unittest
import zipfile
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from legalitaw.benchmark.agentic_service import persist_failed_run, persist_run
from legalitaw.benchmark.agentic_v2 import (
    RUN_MANIFEST_SCHEMA,
    generate_v2_run,
    resolved_run_source,
    score_v2_source,
)
from legalitaw.agentic.loader import select_tasks
from legalitaw.agentic.models import WorkflowArtifact, WorkflowSubmission
from legalitaw.agentic.workspace import WorkspaceRunFailure
from legalitaw.artifacts import write_json_atomic
from legalitaw.cli.v2 import _run_command, _runtime_config, build_parser
from legalitaw.config import build_judge_runtime_config
from legalitaw.modeling.runtime import ModelResponseError


REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW2_ROOT = REPO_ROOT / "task_workflow2.0"


def submission(task_id: str, text: str = "Risposta") -> WorkflowSubmission:
    return WorkflowSubmission(
        task_id=task_id,
        model="fixture-system",
        source="fixture",
        execution_mode="generic_agent",
        artifacts=[WorkflowArtifact(path="answer.md", content=text)],
    )


def score_payload(task_id: str, passed: int = 1) -> dict:
    return {
        "task_id": task_id,
        "n_required": 1,
        "n_required_passed": passed,
        "n_required_unresolved": 0,
        "all_pass": bool(passed),
        "reasoning_scoring_status": "complete",
    }


def runtime_config(batch_size: int = 10):
    return build_judge_runtime_config(
        judge_strategy="batched_single",
        judge_a_provider="openai",
        judge_a_model="gpt-5.6-luna",
        batch_size=batch_size,
    )


def write_top_manifest(root: Path, task_ids: list[str]) -> None:
    write_json_atomic(
        root / "run_manifest.json",
        {
            "schema_version": RUN_MANIFEST_SCHEMA,
            "run_id": "fixture-run",
            "model": "fixture-system",
            "corpus": "task_workflow2.0",
            "requested_task_ids": task_ids,
            "completed_task_ids": [],
            "failed_task_ids": [],
            "attempts": {task_id: [] for task_id in task_ids},
        },
    )


class LegalitaV2CLITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tasks = select_tasks(["WF2-001", "WF2-002", "WF2-003"], root=WORKFLOW2_ROOT)

    def _score(self, source: Path, out: Path, *, tasks=None, config=None, **kwargs):
        calls: list[str] = []

        def evaluate(task, imported, *, judge):
            calls.append(task.spec.task_id)
            return score_payload(task.spec.task_id)

        summary = score_v2_source(
            source,
            tasks=tasks or self.tasks,
            runtime_config=config or runtime_config(),
            out_dir=out,
            create_judge_fn=lambda _: object(),
            evaluate_submission_fn=evaluate,
            evaluation_payload_fn=lambda value: dict(value),
            **kwargs,
        )
        return summary, calls

    def test_resolver_prefers_completed_newest_and_records_decision(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            failed = root / "model" / "old" / task.spec.task_id
            failed.mkdir(parents=True)
            write_json_atomic(
                failed / "run_manifest.json",
                {
                    "task_id": task.spec.task_id,
                    "run_status": "failed",
                    "created_at": "2026-09-08T14:11:00+00:00",
                },
            )
            write_json_atomic(failed / "failure.json", {"message": "timeout"})

            older = root / "model" / "middle" / task.spec.task_id
            older.mkdir(parents=True)
            write_json_atomic(
                older / "run_manifest.json",
                {
                    "task_id": task.spec.task_id,
                    "run_status": "completed",
                    "created_at": "2026-09-08T14:15:00+00:00",
                },
            )
            (older / "answer.md").write_text("vecchia", encoding="utf-8")

            newest = root / "model" / "new" / task.spec.task_id
            newest.mkdir(parents=True)
            write_json_atomic(
                newest / "run_manifest.json",
                {
                    "task_id": task.spec.task_id,
                    "run_status": "completed",
                    "created_at": "2026-09-08T14:21:00+00:00",
                },
            )
            (newest / "answer.md").write_text("nuova", encoding="utf-8")

            with resolved_run_source(root, tasks=[task]) as resolved:
                self.assertEqual(
                    resolved.selected[task.spec.task_id].directory,
                    newest.resolve(),
                )
                self.assertEqual(len(resolved.attempts[task.spec.task_id]), 3)
                self.assertIn("più recente", resolved.decisions[task.spec.task_id])

    def test_submission_json_wins_tie_and_true_ambiguity_stops(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inferred = root / "a" / task.spec.task_id
            inferred.mkdir(parents=True)
            (inferred / "answer.md").write_text("inferita", encoding="utf-8")
            explicit = root / "b" / task.spec.task_id
            explicit.mkdir(parents=True)
            explicit_submission = submission(task.spec.task_id, "esplicita").model_copy(
                update={"created_at": ""}
            )
            write_json_atomic(
                explicit / "submission.json",
                explicit_submission.model_dump(),
            )

            with resolved_run_source(root, tasks=[task]) as resolved:
                self.assertEqual(
                    resolved.selected[task.spec.task_id].directory,
                    explicit.resolve(),
                )
                self.assertIn("submission.json", resolved.decisions[task.spec.task_id])

            (explicit / "submission.json").unlink()
            (explicit / "answer.md").write_text("seconda", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "tentativi indistinguibili"):
                with resolved_run_source(root, tasks=[task]):
                    pass

    def test_flat_nested_and_zip_have_same_score(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            flat = base / "flat"
            (flat / task.spec.task_id).mkdir(parents=True)
            (flat / task.spec.task_id / "answer.md").write_text("uguale", encoding="utf-8")

            nested = base / "nested"
            target = nested / "fixture-system" / "timestamp" / task.spec.task_id
            target.mkdir(parents=True)
            (target / "answer.md").write_text("uguale", encoding="utf-8")

            archive_path = base / "run.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.write(
                    flat / task.spec.task_id / "answer.md",
                    f"wrapped/{task.spec.task_id}/answer.md",
                )

            summaries = []
            for index, source in enumerate((flat, nested, archive_path)):
                summary, calls = self._score(
                    source,
                    base / f"score-{index}",
                    tasks=[task],
                )
                summaries.append(summary)
                self.assertEqual(calls, [task.spec.task_id])
            self.assertEqual([item["overall_score"] for item in summaries], [1.0] * 3)
            self.assertTrue(all(item["partial"] for item in summaries))

    def test_unsafe_zip_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "unsafe.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../escape.md", "no")
            with self.assertRaisesRegex(ValueError, "path non sicuro"):
                with resolved_run_source(archive_path, tasks=[self.tasks[0]]):
                    pass

    def test_manifest_denominator_counts_failed_and_missing(self) -> None:
        completed, failed, missing = self.tasks
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "run"
            root.mkdir()
            write_top_manifest(root, [task.spec.task_id for task in self.tasks])
            ready_dir = root / completed.spec.task_id
            ready_dir.mkdir()
            (ready_dir / "answer.md").write_text("ok", encoding="utf-8")
            failed_dir = root / failed.spec.task_id
            failed_dir.mkdir()
            write_json_atomic(
                failed_dir / "run_manifest.json",
                {"task_id": failed.spec.task_id, "run_status": "failed"},
            )
            write_json_atomic(failed_dir / "failure.json", {"message": "errore"})

            summary, calls = self._score(root, Path(temporary) / "score")

            self.assertEqual(calls, [completed.spec.task_id])
            self.assertFalse(summary["partial"])
            self.assertEqual(summary["n_expected_tasks"], 3)
            self.assertEqual(summary["n_technical_failure_tasks"], 1)
            self.assertEqual(summary["n_missing_tasks"], 1)
            self.assertAlmostEqual(summary["overall_score"], 1 / 3)

    def test_resume_invalidates_artifact_rubric_and_judge_configuration(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source = base / "run"
            source.mkdir()
            write_top_manifest(source, [task.spec.task_id])
            task_dir = source / task.spec.task_id
            task_dir.mkdir()
            artifact = task_dir / "answer.md"
            artifact.write_text("versione uno", encoding="utf-8")
            out = base / "score"

            _, first = self._score(source, out, tasks=[task])
            second_summary, second = self._score(source, out, tasks=[task])
            self.assertEqual(first, [task.spec.task_id])
            self.assertEqual(second, [])
            self.assertEqual(second_summary["checkpoint_reused_count"], 1)

            artifact.write_text("versione due", encoding="utf-8")
            _, artifact_calls = self._score(source, out, tasks=[task])
            self.assertEqual(artifact_calls, [task.spec.task_id])

            changed_rubric = task.rubric.model_copy(
                update={"rubric_version": task.rubric.rubric_version + "+changed"}
            )
            changed_task = replace(task, rubric=changed_rubric)
            _, rubric_calls = self._score(source, out, tasks=[changed_task])
            self.assertEqual(rubric_calls, [task.spec.task_id])

            _, config_calls = self._score(
                source,
                out,
                tasks=[task],
                config=runtime_config(batch_size=7),
            )
            self.assertEqual(config_calls, [task.spec.task_id])

    def test_preflight_cost_and_manifest_exist_before_judge_creation(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source = base / "run"
            (source / task.spec.task_id).mkdir(parents=True)
            (source / task.spec.task_id / "answer.md").write_text("ok", encoding="utf-8")
            out = base / "score"

            def create_judge(_):
                self.assertTrue((out / "preflight.json").is_file())
                self.assertTrue((out / "cost_estimate.json").is_file())
                self.assertTrue((out / "run_manifest.json").is_file())
                return object()

            score_v2_source(
                source,
                tasks=[task],
                runtime_config=runtime_config(),
                out_dir=out,
                create_judge_fn=create_judge,
                evaluate_submission_fn=lambda task, submission, judge: score_payload(task.spec.task_id),
                evaluation_payload_fn=lambda value: dict(value),
            )

    def test_fresh_creates_a_separate_score_run(self) -> None:
        task = self.tasks[0]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source = base / "run"
            (source / task.spec.task_id).mkdir(parents=True)
            (source / task.spec.task_id / "answer.md").write_text("ok", encoding="utf-8")
            summary, _ = self._score(source, base / "scores", tasks=[task], fresh=True)
            self.assertNotEqual(Path(summary["out_dir"]), base / "scores")
            self.assertTrue(Path(summary["out_dir"]).parent.samefile(base / "scores"))

    def test_run_manifest_and_end_to_end_score(self) -> None:
        tasks = self.tasks[:2]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)

            def generate(task, **kwargs):
                return submission(task.spec.task_id, f"output {task.spec.task_id}")

            run_root = generate_v2_run(
                tasks,
                model="fixture-system",
                results_root=base,
                generate_submission_fn=generate,
                persist_run_fn=persist_run,
                persist_failed_run_fn=persist_failed_run,
            )
            manifest = json.loads((run_root / "run_manifest.json").read_text())
            self.assertEqual(manifest["requested_task_ids"], [task.spec.task_id for task in tasks])
            self.assertEqual(manifest["completed_task_ids"], [task.spec.task_id for task in tasks])
            self.assertEqual(manifest["failed_task_ids"], [])
            self.assertTrue(all(len(items) == 1 for items in manifest["attempts"].values()))

            summary, calls = self._score(run_root, run_root / "score-run", tasks=tasks)
            self.assertEqual(calls, [task.spec.task_id for task in tasks])
            self.assertFalse(summary["partial"])
            self.assertEqual(summary["n_expected_tasks"], 2)

    def test_generation_retry_preserves_both_attempts(self) -> None:
        task = self.tasks[0]
        calls = 0

        def generate(selected, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise RuntimeError("errore fixture")
            return submission(selected.spec.task_id)

        with tempfile.TemporaryDirectory() as temporary:
            run_root = generate_v2_run(
                [task],
                model="fixture-system",
                results_root=Path(temporary),
                max_task_attempts=2,
                generate_submission_fn=generate,
                persist_run_fn=persist_run,
                persist_failed_run_fn=persist_failed_run,
            )
            manifest = json.loads((run_root / "run_manifest.json").read_text())
            self.assertEqual(len(manifest["attempts"][task.spec.task_id]), 2)
            self.assertEqual(manifest["completed_task_ids"], [task.spec.task_id])
            self.assertEqual(manifest["failed_task_ids"], [])

    def test_non_retryable_provider_error_aborts_the_whole_run_once(self) -> None:
        calls = 0

        def generate(task, **kwargs):
            nonlocal calls
            calls += 1
            try:
                raise ModelResponseError(
                    "request non supportata",
                    metrics={},
                    retryable=False,
                )
            except ModelResponseError as cause:
                failure = WorkspaceRunFailure(
                    str(cause),
                    task_id=task.spec.task_id,
                    model="fixture-system",
                    error_type=type(cause).__name__,
                    artifacts=[],
                    tool_trace=[],
                    decision_log=[],
                    workspace_manifest={"run_status": "failed"},
                    model_call_metrics={},
                    raw_response=None,
                )
                raise failure from cause

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(WorkspaceRunFailure):
                generate_v2_run(
                    self.tasks[:2],
                    model="fixture-system",
                    results_root=root,
                    max_task_attempts=2,
                    generate_submission_fn=generate,
                    persist_run_fn=persist_run,
                    persist_failed_run_fn=persist_failed_run,
                )
            run_root = next((root / "v2-runs").iterdir())
            manifest = json.loads((run_root / "run_manifest.json").read_text())
            self.assertEqual(calls, 1)
            self.assertEqual(manifest["run_status"], "aborted")
            self.assertEqual(manifest["aborted_task_id"], "WF2-001")
            self.assertEqual(len(manifest["attempts"]["WF2-001"]), 1)
            self.assertEqual(manifest["attempts"]["WF2-002"], [])

    def test_keyboard_interrupt_marks_run_interrupted(self) -> None:
        def generate(task, **kwargs):
            raise KeyboardInterrupt

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(KeyboardInterrupt):
                generate_v2_run(
                    [self.tasks[0]],
                    model="fixture-system",
                    results_root=root,
                    generate_submission_fn=generate,
                    persist_run_fn=persist_run,
                    persist_failed_run_fn=persist_failed_run,
                )
            run_root = next((root / "v2-runs").iterdir())
            manifest = json.loads((run_root / "run_manifest.json").read_text())
            self.assertEqual(manifest["run_status"], "interrupted")
            self.assertEqual(manifest["completed_task_ids"], [])

    def test_cli_limit_is_generation_only_and_score_uses_injected_service(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["run", "--model", "fixture", "--limit", "3"])
        captured: dict[str, object] = {}

        def generate(tasks, **kwargs):
            captured["task_ids"] = [task.spec.task_id for task in tasks]
            return Path("/tmp/fixture-run")

        def unexpected_score(*args, **kwargs):
            raise AssertionError("judge/scoring non deve essere creato per default")

        _run_command(
            args,
            generate_v2_run_fn=generate,
            score_v2_source_fn=unexpected_score,
            validate_runtime_fn=lambda *args, **kwargs: None,
        )
        self.assertEqual(captured["task_ids"], ["WF2-001", "WF2-002", "WF2-003"])

        scored = parser.parse_args(
            ["run", "--model", "fixture", "--limit", "1", "--score"]
        )
        score_calls: list[Path] = []

        def score_service(source, **kwargs):
            score_calls.append(source)
            return {
                "overall_score": 1.0,
                "n_scored_tasks": 1,
                "n_expected_tasks": 1,
                "n_technical_failure_tasks": 0,
                "n_missing_tasks": 0,
                "task_scoring_coverage": 1.0,
                "n_required_unresolved": 0,
                "partial": False,
                "out_dir": "/tmp/fixture-score",
            }

        _run_command(
            scored,
            generate_v2_run_fn=lambda *args, **kwargs: Path("/tmp/fixture-run"),
            score_v2_source_fn=score_service,
            validate_runtime_fn=lambda *args, **kwargs: None,
        )
        self.assertEqual(score_calls, [Path("/tmp/fixture-run")])

    def test_default_cli_judge_is_the_validated_terna(self) -> None:
        args = build_parser().parse_args(["score", "run", "--preflight-only"])
        with patch.dict(os.environ, {}, clear=True):
            config = _runtime_config(args)
        self.assertEqual(config.strategy, "paired_consensus")
        self.assertEqual(
            (config.judge_a.provider, config.judge_a.model), ("typesafe", "jev-1.13.0")
        )
        self.assertEqual(
            (config.judge_b.provider, config.judge_b.model), ("openai", "gpt-5.6-luna")
        )
        self.assertEqual(
            (config.judge_c.provider, config.judge_c.model), ("anthropic", "claude-opus-5-5")
        )
        self.assertEqual(config.batch_size, 10)
        self.assertEqual(config.audit_sample_rate, 0.05)

    def test_default_judge_context_is_compact(self) -> None:
        from legalitaw.evaluation.agentic import judge_context_mode

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(judge_context_mode(), "compact")


if __name__ == "__main__":
    unittest.main()
