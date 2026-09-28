"""Applica al task caricato i controlli deterministici validati.

I controlli vivono in <task>/private/deterministic_checks.json, generato da
scripts/build_deterministic_checks.py (repository di authoring legal-ITA) e validato in shadow mode contro run
gia' giudicate (scripts/shadow_deterministic_checks.py).

Vengono applicate SOLTANTO le proposte con status "validated": diventano
artifact_checks dello spec e portano il criterio corrispondente in
evaluation_mode "deterministic", togliendolo al judge.

Le proposte con status "proposed" non hanno effetto sul runtime: restano
nel file come lavoro da completare.
"""

from __future__ import annotations

import dataclasses
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from .models import LoadedWorkflowTask

OVERLAY_FILENAME = "private/deterministic_checks.json"
SCHEMA_VERSION = "workflow2_deterministic_checks_v1"


def load_overlay(task_directory) -> list[dict]:
    path = task_directory / OVERLAY_FILENAME
    if not path.is_file():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"overlay deterministico non riconosciuto: {path}")
    return [
        proposal
        for proposal in payload.get("proposals", [])
        if proposal.get("status") == "validated"
    ]


def apply_deterministic_overlay(task: "LoadedWorkflowTask") -> "LoadedWorkflowTask":
    """Restituisce il task con i controlli validati applicati."""
    validated = load_overlay(task.directory)
    if not validated:
        return task

    by_criterion = {str(item["criterion_id"]): item for item in validated}
    existing_check_ids = {item.id for item in task.spec.artifact_checks}

    nuovi_check = [
        item["check"]
        for item in validated
        if item["check"]["id"] not in existing_check_ids
    ]
    if not nuovi_check:
        return task

    payload_spec = task.spec.model_dump()
    payload_spec["artifact_checks"] = [*payload_spec.get("artifact_checks", []), *nuovi_check]
    # Rivalidazione completa: i nuovi check passano dal validatore di
    # ArtifactCheck e dal controllo di coerenza sui deliverable attesi.
    spec = type(task.spec).model_validate(payload_spec)

    criteri = []
    for criterion in task.rubric.criteria:
        proposal = by_criterion.get(str(criterion.id))
        if proposal is None or criterion.evaluation_mode == "deterministic":
            criteri.append(criterion)
            continue
        payload = criterion.model_dump()
        payload["evaluation_mode"] = "deterministic"
        payload["verification_class"] = "deterministic"
        payload["deterministic_checks"] = [proposal["check"]["id"]]
        criteri.append(type(criterion).model_validate(payload))

    rubric = type(task.rubric).model_validate(
        {**task.rubric.model_dump(), "criteria": [item.model_dump() for item in criteri]}
    )
    return dataclasses.replace(task, spec=spec, rubric=rubric)
