"""Application services for live agentic workflow runs."""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from legalitaw.evaluation.agentic import evaluation_payload
from legalitaw.evaluation.judge import Judge, create_judge_from_config
from legalitaw.agentic.generic_agent import generate_generic_agent_submission
from legalitaw.agentic.models import LoadedWorkflowTask, WorkflowSubmission
from legalitaw.agentic.submissions import (
    save_submission,
)
from legalitaw.agentic.workspace import (
    WorkspaceRunFailure,
    generate_workspace_submission,
    public_envelope_paths,
)
from legalitaw.artifacts import write_json_atomic
from legalitaw.config import (
    AGENTIC_RESULTS_DIR,
    JudgeRuntimeConfig,
    validate_judge_runtime_config,
)
from legalitaw.modeling.gateway import ModelGateway


log = logging.getLogger(__name__)


class BundleRunFailure(RuntimeError):
    """A failed one-shot run with its last provider response preserved."""

    def __init__(
        self,
        message: str,
        *,
        task: LoadedWorkflowTask,
        model: str,
        raw_response: str | None,
        model_call_metrics: dict[str, Any],
    ) -> None:
        super().__init__(message)
        self.task_id = task.spec.task_id
        self.model = model
        self.error_type = type(self).__name__
        self.artifacts: list[Any] = []
        self.tool_trace: list[dict[str, Any]] = []
        self.decision_log: list[Any] = []
        self.workspace_manifest = {
            "run_status": "failed",
            "private_envelope_mounted": False,
            "shell_available": False,
            "workspace_network_available": False,
            "document_coverage": None,
        }
        self.model_call_metrics = model_call_metrics
        self.raw_response = raw_response
        self.execution_mode = "text_bundle"
        self.created_at = datetime.now(timezone.utc).isoformat()


def _decision_log_payload(entries: list[Any]) -> dict[str, Any]:
    return {
        "schema_version": "decision_log_v1",
        "provenance": "model_authored_structured_summary",
        "contains_hidden_chain_of_thought": False,
        "entries": [
            item.model_dump() if hasattr(item, "model_dump") else dict(item)
            for item in entries
        ],
    }


def _safe_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-") or "unknown"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_json(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def create_run_directory(
    task: LoadedWorkflowTask,
    model: str,
    *,
    results_root: Path = AGENTIC_RESULTS_DIR,
) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    return results_root / _safe_component(model) / timestamp / task.short_id


def _base_run_manifest(
    task: LoadedWorkflowTask,
    *,
    model: str,
    source: str,
    execution_mode: str,
    created_at: str,
) -> dict[str, Any]:
    provenance = task.spec.provenance
    public_inputs = public_envelope_paths(task)
    return {
        "task_id": task.spec.task_id,
        "task_version": task.spec.version,
        "rubric_version": task.rubric.rubric_version,
        "methodology_version": task.spec.methodology_version,
        "task_status": task.spec.status,
        "as_of_date": task.spec.as_of_date,
        "normative_sources": task.spec.normative_sources,
        "benchmark_split": task.spec.benchmark_split,
        "model": model,
        "source": source,
        "execution_mode": execution_mode,
        "submission_contract": "prompt_only_free_artifacts_v1",
        "supported_execution_modes": task.spec.supported_execution_modes,
        "tool_allowlist": task.spec.tool_allowlist,
        "runtime_task_profile_sha256": _sha256_json(task.spec.model_dump()),
        "runtime_rubric_profile_sha256": _sha256_json(task.rubric.model_dump()),
        "scaffolding": (
            task.spec.scaffolding.model_dump() if task.spec.scaffolding else None
        ),
        "public_inputs": public_inputs,
        "public_input_sha256": {
            relative: _sha256(task.directory / relative)
            for relative in public_inputs
        },
        "text_fallbacks_used": task.spec.fallback_paths,
        "task_spec_sha256": _sha256(task.spec_path),
        "rubric_sha256": _sha256(task.rubric_path),
        "provenance": provenance.model_dump() if provenance else None,
        "source_pack_sha256": (
            _sha256(task.directory / provenance.source_pack) if provenance else None
        ),
        "source_registry_sha256": (
            _sha256(task.root / provenance.source_registry) if provenance else None
        ),
        "private_inputs_exposed_to_model": False,
        "created_at": created_at,
    }


