"""Offline canaries for the Workflow 2.0 native artifact broker."""

from __future__ import annotations

import base64
import json
from pathlib import Path
import tempfile
import unittest

from legalitaw.evaluation.agentic import _deterministic_results, judge_task
from legalitaw.agentic.loader import select_tasks
from legalitaw.agentic.models import WorkflowArtifact, WorkflowSubmission
from legalitaw.agentic.native_artifacts import DOCX_MEDIA_TYPE, docx_features, render_docx
from legalitaw.agentic.submissions import import_submission, save_submission
from legalitaw.agentic.workspace import PublicDocumentReader, public_envelope_paths


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW2_ROOT = ROOT / "task_workflow2.0"


def redline_source() -> str:
    articles = "\n".join(
        f"## Articolo {index} — Titolo\nTesto integrale dell'articolo {index}."
        for index in range(1, 16)
    )
    return f"""# Accordo sul trattamento dei dati — redline
{articles}
## Allegato A — Trattamenti
Dati e interessati.
## Allegato B — Sicurezza
Misure [[DEL:facoltative]] [[INS:obbligatorie]] [[NOTE:Art. 15; modifica richiesta dall'art. 28 GDPR.]]
## Punti non cedibili
- Misure di sicurezza.
## Punti trattabili
- Tempi operativi.
## Risposta al comitato rischi
Il testo non è firmabile senza la modifica indicata.
"""


def _canary_source(task_id: str, deliverable: str, *, redline: bool = False) -> str:
    if task_id == "WF2-001":
        return redline_source()
    if task_id == "WF2-008":
        articles = "\n".join(
            f"## Articolo {index} — Titolo\nTesto integrale {index}."
            for index in range(1, 10)
        )
        return (
            "# Contratto di assunzione — canary\n"
            + articles.replace(
                "Testo integrale 7.",
                "[[DEL:durata cinque anni]] [[INS:durata tre anni]] "
                "[[NOTE:Art. 7; durata ridotta a tre anni ai sensi dell'art. 2125 c.c.]]",
            )
        )
    if task_id in {"WF2-013", "WF2-014"} and deliverable.endswith(".docx"):
        return (
            "# Redline canary\n"
            "## Articolo 1 — Oggetto\n"
            "Testo [[DEL:non conforme]] [[INS:conforme]]. "
            "[[NOTE:Articolo 1; modifica necessaria per il pilot.]]\n"
        )
    if deliverable.endswith(".docx"):
        if redline:
            return (
                "# Canary redline\n## Articolo 1 — Oggetto\n"
                "Testo [[DEL:originario]] [[INS:aggiornato]] "
                "[[NOTE:Articolo 1; modifica canary per verificare il formato.]]"
            )
        return "# Canary memo\n## Esito\nDocumento pilot generato correttamente."
    return "# Canary pilot\n## Esito\nArtifact Markdown generato correttamente."


