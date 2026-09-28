"""Offline checks for the WF2-003 agentic workspace pilot."""

from __future__ import annotations

import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from legalitaw.evaluation.agentic import (
    _evidence_within_scope,
    _find_quote_span,
    _normative_references,
    evaluation_payload,
    evaluate_submission,
    judge_task,
)
from legalitaw.agentic.loader import select_tasks, validate_corpus
from legalitaw.agentic.models import WorkflowArtifact, WorkflowSubmission
from legalitaw.agentic.submissions import import_submission
from legalitaw.agentic.workspace import (
    PublicDocumentReader,
    WorkspaceError,
    _xlsx_pages,
)
from legalitaw.schemas import JudgeVote, ResponseEvidence


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW2_ROOT = ROOT / "task_workflow2.0"
DELIVERABLE = """# Nota di due diligence — red flag materiali

## 1 — Cambio di controllo sul cliente principale
- Priorità: alta
- Esposizione stimata: 34% del fatturato
- Rimedio proposto: condizione sospensiva
- Fonte: Accordo_quadro_fornitura_Delfina_Motori.pdf — art. 14

La committente dispone di un diritto di recesso da presidiare prima del closing.

## Sintesi per l'investment committee
Il consenso di Delfina è un punto dirimente.
"""

TIMELINE_DELIVERABLE = """# Timeline signing–closing — Ardesia / Belmonte

## Timeline
| Data o termine | Natura | Vincolatività | Evento, dipendenze e calcolo | Fonte | Soggetto onerato |
|---|---|---|---|---|---|
| 12 febbraio 2027 | determinata | vincolante | Data di sottoscrizione | SPA, frontespizio | Parti |
| 22 febbraio 2027 | determinata | vincolante | notifica golden power: 10 Giorni dalla sottoscrizione | art. 6.2 | Parti |
| 26 febbraio 2027 | determinata | vincolante | richieste di consenso ai terzi: 10 Giorni Lavorativi dalla sottoscrizione | art. 6.3 | Venditore |
| 5 marzo 2027 | determinata | vincolante | comunicazione AGCM: 15 Giorni Lavorativi dalla sottoscrizione | art. 6.1 | Compratore |
| entro 10 Giorni Lavorativi dall'avveramento o rinuncia dell'ultima condizione | relativa al Closing | vincolante | finestra massima; preavviso di almeno 5 Giorni Lavorativi | artt. 9.1-9.2 | Compratore |
| 30 giugno 2027 | determinata | programmatica | Data Obiettivo di Closing | art. 7.1 | Parti |
| 31 ottobre 2027 | determinata | vincolante | Long-Stop Date | art. 8.1 | Parti |
| 15 novembre 2027 | determinata | vincolante | termine per il recesso | art. 8.2 | ciascuna Parte |
| diciottesimo mese successivo al Closing | relativa al Closing | vincolante | svincolo del conto | art. 3.2(b) | banca |
| diciotto mesi dalla data del Closing | relativa al Closing | vincolante | pretese indennitarie generali | art. 11.3 | Compratore |
| cinque anni dalla data del Closing | relativa al Closing | vincolante | pretese fiscali, contributive e ambientali | art. 11.3 | Compratore |
| 30 Giorni dalla data del Closing | relativa al Closing | vincolante | comunicazione a Immobiliare Cascine | Allegato B.3 | Società |

## Checklist delle condizioni sospensive
| Condizione | Stato | Termine o evento | Soggetto onerato | Attività | Rinunciabilità | Conseguenze |
|---|---|---|---|---|---|---|
| AGCM | pendente | non determinabile | Compratore | comunicazione | no | recesso alla Long-Stop Date |
| golden power | pendente | non determinabile | Parti | notifica | no | recesso alla Long-Stop Date |
| Aeromec | pendente | riscontro scritto | Venditore | richiesta | sì | recesso alla Long-Stop Date |
| Banca Sant'Orsola | pendente | riscontro scritto | Venditore | richiesta | sì | recesso alla Long-Stop Date |
| assenza EPR | pendente | fino al Closing | Venditore | gestione ordinaria | sì | recesso alla Long-Stop Date |

## Valutazione della data obiettivo di Closing
La data obiettivo è programmatica; la data effettiva dipende dall'ultima condizione.
"""