def create_judge(config: JudgeRuntimeConfig) -> Any:
    validate_judge_runtime_config(config)
    if config.strategy == "single" and config.judge_a.provider == "anthropic":
        return Judge(model=config.judge_a.model)
    return create_judge_from_config(config)


def generate_agentic_submission(
    task: LoadedWorkflowTask,
    *,
    model: str,
    gateway: ModelGateway | None = None,
    max_steps: int = 40,
    timeout_seconds: int = 900,
) -> WorkflowSubmission:
    log.info(
        "[%s] Task avviato — modello=%s, modalità=agentic_workspace",
        task.short_id,
        model,
    )
    submission = generate_workspace_submission(
        task,
        model=model,
        gateway=gateway,
        max_steps=max_steps,
        timeout_seconds=timeout_seconds,
    )
    log.info(
        "[%s] Workspace completato — step=%d, artifact=%s",
        task.short_id,
        len(submission.tool_trace),
        ", ".join(artifact.path for artifact in submission.artifacts),
    )
    return submission


def generate_generic_submission(
    task: LoadedWorkflowTask,
    *,
    model: str,
    max_steps: int = 40,
    timeout_seconds: int = 900,
    profile: str = "bare",
    max_cost_usd: float | None = None,
) -> WorkflowSubmission:
    log.info(
        "[%s] Task avviato — modello=%s, modalità=generic_agent, profilo=%s",
        task.short_id,
        model,
        profile,
    )
    submission = generate_generic_agent_submission(
        task,
        model=model,
        max_turns=max_steps,
        timeout_seconds=timeout_seconds,
        profile=profile,
        max_cost_usd=max_cost_usd,
    )
    log.info(
        "[%s] Generic agent completato — turni=%s, artifact=%s",
        task.short_id,
        submission.workspace_manifest.get("turns"),
        ", ".join(artifact.path for artifact in submission.artifacts),
    )
    return submission


def persist_run(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
    *,
    score: Any | None = None,
    results_root: Path = AGENTIC_RESULTS_DIR,
) -> Path:
    directory = create_run_directory(task, submission.model, results_root=results_root)
    save_submission(submission, directory)
    tool_trace_path: Path | None = None
    agent_transcript_path: Path | None = None
    decision_log_path: Path | None = None
    workspace_manifest_path: Path | None = None
    if submission.tool_trace:
        tool_trace_path = write_json_atomic(
            directory / "tool_trace.json",
            {"events": submission.tool_trace},
        )
    if submission.agent_transcript:
        agent_transcript_path = write_json_atomic(
            directory / "agent_transcript.json",
            {"messages": submission.agent_transcript},
        )
    if submission.workspace_manifest:
        workspace_manifest_path = write_json_atomic(
            directory / "workspace_manifest.json",
            submission.workspace_manifest,
        )
    if submission.decision_log:
        decision_log_path = write_json_atomic(
            directory / "decision_log.json",
            _decision_log_payload(submission.decision_log),
        )
    manifest = {
        **_base_run_manifest(
            task,
            model=submission.model,
            source=submission.source,
            execution_mode=submission.execution_mode,
            created_at=submission.created_at,
        ),
        "run_status": "completed",
        "artifact_sha256": {
            artifact.path: _sha256(directory / artifact.path)
            for artifact in submission.artifacts
        },
        "tool_trace_sha256": _sha256(tool_trace_path) if tool_trace_path else None,
        "agent_transcript_sha256": (
            _sha256(agent_transcript_path) if agent_transcript_path else None
        ),
        "decision_log_sha256": (
            _sha256(decision_log_path) if decision_log_path else None
        ),
        "decision_log_entries": len(submission.decision_log),
        "workspace_manifest_sha256": (
            _sha256(workspace_manifest_path) if workspace_manifest_path else None
        ),
        "workspace_policy": (
            {
                "private_envelope_mounted": submission.workspace_manifest.get(
                    "private_envelope_mounted"
                ),
                "shell_available": submission.workspace_manifest.get("shell_available"),
                "workspace_network_available": submission.workspace_manifest.get(
                    "workspace_network_available"
                ),
            }
            if submission.workspace_manifest
            else None
        ),
        "document_coverage": submission.workspace_manifest.get("document_coverage"),
    }
    if score is not None:
        manifest["judge_configuration"] = {
            "strategy": score.judge_diagnostics.get("strategy"),
            "models": score.judge_diagnostics.get("models"),
        }
    write_json_atomic(directory / "run_manifest.json", manifest)
    if score is not None:
        write_json_atomic(directory / "score.json", evaluation_payload(score))
    log.info("[%s] Risultati salvati — %s", task.short_id, directory)
    return directory


