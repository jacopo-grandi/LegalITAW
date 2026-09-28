"""Discovery and structural validation for the shared workflow-task layout."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any

from legalitaw.config import AGENTIC_TASKS_DIR

from .models import (
    AuthoritySource,
    LoadedWorkflowTask,
    SourcePack,
    SourceRegistry,
    WorkflowRubric,
    WorkflowTaskSpec,
)


FORBIDDEN_SCORING_KEY_PARTS = ("weight", "threshold", "bonus", "blocking", "cap")


class WorkflowValidationError(ValueError):
    """A task violates the cross-task runtime contract."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise WorkflowValidationError(f"file mancante: {path}") from exc
    except json.JSONDecodeError as exc:
        raise WorkflowValidationError(f"JSON non valido in {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise WorkflowValidationError(f"oggetto JSON atteso in {path}")
    return payload


def _resolve_scoped(task_dir: Path, relative: str, scope: str) -> Path:
    path = (task_dir / relative).resolve()
    expected_root = (task_dir / scope).resolve()
    if not path.is_relative_to(expected_root):
        raise WorkflowValidationError(
            f"{relative!r} esce dalla busta {scope}/ per {task_dir.name}"
        )
    if not path.is_file():
        raise WorkflowValidationError(f"file dichiarato ma assente: {path}")
    return path


def _find_forbidden_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            normalized = str(key).lower()
            if any(part in normalized for part in FORBIDDEN_SCORING_KEY_PARTS):
                found.append(path)
            found.extend(_find_forbidden_keys(item, path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(_find_forbidden_keys(item, f"{prefix}[{index}]"))
    return found


def _validate_deliverables(spec: WorkflowTaskSpec, rubric: WorkflowRubric) -> None:
    expected = set(spec.deliverable_names)
    if len(expected) != len(spec.deliverable_names):
        raise WorkflowValidationError("expected deliverables duplicati")

    rules = spec.deliverable_rules
    if rules is not None:
        referenced = set(rules.one_of_required) | set(rules.always_required)
        if not rules.one_of_required:
            raise WorkflowValidationError("deliverable_rules.one_of_required è vuoto")
        if not referenced.issubset(expected):
            raise WorkflowValidationError(
                "deliverable_rules riferisce file non dichiarati negli expected deliverables"
            )

    for criterion in rubric.criteria:
        if criterion.deliverables and not set(criterion.deliverables).issubset(expected):
            raise WorkflowValidationError(
                f"{criterion.id} riferisce deliverable non dichiarati: "
                f"{sorted(set(criterion.deliverables) - expected)}"
            )


def _validate_evidence_anchors(
    task_dir: Path,
    rubric: WorkflowRubric,
) -> None:
    for criterion in rubric.criteria:
        for anchor in criterion.evidence_anchors:
            _resolve_scoped(task_dir, anchor.document, "public")


def _validate_deterministic_contract(
    spec: WorkflowTaskSpec,
    rubric: WorkflowRubric,
) -> None:
    known_checks = {check.id for check in spec.artifact_checks}
    referenced: set[str] = set()
    for criterion in rubric.criteria:
        if criterion.evaluation_mode != "deterministic":
            if criterion.deterministic_checks:
                raise WorkflowValidationError(
                    f"{criterion.id}: deterministic_checks su criterio judge"
                )
            continue
        criterion_checks = set(criterion.deterministic_checks)
        missing = criterion_checks - known_checks
        if missing:
            raise WorkflowValidationError(
                f"{criterion.id} riferisce artifact check sconosciuti: {sorted(missing)}"
            )
        referenced.update(criterion_checks)
    unused = known_checks - referenced
    if unused:
        raise WorkflowValidationError(
            f"artifact check non collegati a criteri: {sorted(unused)}"
        )


def _resolve_corpus_file(corpus_root: Path, relative: str, scope: str) -> Path:
    path = (corpus_root / relative).resolve()
    expected_root = (corpus_root / scope).resolve()
    if not path.is_relative_to(expected_root):
        raise WorkflowValidationError(
            f"{relative!r} esce dalla directory corpus {scope}/"
        )
    if not path.is_file():
        raise WorkflowValidationError(f"file dichiarato ma assente: {path}")
    return path


def _resolve_inherited_source_pack(corpus_root: Path, relative: str) -> Path:
    path = (corpus_root / relative).resolve()
    if not path.is_relative_to(corpus_root.resolve()):
        raise WorkflowValidationError(
            f"inherited source pack {relative!r} esce dal corpus"
        )
    if path.name != "source_pack.json" or path.parent.name != "private":
        raise WorkflowValidationError(
            "inherited source pack deve puntare a private/source_pack.json"
        )
    if not path.is_file():
        raise WorkflowValidationError(f"file dichiarato ma assente: {path}")
    return path


def _validate_source_snapshot(corpus_root: Path, source: AuthoritySource) -> None:
    """Verify that a stored source snapshot exists and matches its declared hash."""
    snapshot = source.snapshot
    if snapshot.status == "remote_only":
        return
    if snapshot.path is None or snapshot.sha256 is None:  # defensive after Pydantic
        raise WorkflowValidationError(f"{source.id}: snapshot stored incompleto")
    path = _resolve_corpus_file(corpus_root, snapshot.path, "sources")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != snapshot.sha256:
        raise WorkflowValidationError(
            f"{source.id}: SHA-256 snapshot non coincide: "
            f"dichiarato={snapshot.sha256}, calcolato={digest}"
        )


def _validate_provenance(
    task_dir: Path,
    spec: WorkflowTaskSpec,
    rubric: WorkflowRubric,
) -> SourcePack | None:
    provenance = spec.provenance
    if provenance is None:
        if "source_pack" in spec.private_evaluation:
            raise WorkflowValidationError(
                "private_evaluation.source_pack richiede provenance nel task_spec"
            )
        return None

    declared_pack = spec.private_evaluation.get("source_pack")
    if declared_pack != provenance.source_pack:
        raise WorkflowValidationError(
            "provenance.source_pack deve coincidere con private_evaluation.source_pack"
        )

    corpus_root = task_dir.parents[1]
    registry_path = _resolve_corpus_file(
        corpus_root,
        provenance.source_registry,
        "sources",
    )
    pack_path = _resolve_scoped(task_dir, provenance.source_pack, "private")
    try:
        registry = SourceRegistry.model_validate(_read_json(registry_path))
        pack = SourcePack.model_validate(_read_json(pack_path))
    except Exception as exc:
        raise WorkflowValidationError(
            f"provenance non valida per {task_dir.name}: {exc}"
        ) from exc

    if pack.inheritance is not None:
        inherited_path = _resolve_inherited_source_pack(
            corpus_root,
            pack.inheritance.source_pack,
        )
        try:
            inherited = SourcePack.model_validate(_read_json(inherited_path))
        except Exception as exc:
            raise WorkflowValidationError(
                f"inherited source pack non valido {inherited_path}: {exc}"
            ) from exc
        if inherited.task_id != pack.inheritance.task_id:
            raise WorkflowValidationError(
                "task_id dell'inherited source pack non coincide con inheritance.task_id"
            )
        if inherited.inheritance is not None:
            raise WorkflowValidationError(
                "source pack inheritance supporta un solo livello"
            )
        if inherited.source_registry_version != pack.source_registry_version:
            raise WorkflowValidationError(
                "source pack ereditato usa una versione diversa del registro"
            )
        if inherited.case_origin != pack.case_origin:
            raise WorkflowValidationError(
                "source pack ereditato usa una case_origin diversa"
            )
        pack = pack.model_copy(
            update={
                "source_ids": pack.source_ids or inherited.source_ids,
                "document_grounding": (
                    pack.document_grounding or inherited.document_grounding
                ),
                "criterion_authority_coverage": (
                    pack.criterion_authority_coverage
                    or inherited.criterion_authority_coverage
                ),
            }
        )

    if pack.task_id != spec.task_id:
        raise WorkflowValidationError(
            f"task_id source pack {pack.task_id!r} != task_spec {spec.task_id!r}"
        )
    if pack.source_registry_version != registry.registry_version:
        raise WorkflowValidationError(
            "source_registry_version del pack non coincide con il registro"
        )
    if pack.case_origin != provenance.case_origin:
        raise WorkflowValidationError("case_origin incoerente tra provenance e source pack")
    if pack.status != provenance.grounding_status:
        raise WorkflowValidationError(
            "grounding_status incoerente tra provenance e source pack"
        )

    known_sources = {source.id: source for source in registry.sources}
    missing_sources = set(pack.source_ids) - set(known_sources)
    if missing_sources:
        raise WorkflowValidationError(
            f"source pack riferisce fonti sconosciute: {sorted(missing_sources)}"
        )
    for source_id in pack.source_ids:
        _validate_source_snapshot(corpus_root, known_sources[source_id])
    declared_source_urls = {
        item.get("url") for item in spec.normative_sources if item.get("url")
    }
    pack_source_urls = {
        known_sources[source_id].official_url for source_id in pack.source_ids
    }
    if declared_source_urls != pack_source_urls:
        raise WorkflowValidationError(
            "normative_sources non coincide con le fonti del source pack: "
            f"mancanti={sorted(pack_source_urls - declared_source_urls)}, "
            f"extra={sorted(declared_source_urls - pack_source_urls)}"
        )

    public_documents: set[str] = set()
    used_sources: set[str] = set()
    for item in pack.document_grounding:
        _resolve_scoped(task_dir, item.document, "public")
        public_documents.add(item.document)
        for artifact in item.generated_artifacts:
            _resolve_scoped(task_dir, artifact, "public")
            public_documents.add(artifact)
        unknown = set(item.source_ids) - set(pack.source_ids)
        if unknown:
            raise WorkflowValidationError(
                f"document grounding {item.document} usa fonti fuori pack: {sorted(unknown)}"
            )
        used_sources.update(item.source_ids)

    declared_documents = {
        path for path in [*spec.public_inputs, *spec.fallback_paths]
        if path.startswith("public/documents/")
    }
    if public_documents != declared_documents:
        raise WorkflowValidationError(
            "source pack non copre esattamente i documenti pubblici: "
            f"mancanti={sorted(declared_documents - public_documents)}, "
            f"extra={sorted(public_documents - declared_documents)}"
        )

    coverage = {
        item.criterion_id: item for item in pack.criterion_authority_coverage
    }
    rubric_ids = {criterion.id for criterion in rubric.criteria}
    if set(coverage) != rubric_ids:
        raise WorkflowValidationError(
            "criterion_authority_coverage non coincide con la rubrica: "
            f"mancanti={sorted(rubric_ids - set(coverage))}, "
            f"extra={sorted(set(coverage) - rubric_ids)}"
        )
    for item in coverage.values():
        for anchor in item.authority_anchors:
            if anchor.source_id not in pack.source_ids:
                raise WorkflowValidationError(
                    f"{item.criterion_id}: authority source fuori pack {anchor.source_id}"
                )
            locator_ids = {
                locator.id for locator in known_sources[anchor.source_id].locators
            }
            if anchor.locator_id not in locator_ids:
                raise WorkflowValidationError(
                    f"{item.criterion_id}: locator sconosciuto "
                    f"{anchor.source_id}/{anchor.locator_id}"
                )
            used_sources.add(anchor.source_id)
    unused_sources = set(pack.source_ids) - used_sources
    if unused_sources:
        raise WorkflowValidationError(
            f"source pack contiene fonti ornamentali non usate: {sorted(unused_sources)}"
        )
    gaps = [item.criterion_id for item in coverage.values() if item.status == "gap"]
    if gaps and not pack.release_blockers:
        raise WorkflowValidationError(
            f"criterion authority gap senza release blocker: {sorted(gaps)}"
        )
    if pack.status == "authority_mapped_candidate" and not pack.release_blockers:
        raise WorkflowValidationError(
            "authority_mapped_candidate deve dichiarare almeno un release blocker"
        )
    if pack.status in {"source_pack_validated", "expert_validated"}:
        if gaps:
            raise WorkflowValidationError(
                f"source pack validato con authority gap: {sorted(gaps)}"
            )
        remote_only = [
            source_id
            for source_id in pack.source_ids
            if known_sources[source_id].snapshot.status == "remote_only"
        ]
        if remote_only:
            raise WorkflowValidationError(
                "source pack validato con fonti remote_only: "
                f"{sorted(remote_only)}"
            )
    return pack


def load_task(spec_path: Path) -> LoadedWorkflowTask:
    spec_path = spec_path.resolve()
    task_dir = spec_path.parent
    raw_spec = _read_json(spec_path)
    try:
        spec = WorkflowTaskSpec.model_validate(raw_spec)
    except Exception as exc:
        raise WorkflowValidationError(f"task_spec non valido {spec_path}: {exc}") from exc

    if task_dir.parent.name != spec.workflow_family:
        raise WorkflowValidationError(
            f"workflow_family {spec.workflow_family!r} non coincide con la directory "
            f"{task_dir.parent.name!r}"
        )
    task_id_leaf = spec.task_id.rsplit("/", 1)[-1]
    numeric_id = re.search(r"(\d{3})$", task_id_leaf)
    expected_prefix = numeric_id.group(1) if numeric_id else task_id_leaf[:3]
    if task_dir.name[:3] != expected_prefix:
        raise WorkflowValidationError(
            f"ID numerico incoerente tra task_id e directory: {task_dir.name}"
        )

    for relative in spec.public_inputs:
        _resolve_scoped(task_dir, relative, "public")
    for relative in spec.fallback_paths:
        _resolve_scoped(task_dir, relative, "public")
    for relative in spec.private_evaluation.values():
        _resolve_scoped(task_dir, relative, "private")

    rubric_relative = spec.private_evaluation.get("rubric")
    if rubric_relative is None:
        raise WorkflowValidationError("private_evaluation.rubric mancante")
    rubric_path = _resolve_scoped(task_dir, rubric_relative, "private")
    raw_rubric = _read_json(rubric_path)
    forbidden = _find_forbidden_keys(raw_rubric)
    if forbidden:
        raise WorkflowValidationError(
            "chiavi di scoring vietate nella rubrica: " + ", ".join(forbidden)
        )
    try:
        rubric = WorkflowRubric.model_validate(raw_rubric)
    except Exception as exc:
        raise WorkflowValidationError(f"rubrica non valida {rubric_path}: {exc}") from exc
    if rubric.task_id != spec.task_id:
        raise WorkflowValidationError(
            f"task_id rubrica {rubric.task_id!r} != task_spec {spec.task_id!r}"
        )
    _validate_deliverables(spec, rubric)
    _validate_evidence_anchors(task_dir, rubric)
    _validate_deterministic_contract(spec, rubric)
    _validate_provenance(task_dir, spec, rubric)

    return LoadedWorkflowTask(
        root=spec_path.parents[2],
        directory=task_dir,
        spec_path=spec_path,
        rubric_path=rubric_path,
        spec=spec,
        rubric=rubric,
    )


def discover_tasks(root: Path = AGENTIC_TASKS_DIR) -> list[LoadedWorkflowTask]:
    root = root.resolve()
    from .workflow2 import discover_workflow2_tasks, is_workflow2_root

    if is_workflow2_root(root):
        return discover_workflow2_tasks(root)
    spec_paths = sorted(root.glob("*/*/task_spec.json"))
    if not spec_paths:
        raise WorkflowValidationError(f"nessun task_spec.json trovato in {root}")
    tasks = [load_task(path) for path in spec_paths]
    task_ids = [task.spec.task_id for task in tasks]
    if len(task_ids) != len(set(task_ids)):
        raise WorkflowValidationError("task_id duplicati nel corpus agentic")
    return tasks


def select_tasks(
    selectors: list[str] | None,
    *,
    root: Path = AGENTIC_TASKS_DIR,
) -> list[LoadedWorkflowTask]:
    tasks = discover_tasks(root)
    if not selectors or selectors == ["all"]:
        return tasks
    selected: list[LoadedWorkflowTask] = []
    for selector in selectors:
        matches = [
            task
            for task in tasks
            if selector in {task.short_id, task.directory.name, task.spec.task_id}
        ]
        if len(matches) != 1:
            raise WorkflowValidationError(
                f"selettore task {selector!r}: atteso un match, trovati {len(matches)}"
            )
        if matches[0] not in selected:
            selected.append(matches[0])
    return selected


def validate_corpus(root: Path = AGENTIC_TASKS_DIR) -> dict[str, Any]:
    tasks = discover_tasks(root)
    return {
        "status": "ok",
        "task_count": len(tasks),
        "criterion_count": sum(len(task.rubric.criteria) for task in tasks),
        "provenance": {
            "declared_tasks": sum(task.spec.provenance is not None for task in tasks),
            "by_grounding_status": {
                status: sum(
                    task.spec.provenance is not None
                    and task.spec.provenance.grounding_status == status
                    for task in tasks
                )
                for status in sorted(
                    {
                        task.spec.provenance.grounding_status
                        for task in tasks
                        if task.spec.provenance is not None
                    }
                )
            },
        },
        "workflow_families": {
            family: sum(1 for task in tasks if task.spec.workflow_family == family)
            for family in sorted({task.spec.workflow_family for task in tasks})
        },
        "tasks": [
            {
                "short_id": task.short_id,
                "task_id": task.spec.task_id,
                "workflow_family": task.spec.workflow_family,
                "subtask": task.spec.subtask,
                "criteria": len(task.rubric.criteria),
                "deliverables": task.spec.deliverable_names,
            }
            for task in tasks
        ],
    }
