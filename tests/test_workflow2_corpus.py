from __future__ import annotations

import json
from pathlib import Path
import unittest

from legalitaw.evaluation.agentic import judge_task
from legalitaw.agentic.loader import discover_tasks, validate_corpus


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "task_workflow2.0"
COHORT_THREE = {f"WF2-{index:03d}" for index in range(21, 31)}
MIGRATED = {f"WF2-{index:03d}" for index in range(31, 101)}


class Workflow2CorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tasks = discover_tasks(CORPUS)
        cls.by_id = {task.spec.task_id: task for task in cls.tasks}

    def test_all_hundred_profiles_load(self) -> None:
        payload = validate_corpus(CORPUS)
        self.assertEqual(payload["task_count"], 100)
        self.assertEqual(payload["criterion_count"], 5032)
        self.assertEqual(
            set(self.by_id),
            {f"WF2-{index:03d}" for index in range(1, 101)},
        )

    def test_cohort_three_has_public_private_boundary_and_self_contained_prompt(self) -> None:
        for task_id in sorted(COHORT_THREE):
            task = self.by_id[task_id]
            prompt = (task.directory / "public/01_task.md").read_text(encoding="utf-8")
            self.assertNotIn("response_template.md", prompt, task_id)
            self.assertIn("## Allegati obbligatori", prompt, task_id)
            self.assertTrue((task.directory / "public/03_legal_sources.md").is_file(), task_id)
            documents = [
                path
                for path in (task.directory / "public/documents").iterdir()
                if path.is_file() and not path.name.startswith(".")
            ]
            self.assertTrue(documents, task_id)
            self.assertFalse([path for path in documents if path.suffix.lower() == ".md"], task_id)
            for document in documents:
                self.assertIn(f"`{document.name}`", prompt, f"{task_id}: {document.name}")
            self.assertTrue(all(not value.startswith("private/") for value in task.spec.public_inputs), task_id)

    def test_judge_contract_can_be_built_for_every_new_task(self) -> None:
        for task_id in sorted(COHORT_THREE):
            task = self.by_id[task_id]
            contract = judge_task(task)
            expected = sum(item.evaluation_mode == "judge" for item in task.rubric.criteria)
            self.assertEqual(len(contract.criteria), expected, task_id)
            self.assertTrue(contract.query.strip(), task_id)
            self.assertTrue(all(item.match_criteria.strip() for item in contract.criteria), task_id)
            self.assertTrue(
                any(item.verification_class != "judge" for item in contract.criteria),
                f"{task_id}: all criteria collapsed to generic judge verification",
            )

    def test_migrated_profiles_have_complete_routing(self) -> None:
        family_counts: dict[str, int] = {}
        for task_id in sorted(MIGRATED):
            task = self.by_id[task_id]
            family_counts[task.spec.workflow_family] = (
                family_counts.get(task.spec.workflow_family, 0) + 1
            )
            self.assertEqual(task.spec.status, "pilot_ready", task_id)
            self.assertTrue(task.spec.pilot_ready, task_id)
            self.assertEqual(task.spec.migration["source"], "task_workflow2.0.1", task_id)
            routing = json.loads(
                (task.directory / "private/runtime_routing.json").read_text(encoding="utf-8")
            )
            rubric_ids = {criterion.id for criterion in task.rubric.criteria}
            self.assertEqual(routing["criteria_count"], len(rubric_ids), task_id)
            self.assertEqual(set(routing["criteria"]), rubric_ids, task_id)
            for relative in task.spec.public_inputs:
                self.assertTrue((task.directory / relative).is_file(), f"{task_id}: {relative}")

        self.assertEqual(
            family_counts,
            {
                "document_review_and_revision": 24,
                "dossier_analysis": 22,
                "procedural_computation": 24,
            },
        )

    def test_judge_contract_can_be_built_for_all_migrated_tasks(self) -> None:
        for task_id in sorted(MIGRATED):
            task = self.by_id[task_id]
            contract = judge_task(task)
            self.assertEqual(len(contract.criteria), len(task.rubric.criteria), task_id)
            self.assertTrue(contract.query.strip(), task_id)
            self.assertTrue(all(item.match_criteria.strip() for item in contract.criteria), task_id)

    def test_material_legal_fixes_are_active(self) -> None:
        sha = self.by_id["WF2-021"].directory
        sha_reference = (sha / "public/02_reference_pack.md").read_text(encoding="utf-8")
        self.assertIn("art. 838-bis c.p.c.", sha_reference)
        self.assertIn("art. 838-ter c.p.c.", sha_reference)
        self.assertIn("art. 838-quater c.p.c.", sha_reference)
        self.assertNotIn("D.Lgs. 17 gennaio 2003, n. 5", sha_reference)

        sanctions = self.by_id["WF2-028"].directory
        sanctions_reference = (sanctions / "public/02_reference_pack.md").read_text(encoding="utf-8")
        self.assertIn("designazione diretta", sanctions_reference)
        self.assertIn("non deve essere usato per costruire una soglia di ownership", sanctions_reference)
        routing = json.loads((sanctions / "private/runtime_routing.json").read_text(encoding="utf-8"))
        self.assertEqual(routing["criteria_count"], 46)
        self.assertEqual(len(routing["criteria"]), 46)


if __name__ == "__main__":
    unittest.main()
