"""Offline checks for the WF2-003 agentic workspace pilot."""

from __future__ import annotations

from contextlib import redirect_stderr
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

from legalitaw.benchmark.agentic_service import (
    generate_agentic_submission,
    persist_failed_run,
    persist_run,
)
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
    MatterWorkspace,
    WorkspaceError,
    WorkspaceRunFailure,
    _xlsx_pages,
    build_workspace_prompt,
    model_workspace_tools,
)
from legalitaw.modeling.usage import ModelCallResult
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

DELFINA_DOCUMENT = (
    "public/documents/Allegati/Accordo_quadro_fornitura_Delfina_Motori.pdf"
)
ALL_SOURCE_DOCUMENTS = sorted(
    path.relative_to(
        WORKFLOW2_ROOT / "dossier_analysis/003_mna_red_flag_data_room"
    ).as_posix()
    for path in (
        WORKFLOW2_ROOT
        / "dossier_analysis/003_mna_red_flag_data_room/public/documents"
    ).rglob("*")
    if path.is_file() and not path.name.startswith(".")
)


def analysis_decision_call(*, with_evidence: bool = True) -> dict[str, object]:
    evidence = (
        [
            {
                "document": DELFINA_DOCUMENT,
                "locator": "art. 14",
                "finding": "Il cliente può recedere in caso di cambio di controllo.",
            }
        ]
        if with_evidence
        else []
    )
    return {
        "tool": "record_decision",
        "arguments": {
            "stage": "analysis",
            "objective": "Valutare la materialità del rapporto con Delfina Motori.",
            "evidence": evidence,
            "documents_not_reviewed": [],
            "inference": (
                "Il diritto di recesso rende il cambio di controllo rilevante "
                "per la continuità dei ricavi."
            ),
            "alternatives_considered": [
                "Trattare il punto come sola representation & warranty."
            ],
            "decision": (
                "Segnalare il rischio come red flag ad alta priorità e proporre "
                "una condizione sospensiva."
            ),
            "confidence": "high",
            "missing_information": [
                "Non è disponibile un consenso preventivo di Delfina."
            ],
            "checks_performed": [],
            "next_action": "Redigere il deliverable con fonte e rimedio.",
        },
    }


def final_check_call() -> dict[str, object]:
    return {
        "tool": "record_decision",
        "arguments": {
            "stage": "final_check",
            "objective": "Verificare il deliverable prima della submission.",
            "evidence": [
                {
                    "document": DELFINA_DOCUMENT,
                    "locator": "art. 14",
                    "finding": "La fonte citata sostiene il rischio descritto.",
                }
            ],
            "documents_not_reviewed": [],
            "inference": "La conclusione è coerente con la fonte pubblica osservata.",
            "alternatives_considered": [],
            "decision": "Il deliverable è pronto per la submission.",
            "confidence": "high",
            "missing_information": [],
            "checks_performed": [
                "Verificati titolo, priorità, esposizione, rimedio e fonte.",
                "Verificata la sintesi per l'investment committee.",
            ],
            "next_action": "Sottoporre il deliverable.",
        },
    }


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


class SequentialGateway:
    def __init__(self) -> None:
        self.prompts: list[str] = []
        self.responses = [
            {"tool": "list_files", "arguments": {}},
            {
                "tool": "search_documents",
                "arguments": {"query": "Delfina", "limit": 5},
            },
            *[
                {
                    "tool": "open_document",
                    "arguments": {"path": path, "page": 1},
                }
                for path in ALL_SOURCE_DOCUMENTS
            ],
            {
                "tool": "write_artifact",
                "arguments": {"path": "due_diligence_red_flags.md", "content": DELIVERABLE},
            },
            {
                "tool": "submit",
                "arguments": {"path": "due_diligence_red_flags.md"},
            },
        ]

    def complete(self, model: str, prompt: str) -> ModelCallResult:
        self.prompts.append(prompt)
        response = self.responses[len(self.prompts) - 1]
        return ModelCallResult(
            text=json.dumps(response, ensure_ascii=False),
            metrics={
                "provider": "fixture",
                "model": model,
                "latency_ms": 1,
                "input_tokens": 10,
                "output_tokens": 5,
                "total_tokens": 15,
            },
        )