def persist_failed_run(
    task: LoadedWorkflowTask,
    failure: WorkspaceRunFailure | BundleRunFailure,
    *,
    results_root: Path = AGENTIC_RESULTS_DIR,
) -> Path:
    """Persist an auditable failure bundle before returning a non-zero exit."""
    directory = create_run_directory(task, failure.model, results_root=results_root)
    directory.mkdir(parents=True, exist_ok=True)

    partial_hashes: dict[str, str] = {}
    partial_root = directory / "partial_artifacts"
    for artifact in failure.artifacts:
        destination = (partial_root / artifact.path).resolve()
        if not destination.is_relative_to(partial_root.resolve()):
            raise ValueError(f"percorso artifact parziale non sicuro: {artifact.path}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if artifact.binary_base64 is not None:
            destination.write_bytes(
                base64.b64decode(artifact.binary_base64, validate=True)
            )
            destination.with_name(destination.name + ".extracted.txt").write_text(
                artifact.content,
                encoding="utf-8",
            )
        else:
            destination.write_text(artifact.content, encoding="utf-8")
        partial_hashes[artifact.path] = _sha256(destination)

    tool_trace_path = write_json_atomic(
        directory / "tool_trace.json",
        {"events": failure.tool_trace},
    )
    agent_transcript = list(getattr(failure, "agent_transcript", []) or [])
    agent_transcript_path = (
        write_json_atomic(
            directory / "agent_transcript.json",
            {"messages": agent_transcript},
        )
        if agent_transcript
        else None
    )
    decision_log_path = write_json_atomic(
        directory / "decision_log.json",
        _decision_log_payload(failure.decision_log),
    )
    workspace_manifest_path = write_json_atomic(
        directory / "workspace_manifest.json",
        failure.workspace_manifest,
    )
    failure_path = write_json_atomic(
        directory / "failure.json",
        {
            "status": "failed",
            "error_type": failure.error_type,
            "message": str(failure),
            "last_model_response": failure.raw_response,
            "model_call_metrics": failure.model_call_metrics,
            "decision_log_entries": len(failure.decision_log),
            "partial_artifacts": [item.path for item in failure.artifacts],
            "created_at": failure.created_at,
        },
    )
    manifest = {
        **_base_run_manifest(
            task,
            model=failure.model,
            source="live",
            execution_mode=getattr(failure, "execution_mode", "agentic_workspace"),
            created_at=failure.created_at,
        ),
        "run_status": "failed",
        "failure_sha256": _sha256(failure_path),
        "partial_artifact_sha256": partial_hashes,
        "tool_trace_sha256": _sha256(tool_trace_path),
        "agent_transcript_sha256": (
            _sha256(agent_transcript_path) if agent_transcript_path else None
        ),
        "decision_log_sha256": _sha256(decision_log_path),
        "decision_log_entries": len(failure.decision_log),
        "workspace_manifest_sha256": _sha256(workspace_manifest_path),
        "workspace_policy": {
            "private_envelope_mounted": failure.workspace_manifest.get(
                "private_envelope_mounted"
            ),
            "shell_available": failure.workspace_manifest.get("shell_available"),
            "workspace_network_available": failure.workspace_manifest.get(
                "workspace_network_available"
            ),
        },
        "document_coverage": failure.workspace_manifest.get("document_coverage"),
    }
    write_json_atomic(directory / "run_manifest.json", manifest)
    log.error(
        "[%s] Run fallita; evidenze diagnostiche salvate — %s",
        task.short_id,
        directory,
    )
    return directory