class PassJudge:
    model = "fixture-pass-judge"
    strategy = "single"
    judge_models = {"A": model}

    def evaluate(self, **_: object) -> dict[str, str]:
        return {"verdict": "pass", "reasoning": "fixture"}


class EvidenceJudge:
    model = "fixture-evidence-judge"
    strategy = "single"
    judge_models = {"A": model}

    def evaluate(self, **kwargs: object) -> JudgeVote:
        match_criteria = str(kwargs.get("match_criteria") or "")
        is_non_presence = any(
            marker in match_criteria
            for marker in (
                "Operazione logica: assenza/divieto",
                "Operazione logica: condizionale se menzionato",
            )
        )
        is_section_scoped = "Ambito di decisione: soltanto la sezione" in match_criteria
        evidence = []
        if not is_non_presence:
            evidence = [
                (
                    "Il consenso di Delfina è un punto dirimente."
                    if is_section_scoped
                    else "La committente dispone di un diritto di recesso da presidiare "
                    "prima del closing."
                )
            ]
        return JudgeVote(
            judge_id="A",
            provider="fixture",
            model=self.model,
            verdict="pass",
            reasoning="fixture con evidenza",
            evidence=evidence,
            evidence_status="not_found" if is_non_presence else "found",
            status="ok",
            attempts=1,
            latency_ms=1,
        )


class MissingTopicBugJudge(EvidenceJudge):
    model = "fixture-missing-topic-bug"
    judge_models = {"A": model}

    def evaluate(self, **kwargs: object) -> JudgeVote:
        vote = super().evaluate(**kwargs)
        match_criteria = str(kwargs.get("match_criteria") or "")
        if any(
            marker in match_criteria
            for marker in (
                "Operazione logica: assenza/divieto",
                "Operazione logica: condizionale se menzionato",
            )
        ):
            return vote.model_copy(
                update={
                    "verdict": "fail",
                    "reasoning": "bug: tema non trovato",
                    "evidence": [],
                    "evidence_status": "not_found",
                }
            )
        return vote


