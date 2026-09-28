"""Contratti dati normalizzati dei task agentic workflow."""

from __future__ import annotations

import base64
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


WorkflowFamily = Literal[
    "document_review_and_revision",
    "dossier_analysis",
    "procedural_computation",
]

BenchmarkSplit = Literal[
    "public_development",
    "private_calibration",
    "sealed_benchmark",
]
ExpertEffortBand = Literal["short", "medium", "long"]
ExecutionMode = Literal[
    "text_bundle",
    "native_documents",
    "agentic_workspace",
    "generic_agent",
]
CriterionSeverity = Literal["material", "significant", "minor"]
CriterionEvaluationMode = Literal["judge", "deterministic"]
CaseOrigin = Literal[
    "fully_synthetic",
    "source_grounded_synthetic",
    "real_anonymized",
    "real_public",
]
GroundingStatus = Literal[
    "unmapped",
    "authority_mapped_candidate",
    "source_pack_validated",
    "expert_validated",
]
AuthorityCoverageStatus = Literal[
    "authority_backed",
    "factual_only",
    "benchmark_method",
    "gap",
]
DocumentGroundingLevel = Literal[
    "source_structured_synthetic",
    "source_constrained_synthetic",
    "synthetic_carrier",
]
SourceSnapshotStatus = Literal["remote_only", "stored"]
ArtifactCheckType = Literal[
    "required_markdown_headings",
    "max_words",
    "section_max_words",
    "section_list_items_range",
    "ordered_markdown_blocks",
    "repeated_block_required_fields",
    "labeled_value_allowlist",
    "labeled_source_locator",
    "normative_reference_allowlist",
    "required_regex",
    "docx_features",
]
VerificationClass = Literal[
    "esatta",
    "span",
    "scansione",
    "judge",
    "deterministic",
]
CriterionLogic = Literal[
    "required_presence",
    "prohibited_presence",
    "conditional_if_mentioned",
]
EvaluationScope = Literal["all_deliverables", "section"]
DecisionStage = Literal["triage", "analysis", "decision", "final_check"]
DecisionConfidence = Literal["low", "medium", "high"]


def safe_relative_path(value: str, *, label: str) -> str:
    """Validate and normalize a repository-relative POSIX path."""
    normalized = value.replace("\\", "/").strip()
    path = PurePosixPath(normalized)
    if not normalized or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{label} non sicuro: {value!r}")
    return path.as_posix()


class DeliverableRules(BaseModel):
    model_config = ConfigDict(extra="forbid")

    one_of_required: list[str] = Field(default_factory=list)
    always_required: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_paths(self):
        self.one_of_required = [
            safe_relative_path(item, label="deliverable one_of_required")
            for item in self.one_of_required
        ]
        self.always_required = [
            safe_relative_path(item, label="deliverable always_required")
            for item in self.always_required
        ]
        return self


class ExpertEffort(BaseModel):
    model_config = ConfigDict(extra="forbid")

    band: ExpertEffortBand
    estimated_minutes: int = Field(gt=0)
    reference_role: str = Field(min_length=1)


class EvidencePolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    required: bool
    citation_granularity: str = Field(min_length=1)


class ScaffoldingSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: Literal["none", "issue_inventory", "workflow_guidance"]
    exposed_aids: list[str] = Field(default_factory=list)
    primary_measurement: list[str] = Field(default_factory=list)
    not_purely_measured: list[str] = Field(default_factory=list)


class TaskProvenance(BaseModel):
    """Dichiarazione sintetica, senza promozioni implicite a caso reale."""

    model_config = ConfigDict(extra="forbid")

    case_origin: CaseOrigin
    grounding_status: GroundingStatus
    source_registry: str
    source_pack: str
    derived_from_task_id: str | None = None
    redistribution_status: str = Field(min_length=1)
    limitations: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_paths(self):
        self.source_registry = safe_relative_path(
            self.source_registry,
            label="provenance source registry",
        )
        self.source_pack = safe_relative_path(
            self.source_pack,
            label="provenance source pack",
        )
        if not self.source_registry.startswith("sources/"):
            raise ValueError("source_registry deve trovarsi sotto sources/")
        if not self.source_pack.startswith("private/"):
            raise ValueError("source_pack deve trovarsi nella busta private/")
        if any(not item.strip() for item in self.limitations):
            raise ValueError("provenance.limitations contiene un valore vuoto")
        return self


class ArtifactCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    type: ArtifactCheckType
    artifact: str
    headings: list[str] = Field(default_factory=list)
    section: str | None = None
    value: int | None = Field(default=None, gt=0)
    minimum: int | None = Field(default=None, ge=0)
    maximum: int | None = Field(default=None, ge=0)
    block_heading_pattern: str | None = None
    required_fields: list[str] = Field(default_factory=list)
    label: str | None = None
    allowed_values: list[str] = Field(default_factory=list)
    patterns: list[str] = Field(default_factory=list)
    required_features: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_check(self):
        self.artifact = safe_relative_path(self.artifact, label=f"artifact check {self.id}")
        if self.type == "required_markdown_headings" and not self.headings:
            raise ValueError(f"{self.id}: headings obbligatori")
        if self.type == "max_words" and self.value is None:
            raise ValueError(f"{self.id}: value obbligatorio")
        if self.type == "section_max_words" and (
            self.section is None or self.value is None
        ):
            raise ValueError(f"{self.id}: section e value obbligatori")
        if self.type == "section_list_items_range" and (
            self.section is None
            or self.minimum is None
            or self.maximum is None
            or self.minimum > self.maximum
        ):
            raise ValueError(f"{self.id}: range di lista non valido")
        if self.type == "ordered_markdown_blocks" and (
            not self.block_heading_pattern or self.minimum is None
        ):
            raise ValueError(
                f"{self.id}: block_heading_pattern e minimum obbligatori"
            )
        if self.type == "repeated_block_required_fields" and (
            not self.block_heading_pattern or not self.required_fields
        ):
            raise ValueError(
                f"{self.id}: pattern dei blocchi e required_fields obbligatori"
            )
        if self.type == "labeled_value_allowlist" and (
            not self.block_heading_pattern or not self.label or not self.allowed_values
        ):
            raise ValueError(
                f"{self.id}: pattern, label e allowed_values obbligatori"
            )
        if self.type == "labeled_source_locator" and (
            not self.block_heading_pattern or not self.label
        ):
            raise ValueError(f"{self.id}: pattern e label obbligatori")
        if self.type == "normative_reference_allowlist" and not self.allowed_values:
            raise ValueError(f"{self.id}: allowed_values obbligatori")
        if self.type == "required_regex" and not self.patterns:
            raise ValueError(f"{self.id}: patterns obbligatori")
        if self.type == "docx_features" and not self.required_features:
            raise ValueError(f"{self.id}: required_features obbligatori")
        for pattern in self.patterns:
            try:
                re.compile(pattern)
            except re.error as exc:
                raise ValueError(f"{self.id}: regex non valida: {exc}") from exc
        return self