class ExhaustingGateway(SequentialGateway):
    def __init__(self) -> None:
        self.prompts = []
        self.responses = [
            {"tool": "list_files", "arguments": {}},
            {
                "tool": "write_artifact",
                "arguments": {
                    "path": "due_diligence_red_flags.md",
                    "content": DELIVERABLE,
                },
            },
            {
                "tool": "write_artifact",
                "arguments": {
                    "path": "due_diligence_red_flags.md",
                    "content": DELIVERABLE,
                },
            },
            {
                "tool": "write_artifact",
                "arguments": {
                    "path": "due_diligence_red_flags.md",
                    "content": DELIVERABLE,
                },
            },
            {
                "tool": "write_artifact",
                "arguments": {
                    "path": "due_diligence_red_flags.md",
                    "content": DELIVERABLE,
                },
            },
        ]


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

    def test_workspace_prompt_contains_no_hidden_output_contract(self) -> None:
        prompt = build_workspace_prompt(
            self.task,
            current_step=1,
            max_steps=40,
            allowed_tools=model_workspace_tools(self.task),
        )
        self.assertNotIn(self.task.spec.agentic_output_format or "", prompt)
        self.assertNotIn("due_diligence_red_flags.md", prompt)
        for instruction in self.task.spec.agentic_instructions:
            self.assertNotIn(instruction, prompt)
        self.assertNotIn("record_decision", prompt)

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
        workspace = MatterWorkspace(self.timeline_task)
        try:
            path = "public/documents/SPA_Ardesia_Belmonte.docx"
            metadata = workspace.execute("inspect_metadata", {"path": path})
            self.assertGreaterEqual(metadata["page_count"], 3)
            content = "\n".join(
                workspace.execute(
                    "open_document",
                    {"path": path, "page": page},
                )["content"]
                for page in range(1, metadata["page_count"] + 1)
            )
            self.assertIn("Allegato D – Adempimenti di Closing", content)
            self.assertIn("Allegato E – Dati rilevanti", content)
            self.assertIn("1.184.000.000", content)
        finally:
            workspace.close()

    def test_timeline_exact_dates_are_judged_under_free_artifact_contract(self) -> None:
        submission = WorkflowSubmission(
            task_id=self.timeline_task.spec.task_id,
            model="fixture-model",
            source="fixture",
            execution_mode="agentic_workspace",
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
            execution_mode="agentic_workspace",
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

    def test_workspace_copies_public_inputs_and_blocks_private_traversal(self) -> None:
        workspace = MatterWorkspace(self.task)
        root = workspace.root
        try:
            listing = workspace.execute("list_files", {})
            self.assertEqual(listing["count"], 28)
            self.assertFalse(workspace.manifest["private_envelope_mounted"])
            self.assertFalse(workspace.manifest["shell_available"])
            self.assertFalse(workspace.manifest["workspace_network_available"])
            self.assertFalse((workspace.matter / "private").exists())
            with self.assertRaises(WorkspaceError):
                workspace.execute(
                    "open_document",
                    {"path": "../private/rubric.json"},
                )
            self.assertEqual(workspace.trace[-1]["status"], "error")
            self.assertIn("non accessibile", workspace.trace[-1]["error"])
            hits = workspace.execute(
                "search_documents",
                {"query": "Delfina Motori", "limit": 5},
            )
            self.assertTrue(hits["hits"])
            self.assertTrue(
                any("Delfina" in item["snippet"] for item in hits["hits"])
            )
        finally:
            workspace.close()
        self.assertFalse(root.exists())

    def test_runtime_coverage_distinguishes_search_from_open(self) -> None:
        workspace = MatterWorkspace(self.task)
        try:
            hits = workspace.execute(
                "search_documents",
                {"query": "Delfina Motori", "limit": 5},
            )
            hit_path = hits["hits"][0]["path"]
            searched = workspace.document_coverage()
            self.assertIn(hit_path, searched["search_only_sources"])
            self.assertIn(hit_path, searched["unopened_sources"])

            workspace.execute("open_document", {"path": hit_path, "page": 1})
            opened = workspace.document_coverage()
            self.assertNotIn(hit_path, opened["search_only_sources"])
            self.assertNotIn(hit_path, opened["unopened_sources"])
            row = next(
                item for item in opened["by_source"] if item["path"] == hit_path
            )
            self.assertEqual(row["opened_pages"], [1])
            self.assertEqual(row["fully_read_pages"], [1])
            self.assertLess(opened["document_open_rate"], 1.0)
            self.assertEqual(
                opened["policy"],
                "observe_only",
            )
        finally:
            workspace.close()

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

    def test_decision_log_tool_is_not_part_of_the_free_output_contract(self) -> None:
        workspace = MatterWorkspace(self.task)
        try:
            with self.assertRaisesRegex(
                WorkspaceError,
                "tool non autorizzato",
            ):
                workspace.execute("record_decision", {})

            workspace.execute(
                "write_artifact",
                {"path": "risposta-libera.md", "content": DELIVERABLE},
            )
            submitted = workspace.execute(
                "submit",
                {"path": "risposta-libera.md"},
            )
            self.assertEqual(submitted["submitted"], "risposta-libera.md")
            self.assertEqual(workspace.decision_log, [])
        finally:
            workspace.close()

    def test_judge_receives_public_evidence_but_no_private_envelope(self) -> None:
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
            execution_mode="agentic_workspace",
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
            execution_mode="agentic_workspace",
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
            execution_mode="agentic_workspace",
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
            execution_mode="agentic_workspace",
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

    def test_fixture_agent_uses_tools_and_persists_replay_evidence(self) -> None:
        gateway = SequentialGateway()
        submission = generate_agentic_submission(
            self.task,
            model="fixture-agent",
            gateway=gateway,  # type: ignore[arg-type]
            max_steps=34,
            timeout_seconds=60,
        )
        self.assertEqual(submission.execution_mode, "agentic_workspace")
        self.assertEqual(
            [item["tool"] for item in submission.tool_trace],
            [
                "list_files",
                "search_documents",
                *["open_document"] * len(ALL_SOURCE_DOCUMENTS),
                "write_artifact",
                "submit",
            ],
        )
        self.assertNotIn("Delfina Motori", gateway.prompts[0])
        self.assertIn("Delfina Motori", gateway.prompts[2])
        self.assertNotIn("private/", "\n".join(gateway.prompts))
        self.assertIn('current_step="1"', gateway.prompts[0])
        self.assertIn('remaining_steps_including_current="34"', gateway.prompts[0])
        self.assertIn(
            'phase="finalization"',
            gateway.prompts[2 + len(ALL_SOURCE_DOCUMENTS)],
        )
        expected_calls = len(ALL_SOURCE_DOCUMENTS) + 4
        self.assertEqual(submission.model_call_metrics["call_count"], expected_calls)
        self.assertEqual(submission.model_call_metrics["total_tokens"], expected_calls * 15)
        self.assertEqual(submission.decision_log, [])

        with tempfile.TemporaryDirectory() as directory:
            run_dir = persist_run(
                self.task,
                submission,
                results_root=Path(directory),
            )
            manifest = json.loads(
                (run_dir / "run_manifest.json").read_text(encoding="utf-8")
            )
            self.assertTrue((run_dir / "tool_trace.json").is_file())
            self.assertFalse((run_dir / "decision_log.json").exists())
            self.assertTrue((run_dir / "workspace_manifest.json").is_file())
            self.assertFalse(manifest["private_inputs_exposed_to_model"])
            self.assertEqual(
                manifest["workspace_policy"],
                {
                    "private_envelope_mounted": False,
                    "shell_available": False,
                    "workspace_network_available": False,
                },
            )
            self.assertTrue(manifest["tool_trace_sha256"])
            self.assertIsNone(manifest["decision_log_sha256"])
            self.assertEqual(manifest["decision_log_entries"], 0)
            self.assertEqual(
                manifest["document_coverage"]["source_count"],
                27,
            )
            self.assertFalse(manifest["document_coverage"]["all_sources_opened"])
            coverage_paths = {
                item["path"]
                for item in manifest["document_coverage"]["by_source"]
            }
            self.assertIn(DELFINA_DOCUMENT, coverage_paths)

    def test_exhausted_run_persists_trace_metrics_and_partial_artifact(self) -> None:
        gateway = ExhaustingGateway()
        with self.assertLogs("legalitaw.agentic.workspace", level="INFO") as logs:
            with self.assertRaises(WorkspaceRunFailure) as captured:
                generate_agentic_submission(
                    self.task,
                    model="fixture-exhausted-agent",
                    gateway=gateway,  # type: ignore[arg-type]
                    max_steps=5,
                    timeout_seconds=60,
                )

        failure = captured.exception
        self.assertEqual(failure.error_type, "WorkspaceError")
        self.assertEqual(failure.model_call_metrics["call_count"], 5)
        self.assertEqual(failure.model_call_metrics["total_tokens"], 75)
        self.assertEqual(len(failure.tool_trace), 5)
        self.assertEqual(failure.artifacts[0].content, DELIVERABLE)
        self.assertEqual(failure.workspace_manifest["run_status"], "failed")
        self.assertEqual(failure.workspace_manifest["finalization_steps"], 2)
        self.assertEqual(len(failure.decision_log), 0)
        self.assertIn("step=1/5", "\n".join(logs.output))
        self.assertIn("tool=list_files", "\n".join(logs.output))
        self.assertIn('phase="finalization"', gateway.prompts[3])
        self.assertIn(
            "Tool consentiti in questo turno: submit, write_artifact",
            gateway.prompts[3],
        )
        self.assertIn("non ammesso", failure.tool_trace[-1]["error"])

        with tempfile.TemporaryDirectory() as directory:
            run_dir = persist_failed_run(
                self.task,
                failure,
                results_root=Path(directory),
            )
            manifest = json.loads(
                (run_dir / "run_manifest.json").read_text(encoding="utf-8")
            )
            failure_payload = json.loads(
                (run_dir / "failure.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["run_status"], "failed")
            self.assertFalse(manifest["private_inputs_exposed_to_model"])
            self.assertEqual(failure_payload["model_call_metrics"]["call_count"], 5)
            self.assertTrue((run_dir / "tool_trace.json").is_file())
            self.assertTrue((run_dir / "decision_log.json").is_file())
            self.assertTrue((run_dir / "workspace_manifest.json").is_file())
            self.assertEqual(manifest["decision_log_entries"], 0)
            self.assertTrue(manifest["decision_log_sha256"])
            self.assertTrue(
                (
                    run_dir
                    / "partial_artifacts"
                    / "due_diligence_red_flags.md"
                ).is_file()
            )
            self.assertFalse((run_dir / "submission.json").exists())


if __name__ == "__main__":
    unittest.main()
