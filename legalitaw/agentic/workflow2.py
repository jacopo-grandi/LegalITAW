"""Non-destructive runtime profiles for the imported Workflow 2.0 corpus.

The imported corpus remains canonical and read-only. This module projects an
explicitly reviewed subset into the executable agentic contract without
rewriting task specs or rubrics in place.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .models import LoadedWorkflowTask, WorkflowRubric, WorkflowTaskSpec
from .deterministic_overlay import apply_deterministic_overlay


COMMON_TOOLS = [
    "list_files",
    "search_documents",
    "open_document",
    "inspect_metadata",
    "write_artifact",
    "submit",
]

WF2_003_OUTPUT_FORMAT = """# Nota di due diligence — red flag materiali
## 1 — Titolo del red flag
- Priorità: ...
- Esposizione stimata: ...
- Rimedio proposto: indennizzo specifico | condizione sospensiva | price adjustment | representation & warranty
- Fonte: nome_file — clausola, articolo, pagina o voce precisa
Testo dell'analisi.

Ripeti i blocchi in ordine di priorità e chiudi con:
## Sintesi per l'investment committee"""

WF2_010_OUTPUT_FORMAT = """# Timeline signing–closing — Ardesia / Belmonte
## Timeline
Usa una tabella con le colonne: Data o termine; Natura (determinata, relativa al Closing, non determinabile); Vincolatività (vincolante o programmatica); Evento, dipendenze e calcolo; Fonte; Soggetto onerato.
Per ogni computo indica evento iniziale, numero e tipo di giorni e trattamento di sabati, domeniche e festività.

## Checklist delle condizioni sospensive
Usa una riga per ciascuna delle cinque condizioni, con: condizione; stato alla data di sottoscrizione; termine o evento determinante; soggetto onerato; attività richiesta; rinunciabilità; conseguenze del mancato avveramento.

## Valutazione della data obiettivo di Closing
Rispondi in modo motivato alla domanda del consiglio, separando date contrattuali, scenari procedimentali e informazioni non determinabili."""


def _wf2_010_exact_checks() -> list[dict[str, Any]]:
    deliverable = "spa_signing_closing_timeline.md"
    patterns: dict[str, list[str]] = {
        "C.1": [
            r"^(?=[^\n]*\b12\s+febbraio\s+2027\b)(?=[^\n]*Data\s+di\s+[Ss]ottoscrizione)[^\n]+$"
        ],
        "C.2": [
            r"^(?=[^\n]*\b22\s+febbraio\s+2027\b)(?=[^\n]*(?:golden\s+power|notifica))[^\n]+$"
        ],
        "C.3": [
            r"^(?=[^\n]*\b26\s+febbraio\s+2027\b)(?=[^\n]*(?:terzi|consens\w*))[^\n]+$"
        ],
        "C.4": [
            r"^(?=[^\n]*\b5\s+marzo\s+2027\b)(?=[^\n]*AGCM)[^\n]+$"
        ],
        "C.5": [
            r"^(?=[^\n]*10\s+Giorni\s+Lavorativi)(?=[^\n]*(?:ultima|avverat|rinunciat))[^\n]+$",
            r"^(?=[^\n]*preavviso)(?=[^\n]*5\s+Giorni\s+Lavorativi)[^\n]+$",
        ],
        "C.6": [
            r"^(?=[^\n]*\b31\s+ottobre\s+2027\b)(?=[^\n]*Long[-–— ]Stop)[^\n]+$"
        ],
        "C.7": [
            r"^(?=[^\n]*\b15\s+novembre\s+2027\b)(?=[^\n]*recesso)[^\n]+$"
        ],
        "C.8": [
            r"^(?=[^\n]*(?:diciottesimo|18(?:[°ºo]|esimo)?)\s+mes\w*)(?=[^\n]*Closing)(?=[^\n]*(?:svincol|conto))[^\n]+$"
        ],
        "C.9": [
            r"^(?=[^\n]*(?:diciotto|18)\s+mesi)(?=[^\n]*Closing)(?=[^\n]*(?:pretes\w*|indenn\w*))[^\n]+$"
        ],
        "C.10": [
            r"^(?=[^\n]*(?:cinque|5)\s+anni)(?=[^\n]*Closing)(?=[^\n]*(?:fiscal\w*|contribut\w*|ambient\w*))[^\n]+$"
        ],
        "C.11": [
            r"^(?=[^\n]*30\s+Giorn\w*)(?=[^\n]*Closing)(?=[^\n]*Immobiliare\s+Cascine)[^\n]+$"
        ],
        "C.12": [
            r"^(?=[^\n]*\b30\s+giugno\s+2027\b)(?=[^\n]*Data\s+Obiettivo)[^\n]+$"
        ],
    }
    return [
        {
            "id": f"WF2-010-{criterion_id.replace('.', '')}",
            "type": "required_regex",
            "artifact": deliverable,
            "patterns": criterion_patterns,
        }
        for criterion_id, criterion_patterns in patterns.items()
    ]