class WorkflowTaskSpec(BaseModel):
    """Schema tollerante del corpus, con normalizzazione delle varianti v0.1."""

    model_config = ConfigDict(extra="allow")

    task_id: str
    version: str
    status: str
    language: str
    jurisdiction: list[str]
    as_of_date: str
    workflow_family: WorkflowFamily
    subtask: str
    output_mode: str
    granularity: str
    legal_area: str | list[str]
    document_type: str
    difficulty: str
    estimated_completion_minutes: int = Field(gt=0)
    methodology_version: str | None = None
    benchmark_split: BenchmarkSplit | None = None
    expert_effort: ExpertEffort | None = None
    capabilities_tested: list[str] = Field(default_factory=list)
    supported_execution_modes: list[ExecutionMode] = Field(default_factory=list)
    submission_contract: str | None = None
    tool_allowlist: list[str] = Field(default_factory=list)
    agentic_instructions: list[str] = Field(default_factory=list)
    agentic_output_format: str | None = None
    evidence_policy: EvidencePolicy | None = None
    scaffolding: ScaffoldingSpec | None = None
    provenance: TaskProvenance | None = None
    artifact_checks: list[ArtifactCheck] = Field(default_factory=list)
    synthetic_case: bool
    contains_personal_data: bool
    public_inputs: list[str]
    text_only_fallback: str | None = None
    text_only_fallbacks: list[str] = Field(default_factory=list)
    expected_deliverable: str | None = None
    expected_deliverables: list[str] = Field(default_factory=list)
    deliverable_rules: DeliverableRules | None = None
    private_evaluation: dict[str, str]
    evaluation_dimensions: list[str]
    normative_sources: list[dict[str, Any]]

    @model_validator(mode="after")
    def normalize_variants(self):
        self.public_inputs = [
            safe_relative_path(item, label="public input")
            for item in self.public_inputs
        ]
        self.text_only_fallbacks = [
            safe_relative_path(item, label="text fallback")
            for item in self.text_only_fallbacks
        ]
        if self.text_only_fallback:
            self.text_only_fallback = safe_relative_path(
                self.text_only_fallback,
                label="text fallback",
            )
        self.expected_deliverables = [
            safe_relative_path(item, label="expected deliverable")
            for item in self.expected_deliverables
        ]
        if self.expected_deliverable:
            self.expected_deliverable = safe_relative_path(
                self.expected_deliverable,
                label="expected deliverable",
            )
        self.private_evaluation = {
            key: safe_relative_path(value, label=f"private_evaluation.{key}")
            for key, value in self.private_evaluation.items()
        }
        if bool(self.expected_deliverable) == bool(self.expected_deliverables):
            raise ValueError(
                "usare esattamente uno tra expected_deliverable ed expected_deliverables"
            )
        if (
            self.expert_effort is not None
            and self.expert_effort.estimated_minutes
            != self.estimated_completion_minutes
        ):
            raise ValueError(
                "expert_effort.estimated_minutes deve coincidere con "
                "estimated_completion_minutes"
            )
        self.capabilities_tested = [item.strip() for item in self.capabilities_tested]
        if any(not item for item in self.capabilities_tested):
            raise ValueError("capabilities_tested contiene un valore vuoto")
        if len(self.capabilities_tested) != len(set(self.capabilities_tested)):
            raise ValueError("capabilities_tested contiene duplicati")
        if len(self.supported_execution_modes) != len(
            set(self.supported_execution_modes)
        ):
            raise ValueError("supported_execution_modes contiene duplicati")
        if len(self.tool_allowlist) != len(set(self.tool_allowlist)):
            raise ValueError("tool_allowlist contiene duplicati")
        if any(not item.strip() for item in self.tool_allowlist):
            raise ValueError("tool_allowlist contiene un valore vuoto")
        if any(not item.strip() for item in self.agentic_instructions):
            raise ValueError("agentic_instructions contiene un valore vuoto")
        if self.agentic_output_format is not None:
            self.agentic_output_format = self.agentic_output_format.strip()
            if not self.agentic_output_format:
                raise ValueError("agentic_output_format non può essere vuoto")
        artifact_check_ids = [item.id for item in self.artifact_checks]
        if len(artifact_check_ids) != len(set(artifact_check_ids)):
            raise ValueError("artifact_checks contiene ID duplicati")
        expected = set(self.deliverable_names)
        for check in self.artifact_checks:
            if check.artifact not in expected:
                raise ValueError(
                    f"artifact check {check.id} riferisce un deliverable non atteso"
                )
        return self

    @property
    def fallback_paths(self) -> list[str]:
        values = list(self.text_only_fallbacks)
        if self.text_only_fallback:
            values.append(self.text_only_fallback)
        return values

    @property
    def deliverable_names(self) -> list[str]:
        if self.expected_deliverable:
            return [self.expected_deliverable]
        return list(self.expected_deliverables)

    @property
    def preferred_text_deliverables(self) -> list[str]:
        rules = self.deliverable_rules
        if rules is None:
            return list(self.deliverable_names)
        alternatives = [item for item in rules.one_of_required if item.endswith(".md")]
        chosen = alternatives[:1] or rules.one_of_required[:1]
        return [*chosen, *rules.always_required]


