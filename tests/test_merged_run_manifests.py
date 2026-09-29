import json
import tempfile
import unittest
from pathlib import Path

from legalitaw.benchmark.agentic_v2 import RUN_MANIFEST_SCHEMA, _find_v2_manifest


def _write(root: Path, name: str, model: str, tasks: list[str], created_at: str) -> None:
    directory = root / "v2-runs" / name
    directory.mkdir(parents=True)
    (directory / "run_manifest.json").write_text(
        json.dumps(
            {
                "schema_version": RUN_MANIFEST_SCHEMA,
                "run_id": name,
                "model": model,
                "created_at": created_at,
                "requested_task_ids": tasks,
            }
        ),
        encoding="utf-8",
    )


class MergedRunManifestTest(unittest.TestCase):
    def test_parallel_blocks_and_reruns_are_merged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root, "a", "m", ["WF2-001", "WF2-002"], "2026-09-29T10:00:00")
            _write(root, "b", "m", ["WF2-003"], "2026-09-29T10:00:01")
            _write(root, "c", "m", ["WF2-002"], "2026-09-29T12:00:00")
            merged = _find_v2_manifest(root)
        self.assertEqual(merged["requested_task_ids"], ["WF2-001", "WF2-002", "WF2-003"])
        self.assertEqual(merged["merged_from"], ["a", "b", "c"])

    def test_different_models_are_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root, "a", "m1", ["WF2-001"], "1")
            _write(root, "b", "m2", ["WF2-002"], "2")
            with self.assertRaises(ValueError):
                _find_v2_manifest(root)


if __name__ == "__main__":
    unittest.main()