TASK_PROFILES: dict[str, dict[str, Any]] = {
    "WF2-001": {
        "criteria_count": 49,
        "document_count": 1,
        "deliverable": "DPA_Nimbus_Aurea_redline.docx",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2", "A.3", "A.4"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-09-14",
        "workflow_family": "document_review_and_revision",
        "subtask": "dpa_review_redline",
        "granularity": "whole_contract",
        "legal_area": ["privacy", "data_protection", "commercial_contracts"],
        "document_type": "data_processing_agreement",
        "estimated_minutes": 120,
        "capabilities": [
            "contract_navigation",
            "targeted_redlining",
            "legal_issue_spotting",
            "negotiation_prioritization",
            "artifact_generation",
        ],
        "agentic_instructions": [
            "Consulta la bozza completa soltanto tramite i tool del matter.",
            "Restituisci il contratto integrale: articoli 1-15, Allegato A e Allegato B.",
            "Nel sorgente del DOCX racchiudi ogni soppressione in [[DEL:...]], ogni inserimento in [[INS:...]] e aggiungi subito dopo [[NOTE:...]] con clausola e norma.",
            "Ogni modifica deve avere una nota; limita i riferimenti normativi alle fonti del reference pack.",
            "Chiudi con due sezioni distinte: Punti non cedibili e Punti trattabili, oltre alla risposta al comitato rischi.",
        ],
        "output_format": """# Accordo sul trattamento dei dati — redline
## Articolo 1 — ...
Riporta il testo integrale. Per ogni modifica usa in sequenza [[DEL:testo originale]] [[INS:testo proposto]] [[NOTE:Art. X; spiegazione; riferimento normativo]].
Ripeti per tutti gli articoli fino a:
## Articolo 15 — ...
## Allegato A — ...
## Allegato B — ...
## Punti non cedibili
- ...
## Punti trattabili
- ...
## Risposta al comitato rischi
...""",
        "scaffolding_aids": ["output_schema", "native_redline_markers", "normative_allowlist"],
        "primary_measurement": ["targeted_redlining", "legal_issue_spotting"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": [
            "document_fidelity",
            "legal_correctness",
            "redline_quality",
            "negotiation_prioritization",
            "scope_discipline",
        ],
        "normative_sources": [
            {"title": "Regolamento (UE) 2016/679, incl. artt. 28, 29, 31-34 e Capo V"},
            {"title": "D.Lgs. 196/2003"},
            {"title": "Decisione di esecuzione (UE) 2021/914"},
            {"title": "Provvedimento Garante 6 giugno 2024, n. 364"},
        ],
        "artifact_checks": [
            {
                "id": "WF2-001-A1",
                "type": "docx_features",
                "artifact": "DPA_Nimbus_Aurea_redline.docx",
                "required_features": ["valid_package"],
                "patterns": [
                    *[rf"^##\s+Articolo\s+{index}\b" for index in range(1, 16)],
                    r"^##\s+Allegato\s+A\b",
                    r"^##\s+Allegato\s+B\b",
                ],
            },
            {
                "id": "WF2-001-A2",
                "type": "docx_features",
                "artifact": "DPA_Nimbus_Aurea_redline.docx",
                "required_features": ["track_revisions", "insertions", "deletions"],
            },
            {
                "id": "WF2-001-A3",
                "type": "docx_features",
                "artifact": "DPA_Nimbus_Aurea_redline.docx",
                "required_features": ["comments", "comments_cover_changes", "comments_reference_norm"],
            },
            {
                "id": "WF2-001-A4",
                "type": "required_markdown_headings",
                "artifact": "DPA_Nimbus_Aurea_redline.docx",
                "headings": ["Punti non cedibili", "Punti trattabili"],
            },
        ],
    },
    "WF2-002": {
        "criteria_count": 48,
        "document_count": 5,
        "deliverable": "deadline_memo_insolvenza.docx",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2", *{f"C.{index}" for index in range(1, 8)}},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2027-02-01",
        "workflow_family": "procedural_computation",
        "subtask": "insolvency_deadline_chain",
        "granularity": "whole_procedural_file",
        "legal_area": ["insolvency", "civil_procedure"],
        "document_type": "insolvency_procedural_file",
        "estimated_minutes": 90,
        "capabilities": ["document_chronology", "deadline_computation", "procedural_analysis", "artifact_generation"],
        "agentic_instructions": [
            "Apri tutti i cinque documenti e ricostruisci separatamente opposizione e ricorso per cassazione.",
            "Assumi come data di riferimento il 1 febbraio 2027.",
            "La scadenza dell'opposizione da usare nel pilot è il 14 settembre 2026.",
            "Per ogni data indica atto-fonte e riferimento normativo con articolo e comma; distingue irregolarità incidenti e non incidenti.",
        ],
        "output_format": """# Memo termini — Ferramenta Bardini / Officine Valdarno
## Opposizione allo stato passivo
- Decorrenza: ...
- Scadenza: ...
- Atto-fonte: ...
- Norma, articolo e comma: ...
- Tempestività e irregolarità: ...
## Ricorso per cassazione
- Decorrenza: ...
- Scadenza: ...
- Atto-fonte: ...
- Norma, articolo e comma: ...
- Tempo residuo al 1 febbraio 2027: ...
## Valutazione dell'indicazione del cliente
...""",
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["deadline_computation", "procedural_analysis"],
        "not_purely_measured": ["document_formatting"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "deadline_computation", "false_positive_control"],
        "normative_sources": [
            {"title": "Codice della crisi d'impresa e dell'insolvenza, artt. 133 e 207"},
            {"title": "Codice di procedura civile, artt. 325, 326 e 327"},
            {"title": "L. 263/2005, art. 2, comma 1, lett. f), sull'art. 155 c.p.c."},
        ],
        "artifact_checks": [
            {"id": "WF2-002-A1", "type": "docx_features", "artifact": "deadline_memo_insolvenza.docx", "required_features": ["valid_package"]},
            {"id": "WF2-002-A2", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Scadenza:\s*14\s+settembre\s+2026", r"Scadenza:\s*25\s+febbraio\s+2027"]},
            {"id": "WF2-002-C1", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Decorrenza:\s*13\s+luglio\s+2026"]},
            {"id": "WF2-002-C2", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Scadenza:\s*14\s+settembre\s+2026"]},
            {"id": "WF2-002-C3", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Scadenza:\s*14\s+settembre\s+2026"]},
            {"id": "WF2-002-C4", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Decorrenza:\s*26\s+gennaio\s+2027"]},
            {"id": "WF2-002-C5", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Scadenza:\s*25\s+febbraio\s+2027"]},
            {"id": "WF2-002-C6", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"Scadenza:\s*25\s+febbraio\s+2027"]},
            {"id": "WF2-002-C7", "type": "required_regex", "artifact": "deadline_memo_insolvenza.docx", "patterns": [r"(?:Tempo\s+residuo[^\n]*|restano)[^\n]*24\s+giorni"]},
        ],
    },
    "WF2-003": {
        "criteria_count": 57,
        "document_count": 26,
        "deliverable": "due_diligence_red_flags.md",
        "additional_public_inputs": [],
        "deterministic_criteria": {f"A.{index}" for index in range(1, 7)},
        "section_scoped_criteria": {"B.47", "B.48", "B.49", "B.50", "B.51"},
        "conditional_criteria": {"B.32"},
        "scope_locator": "Sintesi per l'investment committee",
        "as_of_date": "2026-10-01",
        "workflow_family": "dossier_analysis",
        "subtask": "due_diligence_memo",
        "granularity": "whole_data_room",
        "legal_area": ["corporate_mna", "employment", "environmental", "tax"],
        "document_type": "mna_data_room",
        "estimated_minutes": 120,
        "capabilities": [
            "document_triage",
            "cross_document_reasoning",
            "false_positive_control",
            "prioritization",
            "artifact_generation",
        ],
        "agentic_instructions": [
            "Consulta i documenti soltanto tramite i tool del matter.",
            "Non assumere che ogni documento contenga un red flag materiale.",
            "Le sole fonti normative ammesse in questa run sono gli artt. 242 e 244 del D.Lgs. 152/2006 e l'art. 23 del D.Lgs. 81/2015.",
            "I richiami alle clausole e alle voci dei documenti del fascicolo non sono citazioni normative esterne.",
            "Produci il deliverable due_diligence_red_flags.md usando il formato indicato dal protocollo.",
        ],
        "output_format": WF2_003_OUTPUT_FORMAT,
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["document_triage", "cross_document_reasoning"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": [
            "document_fidelity",
            "legal_correctness",
            "completeness",
            "false_positive_control",
            "scope_discipline",
        ],
        "normative_sources": [
            {"title": "D.Lgs. 152/2006, artt. 242 e 244"},
            {"title": "D.Lgs. 81/2015, art. 23"},
        ],
        "artifact_checks": [
            {
                "id": "WF2-003-A1",
                "type": "ordered_markdown_blocks",
                "artifact": "due_diligence_red_flags.md",
                "block_heading_pattern": r"^##\s+(?:Red flag\s+)?(?P<number>\d+)[.)\s—-]",
                "minimum": 1,
            },
            {
                "id": "WF2-003-A2",
                "type": "repeated_block_required_fields",
                "artifact": "due_diligence_red_flags.md",
                "block_heading_pattern": r"^##\s+(?:Red flag\s+)?(?P<number>\d+)[.)\s—-]",
                "required_fields": ["Esposizione stimata", "Rimedio proposto"],
            },
            {
                "id": "WF2-003-A3",
                "type": "labeled_value_allowlist",
                "artifact": "due_diligence_red_flags.md",
                "block_heading_pattern": r"^##\s+(?:Red flag\s+)?(?P<number>\d+)[.)\s—-]",
                "label": "Rimedio proposto",
                "allowed_values": [
                    "indennizzo specifico",
                    "condizione sospensiva",
                    "price adjustment",
                    "representation & warranty",
                ],
            },
            {
                "id": "WF2-003-A4",
                "type": "labeled_source_locator",
                "artifact": "due_diligence_red_flags.md",
                "block_heading_pattern": r"^##\s+(?:Red flag\s+)?(?P<number>\d+)[.)\s—-]",
                "label": "Fonte",
            },
            {
                "id": "WF2-003-A5",
                "type": "required_markdown_headings",
                "artifact": "due_diligence_red_flags.md",
                "headings": ["Sintesi per l'investment committee"],
            },
            {
                "id": "WF2-003-A6",
                "type": "normative_reference_allowlist",
                "artifact": "due_diligence_red_flags.md",
                "allowed_values": [
                    "d.lgs.152/2006#242",
                    "d.lgs.152/2006#244",
                    "d.lgs.81/2015#23",
                ],
            },
        ],
    },
    "WF2-004": {
        "criteria_count": 46,
        "document_count": 3,
        "deliverable": "spa_review_issues.md",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.3", "A.4", "A.5"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-10-30",
        "workflow_family": "document_review_and_revision",
        "subtask": "spa_review_memo",
        "granularity": "transaction_document_set",
        "legal_area": ["corporate_mna", "commercial_contracts"],
        "document_type": "share_purchase_agreement",
        "estimated_minutes": 120,
        "capabilities": ["contract_navigation", "term_sheet_comparison", "issue_prioritization", "scope_discipline", "artifact_generation"],
        "agentic_instructions": [
            "Apri SPA, term sheet e mail di mandato e tratta tutti e tre come fonti del matter.",
            "Produci esclusivamente una issue list: non riscrivere il contratto e non creare un redline.",
            "Ordina i rilievi per priorità, cita clausola o documento e segnala gli scostamenti dal term sheet.",
            "Le sole fonti normative ammesse sono gli artt. 1229 e 2596 c.c.",
        ],
        "output_format": """# Review SPA — Larese Automazioni
## 1 — Titolo del rilievo
- Priorità: alta | media | bassa
- Clausola/Fonte: ...
- Esposizione: ...
- Rinegoziazione richiesta: ...
- Scostamento dal term sheet: sì | no | non applicabile
Analisi concisa.
Ripeti i blocchi in ordine di priorità.
## Scostamenti dal term sheet
- ...
## Punti non cedibili
- ...""",
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["contract_navigation", "term_sheet_comparison", "issue_prioritization"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "completeness", "prioritization", "scope_discipline"],
        "normative_sources": [{"title": "Codice civile, artt. 1229 e 2596"}],
        "artifact_checks": [
            {"id": "WF2-004-A1", "type": "ordered_markdown_blocks", "artifact": "spa_review_issues.md", "block_heading_pattern": r"^##\s+(?P<number>\d+)[.)\s—-]", "minimum": 1},
            {"id": "WF2-004-A3", "type": "labeled_source_locator", "artifact": "spa_review_issues.md", "block_heading_pattern": r"^##\s+(?P<number>\d+)[.)\s—-]", "label": "Clausola/Fonte"},
            {"id": "WF2-004-A4", "type": "required_markdown_headings", "artifact": "spa_review_issues.md", "headings": ["Punti non cedibili"]},
            {"id": "WF2-004-A5", "type": "normative_reference_allowlist", "artifact": "spa_review_issues.md", "allowed_values": ["c.c.#1229", "c.c.#2596"]},
        ],
    },
    "WF2-005": {
        "criteria_count": 33,
        "document_count": 5,
        "deliverable": "deadline_memo_tar.docx",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2", "C.1", "C.2", "C.3"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-09-18",
        "workflow_family": "procedural_computation",
        "subtask": "administrative_appeal_deadline",
        "granularity": "whole_procedural_file",
        "legal_area": ["administrative_law", "administrative_procedure"],
        "document_type": "administrative_procedural_file",
        "estimated_minutes": 75,
        "capabilities": ["document_chronology", "deadline_computation", "procedural_analysis", "uncertainty_management", "artifact_generation"],
        "agentic_instructions": [
            "Apri tutti i cinque documenti, inclusa la mail informale del 23 luglio 2026.",
            "Indica una sola scadenza per la notificazione del ricorso: 30 ottobre 2026.",
            "Distingui il fatto di decorrenza dall'atto-fonte e cita articolo e comma per la norma applicata.",
            "Valuta separatamente se il tentativo bonario o l'istanza pendente incidano sul termine.",
        ],
        "output_format": """# Memo termine ricorso TAR — Verzana Imballaggi
## Termine per agire
- Fatto di decorrenza: ...
- Data di decorrenza: ...
- Scadenza: ...
- Atto-fonte: ...
- Norma, articolo e comma: ...
## Via bonaria e istanza pendente
... 
## Istruzioni operative
...""",
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["deadline_computation", "procedural_analysis", "uncertainty_management"],
        "not_purely_measured": ["document_formatting"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "deadline_computation", "uncertainty_management"],
        "normative_sources": [
            {"title": "Codice del processo amministrativo, artt. 29 e 41"},
            {"title": "L. 241/1990, artt. 3 e 10-bis"},
        ],
        "artifact_checks": [
            {"id": "WF2-005-A1", "type": "docx_features", "artifact": "deadline_memo_tar.docx", "required_features": ["valid_package"]},
            {"id": "WF2-005-A2", "type": "required_regex", "artifact": "deadline_memo_tar.docx", "patterns": [r"Scadenza:\s*30\s+ottobre\s+2026"]},
            {"id": "WF2-005-C1", "type": "required_regex", "artifact": "deadline_memo_tar.docx", "patterns": [r"Data\s+di\s+decorrenza:\s*6\s+agosto\s+2026"]},
            {"id": "WF2-005-C2", "type": "required_regex", "artifact": "deadline_memo_tar.docx", "patterns": [r"Scadenza:\s*30\s+ottobre\s+2026"]},
            {"id": "WF2-005-C3", "type": "required_regex", "artifact": "deadline_memo_tar.docx", "patterns": [r"Scadenza:\s*30\s+ottobre\s+2026"]},
        ],
    },
    "WF2-006": {
        "criteria_count": 59,
        "document_count": 5,
        "deliverable": "aml_evidence_matrix.md",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2", "A.3", "A.4", "A.5", "C.1"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-06-18",
        "workflow_family": "dossier_analysis",
        "subtask": "aml_suspicious_activity",
        "granularity": "whole_aml_file",
        "legal_area": ["aml", "banking"],
        "document_type": "aml_monitoring_file",
        "estimated_minutes": 105,
        "capabilities": ["document_triage", "cross_document_reasoning", "evidence_classification", "false_positive_control", "artifact_generation"],
        "agentic_instructions": [
            "Apri tutti i cinque documenti e separa ciò che è provato da ciò che è dichiarato o riportato in causale.",
            "Classifica ogni rilievo esclusivamente come anomalo, regolare o non determinabile.",
            "Per gli elementi non determinabili indica informazione mancante e destinatario della richiesta.",
            "Le sole fonti normative ammesse sono gli artt. 20, 22, 35, 39, 42 e 49 D.Lgs. 231/2007 e la L. 1966/1939.",
        ],
        "output_format": """# Matrice AML — Meridiana Logistica
## 1 — Titolo del rilievo
- Rilievo: ...
- Qualificazione: anomalo | regolare | non determinabile
- Stato probatorio: provato da documento | dichiarato dal cliente | riportato in causale
- Fonte: ...
- Informazione mancante e destinatario: ...
Analisi.
Ripeti per ogni elemento.
## Valutazione conclusiva
...
## Azioni e tempi
- Azione — responsabile — termine
## Operatività nel frattempo
...""",
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["cross_document_reasoning", "evidence_classification", "false_positive_control"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "evidence_classification", "completeness", "false_positive_control"],
        "normative_sources": [{"title": "D.Lgs. 231/2007, artt. 20, 22, 35, 39, 42 e 49"}, {"title": "L. 1966/1939"}],
        "artifact_checks": [
            {"id": "WF2-006-A1", "type": "repeated_block_required_fields", "artifact": "aml_evidence_matrix.md", "block_heading_pattern": r"^##\s+(?P<number>\d+)[.)\s—-]", "required_fields": ["Rilievo", "Qualificazione", "Fonte"]},
            {"id": "WF2-006-A2", "type": "labeled_value_allowlist", "artifact": "aml_evidence_matrix.md", "block_heading_pattern": r"^##\s+(?P<number>\d+)[.)\s—-]", "label": "Qualificazione", "allowed_values": ["anomalo", "regolare", "non determinabile"]},
            {"id": "WF2-006-A3", "type": "repeated_block_required_fields", "artifact": "aml_evidence_matrix.md", "block_heading_pattern": r"^##\s+(?P<number>\d+)[.)\s—-]", "required_fields": ["Stato probatorio"]},
            {"id": "WF2-006-A4", "type": "required_markdown_headings", "artifact": "aml_evidence_matrix.md", "headings": ["Valutazione conclusiva", "Azioni e tempi", "Operatività nel frattempo"]},
            {"id": "WF2-006-A5", "type": "normative_reference_allowlist", "artifact": "aml_evidence_matrix.md", "allowed_values": ["d.lgs.231/2007#20", "d.lgs.231/2007#22", "d.lgs.231/2007#35", "d.lgs.231/2007#39", "d.lgs.231/2007#42", "d.lgs.231/2007#49", "l.1966/1939"]},
            {"id": "WF2-006-C1", "type": "required_regex", "artifact": "aml_evidence_matrix.md", "patterns": [r"15\s+giugno\s+2026[^\n]*(?:integrazion|document)"]},
        ],
    },
    "WF2-007": {
        "criteria_count": 42,
        "document_count": 7,
        "deliverable": "kyc_titolari_effettivi.md",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2", "A.3", "A.4"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-09-21",
        "workflow_family": "dossier_analysis",
        "subtask": "beneficial_ownership",
        "granularity": "whole_kyc_file",
        "legal_area": ["aml", "corporate"],
        "document_type": "kyc_beneficial_ownership_file",
        "estimated_minutes": 90,
        "capabilities": ["ownership_reconstruction", "cross_document_reasoning", "evidence_attribution", "uncertainty_management", "artifact_generation"],
        "agentic_instructions": [
            "Apri tutti i sette documenti e ricostruisci prima l'assetto, poi i titolari effettivi.",
            "Per ogni titolare usa una sola base tra proprietà, beneficio economico e controllo e indica il documento-fonte.",
            "Verifica l'autodichiarazione e separa lacune documentali da conclusioni positive.",
            "Le sole fonti normative ammesse sono gli artt. 20 e 22 D.Lgs. 231/2007.",
        ],
        "output_format": """# Memo titolarità effettiva — Larius Partecipazioni
## Assetto ricostruito
...
## Titolari effettivi
### 1 — Nome
- Base: proprietà | beneficio economico | controllo
- Fonte: ...
- Analisi: ...
Ripeti per ciascun titolare.
## Verifica dell'autodichiarazione
...
## Dati mancanti
- ...
## Chiusura CDD
...""",
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["ownership_reconstruction", "cross_document_reasoning", "uncertainty_management"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "ownership_reconstruction", "evidence_attribution", "uncertainty_management"],
        "normative_sources": [{"title": "D.Lgs. 231/2007, artt. 20 e 22"}],
        "artifact_checks": [
            {"id": "WF2-007-A1", "type": "ordered_markdown_blocks", "artifact": "kyc_titolari_effettivi.md", "block_heading_pattern": r"^###\s+(?P<number>\d+)[.)\s—-]", "minimum": 1},
            {"id": "WF2-007-A2", "type": "repeated_block_required_fields", "artifact": "kyc_titolari_effettivi.md", "block_heading_pattern": r"^###\s+(?P<number>\d+)[.)\s—-]", "required_fields": ["Base", "Fonte"]},
            {"id": "WF2-007-A3", "type": "labeled_value_allowlist", "artifact": "kyc_titolari_effettivi.md", "block_heading_pattern": r"^###\s+(?P<number>\d+)[.)\s—-]", "label": "Base", "allowed_values": ["proprietà", "beneficio economico", "controllo"]},
            {"id": "WF2-007-A4", "type": "normative_reference_allowlist", "artifact": "kyc_titolari_effettivi.md", "allowed_values": ["d.lgs.231/2007#20", "d.lgs.231/2007#22"]},
        ],
    },
    "WF2-008": {
        "criteria_count": 36,
        "document_count": 1,
        "deliverable": "Contratto_Sereni_redline.docx",
        "additional_public_inputs": ["public/03_decision_inputs.md"],
        "deterministic_criteria": {"A.1", "A.2", "A.3", "A.4", "A.5", "A.6", "B.12"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-08-20",
        "workflow_family": "document_review_and_revision",
        "subtask": "targeted_non_compete_redline",
        "granularity": "single_clause_in_whole_contract",
        "legal_area": ["employment"],
        "document_type": "employment_contract",
        "estimated_minutes": 75,
        "capabilities": ["contract_navigation", "targeted_redlining", "scope_discipline", "legal_issue_spotting", "artifact_generation"],
        "agentic_instructions": [
            "Consulta il contratto e la nota con gli input decisionali soltanto tramite i tool del matter.",
            "Restituisci il contratto integrale con la stessa numerazione degli articoli 1-9.",
            "Modifica esclusivamente l'articolo 7; non alterare gli altri articoli.",
            "Nel sorgente del DOCX usa [[DEL:...]], [[INS:...]] e una [[NOTE:...]] per ogni modifica, includendo il riferimento all'art. 2125 c.c.",
            "La durata nel testo modificato e nelle note deve coincidere e non superare tre anni.",
        ],
        "output_format": """# Contratto di assunzione — Marco Sereni
## Articolo 1 — ...
Riporta integralmente gli articoli non modificati.
...
## Articolo 7 — Patto di non concorrenza
Usa [[DEL:testo originale]] [[INS:testo proposto]] [[NOTE:Art. 7; spiegazione; art. 2125 c.c.]] per ogni modifica.
...
## Articolo 9 — ...""",
        "scaffolding_aids": ["output_schema", "native_redline_markers", "decision_inputs", "normative_allowlist"],
        "primary_measurement": ["targeted_redlining", "scope_discipline", "legal_issue_spotting"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": ["document_fidelity", "legal_correctness", "redline_quality", "scope_discipline"],
        "normative_sources": [{"title": "Codice civile, art. 2125"}],
        "artifact_checks": [
            {"id": "WF2-008-A1", "type": "docx_features", "artifact": "Contratto_Sereni_redline.docx", "required_features": ["valid_package"], "patterns": [*[rf"^##\s+Articolo\s+{index}\b" for index in range(1, 10)]]},
            {"id": "WF2-008-A2", "type": "docx_features", "artifact": "Contratto_Sereni_redline.docx", "required_features": ["track_revisions", "insertions", "deletions"]},
            {"id": "WF2-008-A3", "type": "docx_features", "artifact": "Contratto_Sereni_redline.docx", "required_features": ["comments", "comments_cover_changes"]},
            {"id": "WF2-008-A4", "type": "docx_features", "artifact": "Contratto_Sereni_redline.docx", "required_features": ["comments_reference_norm"]},
            {"id": "WF2-008-A5", "type": "normative_reference_allowlist", "artifact": "Contratto_Sereni_redline.docx", "allowed_values": ["c.c.#2125"]},
            {"id": "WF2-008-A6", "type": "required_regex", "artifact": "Contratto_Sereni_redline.docx", "patterns": [r"\[\[INS:[^\]]*(?:tre|3|36)\s*(?:anni|mes)[^\]]*\]\]", r"\[\[NOTE:[^\]]*(?:tre|3|36)\s*(?:anni|mes)[^\]]*\]\]"]},
            {"id": "WF2-008-B12", "type": "required_regex", "artifact": "Contratto_Sereni_redline.docx", "patterns": [r"\[\[INS:[^\]]*(?:tre|3|36)\s*(?:anni|mes)[^\]]*\]\]"]},
        ],
    },
    "WF2-009": {
        "criteria_count": 29,
        "document_count": 9,
        "deliverable": "cronologia_disciplinare.md",
        "additional_public_inputs": [],
        "deterministic_criteria": {"A.1", "A.2"},
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": "2026-05-16",
        "workflow_family": "dossier_analysis",
        "subtask": "employment_chronology",
        "granularity": "whole_employment_file",
        "legal_area": ["employment"],
        "document_type": "disciplinary_procedure_file",
        "estimated_minutes": 75,
        "capabilities": ["document_chronology", "cross_document_reasoning", "conflict_detection", "evidence_attribution", "artifact_generation"],
        "agentic_instructions": [
            "Apri tutti i nove documenti e ricostruisci le date distinguendo formazione, invio, ricezione ed efficacia.",
            "Ordina le righe per data di efficacia crescente; le righe non determinabili possono essere collocate a parte.",
            "Compila sempre la fonte con il nome o il numero del documento e registra conflitti o anomalie senza valutare la legittimità del licenziamento.",
        ],
        "output_format": """# Cronologia procedimento disciplinare — Chiara Bianchi
| Formazione | Invio/Spedizione | Ricezione/Consegna | Efficacia | Fonte | Conflitti |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |
## Conflitti e date non determinabili
- ...""",
        "scaffolding_aids": ["output_schema"],
        "primary_measurement": ["document_chronology", "cross_document_reasoning", "conflict_detection"],
        "not_purely_measured": ["table_schema_discovery"],
        "evaluation_dimensions": ["document_fidelity", "chronology_accuracy", "completeness", "conflict_detection", "scope_discipline"],
        "normative_sources": [],
        "artifact_checks": [
            {"id": "WF2-009-A1", "type": "required_regex", "artifact": "cronologia_disciplinare.md", "patterns": [r"^\|[^\n]+\|\s*$", r"^\|\s*:?-{3,}[^\n]+\|\s*$"]},
            {"id": "WF2-009-A2", "type": "required_regex", "artifact": "cronologia_disciplinare.md", "patterns": [r"^\|\s*(?:Formazione|Data\s+di\s+formazione|Redazione)\s*\|\s*(?:Invio|Spedizione|Invio/Spedizione)\s*\|\s*(?:Ricezione|Consegna|Ricezione/Consegna)\s*\|\s*(?:Efficacia|Decorrenza\s+degli\s+effetti)\s*\|\s*(?:Fonte|Documento)\s*\|\s*(?:Conflitti|Anomalie|Contraddizioni)\s*\|"]},
        ],
    },
    "WF2-010": {
        "criteria_count": 97,
        "document_count": 1,
        "deliverable": "spa_signing_closing_timeline.md",
        "additional_public_inputs": ["public/03_temporal_assumptions.md"],
        "deterministic_criteria": {
            "A.6",
            *{f"C.{index}" for index in range(1, 13)},
        },
        "section_scoped_criteria": set(),
        "conditional_criteria": {"B.9", "B.71", "B.72", "B.73", "B.74"},
        "scope_locator": None,
        "as_of_date": "2027-02-12",
        "workflow_family": "procedural_computation",
        "subtask": "transaction_timeline",
        "granularity": "whole_transaction_document",
        "legal_area": ["corporate_mna", "competition", "foreign_investment"],
        "document_type": "share_purchase_agreement",
        "estimated_minutes": 90,
        "capabilities": [
            "contract_navigation",
            "temporal_reasoning",
            "deadline_computation",
            "dependency_mapping",
            "uncertainty_management",
            "artifact_generation",
        ],
        "agentic_instructions": [
            "Consulta lo SPA e la nota temporale soltanto tramite i tool del matter.",
            "Leggi tutte le pagine logiche del DOCX, inclusi gli Allegati B, D ed E.",
            "Non sostituire le soglie nazionali 2027 con soglie 2026 e non inventare soglie mancanti.",
            "Separa date determinate, termini relativi al Closing e date non determinabili perché dipendenti da eventi futuri o terzi.",
            "Le sole fonti normative ammesse sono gli artt. 1187, 1353, 1358, 1359, 1360 e 2963 c.c.; l'art. 16 L. 287/1990; il Regolamento (CE) 139/2004; il D.L. 21/2012.",
            "I richiami agli articoli e agli allegati dello SPA sono fonti contrattuali, non citazioni normative esterne.",
            "Produci spa_signing_closing_timeline.md usando il formato indicato dal protocollo.",
        ],
        "output_format": WF2_010_OUTPUT_FORMAT,
        "scaffolding_aids": [
            "output_schema",
            "normative_allowlist",
            "temporal_assumptions",
        ],
        "primary_measurement": [
            "temporal_reasoning",
            "deadline_computation",
            "dependency_mapping",
            "uncertainty_management",
        ],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": [
            "document_fidelity",
            "legal_correctness",
            "deadline_computation",
            "dependency_completeness",
            "uncertainty_management",
            "scope_discipline",
        ],
        "normative_sources": [
            {"title": "Codice civile, artt. 1187, 1353, 1358, 1359, 1360 e 2963"},
            {"title": "L. 287/1990, art. 16"},
            {"title": "Regolamento (CE) 139/2004"},
            {"title": "D.L. 21/2012"},
        ],
        "artifact_checks": [
            {
                "id": "WF2-010-A6",
                "type": "normative_reference_allowlist",
                "artifact": "spa_signing_closing_timeline.md",
                "allowed_values": [
                    "c.c.#1187",
                    "c.c.#1353",
                    "c.c.#1358",
                    "c.c.#1359",
                    "c.c.#1360",
                    "c.c.#2963",
                    "l.287/1990",
                    "regolamento(ce)139/2004",
                    "d.l.21/2012",
                ],
            },
            *_wf2_010_exact_checks(),
        ],
    },
}


def _cohort_two_profile(
    *,
    criteria_count: int,
    document_count: int,
    deliverable: str,
    as_of_date: str,
    workflow_family: str,
    subtask: str,
    legal_area: list[str],
    document_type: str,
    instructions: list[str],
    output_format: str,
    normative_sources: list[dict[str, str]],
    deterministic_criteria: set[str] | None = None,
    artifact_checks: list[dict[str, Any]] | None = None,
    deliverables: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "criteria_count": criteria_count,
        "document_count": document_count,
        "deliverable": deliverable,
        "deliverables": deliverables or [deliverable],
        "additional_public_inputs": ["public/03_legal_sources.md"],
        "deterministic_criteria": deterministic_criteria or set(),
        "section_scoped_criteria": set(),
        "conditional_criteria": set(),
        "scope_locator": None,
        "as_of_date": as_of_date,
        "workflow_family": workflow_family,
        "subtask": subtask,
        "granularity": "whole_matter_file",
        "legal_area": legal_area,
        "document_type": document_type,
        "estimated_minutes": 120,
        "capabilities": [
            "document_navigation",
            "cross_document_reasoning",
            "legal_issue_spotting",
            "false_positive_control",
            "artifact_generation",
        ],
        "agentic_instructions": [
            "Apri tutti i documenti del fascicolo e il file pubblico delle fonti normative.",
            "Distingui fatti documentati, inferenze e informazioni mancanti.",
            "Usa soltanto le fonti normative del reference pack chiuso.",
            *instructions,
        ],
        "output_format": output_format,
        "scaffolding_aids": ["output_schema", "normative_allowlist"],
        "primary_measurement": ["cross_document_reasoning", "legal_issue_spotting"],
        "not_purely_measured": ["deliverable_structure_discovery"],
        "evaluation_dimensions": [
            "document_fidelity",
            "legal_correctness",
            "completeness",
            "false_positive_control",
            "scope_discipline",
        ],
        "normative_sources": normative_sources,
        "artifact_checks": artifact_checks or [],
    }


TASK_PROFILES.update(
    {
        "WF2-011": _cohort_two_profile(
            criteria_count=41,
            document_count=9,
            deliverable="data_breach_action_plan.md",
            as_of_date="2026-12-09",
            workflow_family="procedural_computation",
            subtask="data_breach_deadline_audit",
            legal_area=["privacy", "data_protection"],
            document_type="data_breach_incident_file",
            instructions=[
                "Per ogni adempimento indica termine, decorrenza, calcolo, stato e azione immediata.",
                "Tratta 12.400 interessati come perimetro minimo certo e motiva separatamente la decisione sui 41.027 utenti.",
            ],
            output_format="""# Audit data breach\n## Adempimenti e scadenze\nUsa una tabella con: adempimento; termine; decorrenza e fonte; calcolo; stato; azione immediata.\n## Comunicazione agli interessati\nDistingui il perimetro minimo certo dalla decisione motivata sugli altri utenti.\n## Aggiornamenti documentali e contrattuali\n...""",
            normative_sources=[
                {"title": "Regolamento (UE) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/ita"},
                {"title": "Linee guida EDPB 9/2022", "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en"},
                {"title": "Regolamento n. 1182/71", "url": "https://eur-lex.europa.eu/eli/reg/1971/1182/oj/ita"},
                {"title": "Decisione di esecuzione (UE) 2021/915", "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/915/oj/ita"},
            ],
            deterministic_criteria={"C.1", "C.4", "C.11"},
            artifact_checks=[
                {"id": "WF2-011-C1", "type": "required_regex", "artifact": "data_breach_action_plan.md", "patterns": [r"5\s+dicembre\s+2026[^\n]*18[:.]40"]},
                {"id": "WF2-011-C4", "type": "required_regex", "artifact": "data_breach_action_plan.md", "patterns": [r"8\s+dicembre\s+2026"]},
                {"id": "WF2-011-C11", "type": "required_regex", "artifact": "data_breach_action_plan.md", "patterns": [r"\b380\b[^\n]*(?:invalidit|salute)"]},
            ],
        ),
        "WF2-012": _cohort_two_profile(
            criteria_count=52,
            document_count=12,
            deliverable="real_estate_due_diligence.md",
            as_of_date="2026-07-07",
            workflow_family="dossier_analysis",
            subtask="real_estate_due_diligence",
            legal_area=["real_estate", "civil_law"],
            document_type="real_estate_due_diligence_file",
            instructions=["Ordina i rilievi per priorità e traduci le lacune essenziali in condizioni del preliminare."],
            output_format="""# Due diligence immobiliare\n## Rilievi in ordine di priorità\n## Elementi in ordine\n## Documenti e verifiche mancanti\nPer ogni voce indica a chi richiederla.\n## Condizioni per il preliminare\n## Calcoli""",
            normative_sources=[
                {"title": "D.P.R. 380/2001", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:2001-06-06;380"},
                {"title": "L. 52/1985", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1985-02-27;52"},
                {"title": "L. 182/2025", "url": "https://www.gazzettaufficiale.it/eli/gu/2025/12/03/281/sg/pdf"},
                {"title": "D.Lgs. 192/2005", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-08-19;192"},
            ],
            deterministic_criteria={"C.1", "C.2", "C.4", "C.7"},
            artifact_checks=[
                {"id": "WF2-012-C1", "type": "required_regex", "artifact": "real_estate_due_diligence.md", "patterns": [r"96[,.]20\s*m[q²2]"]},
                {"id": "WF2-012-C2", "type": "required_regex", "artifact": "real_estate_due_diligence.md", "patterns": [r"104[,.]60\s*m[q²2]"]},
                {"id": "WF2-012-C4", "type": "required_regex", "artifact": "real_estate_due_diligence.md", "patterns": [r"8[,.]40\s*m[q²2]"]},
                {"id": "WF2-012-C7", "type": "required_regex", "artifact": "real_estate_due_diligence.md", "patterns": [r"7[.]?899[,.]60"]},
            ],
        ),
        "WF2-013": _cohort_two_profile(
            criteria_count=49,
            document_count=6,
            deliverable="contratto_distribuzione_redline.docx",
            deliverables=["contratto_distribuzione_redline.docx", "nota_modifiche_distribuzione.md"],
            as_of_date="2027-03-15",
            workflow_family="document_review_and_revision",
            subtask="distribution_agreement_redline",
            legal_area=["competition", "commercial_contracts"],
            document_type="distribution_agreement",
            instructions=[
                "Produci due file: il contratto integrale in DOCX con revisioni visibili e la nota separata in Markdown.",
                "Nella nota indica esposizione, clausola di origine, modifica proposta e due o tre non negoziabili.",
            ],
            output_format="""Artefatto 1: contratto_distribuzione_redline.docx — testo integrale con [[DEL:...]], [[INS:...]] e [[NOTE:...]].\nArtefatto 2: nota_modifiche_distribuzione.md\n# Nota delle modifiche\n## Rilievi\n## Invalidità e conseguenze\n## Punti non cedibili""",
            normative_sources=[
                {"title": "Regolamento (UE) 2022/720", "url": "https://eur-lex.europa.eu/eli/reg/2022/720/oj/ita"},
                {"title": "Orientamenti sulle restrizioni verticali 2022", "url": "https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:52022XC0630(01)"},
                {"title": "Art. 101 TFUE", "url": "https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:12012E101"},
            ],
            deterministic_criteria={"C.1", "C.2", "C.3", "C.4", "C.5", "C.6", "C.7"},
            artifact_checks=[
                {"id": "WF2-013-C1", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"23[,.]4\s*%"]},
                {"id": "WF2-013-C2", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"4[,.]1\s*%"]},
                {"id": "WF2-013-C3", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"1.?\s*aprile\s+2027", r"31\s+marzo\s+2034"]},
                {"id": "WF2-013-C4", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"31\s+marzo\s+2032"]},
                {"id": "WF2-013-C5", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"1[.]?400[.]?000", r"1[.]?060[.]?000"]},
                {"id": "WF2-013-C6", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"1[.]?330[.]?000"]},
                {"id": "WF2-013-C7", "type": "required_regex", "artifact": "nota_modifiche_distribuzione.md", "patterns": [r"148[.]?000"]},
            ],
        ),
        "WF2-014": _cohort_two_profile(
            criteria_count=44,
            document_count=1,
            deliverable="accordo_quadro_redline.docx",
            deliverables=["accordo_quadro_redline.docx", "nota_rilievi_subfornitura.md"],
            as_of_date="2027-09-16",
            workflow_family="document_review_and_revision",
            subtask="subcontract_targeted_redline",
            legal_area=["commercial_contracts", "subcontracting"],
            document_type="subcontract_framework_agreement",
            instructions=[
                "Produci due file e limita le revisioni agli articoli 3-15.",
                "Non imporre nel gold una tesi sulla sostituzione automatica del termine: correggi il termine a un valore conforme.",
            ],
            output_format="""Artefatto 1: accordo_quadro_redline.docx — contratto integrale con revisioni visibili limitate agli articoli 3-15.\nArtefatto 2: nota_rilievi_subfornitura.md\n# Nota dei rilievi\n## Rilievi in ordine di importanza\n## Firmabilità""",
            normative_sources=[
                {"title": "L. 192/1998", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1998-06-18;192"},
                {"title": "D.Lgs. 231/2002", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2002-10-09;231"},
            ],
            deterministic_criteria={"A.1", "A.2"},
            artifact_checks=[
                {"id": "WF2-014-A1", "type": "docx_features", "artifact": "accordo_quadro_redline.docx", "required_features": ["valid_package", "track_revisions", "insertions", "deletions"]},
                {"id": "WF2-014-A2", "type": "required_markdown_headings", "artifact": "nota_rilievi_subfornitura.md", "headings": ["Nota dei rilievi", "Firmabilità"]},
            ],
        ),
        "WF2-015": _cohort_two_profile(
            criteria_count=59,
            document_count=2,
            deliverable="calendario_licenziamento_collettivo.md",
            as_of_date="2027-01-18",
            workflow_family="procedural_computation",
            subtask="collective_redundancy_timeline",
            legal_area=["employment", "collective_redundancy"],
            document_type="collective_redundancy_file",
            instructions=["Mostra il conteggio dei dieci esuberi, le dipendenze e la valutazione del calendario del consiglio."],
            output_format="""# Calendario della procedura\nUsa una tabella con: data o termine; passaggio; attore; dipendenza; calcolo; documento; norma.\n## Conteggio degli addetti interessati\n## Checklist aziendale\n## Chiusura senza accordo\n## Valutazione del calendario del consiglio""",
            normative_sources=[{"title": "L. 223/1991", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1991-07-23;223"}],
            deterministic_criteria={"C.1", "C.2", "C.3", "C.4", "C.5"},
            artifact_checks=[
                {"id": "WF2-015-C1", "type": "required_regex", "artifact": "calendario_licenziamento_collettivo.md", "patterns": [r"22\s+gennaio\s+2027"]},
                {"id": "WF2-015-C2", "type": "required_regex", "artifact": "calendario_licenziamento_collettivo.md", "patterns": [r"(?:esclus|non\s+comput)[^\n]*(?:22\s+gennaio|giorno\s+iniziale)"]},
                {"id": "WF2-015-C3", "type": "required_regex", "artifact": "calendario_licenziamento_collettivo.md", "patterns": [r"29\s+gennaio\s+2027"]},
                {"id": "WF2-015-C4", "type": "required_regex", "artifact": "calendario_licenziamento_collettivo.md", "patterns": [r"8\s+marzo\s+2027"]},
                {"id": "WF2-015-C5", "type": "required_regex", "artifact": "calendario_licenziamento_collettivo.md", "patterns": [r"7\s+aprile\s+2027"]},
            ],
        ),
        "WF2-016": _cohort_two_profile(
            criteria_count=32,
            document_count=3,
            deliverable="whistleblowing_review.md",
            as_of_date="2026-10-22",
            workflow_family="document_review_and_revision",
            subtask="whistleblowing_system_review",
            legal_area=["whistleblowing", "compliance", "privacy"],
            document_type="whistleblowing_policy_set",
            instructions=["Valuta applicabilità, accessibilità, minimizzazione del modulo e conflitti del gestore; non riscrivere la procedura."],
            output_format="""# Nota di revisione del sistema whistleblowing\n## Rilievi in ordine di priorità\nPer ogni rilievo: fonte; non conformità; correzione proposta.\n## Presidi organizzativi""",
            normative_sources=[
                {"title": "D.Lgs. 24/2023", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-10;24"},
                {"title": "Linee guida ANAC n. 1/2025", "url": "https://www.anticorruzione.it/-/del.n.478-26.11.2025.llgg.wb"},
            ],
        ),
        "WF2-017": _cohort_two_profile(
            criteria_count=42,
            document_count=3,
            deliverable="memo_opposizione_sanzione_aml.md",
            as_of_date="2026-10-19",
            workflow_family="procedural_computation",
            subtask="aml_sanction_opposition_deadline",
            legal_area=["aml", "civil_procedure", "sanctions"],
            document_type="administrative_sanction_file",
            instructions=["Indica il 7 dicembre come scadenza ordinaria e ricostruisci separatamente l'effetto sospensivo dell'istanza ex art. 68."],
            output_format="""# Memo opposizione sanzione AML\n## Atto, giudice e competenza\n## Decorrenza e scadenza ordinaria\n## Istanza di riduzione e sospensione\n## Azioni immediate""",
            normative_sources=[
                {"title": "D.Lgs. 150/2011", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-09-01;150"},
                {"title": "D.Lgs. 231/2007, art. 68", "url": "https://def.giustiziatributaria.gov.it/DocTribFrontend/executePrintArticolo.do?articolo=Articolo+68&codiceOrdinamento=0000000000000680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7BC34AE818-6744-412E-83D3-F5BA751A4010%7D"},
            ],
            deterministic_criteria={"C.1", "C.2"},
            artifact_checks=[
                {"id": "WF2-017-C1", "type": "required_regex", "artifact": "memo_opposizione_sanzione_aml.md", "patterns": [r"8\s+ottobre\s+2026"]},
                {"id": "WF2-017-C2", "type": "required_regex", "artifact": "memo_opposizione_sanzione_aml.md", "patterns": [r"7\s+dicembre\s+2026"]},
            ],
        ),
        "WF2-018": _cohort_two_profile(
            criteria_count=36,
            document_count=11,
            deliverable="cronologia_delibere_societarie.md",
            as_of_date="2027-05-27",
            workflow_family="dossier_analysis",
            subtask="corporate_resolution_chronology",
            legal_area=["corporate", "company_law"],
            document_type="corporate_resolution_file",
            instructions=["Produci soltanto la cronologia richiesta e non aggiungere un parere al consiglio; non inventare la data della regolarizzazione."],
            output_format="""# Cronologia societaria\n| Atto | Formazione | Deposito o comunicazione | Iscrizione | Efficacia | Nei confronti di chi | Dipendenza/calcolo | Fonte |\n|---|---|---|---|---|---|---|---|""",
            normative_sources=[{"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"}],
            deterministic_criteria={"A.1", "B.1", "B.5", "B.7", "B.12", "B.19", "B.20"},
            artifact_checks=[
                {"id": "WF2-018-A1", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"^\|[^\n]+\|\s*$", r"^\|\s*:?-{3,}"]},
                {"id": "WF2-018-B1", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"6\s+maggio\s+2027[^\n]*(?:oggetto|articolo\s+3)"]},
                {"id": "WF2-018-B5", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"6\s+maggio\s+2027[^\n]*(?:delega|articolo\s+5)"]},
                {"id": "WF2-018-B7", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"20\s+maggio\s+2027[^\n]*aumento"]},
                {"id": "WF2-018-B12", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"8\s+aprile\s+2027[^\n]*(?:nomina|Roncadella)"]},
                {"id": "WF2-018-B19", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"1[.]?500[.]?000[^\n]*(?:sottoscritto|versato)"]},
                {"id": "WF2-018-B20", "type": "required_regex", "artifact": "cronologia_delibere_societarie.md", "patterns": [r"2[.]?100[.]?000[^\n]*deliberato"]},
            ],
        ),
        "WF2-019": _cohort_two_profile(
            criteria_count=30,
            document_count=10,
            deliverable="parere_copertura_assicurativa.md",
            as_of_date="2028-03-16",
            workflow_family="dossier_analysis",
            subtask="insurance_coverage_opinion",
            legal_area=["insurance", "civil_law"],
            document_type="insurance_claim_file",
            instructions=["Tratta separatamente Cofrid, Talamone e Marimonti e indica importi lordi, franchigia e netto senza presumere la responsabilità."],
            output_format="""# Parere sulla copertura assicurativa\n## Cofrid\n## Talamone\n## Marimonti\n## Contestazioni alla lettera della compagnia\n## Azioni immediate""",
            normative_sources=[{"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"}],
            deterministic_criteria={"C.1", "C.2", "C.3", "C.6"},
            artifact_checks=[
                {"id": "WF2-019-C1", "type": "required_regex", "artifact": "parere_copertura_assicurativa.md", "patterns": [r"118[.]?500"]},
                {"id": "WF2-019-C2", "type": "required_regex", "artifact": "parere_copertura_assicurativa.md", "patterns": [r"867[.]?900"]},
                {"id": "WF2-019-C3", "type": "required_regex", "artifact": "parere_copertura_assicurativa.md", "patterns": [r"15[.]?000"]},
                {"id": "WF2-019-C6", "type": "required_regex", "artifact": "parere_copertura_assicurativa.md", "patterns": [r"852[.]?900"]},
            ],
        ),
        "WF2-020": _cohort_two_profile(
            criteria_count=27,
            document_count=11,
            deliverable="nota_istruttoria_garante.md",
            as_of_date="2028-02-02",
            workflow_family="dossier_analysis",
            subtask="garante_information_request_response",
            legal_area=["privacy", "marketing"],
            document_type="data_protection_authority_file",
            instructions=["Rispondi quesito per quesito e tratta la ricevuta PEC come mancante; limita il non-issue soft spam ai tre invii contestati."],
            output_format="""# Nota istruttoria interna\n## Quesito 1\n- Documentato:\n- Non documentato:\n- Esposizione:\nRipeti per i cinque quesiti.\n## Documenti da acquisire\n## Azioni di remediation""",
            normative_sources=[
                {"title": "Regolamento (UE) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/ita"},
                {"title": "D.Lgs. 196/2003", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196"},
            ],
            deterministic_criteria={"C.1", "C.3", "C.4"},
            artifact_checks=[
                {"id": "WF2-020-C1", "type": "required_regex", "artifact": "nota_istruttoria_garante.md", "patterns": [r"4\s+giugno\s+2027"]},
                {"id": "WF2-020-C3", "type": "required_regex", "artifact": "nota_istruttoria_garante.md", "patterns": [r"9\s+marzo\s+2027"]},
                {"id": "WF2-020-C4", "type": "required_regex", "artifact": "nota_istruttoria_garante.md", "patterns": [r"(?:tre|3)\s+(?:invii|comunicazioni)"]},
            ],
        ),
    }
)


# Cohort three (WF2-021..030) is authored locally from source-grounded synthetic
# matters.  The public prompts embed their response schema and enumerate every
# attachment; public/03_legal_sources.md freezes the applicable source pack at
# 2026-08-25 even where the narrative facts occur later.
TASK_PROFILES.update(
    {
        "WF2-021": _cohort_two_profile(
            criteria_count=48,
            document_count=3,
            deliverable="patto_parasociale_redline.docx",
            as_of_date="2026-10-06",
            workflow_family="document_review_and_revision",
            subtask="sha_reserved_matters_deadlock_redline",
            legal_area=["corporate", "company_law", "mna"],
            document_type="shareholders_agreement_and_articles",
            instructions=[
                "Restituisci la bozza integrale, con premesse e articoli 1-19, e rendi visibili inserimenti e soppressioni.",
                "Associa a ogni modifica una nota con clausola e fonte; separa gli interventi extra-testuali dalla risposta al comitato investimenti.",
                "Per l'arbitrato societario usa l'art. 838-bis c.p.c.; non applicarlo alla clausola compromissoria meramente contrattuale del Patto né all'arbitraggio sul prezzo.",
            ],
            output_format="""# Patto parasociale — redline
Riporta premesse e articoli 1-19. Per ogni modifica usa [[DEL:testo originale]], [[INS:testo proposto]] e [[NOTE:clausola; ragione; fonte]].
## Interventi extra-testuali prima della firma
## Risposta al comitato investimenti""",
            normative_sources=[
                {"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"},
                {"title": "Codice di procedura civile, art. 838-bis", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1940-10-28;1440"},
                {"title": "D.Lgs. 149/2022", "url": "https://www.gazzettaufficiale.it/eli/gu/2022/10/17/243/so/38/sg/pdf"},
            ],
        ),
        "WF2-022": _cohort_two_profile(
            criteria_count=61,
            document_count=8,
            deliverable="memo_earnout_post_closing.md",
            as_of_date="2029-07-09",
            workflow_family="dossier_analysis",
            subtask="earnout_post_closing_dispute",
            legal_area=["corporate", "mna", "commercial_contracts"],
            document_type="share_purchase_earnout_file",
            instructions=[
                "Ricostruisci il parametro convenzionale voce per voce prima di qualificare la contestazione.",
                "Distingui rettifiche del parametro, eventuali inadempimenti e dati ancora da acquisire.",
            ],
            output_format="""# Memo earn-out post-closing
## Conclusione
## Ricostruzione del parametro
## Rilievi in ordine di importanza
## Scadenze e importi, con il calcolo
## Che cosa manca dal fascicolo
## Che cosa fare adesso""",
            normative_sources=[{"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"}],
        ),
        "WF2-023": _cohort_two_profile(
            criteria_count=77,
            document_count=8,
            deliverable="nota_rilievi_saas.md",
            as_of_date="2029-11-21",
            workflow_family="document_review_and_revision",
            subtask="saas_sla_license_liability_review_only",
            legal_area=["commercial_contracts", "technology", "data_protection"],
            document_type="saas_contract_file",
            instructions=[
                "Non riscrivere la bozza: produci una nota di review ancorata a clausole e documenti.",
                "Tratta separatamente SLA, licenza, responsabilità, continuità del servizio e conseguenze della mancata firma.",
            ],
            output_format="""# Nota dei rilievi SaaS
## Rilievi
Per ogni voce: rilievo; fonte; esposizione; che cosa chiedere.
## Scadenze e importi, con il calcolo
## Punti su cui non cedere
## Che cosa succede se non firmiamo""",
            normative_sources=[
                {"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"},
                {"title": "Regolamento (UE) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/ita"},
            ],
        ),
        "WF2-024": _cohort_two_profile(
            criteria_count=73,
            document_count=10,
            deliverable="audit_termini_somministrazione.md",
            as_of_date="2030-03-12",
            workflow_family="procedural_computation",
            subtask="supply_price_revision_force_majeure_deadline_chain",
            legal_area=["commercial_contracts", "civil_law", "litigation"],
            document_type="supply_contract_deadline_file",
            instructions=[
                "Separa termini scaduti, aperti e futuri e mostra per ciascuno evento iniziale, regola, calcolo e conseguenza.",
                "Non colmare la prova di ricezione o gli allegati mancanti: esplicita l'effetto della lacuna.",
            ],
            output_format="""# Audit dei termini — somministrazione
## Quadro dei termini
## Termini scaduti e che cosa si è perso
## Termini aperti: che cosa fare, entro quando
## Termini futuri da calendarizzare
## Affermazioni della nota interna da correggere
## Che cosa manca dal fascicolo""",
            normative_sources=[{"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"}],
        ),
        "WF2-025": _cohort_two_profile(
            criteria_count=67,
            document_count=11,
            deliverable="matrice_evidenze_sequestro.md",
            as_of_date="2030-10-14",
            workflow_family="dossier_analysis",
            subtask="conservatory_seizure_evidence_matrix",
            legal_area=["civil_procedure", "litigation", "civil_law"],
            document_type="conservatory_seizure_evidence_file",
            instructions=[
                "Distingui prova documentale, dichiarazione di parte, informazione riferita e fatto non documentato.",
                "Non redigere il ricorso: valuta credito, periculum e beni aggredibili, indicando integrazioni e sequenza operativa.",
            ],
            output_format="""# Matrice delle evidenze — sequestro conservativo
## Matrice delle evidenze
## Il credito: che cosa è provato e per quale importo
## Il fondato timore
## Beni e crediti aggredibili
## Elementi non utilizzabili
## Che cosa manca e come procurarlo
## Sequenza e termini
## Risposta al cliente sull'albergo""",
            normative_sources=[
                {"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"},
                {"title": "Codice di procedura civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1940-10-28;1440"},
            ],
        ),
        "WF2-026": _cohort_two_profile(
            criteria_count=70,
            document_count=11,
            deliverable="red_flag_report_dpia.md",
            as_of_date="2031-03-06",
            workflow_family="dossier_analysis",
            subtask="dpia_extra_eea_transfer_red_flag_report",
            legal_area=["privacy", "data_protection", "technology"],
            document_type="dpia_and_transfer_assessment_file",
            instructions=[
                "Classifica ogni rilievo come bloccante o non bloccante e indica documento, conseguenza, azione e responsabile.",
                "Applica la lista di adeguatezza e le fonti nello stato congelato al 25 agosto 2026; non inferire sviluppi successivi.",
                "Non inventare clausole SCC non incluse nel pacchetto: segnala la limitazione del fascicolo.",
            ],
            output_format="""# Red-flag report DPIA e trasferimenti
## Sintesi per la decisione
## Rilievi bloccanti
## Rilievi non bloccanti
## Che cosa non è un rilievo
## Date e numeri, con il calcolo
## Che cosa manca dal pacchetto""",
            normative_sources=[
                {"title": "Regolamento (UE) 2016/679", "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/ita"},
                {"title": "Decisione di esecuzione (UE) 2021/914", "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj/ita"},
                {"title": "Decisioni di adeguatezza della Commissione", "url": "https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en"},
            ],
        ),
        "WF2-027": _cohort_two_profile(
            criteria_count=50,
            document_count=9,
            deliverable="review_memo.md",
            as_of_date="2027-03-11",
            workflow_family="document_review_and_revision",
            subtask="executive_termination_settlement_review",
            legal_area=["employment", "civil_law", "civil_procedure"],
            document_type="executive_termination_settlement_file",
            instructions=[
                "Valuta la bozza nell'interesse del dirigente senza redigere una versione emendata.",
                "Distingui diritti già maturati, incentivo, rinunce, sede di conciliazione, termini e documenti mancanti.",
            ],
            output_format="""# Review memo — dirigente
## Sintesi
## Rilievi in ordine di priorità
## Che cosa si perde firmando la bozza così com'è
## Che cosa è in ordine
## Che cosa manca dal fascicolo
## Termini e prossimi passi""",
            normative_sources=[
                {"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"},
                {"title": "Legge 300/1970", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1970-05-20;300"},
                {"title": "Legge 604/1966", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1966-07-15;604"},
            ],
        ),
        "WF2-028": _cohort_two_profile(
            criteria_count=46,
            document_count=10,
            deliverable="deadline_audit.md",
            as_of_date="2027-03-15",
            workflow_family="procedural_computation",
            subtask="sanctions_screening_deadline_chain",
            legal_area=["aml", "sanctions", "financial_regulation"],
            document_type="sanctions_screening_and_freezing_file",
            instructions=[
                "Tratta separatamente il rapporto della cliente direttamente designata e i fondi sul conto di transito.",
                "L'assetto proprietario della cliente è un distractor: non calcolare soglie di ownership per fondare il congelamento.",
                "Per ogni adempimento indica decorrenza, termine, calcolo, stato, documento e azione residua.",
            ],
            output_format="""# Deadline audit — sanctions screening
## Sintesi
## Matrice degli adempimenti
## Ancore e dipendenze
## Che cosa non richiede rilievo
## Che cosa manca dal fascicolo
## Azioni residue""",
            normative_sources=[
                {"title": "D.Lgs. 109/2007", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007;109"},
                {"title": "D.Lgs. 231/2007", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007;231"},
            ],
        ),
        "WF2-029": _cohort_two_profile(
            criteria_count=41,
            document_count=9,
            deliverable="issue_memo.md",
            as_of_date="2027-02-04",
            workflow_family="dossier_analysis",
            subtask="model_231_third_party_red_flags",
            legal_area=["compliance", "anti_corruption", "corporate_crime"],
            document_type="model_231_third_party_file",
            instructions=[
                "Distingui violazioni dei presidi interni, indicatori di rischio e affermazioni di illecito non sostenibili dagli atti.",
                "Ricostruisci il rapporto e formula una decisione sul rinnovo con termine e verifiche prioritarie.",
            ],
            output_format="""# Issue memo — Modello 231 e terza parte
## Sintesi
## Ricostruzione del rapporto
## Scostamenti dai presidi del Modello
## Limiti del fascicolo
## Che cosa non costituisce rilievo
## Decisione, termine e verifiche""",
            normative_sources=[{"title": "D.Lgs. 231/2001", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001;231"}],
        ),
        "WF2-030": _cohort_two_profile(
            criteria_count=38,
            document_count=8,
            deliverable="deadline_memo.md",
            as_of_date="2027-02-08",
            workflow_family="procedural_computation",
            subtask="do_claims_made_notice_deadline",
            legal_area=["insurance", "civil_law", "litigation"],
            document_type="do_claims_made_policy_file",
            instructions=[
                "Indica una sola data di denuncia e ricostruisci il calcolo dal fatto qualificato come richiesta risarcitoria.",
                "Tratta la copertura come componente secondaria: separa operatività, limiti del fascicolo e conseguenze non determinabili.",
            ],
            output_format="""# Deadline memo — polizza D&O
## Data entro cui denunciare
## Regola applicata e dies a quo
## Tabella di calcolo
## Date non determinanti
## Operatività della garanzia alla data di riferimento
## Che cosa fare e che cosa non fare""",
            normative_sources=[{"title": "Codice civile", "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262"}],
        ),
    }
)

for _task_id, _profile in TASK_PROFILES.items():
    _profile["document_coverage_policy"] = "observe_only"
    _profile["native_artifact_mode"] = (
        "docx_redline"
        if _task_id in {"WF2-001", "WF2-008", "WF2-013", "WF2-014", "WF2-021"}
        else "docx"
        if _task_id in {"WF2-002", "WF2-005"}
        else "markdown"
    )
    _profile["document_preset"] = (
        "contract_negotiation_brief"
        if _task_id in {"WF2-001", "WF2-008", "WF2-013", "WF2-014", "WF2-021"}
        else "standard_business_brief"
    )

SUPPORTED_TASKS = set(TASK_PROFILES)


def is_workflow2_root(root: Path) -> bool:
    manifest = root / "manifest.json"
    if not manifest.is_file():
        return False
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return payload.get("corpus_id") == "task_workflow2.0"


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"oggetto JSON atteso in {path}")
    return payload


def _criterion_title(raw_text: str, criterion_id: str) -> str:
    first = raw_text.splitlines()[0].strip()
    first = re.sub(rf"^{re.escape(criterion_id)}\s+", "", first)
    first = re.sub(r"\s*\[[^]]+\]", "", first)
    first = re.sub(r"\s*→\s*MECC\.?$", "", first, flags=re.IGNORECASE)
    return first.strip(" .—") or criterion_id


def _severity(value: str | None) -> str | None:
    return {
        "alta": "material",
        "media": "significant",
        "bassa": "minor",
    }.get((value or "").casefold())


def _match_criteria(item: dict[str, Any]) -> str:
    verification = item.get("verification")
    passed = item.get("pass_condition")
    failed = item.get("fail_condition")
    indifferent = item.get("indifferent")
    if not verification or not passed:
        return str(item.get("raw_text") or "").strip()
    parts = [
        f"Oggetto del criterio: {verification}",
        f"PASS se: {passed}",
    ]
    if failed:
        parts.append(f"FAIL se: {failed}")
    if indifferent:
        parts.append(f"Indifferente: {indifferent}")
    source = item.get("source")
    if source:
        parts.append(f"Evidence anchor privato: {source}")
    return "\n".join(parts)


def _runtime_route(item: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    criterion_id = str(item["id"])
    try:
        return profile["runtime_routing"][criterion_id]
    except KeyError as exc:
        raise ValueError(f"routing runtime mancante per {criterion_id}") from exc


def _verification_class(item: dict[str, Any], profile: dict[str, Any]) -> str:
    return str(_runtime_route(item, profile)["verification_class"])


def _criterion_logic(item: dict[str, Any], profile: dict[str, Any]) -> str:
    return str(_runtime_route(item, profile)["criterion_logic"])


def _evaluation_scope(
    item: dict[str, Any], profile: dict[str, Any]
) -> tuple[str, str | None]:
    route = _runtime_route(item, profile)
    return str(route["evaluation_scope"]), route.get("scope_locator")


def _normalized_rubric(
    raw: dict[str, Any], profile: dict[str, Any]
) -> WorkflowRubric:
    task_id = str(raw["task_id"])
    deliverables = list(profile.get("deliverables") or [profile["deliverable"]])
    criteria: list[dict[str, Any]] = []
    for item in raw.get("criteria", []):
        criterion_id = str(item["id"])
        verification_class = _verification_class(item, profile)
        evaluation_scope, scope_locator = _evaluation_scope(item, profile)
        deterministic = criterion_id in profile["deterministic_criteria"]
        category = (
            "format"
            if criterion_id.startswith("A.")
            else "dates"
            if criterion_id.startswith("C.")
            else "legal"
        )
        criteria.append(
            {
                "id": criterion_id,
                "title": _criterion_title(
                    str(item.get("raw_text") or ""), criterion_id
                ),
                "scoring_type": "required",
                "category": category,
                "deliverables": deliverables,
                "match_criteria": _match_criteria(item),
                "pass_condition": item.get("pass_condition")
                or str(item.get("raw_text") or "").strip(),
                "severity": _severity(item.get("severity")),
                "evaluation_mode": "deterministic" if deterministic else "judge",
                "deterministic_checks": (
                    [f"{task_id}-{criterion_id.replace('.', '')}"]
                    if deterministic
                    else []
                ),
                "verification_class": verification_class,
                "criterion_type": item.get("criterion_type"),
                "criterion_logic": _criterion_logic(item, profile),
                "evaluation_scope": evaluation_scope,
                "scope_locator": scope_locator,
            }
        )
    return WorkflowRubric.model_validate(
        {
            "task_id": task_id,
            "rubric_version": "0.2.0-draft+agentic.2",
            "scoring_method": "all_pass_and_criterion_rate",
            "criteria": criteria,
        }
    )


def load_workflow2_task(root: Path, task_id: str) -> LoadedWorkflowTask:
    root = root.resolve()
    if task_id not in SUPPORTED_TASKS:
        raise ValueError(f"profilo agentic non disponibile per {task_id}")
    profile = dict(TASK_PROFILES[task_id])
    deliverables = list(profile.get("deliverables") or [profile["deliverable"]])
    manifest = _read_json(root / "manifest.json")
    manifest_item = next(
        item for item in manifest["tasks"] if item.get("task_id") == task_id
    )
    task_dir = root / manifest_item["relative_path"]
    imported_spec_path = task_dir / "task_spec.json"
    imported_rubric_path = task_dir / "private/rubric.json"
    imported_spec = _read_json(imported_spec_path)
    raw_rubric = _read_json(imported_rubric_path)
    routing = _read_json(task_dir / "private/runtime_routing.json")
    route_criteria = routing.get("criteria")
    if (
        routing.get("schema_version") != "workflow2_runtime_routing_v1"
        or routing.get("task_id") != task_id
        or not isinstance(route_criteria, dict)
    ):
        raise ValueError(f"routing runtime non valido per {task_id}")
    profile["runtime_routing"] = route_criteria

    if imported_spec.get("task_id") != task_id or raw_rubric.get("task_id") != task_id:
        raise ValueError(f"identità incoerente nel corpus importato per {task_id}")
    if imported_spec.get("revision_status") != "pilot_ready":
        raise ValueError(f"{task_id} non è più marcato pilot_ready nel corpus importato")
    if raw_rubric.get("status") != "pilot_ready":
        raise ValueError(f"rubrica di {task_id} non più marcata pilot_ready")
    raw_criteria = raw_rubric.get("criteria")
    if not isinstance(raw_criteria, list):
        raise ValueError(f"rubrica di {task_id} senza lista criteria")
    criterion_ids = {str(item.get("id")) for item in raw_criteria}
    if set(route_criteria) != criterion_ids:
        raise ValueError(
            f"routing runtime incompleto per {task_id}: "
            f"rubrica={len(criterion_ids)}, routing={len(route_criteria)}"
        )
    expected_criteria = int(profile["criteria_count"])
    declared_counts = {
        "manifest": manifest_item.get("criteria_count"),
        "rubric": raw_rubric.get("criteria_count"),
        "actual": len(raw_criteria),
    }
    if any(value != expected_criteria for value in declared_counts.values()):
        raise ValueError(
            f"drift nella rubrica di {task_id}: {declared_counts}; "
            f"attesi {expected_criteria} criteri"
        )

    public_documents = sorted(
        path.relative_to(task_dir).as_posix()
        for path in (task_dir / "public/documents").rglob("*")
        if path.is_file() and not path.name.startswith(".")
    )
    expected_documents = int(profile["document_count"])
    if len(public_documents) != expected_documents:
        raise ValueError(
            f"drift nel fascicolo di {task_id}: documenti={len(public_documents)}, "
            f"attesi={expected_documents}"
        )
    public_inputs = [
        "public/01_task.md",
        "public/02_reference_pack.md",
        *profile["additional_public_inputs"],
        *public_documents,
    ]
    missing_public = [item for item in public_inputs if not (task_dir / item).is_file()]
    if missing_public:
        raise ValueError(f"input pubblici mancanti per {task_id}: {missing_public}")

    expected_deliverable_fields = (
        {"expected_deliverable": deliverables[0]}
        if len(deliverables) == 1
        else {"expected_deliverables": deliverables}
    )
    spec = WorkflowTaskSpec.model_validate(
        {
            "task_id": task_id,
            "version": "2.0.0-draft+agentic.3",
            "status": imported_spec["revision_status"],
            "language": "it",
            "jurisdiction": ["IT", "EU"],
            "as_of_date": profile["as_of_date"],
            "workflow_family": profile["workflow_family"],
            "subtask": profile["subtask"],
            "output_mode": "prompt_only_free_artifacts",
            "granularity": profile["granularity"],
            "legal_area": profile["legal_area"],
            "document_type": profile["document_type"],
            "difficulty": "high",
            "estimated_completion_minutes": profile["estimated_minutes"],
            "methodology_version": "0.3.0-draft",
            "benchmark_split": "public_development",
            "expert_effort": {
                "band": "long",
                "estimated_minutes": profile["estimated_minutes"],
                "reference_role": "senior_associate",
            },
            "capabilities_tested": profile["capabilities"],
            "supported_execution_modes": [
                "generic_agent",
                "text_bundle",
                "agentic_workspace",
            ],
            "submission_contract": "prompt_only_free_artifacts_v1",
            "tool_allowlist": COMMON_TOOLS,
            "agentic_instructions": profile["agentic_instructions"],
            "agentic_output_format": profile["output_format"],
            "evidence_policy": {
                "required": True,
                "citation_granularity": "document_and_locator",
            },
            "scaffolding": {
                "level": "workflow_guidance",
                "exposed_aids": profile["scaffolding_aids"],
                "primary_measurement": profile["primary_measurement"],
                "not_purely_measured": profile["not_purely_measured"],
            },
            "synthetic_case": True,
            "contains_personal_data": False,
            "public_inputs": public_inputs,
            **expected_deliverable_fields,
            "private_evaluation": {
                "rubric": "private/rubric.json",
                "review_notes": "private/review_notes.md",
            },
            "evaluation_dimensions": profile["evaluation_dimensions"],
            "normative_sources": profile["normative_sources"],
            "artifact_checks": profile["artifact_checks"],
            "pilot_status": imported_spec.get("pilot_status"),
            "gold_legal_signoff": imported_spec.get("gold_legal_signoff"),
            "document_coverage_policy": profile["document_coverage_policy"],
            "native_artifact_mode": profile["native_artifact_mode"],
            "document_preset": profile["document_preset"],
            "runtime_routing": routing,
        }
    )
    rubric = _normalized_rubric(raw_rubric, profile)
    return apply_deterministic_overlay(
        LoadedWorkflowTask(
            root=root,
            directory=task_dir,
            spec_path=imported_spec_path,
            rubric_path=imported_rubric_path,
            spec=spec,
            rubric=rubric,
        )
    )


def discover_workflow2_tasks(root: Path) -> list[LoadedWorkflowTask]:
    from .loader import load_task

    tasks = [
        load_workflow2_task(root, task_id) for task_id in sorted(SUPPORTED_TASKS)
    ]
    for spec_path in sorted(root.glob("*/*/task_spec.json")):
        raw = _read_json(spec_path)
        task_id = str(raw.get("task_id") or "")
        if task_id in SUPPORTED_TASKS:
            continue
        if re.fullmatch(r"WF2-(?:0(?:3[1-9]|[4-9]\d)|100)", task_id):
            loaded = load_task(spec_path)
            tasks.append(
                apply_deterministic_overlay(
                    LoadedWorkflowTask(
                        root=loaded.root,
                        directory=loaded.directory,
                        spec_path=loaded.spec_path,
                        rubric_path=loaded.rubric_path,
                        spec=loaded.spec.model_copy(
                            update={
                                "output_mode": "prompt_only_free_artifacts",
                                "supported_execution_modes": [
                                    "generic_agent",
                                    "text_bundle",
                                    "agentic_workspace",
                                ],
                                "submission_contract": "prompt_only_free_artifacts_v1",
                                "tool_allowlist": [
                                    tool
                                    for tool in loaded.spec.tool_allowlist
                                    if tool != "record_decision"
                                ],
                                "document_coverage_policy": "observe_only",
                            }
                        ),
                        rubric=loaded.rubric,
                    )
                )
            )

    task_ids = [task.spec.task_id for task in tasks]
    if len(task_ids) != len(set(task_ids)):
        raise ValueError("task_id duplicati nel corpus Workflow 2.0")
    return sorted(tasks, key=lambda task: int(task.spec.task_id.rsplit("-", 1)[-1]))