class Workflow2AgenticWorkspaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.task = select_tasks(["WF2-003"], root=WORKFLOW2_ROOT)[0]
        cls.timeline_task = select_tasks(["WF2-010"], root=WORKFLOW2_ROOT)[0]

    def test_adapter_exposes_all_hundred_supported_pilots(self) -> None:
        payload = validate_corpus(WORKFLOW2_ROOT)
        self.assertEqual(payload["task_count"], 100)
        self.assertEqual(payload["criterion_count"], 5032)
        self.assertEqual(self.task.spec.status, "pilot_ready")
        self.assertEqual(
            self.task.spec.supported_execution_modes,
            ["generic_agent", "text_bundle", "agentic_workspace"],
        )
        self.assertEqual(
            self.task.spec.output_mode,
            "prompt_only_free_artifacts",
        )
        self.assertEqual(
            self.task.spec.expected_deliverable,
            "due_diligence_red_flags.md",
        )
        self.assertEqual(len(self.task.spec.public_inputs), 28)
        self.assertEqual(self.task.spec.version, "2.0.0-draft+agentic.3")
        self.assertNotIn("record_decision", self.task.spec.tool_allowlist)


    def test_external_submission_accepts_free_nested_artifact_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            nested = source / "consegna" / "memo-scelto-da-next-os.md"
            nested.parent.mkdir()
            nested.write_text(DELIVERABLE, encoding="utf-8")
            submission = import_submission(
                self.task,
                source=source,
                model="next-os-fixture",
            )
        self.assertEqual(
            [artifact.path for artifact in submission.artifacts],
            ["consegna/memo-scelto-da-next-os.md"],
        )

    def test_timeline_profile_is_distinct_and_fully_routed(self) -> None:
        task = self.timeline_task
        self.assertEqual(task.spec.workflow_family, "procedural_computation")
        self.assertEqual(task.spec.as_of_date, "2027-02-12")
        self.assertEqual(
            task.spec.expected_deliverable,
            "spa_signing_closing_timeline.md",
        )
        self.assertIn("public/03_temporal_assumptions.md", task.spec.public_inputs)
        counts: dict[str, int] = {}
        for criterion in task.rubric.criteria:
            counts[criterion.verification_class] = (
                counts.get(criterion.verification_class, 0) + 1
            )
        self.assertEqual(
            counts,
            {"judge": 12, "deterministic": 13, "span": 54, "scansione": 18},
        )
        self.assertNotIn("unassigned", counts)
        criteria = {item.id: item for item in task.rubric.criteria}
        self.assertEqual(criteria["B.9"].criterion_logic, "conditional_if_mentioned")
        self.assertEqual(
            criteria["B.71"].criterion_logic,
            "conditional_if_mentioned",
        )
        self.assertEqual(criteria["B.42"].criterion_logic, "prohibited_presence")

    def test_timeline_docx_is_paged_without_hiding_late_annexes(self) -> None:
        reader = PublicDocumentReader(self.timeline_task)
        pages = reader.document_pages("public/documents/SPA_Ardesia_Belmonte.docx")
        self.assertGreaterEqual(len(pages), 3)
        content = "\n".join(pages)
        self.assertIn("Allegato D – Adempimenti di Closing", content)
        self.assertIn("Allegato E – Dati rilevanti", content)
        self.assertIn("1.184.000.000", content)

    def test_document_reader_blocks_private_and_undeclared_paths(self) -> None:
        reader = PublicDocumentReader(self.task)
        for relative in ("private/rubric.json", "public/../private/rubric.json", "public/response_template.md"):
            with self.assertRaises(WorkspaceError):
                reader.document_pages(relative)

    def test_timeline_exact_dates_are_judged_under_free_artifact_contract(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.timeline_task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="spa_signing_closing_timeline.md",
                    content=TIMELINE_DELIVERABLE,
                )
            ],
            model_call_metrics={"provider": "fixture"},
        )
        score = evaluate_submission(self.timeline_task, submission, judge=PassJudge())
        deterministic = {
            item.id: item.verdict
            for item in score.criteria_results
            if item.consensus_method == "deterministic"
        }
        self.assertEqual(deterministic, {})
        self.assertEqual(
            score.judge_diagnostics["legacy_artifact_checks"]["count"],
            13,
        )
        self.assertTrue(all(item.verdict == "pass" for item in score.criteria_results))
        self.assertEqual(
            score.judge_diagnostics["judge_panel"]["agent_provider"],
            "fixture",
        )

    def test_timeline_judge_context_includes_temporal_assumptions(self) -> None:
        normalized = judge_task(self.timeline_task)
        self.assertIn("soglie nazionali", normalized.query)
        self.assertIn("90 giorni dall'avvio", normalized.query)
        self.assertNotIn("private/", normalized.query)

    def test_evidence_locator_accepts_typographic_equivalents(self) -> None:
        content = "Non si può assumere che l’esposizione — già incerta — sia coperta."
        quote = "Non si può assumere che l'esposizione - già incerta - sia coperta."
        span = _find_quote_span(content, quote)
        self.assertIsNotNone(span)
        assert span is not None
        self.assertEqual(content[slice(*span)], content)

    def test_all_criteria_receive_a_settled_route(self) -> None:
        counts: dict[str, int] = {}
        for criterion in self.task.rubric.criteria:
            counts[criterion.verification_class] = (
                counts.get(criterion.verification_class, 0) + 1
            )
        self.assertEqual(
            counts,
            {"deterministic": 6, "scansione": 13, "span": 36, "judge": 2},
        )
        self.assertNotIn("unassigned", counts)

    def test_criterion_logic_and_scope_are_explicit(self) -> None:
        criteria = {item.id: item for item in self.task.rubric.criteria}
        self.assertEqual(criteria["B.26"].criterion_logic, "prohibited_presence")
        self.assertIn(
            "La mancata menzione del tema soddisfa il criterio",
            criteria["B.26"].normalized_match_criteria,
        )
        self.assertEqual(criteria["B.32"].criterion_logic, "conditional_if_mentioned")
        self.assertIn(
            "Se il tema non è trattato, assegna PASS",
            criteria["B.32"].normalized_match_criteria,
        )
        self.assertEqual(criteria["B.51"].evaluation_scope, "section")
        self.assertEqual(
            criteria["B.51"].scope_locator,
            "Sintesi per l'investment committee",
        )
        self.assertIn(
            "Le occorrenze fuori da questa sezione non possono determinare il verdetto",
            criteria["B.51"].normalized_match_criteria,
        )

    def test_section_scope_rejects_evidence_from_the_body(self) -> None:
        quote = (
            "La committente dispone di un diritto di recesso da presidiare prima del closing."
        )
        start = DELIVERABLE.index(quote)
        submission = WorkflowSubmission(
            task_id=self.task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="due_diligence_red_flags.md",
                    content=DELIVERABLE,
                )
            ],
        )
        criterion = next(item for item in self.task.rubric.criteria if item.id == "B.51")
        evidence = ResponseEvidence(
            artifact="due_diligence_red_flags.md",
            quote=quote,
            char_start=start,
            char_end=start + len(quote),
            line_start=10,
            line_end=10,
        )

        accepted, rejected = _evidence_within_scope(
            submission,
            criterion,
            [evidence],
        )

        self.assertEqual(accepted, [])
        self.assertEqual(rejected, [quote])


    def test_xlsx_reader_extracts_cells_dates_and_cached_formulas(self) -> None:
        path = (
            WORKFLOW2_ROOT
            / "dossier_analysis"
            / "006_aml_suspicious_activity"
            / "public"
            / "documents"
            / "Allegato_3_Estratto_conto.xlsx"
        )
        content = "\n".join(_xlsx_pages(path))
        self.assertIn("[FOGLIO Estratto conto]", content)
        self.assertIn("A13=2026-05-04", content)
        self.assertIn("F14=78500", content)
        self.assertIn("G13==C10+N(F13)-N(E13) -> 23200", content)


    def test_judge_receives_public_evidence_but_no_private_envelope(self) -> None:
        with patch.dict(os.environ, {"LEGALITA_JUDGE_CONTEXT": "full"}):
            normalized = judge_task(self.task)
        self.assertEqual(len(normalized.criteria), 57)
        self.assertIn("Vetralia Componenti", normalized.query)
        self.assertLess(len(normalized.query), 150_000)
        self.assertIn("Accordo_quadro_fornitura_Delfina_Motori.pdf", normalized.query)
        self.assertNotIn("concentrazioni soglia di contaminazione", normalized.query)
        self.assertNotIn("private/", normalized.query)
        self.assertNotIn("criteria_atomized", normalized.query)
        self.assertIn("unica fonte dei requisiti", normalized.query)

    def test_legacy_artifact_checks_are_not_applied_to_free_outputs(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="due_diligence_red_flags.md",
                    content=DELIVERABLE,
                )
            ],
        )
        score = evaluate_submission(self.task, submission, judge=PassJudge())
        self.assertTrue(score.all_pass)
        self.assertEqual(score.n_required, 57)
        self.assertEqual(
            score.judge_diagnostics["verification_class_rates"]["deterministic"][
                "evaluated"
            ],
            6,
        )
        deterministic = {
            item.id: item.verdict
            for item in score.criteria_results
            if item.consensus_method == "deterministic"
        }
        self.assertEqual(deterministic, {})
        self.assertEqual(
            score.judge_diagnostics["legacy_artifact_checks"],
            {
                "status": "diagnostic_only_not_applied",
                "contract": "prompt_only_free_artifacts_v1",
                "count": 6,
                "check_ids": [f"WF2-003-A{index}" for index in range(1, 7)],
            },
        )
        payload = evaluation_payload(score)
        self.assertEqual(
            payload["submission_contract"],
            "prompt_only_free_artifacts_v1",
        )
        self.assertEqual(
            payload["criterion_routing_contract"],
            "all_criteria_semantic_judge_v1",
        )

    def test_hidden_normative_allowlist_is_not_applied(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="due_diligence_red_flags.md",
                    content=(
                        DELIVERABLE
                        + "\nIl rilievo è valutato anche ai sensi dell'art. 99 del "
                        "D.Lgs. 152/2006 e dell'art. 2087 c.c.\n"
                    ),
                )
            ],
        )

        score = evaluate_submission(self.task, submission, judge=PassJudge())
        result = next(item for item in score.criteria_results if item.id == "A.6")

        self.assertNotEqual(result.consensus_method, "deterministic")
        self.assertEqual(result.verdict, "pass")
        self.assertEqual(
            score.judge_diagnostics["legacy_artifact_checks"]["status"],
            "diagnostic_only_not_applied",
        )

    def test_normative_extractor_ignores_contract_articles(self) -> None:
        references = _normative_references(
            "Si applicano gli artt. 242 e 244 del D.Lgs. 152/2006 e l'art. 23 "
            "del D.Lgs. 81/2015. Il contratto richiama inoltre gli artt. 10 e 14."
        )
        self.assertEqual(
            {key for key, _ in references},
            {
                "d.lgs.152/2006#242",
                "d.lgs.152/2006#244",
                "d.lgs.81/2015#23",
            },
        )

    def test_timeline_normative_aliases_are_canonicalized(self) -> None:
        references = _normative_references(
            "Si applicano gli artt. 1187, 1353, 1358, 1359, 1360 e 2963 c.c.; "
            "l'art. 16 L. 287/1990; il Reg. (CE) 139/2004 e il D.L. 21/2012."
        )
        self.assertEqual(
            {key for key, _ in references},
            {
                "c.c.#1187",
                "c.c.#1353",
                "c.c.#1358",
                "c.c.#1359",
                "c.c.#1360",
                "c.c.#2963",
                "l.287/1990",
                "regolamento(ce)139/2004",
                "d.l.21/2012",
            },
        )

    def test_every_criterion_result_has_auditable_response_evidence(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="due_diligence_red_flags.md",
                    content=DELIVERABLE,
                )
            ],
        )
        score = evaluate_submission(self.task, submission, judge=EvidenceJudge())

        self.assertEqual(len(score.criteria_results), 57)
        self.assertTrue(
            all(
                item.evidence_status in {"found", "global_scan"}
                or (
                    item.evidence_status == "not_found"
                    and item.criterion_logic in {
                        "prohibited_presence",
                        "conditional_if_mentioned",
                    }
                )
                for item in score.criteria_results
            )
        )
        anchored = next(item for item in score.criteria_results if item.id == "B.1")
        self.assertEqual(
            anchored.response_evidence[0].artifact,
            "due_diligence_red_flags.md",
        )
        self.assertGreaterEqual(anchored.response_evidence[0].line_start, 1)
        self.assertEqual(
            score.judge_diagnostics["criterion_evidence"]["issues"],
            {},
        )
        self.assertFalse(
            score.judge_diagnostics["criterion_evidence"]["review_required"]
        )

    def test_lint_flags_impossible_negative_and_conditional_failures(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="generic_agent",
            artifacts=[
                WorkflowArtifact(
                    path="due_diligence_red_flags.md",
                    content=DELIVERABLE,
                )
            ],
        )

        score = evaluate_submission(
            self.task,
            submission,
            judge=MissingTopicBugJudge(),
        )
        flags = score.judge_diagnostics["criterion_evidence"]["review_flags"]

        self.assertIn("B.26", flags["absence_fail_without_positive_evidence"])
        self.assertIn("B.32", flags["conditional_fail_without_trigger_evidence"])
        self.assertIn("B.51", flags["scoped_fail_without_in_scope_evidence"])
        self.assertTrue(
            score.judge_diagnostics["criterion_evidence"]["review_required"]
        )
        self.assertEqual(
            score.judge_diagnostics["judge_panel"]["reporting_status"],
            "diagnostic_only",
        )


if __name__ == "__main__":
    unittest.main()