class Workflow2NativeArtifactTest(unittest.TestCase):
    def test_every_public_input_is_readable_as_text(self) -> None:
        for task in select_tasks(["all"], root=WORKFLOW2_ROOT):
            with self.subTest(task=task.spec.task_id):
                reader = PublicDocumentReader(task)
                sources = [
                    path
                    for path in public_envelope_paths(task)
                    if path != "public/01_task.md"
                ]
                self.assertTrue(sources)
                for relative in sources:
                    self.assertTrue(reader.document_pages(relative), relative)

    def test_all_hundred_profiles_have_explicit_runtime_contracts(self) -> None:
        tasks = select_tasks(["all"], root=WORKFLOW2_ROOT)
        self.assertEqual(len(tasks), 100)
        self.assertEqual(sum(len(task.rubric.criteria) for task in tasks), 5032)
        for task in tasks:
            self.assertEqual(
                task.spec.submission_contract,
                "prompt_only_free_artifacts_v1",
            )
            self.assertNotIn("record_decision", task.spec.tool_allowlist)
            self.assertEqual(len(judge_task(task).criteria), len(task.rubric.criteria))
            self.assertEqual(task.spec.pilot_status, "ready")
            self.assertIn(
                task.spec.gold_legal_signoff,
                {"pending", "delegated_maintainer_release"},
            )
            self.assertEqual(
                task.spec.document_coverage_policy,
                "observe_only",
            )
            routing = getattr(task.spec, "runtime_routing", None)
            if routing is None:
                routing = json.loads(
                    (task.directory / "private/runtime_routing.json").read_text(
                        encoding="utf-8"
                    )
                )
            self.assertEqual(routing["criteria_count"], len(task.rubric.criteria))
            self.assertEqual(
                set(routing["criteria"]),
                {criterion.id for criterion in task.rubric.criteria},
            )
            deterministic = {
                criterion.id
                for criterion in task.rubric.criteria
                if criterion.evaluation_mode == "deterministic"
            }
            self.assertEqual(
                {check.id for check in task.spec.artifact_checks},
                {
                    f"{task.spec.task_id}-{criterion_id.replace('.', '')}"
                    for criterion_id in deterministic
                },
            )

    def test_redline_docx_has_native_revisions_comments_and_passes_structure(self) -> None:
        task = select_tasks(["WF2-001"], root=WORKFLOW2_ROOT)[0]
        source = redline_source()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / task.spec.expected_deliverable
            counts = render_docx(
                source,
                path,
                redline=True,
                preset="contract_negotiation_brief",
                author="WF2-001 canary",
            )
            self.assertEqual(counts, {"insertions": 1, "deletions": 1, "comments": 1})
            features = docx_features(path)
            self.assertTrue(features["track_revisions_enabled"])
            self.assertEqual(features["insertions"], 1)
            self.assertEqual(features["deletions"], 1)
            self.assertEqual(features["comments"], 1)

            raw = path.read_bytes()
            submission = WorkflowSubmission(
                task_id=task.spec.task_id,
                model="native-canary",
                source="fixture",
                execution_mode="generic_agent",
                artifacts=[
                    WorkflowArtifact(
                        path=task.spec.expected_deliverable,
                        content=source,
                        media_type=DOCX_MEDIA_TYPE,
                        binary_base64=base64.b64encode(raw).decode("ascii"),
                    )
                ],
            )
            results, _ = _deterministic_results(task, submission)
            self.assertEqual(
                {item.id: item.verdict for item in results},
                {"A.1": "pass", "A.2": "pass", "A.3": "pass", "A.4": "pass"},
            )

    def test_native_docx_round_trips_through_persistence_and_import(self) -> None:
        task = select_tasks(["WF2-002"], root=WORKFLOW2_ROOT)[0]
        source = """# Memo termini
## Opposizione allo stato passivo
- Decorrenza: 13 luglio 2026
- Scadenza: 14 settembre 2026
## Ricorso per cassazione
- Decorrenza: 26 gennaio 2027
- Scadenza: 25 febbraio 2027
- Tempo residuo al 1 febbraio 2027: 24 giorni
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / task.spec.expected_deliverable
            render_docx(
                source,
                path,
                redline=False,
                preset="standard_business_brief",
                author="WF2-002 canary",
            )
            raw = path.read_bytes()
            submission = WorkflowSubmission(
                task_id=task.spec.task_id,
                model="native-canary",
                source="fixture",
                execution_mode="generic_agent",
                artifacts=[
                    WorkflowArtifact(
                        path=task.spec.expected_deliverable,
                        content=source,
                        media_type=DOCX_MEDIA_TYPE,
                        binary_base64=base64.b64encode(raw).decode("ascii"),
                    )
                ],
            )
            persisted = root / "persisted"
            save_submission(submission, persisted)
            self.assertEqual((persisted / task.spec.expected_deliverable).read_bytes(), raw)
            self.assertTrue(
                (persisted / f"{task.spec.expected_deliverable}.extracted.txt").is_file()
            )
            imported = import_submission(task, source=persisted, model="roundtrip")
            self.assertIsNotNone(imported.artifacts[0].binary_base64)
            self.assertIn("14 settembre 2026", imported.artifacts[0].content)


if __name__ == "__main__":
    unittest.main()
