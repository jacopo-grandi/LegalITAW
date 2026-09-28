"""
Modelli dati condivisi da giudici, scoring e risultati WF2.
Tutti i moduli importano da qui — non duplicare strutture dati altrove.
"""

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, Field, model_validator


# ---------------------------------------------------------------------------
# Criteri e task da giudicare
# ---------------------------------------------------------------------------

class Criterion(BaseModel):
    """Singolo criterio della rubrica, nella forma PASS/FAIL passata al judge."""
    id:             str   # es. "C-001"
    title:          str   # titolo breve del criterio
    match_criteria: str   # "PASS se... FAIL se..." — standard per il judge
    deliverables:   list[str] = Field(default_factory=lambda: ["response.md"])
    scoring_type:   str = "required"
    category:       str = "legal"
    criterion_type: str | None = None
    criterion_logic: str | None = None
    verification_class: str | None = None
    evaluation_scope: str | None = None
    scope_locator: str | None = None


@dataclass(frozen=True)
class WorkflowJudgeTask:
    """Task WF2 normalizzato per il judge: incarico, contesto e criteri."""
    task_id: str
    query: str
    criteria: list[Criterion]
    task_type: str = "agentic_workflow"


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

JudgeId = Literal["A", "B", "C"]
JudgeProvider = str
JudgeVerdict = Literal["pass", "fail"]
ConsensusVerdict = Literal["pass", "fail", "unresolved"]
JudgeStatus = Literal["ok", "error"]
JudgeEvidenceStatus = Literal["found", "not_found", "unavailable"]
CriterionEvidenceStatus = Literal[
    "found",
    "not_found",
    "global_scan",
    "invalid",
    "unavailable",
]
ConsensusMethod = Literal[
    "initial_agreement",
    "tie_breaker",
    "recovery_agreement",
    "primary_only",
    "audit_agreement",
    "reviewer_override",
    "audit_recovery",
    "audit_unavailable_primary_retained",
    "agreement_audited",
    "evidence_tie_breaker",
    "tie_breaker_unavailable_agreement_retained",
    "unresolved",
]
ScoringStatus = Literal["complete", "incomplete"]


class JudgeVote(BaseModel):
    """Voto prodotto da un singolo judge per un criterio binario."""

    judge_id: JudgeId
    provider: JudgeProvider
    model: str
    verdict: JudgeVerdict | None
    reasoning: str | None
    evidence: list[str] = Field(default_factory=list)
    evidence_status: JudgeEvidenceStatus = "unavailable"
    status: JudgeStatus
    error: str | None = None
    attempts: int = Field(ge=0)
    latency_ms: int | None = Field(default=None, ge=0)
    probability: float | None = Field(default=None, ge=0.0, le=1.0)
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)

    @model_validator(mode="after")
    def validate_status_consistency(self):
        if self.status == "ok":
            if self.verdict not in ("pass", "fail"):
                raise ValueError("Un voto ok deve avere verdict pass/fail.")
            if self.error is not None:
                raise ValueError("Un voto ok non deve avere error valorizzato.")
            if self.evidence_status == "found" and not self.evidence:
                raise ValueError("evidence_status=found richiede almeno un estratto.")
            if self.evidence_status == "not_found" and self.evidence:
                raise ValueError("evidence_status=not_found non ammette estratti.")
        if self.status == "error" and self.error is None:
            raise ValueError("Un voto in errore deve avere un messaggio sintetico.")
        return self


class ResponseEvidence(BaseModel):
    """Estratto verificato e localizzato nel deliverable dell'agente."""

    artifact: str
    quote: str = Field(min_length=1)
    char_start: int = Field(ge=0)
    char_end: int = Field(gt=0)
    line_start: int = Field(ge=1)
    line_end: int = Field(ge=1)

    @model_validator(mode="after")
    def validate_span(self):
        if self.char_end <= self.char_start:
            raise ValueError("Lo span di evidenza deve avere lunghezza positiva.")
        if self.line_end < self.line_start:
            raise ValueError("Intervallo di righe dell'evidenza non valido.")
        return self


