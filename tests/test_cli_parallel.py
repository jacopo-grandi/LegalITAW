import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from legalitaw.cli.parallel import child_argv, done_task_ids, run_parallel, split_blocks
from legalitaw.cli.v2 import _lancia_run_argv, _run_command, build_parser


def fake_task(task_id: str):
    return SimpleNamespace(spec=SimpleNamespace(task_id=task_id))


def write_manifest(results: Path, run_id: str, **fields) -> Path:
    run_root = results / "v2-runs" / run_id
    run_root.mkdir(parents=True, exist_ok=True)
    manifest = {"run_id": run_id, "model": "fixture", "run_status": "running", "attempts": {}}
    manifest.update(fields)
    (run_root / "run_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return run_root


class SplitTests(unittest.TestCase):
    def test_hundred_tasks_in_four_blocks_match_the_manual_split(self) -> None:
        ids = [f"WF2-{n:03d}" for n in range(1, 101)]
        blocks = split_blocks(ids, 4)
        self.assertEqual([len(b) for b in blocks], [25, 25, 25, 25])
        self.assertEqual([b[0] for b in blocks], ["WF2-001", "WF2-026", "WF2-051", "WF2-076"])

    def test_uneven_and_small_splits(self) -> None:
        self.assertEqual([len(b) for b in split_blocks(list(range(10)), 3)], [4, 3, 3])
        self.assertEqual(split_blocks([1, 2], 4), [[1], [2]])
        with self.assertRaises(ValueError):
            split_blocks([1], 0)


class ChildArgvTests(unittest.TestCase):
    def test_forwards_run_options_but_not_parallel_ones(self) -> None:
        args = build_parser().parse_args(
            ["run", "--model", "m", "--parallel", "4", "--max-task-attempts", "2", "--results", "/r"]
        )
        argv = child_argv(args, ["WF2-001", "WF2-002"])
        self.assertIn("--max-task-attempts", argv)
        self.assertEqual(argv[-3:], ["--tasks", "WF2-001", "WF2-002"])
        self.assertNotIn("--parallel", argv)
        self.assertNotIn("--skip-done", argv)
        self.assertEqual(argv[argv.index("--results") + 1], "/r")


class DoneTasksTests(unittest.TestCase):
    def test_aborted_task_and_other_models_are_not_done(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)
            write_manifest(results, "a", completed_task_ids=["WF2-001"], failed_task_ids=["WF2-002"])
            write_manifest(
                results,
                "b",
                completed_task_ids=["WF2-026"],
                failed_task_ids=["WF2-027"],
                run_status="aborted",
                aborted_task_id="WF2-027",
            )
            write_manifest(results, "c", model="altro", completed_task_ids=["WF2-051"])
            self.assertEqual(
                done_task_ids(results, model="fixture"), {"WF2-001", "WF2-002", "WF2-026"}
            )


class FakeProcess:
    def __init__(self, on_start):
        self._ticks = 0
        on_start()

    def poll(self):
        self._ticks += 1
        return 0 if self._ticks > 1 else None

    def wait(self, timeout=None):
        return 0


class RunParallelTests(unittest.TestCase):
    def test_launches_one_process_per_block_and_reports_cost(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp) / "res"
            launched: list[list[str]] = []

            def popen(argv, **kwargs):
                ids = argv[argv.index("--tasks") + 1 :]
                launched.append(ids)

                def finish():
                    run_root = write_manifest(
                        results,
                        f"run-{ids[0]}",
                        requested_task_ids=ids,
                        completed_task_ids=ids,
                        failed_task_ids=[],
                        run_status="completed",
                        attempts={i: [f"attempts/m/x/{i}"] for i in ids},
                    )
                    for i in ids:
                        attempt = run_root / "attempts" / "m" / "x" / i
                        attempt.mkdir(parents=True)
                        (attempt / "submission.json").write_text(
                            json.dumps({"model_call_metrics": {"estimated_cost_usd": 0.5}}),
                            encoding="utf-8",
                        )

                return FakeProcess(finish)

            args = build_parser().parse_args(
                ["run", "--model", "fixture", "--parallel", "2", "--results", str(results),
                 "--log-dir", str(Path(tmp) / "logs")]
            )
            out = io.StringIO()
            tasks = [fake_task(f"WF2-{n:03d}") for n in range(1, 5)]
            code = run_parallel(args, tasks, popen=popen, sleep=lambda _: None, out=out)
            self.assertEqual(code, 0)
            self.assertEqual(launched, [["WF2-001", "WF2-002"], ["WF2-003", "WF2-004"]])
            text = out.getvalue()
            self.assertIn("4 consegnati, 0 falliti, $2.00", text)
            self.assertIn("run-WF2-003", text)
            self.assertTrue((Path(tmp) / "logs" / "b2.log").exists())


class RunCommandTests(unittest.TestCase):
    def _run(self, argv, results: Path, captured: dict):
        args = build_parser().parse_args(argv + ["--results", str(results)])

        def parallel(a, tasks):
            captured["ids"] = [t.spec.task_id for t in tasks]
            return 0

        return _run_command(
            args,
            generate_v2_run_fn=lambda *a, **k: (_ for _ in ()).throw(AssertionError("no seriale")),
            score_v2_source_fn=lambda *a, **k: None,
            validate_runtime_fn=lambda *a, **k: None,
            run_parallel_fn=parallel,
        )

    def test_parallel_with_skip_done_only_sends_missing_tasks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)
            write_manifest(results, "a", completed_task_ids=["WF2-001"], failed_task_ids=["WF2-003"])
            captured: dict = {}
            self._run(
                ["run", "--model", "fixture", "--limit", "4", "--parallel", "2", "--skip-done"],
                results,
                captured,
            )
            self.assertEqual(captured["ids"], ["WF2-002", "WF2-004"])

    def test_parallel_refuses_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                self._run(["run", "--model", "fixture", "--parallel", "4", "--score"], Path(tmp), {})


class LanciaTests(unittest.TestCase):
    def test_lancia_becomes_the_standard_parallel_run(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["lancia", "gemini-4-neon", "--risultati", "/base"])
        run = parser.parse_args(_lancia_run_argv(args, today="2026-11-20"))
        self.assertEqual(run.command, "run")
        self.assertEqual(run.model, "gemini-4-neon")
        self.assertEqual(run.parallel, 4)
        self.assertEqual(run.results, Path("/base/gemini-4-neon-low-wf2-100"))
        self.assertEqual(run.log_dir, Path("/base/logs/2026-11-20_gemini-4-neon-low"))
        self.assertFalse(run.skip_done)

    def test_lancia_options(self) -> None:
        parser = build_parser()
        args = parser.parse_args(
            ["lancia", "deepseek/deepseek-v4-flash", "--ragionamento", "high", "--blocchi", "2",
             "--nome", "flash-high", "--riprendi", "--risultati", "/b"]
        )
        run = parser.parse_args(_lancia_run_argv(args, today="2026-11-20"))
        self.assertEqual(run.parallel, 2)
        self.assertEqual(run.results, Path("/b/flash-high-wf2-100"))
        self.assertTrue(run.skip_done)
        default = parser.parse_args(["lancia", "deepseek/deepseek-v4-flash", "--risultati", "/b"])
        self.assertEqual(
            parser.parse_args(_lancia_run_argv(default, today="x")).results,
            Path("/b/deepseek-deepseek-v4-flash-low-wf2-100"),
        )


if __name__ == "__main__":
    unittest.main()