class EvidenceAnchor(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document: str
    locator: str = Field(min_length=1)
    supports: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_document(self):
        self.document = safe_relative_path(
            self.document,
            label="criterion evidence anchor document",
        )
        if not self.document.startswith("public/"):
            raise ValueError("evidence anchor deve riferire un input public/")
        return self


class AuthorityAnchor(BaseModel):
    """Proposizione giuridica collegata a un locator del registro fonti."""

    model_config = ConfigDict(extra="forbid")

    source_id: str = Field(min_length=1)
    locator_id: str = Field(min_length=1)
    supports: str = Field(min_length=1)


class AuthorityLocator(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    citation: str = Field(min_length=1)
    supports: str = Field(min_length=1)


class SourceSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: SourceSnapshotStatus
    path: str | None = None
    sha256: str | None = None

    @model_validator(mode="after")
    def validate_snapshot(self):
        if self.status == "remote_only":
            if self.path is not None or self.sha256 is not None:
                raise ValueError("snapshot remote_only non può dichiarare path o sha256")
            return self
        if not self.path or not self.sha256:
            raise ValueError("snapshot stored richiede path e sha256")
        self.path = safe_relative_path(self.path, label="source snapshot")
        if not self.path.startswith("sources/snapshots/"):
            raise ValueError("snapshot deve trovarsi sotto sources/snapshots/")
        if len(self.sha256) != 64:
            raise ValueError("sha256 snapshot non valido")
        return self


class AuthoritySource(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    source_type: Literal["binding_law", "official_template", "official_guidance"]
    title: str = Field(min_length=1)
    publisher: str = Field(min_length=1)
    official_url: str = Field(min_length=1)
    jurisdiction: list[str]
    official_status: str = Field(min_length=1)
    accessed_on: str
    redistribution: str = Field(min_length=1)
    snapshot: SourceSnapshot
    locators: list[AuthorityLocator]

    @model_validator(mode="after")
    def validate_source(self):
        if not self.official_url.startswith("https://"):
            raise ValueError(f"{self.id}: official_url deve usare https")
        ids = [item.id for item in self.locators]
        if not ids or len(ids) != len(set(ids)):
            raise ValueError(f"{self.id}: locator mancanti o duplicati")
        return self


class SourceRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    registry_version: str
    as_of_date: str
    sources: list[AuthoritySource]

    @model_validator(mode="after")
    def validate_registry(self):
        ids = [item.id for item in self.sources]
        if not ids or len(ids) != len(set(ids)):
            raise ValueError("source registry vuoto o con ID duplicati")
        return self


class DocumentGrounding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document: str
    generated_artifacts: list[str] = Field(default_factory=list)
    grounding_level: DocumentGroundingLevel
    source_ids: list[str] = Field(default_factory=list)
    transformations: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_documents(self):
        self.document = safe_relative_path(
            self.document,
            label="document grounding document",
        )
        self.generated_artifacts = [
            safe_relative_path(item, label="document grounding generated artifact")
            for item in self.generated_artifacts
        ]
        for path in [self.document, *self.generated_artifacts]:
            if not path.startswith("public/documents/"):
                raise ValueError("document grounding deve riferire public/documents/")
        if self.grounding_level != "synthetic_carrier" and not self.source_ids:
            raise ValueError("documento source-grounded senza source_ids")
        return self


class CriterionAuthorityCoverage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criterion_id: str = Field(min_length=1)
    status: AuthorityCoverageStatus
    authority_anchors: list[AuthorityAnchor] = Field(default_factory=list)
    rationale: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_coverage(self):
        if self.status == "authority_backed" and not self.authority_anchors:
            raise ValueError(
                f"{self.criterion_id}: authority_backed senza authority_anchors"
            )
        if self.status in {"factual_only", "benchmark_method"} and self.authority_anchors:
            raise ValueError(
                f"{self.criterion_id}: status {self.status} con authority_anchors"
            )
        return self


class SourcePackInheritance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    task_id: str = Field(min_length=1)
    source_pack: str
    delta: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_source_pack(self):
        self.source_pack = safe_relative_path(
            self.source_pack,
            label="inherited source pack",
        )
        if "/private/" not in f"/{self.source_pack}":
            raise ValueError("inherited source pack deve trovarsi in private/")
        return self


class SourcePack(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_pack_version: str
    task_id: str
    source_registry_version: str
    status: GroundingStatus
    case_origin: CaseOrigin
    inheritance: SourcePackInheritance | None = None
    source_ids: list[str] = Field(default_factory=list)
    document_grounding: list[DocumentGrounding] = Field(default_factory=list)
    criterion_authority_coverage: list[CriterionAuthorityCoverage] = Field(
        default_factory=list
    )
    release_blockers: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_pack(self):
        if len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("source pack con source_ids duplicati")
        criterion_ids = [item.criterion_id for item in self.criterion_authority_coverage]
        if len(criterion_ids) != len(set(criterion_ids)):
            raise ValueError("source pack con criterion_id duplicati")
        documents = [item.document for item in self.document_grounding]
        if len(documents) != len(set(documents)):
            raise ValueError("source pack con document grounding duplicati")
        if self.inheritance is None and (
            not self.source_ids
            or not self.document_grounding
            or not self.criterion_authority_coverage
        ):
            raise ValueError("source pack standalone incompleto")
        if self.status == "expert_validated" and self.release_blockers:
            raise ValueError("source pack expert_validated con release_blockers aperti")
        return self


class WorkflowCriterion(BaseModel):
    """Rubric criterion supporting both formats currently present in the corpus."""

    model_config = ConfigDict(extra="allow")

    id: str
    scoring_type: str = "required"
    category: str = "legal"
    deliverables: list[str] = Field(default_factory=list)
    title: str | None = None
    match_criteria: str | None = None
    criterion: str | None = None
    pass_condition: str | None = None
    severity: CriterionSeverity | None = None
    evidence_anchors: list[EvidenceAnchor] = Field(default_factory=list)
    accepted_variants: list[str] = Field(default_factory=list)
    must_not_assert: list[str] = Field(default_factory=list)
    evaluation_mode: CriterionEvaluationMode = "judge"
    deterministic_checks: list[str] = Field(default_factory=list)
    verification_class: VerificationClass = "judge"
    criterion_type: str | None = None
    criterion_logic: CriterionLogic = "required_presence"
    evaluation_scope: EvaluationScope = "all_deliverables"
    scope_locator: str | None = None

    @model_validator(mode="after")
    def validate_observable_rule(self):
        if self.scoring_type != "required":
            raise ValueError("i task agentic ammettono soltanto criteri required")
        if (
            self.evaluation_mode == "judge"
            and not self.match_criteria
            and not (self.criterion and self.pass_condition)
        ):
            raise ValueError(
                "il criterio richiede match_criteria oppure criterion + pass_condition"
            )
        if self.evaluation_mode == "deterministic":
            if not self.pass_condition:
                raise ValueError(
                    f"{self.id}: criterio deterministico senza pass_condition"
                )
            if not self.deterministic_checks:
                raise ValueError(
                    f"{self.id}: criterio deterministico senza deterministic_checks"
                )
            self.verification_class = "deterministic"
        if self.evaluation_scope == "section" and not (self.scope_locator or "").strip():
            raise ValueError(f"{self.id}: lo scope section richiede scope_locator")
        self.deliverables = [
            safe_relative_path(item, label=f"criterion {self.id} deliverable")
            for item in self.deliverables
        ]
        self.accepted_variants = [item.strip() for item in self.accepted_variants]
        self.must_not_assert = [item.strip() for item in self.must_not_assert]
        if any(not item for item in self.accepted_variants):
            raise ValueError(f"{self.id}: accepted_variants contiene un valore vuoto")
        if any(not item for item in self.must_not_assert):
            raise ValueError(f"{self.id}: must_not_assert contiene un valore vuoto")
        return self

    @property
    def normalized_title(self) -> str:
        return (self.title or self.criterion or self.id).strip()

    @property
    def normalized_match_criteria(self) -> str:
        if self.match_criteria:
            base = self.match_criteria.strip()
        else:
            base = (
                f"Oggetto del criterio: {(self.criterion or '').strip()}\n"
                f"PASS se: {(self.pass_condition or '').strip()}\n"
                "FAIL se il risultato richiesto è assente, errato, contraddetto o "
                "fondato su fatti non presenti nel fascicolo."
            )

        structured: list[str] = []
        if self.criterion_logic == "required_presence":
            structured.append(
                "Operazione logica: presenza richiesta. Se la proposizione richiesta "
                "manca nell'ambito indicato, assegna FAIL."
            )
        elif self.criterion_logic == "prohibited_presence":
            structured.append(
                "Operazione logica: assenza/divieto. La mancata menzione del tema "
                "soddisfa il criterio; assegna FAIL soltanto se trovi nell'ambito "
                "indicato l'affermazione o il trattamento vietato dalla fail condition."
            )
        else:
            structured.append(
                "Operazione logica: condizionale se menzionato. Se il tema non è "
                "trattato, assegna PASS; se è trattato, valuta soltanto se riceve il "
                "trattamento richiesto o quello vietato dalla fail condition."
            )
        if self.evaluation_scope == "section":
            structured.append(
                f'Ambito di decisione: soltanto la sezione "{self.scope_locator}". '
                "Le occorrenze fuori da questa sezione non possono determinare il verdetto."
            )
        else:
            structured.append("Ambito di decisione: tutti i deliverable consegnati.")
        if self.verification_class == "span":
            structured.append(
                "Classe di verifica: span semantico; cerca la proposizione nel "
                "passaggio pertinente del deliverable, senza richiedere coincidenza letterale."
            )
        elif self.verification_class == "scansione":
            structured.append(
                "Classe di verifica: scansione completa dell'ambito di decisione sopra "
                "indicato; applica la fail condition soltanto entro quell'ambito."
            )
        elif self.verification_class == "esatta":
            structured.append(
                "Classe di verifica: valore esatto nel contesto identificato; una coincidenza "
                "in un passaggio estraneo non soddisfa il criterio."
            )
        if self.pass_condition and self.match_criteria:
            structured.append(f"Condizione strutturata di PASS: {self.pass_condition.strip()}")
        if self.evidence_anchors:
            anchors = "; ".join(
                f"{item.document} — {item.locator}: {item.supports}"
                for item in self.evidence_anchors
            )
            structured.append(f"Evidence anchor privati: {anchors}")
        if self.accepted_variants:
            structured.append(
                "Varianti accettate: " + "; ".join(self.accepted_variants)
            )
        if self.must_not_assert:
            structured.append(
                "Negative space / affermazioni vietate: "
                + "; ".join(self.must_not_assert)
            )
        if self.severity:
            structured.append(
                f"Severità diagnostica (non modifica lo scoring): {self.severity}"
            )
        return "\n".join([base, *structured])

    @property
    def normalized_evidence_scope(self) -> str:
        if self.evaluation_scope == "section":
            return f"section:{self.scope_locator}"
        return "all_deliverables"


class WorkflowRubric(BaseModel):
    model_config = ConfigDict(extra="allow")

    task_id: str
    rubric_version: str | None = None
    scoring_method: str
    criteria: list[WorkflowCriterion]
    diagnostic_clusters: list["DiagnosticCluster"] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_scoring(self):
        if self.scoring_method != "all_pass_and_criterion_rate":
            raise ValueError(
                "scoring_method deve essere all_pass_and_criterion_rate"
            )
        if not self.criteria:
            raise ValueError("la rubrica deve contenere almeno un criterio")
        ids = [criterion.id for criterion in self.criteria]
        if len(ids) != len(set(ids)):
            raise ValueError("gli ID dei criteri devono essere univoci")
        cluster_ids = [cluster.id for cluster in self.diagnostic_clusters]
        if len(cluster_ids) != len(set(cluster_ids)):
            raise ValueError("gli ID dei diagnostic cluster devono essere univoci")
        known = set(ids)
        for cluster in self.diagnostic_clusters:
            referenced = set(cluster.entry_criteria) | set(cluster.dependent_criteria)
            if not referenced.issubset(known):
                raise ValueError(
                    f"cluster {cluster.id} riferisce criteri sconosciuti: "
                    f"{sorted(referenced - known)}"
                )
            for source, target in cluster.hypothesized_edges:
                if source not in referenced or target not in referenced:
                    raise ValueError(
                        f"cluster {cluster.id}: edge fuori dal cluster {source}->{target}"
                    )
        return self


class DiagnosticCluster(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    entry_criteria: list[str] = Field(default_factory=list)
    dependent_criteria: list[str] = Field(default_factory=list)
    hypothesized_edges: list[tuple[str, str]] = Field(default_factory=list)
    interpretation: str = Field(min_length=1)


@dataclass(frozen=True)
class LoadedWorkflowTask:
    root: Path
    directory: Path
    spec_path: Path
    rubric_path: Path
    spec: WorkflowTaskSpec
    rubric: WorkflowRubric

    @property
    def short_id(self) -> str:
        return self.spec.task_id.rsplit("/", 1)[-1]


class WorkflowArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: str
    content: str
    media_type: str = "text/markdown"
    binary_base64: str | None = None
    sha256: str | None = None

    @model_validator(mode="after")
    def validate_artifact(self):
        self.path = safe_relative_path(self.path, label="artifact path")
        if not self.content.strip():
            raise ValueError(f"artifact vuoto: {self.path}")
        if self.binary_base64 is not None:
            try:
                raw = base64.b64decode(self.binary_base64, validate=True)
            except ValueError as exc:
                raise ValueError(f"artifact binario non valido: {self.path}") from exc
            if not raw:
                raise ValueError(f"artifact binario vuoto: {self.path}")
            digest = hashlib.sha256(raw).hexdigest()
            if self.sha256 is not None and self.sha256 != digest:
                raise ValueError(f"sha256 binario incoerente: {self.path}")
            self.sha256 = digest
        elif not self.media_type.startswith("text/"):
            raise ValueError(
                f"artifact non testuale senza binary_base64: {self.path}"
            )
        return self


class DecisionEvidence(BaseModel):
    """A concise, public-envelope fact supporting a model-authored decision."""

    model_config = ConfigDict(extra="forbid")

    document: str
    locator: str | None = Field(default=None, max_length=300)
    finding: str = Field(min_length=1, max_length=700)

    @model_validator(mode="after")
    def validate_evidence(self):
        self.document = safe_relative_path(
            self.document,
            label="decision evidence document",
        )
        if not self.document.startswith("public/"):
            raise ValueError("decision evidence document deve essere pubblico")
        self.finding = self.finding.strip()
        if self.locator is not None:
            self.locator = self.locator.strip() or None
        return self


class DecisionLogEntry(BaseModel):
    """Bounded audit summary authored by the model, never hidden chain-of-thought."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["decision_log_v1"] = "decision_log_v1"
    sequence: int = Field(ge=1)
    timestamp: str = Field(min_length=1)
    tool_sequence: int = Field(ge=1)
    artifact_revision: int = Field(ge=0)
    stage: DecisionStage
    objective: str = Field(min_length=1, max_length=240)
    evidence: list[DecisionEvidence] = Field(default_factory=list, max_length=20)
    documents_not_reviewed: list[str] = Field(default_factory=list, max_length=100)
    inference: str = Field(min_length=1, max_length=1200)
    alternatives_considered: list[str] = Field(default_factory=list, max_length=10)
    decision: str = Field(min_length=1, max_length=1200)
    confidence: DecisionConfidence
    missing_information: list[str] = Field(default_factory=list, max_length=20)
    checks_performed: list[str] = Field(default_factory=list, max_length=20)
    next_action: str = Field(min_length=1, max_length=600)

    @model_validator(mode="after")
    def validate_entry(self):
        for field_name in (
            "objective",
            "inference",
            "decision",
            "next_action",
        ):
            setattr(self, field_name, getattr(self, field_name).strip())
        self.documents_not_reviewed = [
            safe_relative_path(item, label="decision document not reviewed")
            for item in self.documents_not_reviewed
        ]
        if any(not item.startswith("public/") for item in self.documents_not_reviewed):
            raise ValueError("documents_not_reviewed deve contenere solo path pubblici")
        if len(self.documents_not_reviewed) != len(set(self.documents_not_reviewed)):
            raise ValueError("documents_not_reviewed contiene duplicati")
        for field_name in (
            "alternatives_considered",
            "missing_information",
            "checks_performed",
        ):
            values = [item.strip() for item in getattr(self, field_name)]
            if any(not item for item in values):
                raise ValueError(f"{field_name} contiene un valore vuoto")
            setattr(self, field_name, values)
        if self.stage == "final_check" and not self.checks_performed:
            raise ValueError("final_check richiede almeno un controllo eseguito")
        return self


class WorkflowSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    task_id: str
    model: str
    source: Literal["live", "external", "fixture"]
    execution_mode: str = "text_bundle_mvp"
    artifacts: list[WorkflowArtifact]
    raw_response: str | None = None
    model_call_metrics: dict[str, Any] = Field(default_factory=dict)
    agent_transcript: list[dict[str, Any]] = Field(default_factory=list)
    tool_trace: list[dict[str, Any]] = Field(default_factory=list)
    decision_log: list[DecisionLogEntry] = Field(default_factory=list)
    workspace_manifest: dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    @model_validator(mode="after")
    def validate_artifacts(self):
        if not self.artifacts:
            raise ValueError("la submission deve contenere almeno un artifact")
        paths = [artifact.path for artifact in self.artifacts]
        if len(paths) != len(set(paths)):
            raise ValueError("artifact duplicati nella submission")
        return self