class ConsensusResult(BaseModel):
    """Risultato deterministico del consenso tra judge."""

    verdict: ConsensusVerdict
    reasoning: str
    consensus_method: ConsensusMethod
    supporting_judges: list[JudgeId] = Field(default_factory=list)
    tie_breaker_used: bool
    judge_votes: list[JudgeVote] = Field(default_factory=list)

class CriterionResult(BaseModel):
    """Risultato del judge per un singolo criterio."""
    id:        str   # corrisponde a Criterion.id
    title:     str
    verdict:   str   # "pass", "fail" o "unresolved"
    reasoning: str
    verification_class: str | None = None
    criterion_type: str | None = None
    criterion_logic: str | None = None
    evaluation_scope: str | None = None
    scope_locator: str | None = None
    evidence_status: CriterionEvidenceStatus = "unavailable"
    response_evidence: list[ResponseEvidence] = Field(default_factory=list)
    evidence_scope: str | None = None
    evidence_notes: list[str] = Field(default_factory=list)
    scoring_type: str = "required"
    category:     str = "legal"
    consensus_method: str | None = None
    supporting_judges: list[str] = Field(default_factory=list)
    tie_breaker_used: bool = False
    judge_votes: list[JudgeVote] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_evidence_contract(self):
        if self.evidence_status == "found" and not self.response_evidence:
            raise ValueError("evidence_status=found richiede uno span localizzato.")
        if self.evidence_status != "found" and self.response_evidence:
            raise ValueError("Gli span localizzati richiedono evidence_status=found.")
        if self.evidence_status in {"not_found", "global_scan"} and not self.evidence_scope:
            raise ValueError("La verifica senza span richiede evidence_scope.")
        return self


class TaskScore(BaseModel):
    """Output completo della valutazione di un task (struttura derivata da Harvey LAB)."""
    task_id:          str
    model:            str               # es. "gpt-4o", "claude-sonnet-4-6"
    model_output:     str               # risposta integrale del modello sotto esame
    model_call_provider: str | None = None
    model_call_latency_ms: int | None = Field(default=None, ge=0)
    model_call_input_tokens: int | None = Field(default=None, ge=0)
    model_call_output_tokens: int | None = Field(default=None, ge=0)
    model_call_total_tokens: int | None = Field(default=None, ge=0)
    model_call_cached_input_tokens: int | None = Field(default=None, ge=0)
    model_call_reasoning_tokens: int | None = Field(default=None, ge=0)
    model_call_estimated_cost_usd: float | None = Field(default=None, ge=0)
    model_call_cost_source: str | None = None
    model_call_usage: dict[str, object] = Field(default_factory=dict)
    evaluation_error: str | None = None
    score:            float | None      # 1.0 se all-pass, 0.0 altrimenti, None se incompleto
    all_pass:         bool | None
    reasoning_score:  float | None = None
    reasoning_all_pass: bool | None = None
    reasoning_scoring_status: ScoringStatus = "incomplete"
    content_all_pass: bool | None = None
    scoring_status:   ScoringStatus = "complete"
    n_criteria:       int
    n_passed:         int
    n_unresolved:     int = 0
    n_required:       int
    n_required_passed: int
    n_required_unresolved: int = 0
    n_bonus:          int
    n_bonus_passed:   int
    n_bonus_unresolved: int = 0
    required_pass_rate: float | None
    bonus_pass_rate:  float | None = None
    unresolved_rate:  float = 0.0
    summary:          str
    criteria_results: list[CriterionResult]
    judge_model:      str
    judge_strategy:   str = "single"
    judge_models:     dict[str, str] = Field(default_factory=dict)
    judge_diagnostics: dict[str, object] = Field(default_factory=dict)
    scored_at:        str               # ISO datetime
