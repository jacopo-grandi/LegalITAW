"""Parse, import, validate and serialize workflow submissions."""

from __future__ import annotations

import base64
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree

from legalitaw.artifacts import write_json_atomic

from .models import LoadedWorkflowTask, WorkflowArtifact, WorkflowSubmission
from .native_artifacts import DOCX_MEDIA_TYPE, render_docx


class SubmissionError(ValueError):
    """The model output or imported artifacts violate the task contract."""


SUPPORTED_EXTERNAL_ARTIFACT_SUFFIXES = frozenset({".md", ".txt", ".docx", ".pdf"})
IGNORED_EXTERNAL_FILENAMES = frozenset(
    {
        "decision_log.json",
        "agent_transcript.json",
        "failure.json",
        "run_manifest.json",
        "score.json",
        "submission.json",
        "tool_trace.json",
        "workspace_manifest.json",
    }
)


def _json_object(text: str) -> dict:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    decoder = json.JSONDecoder()
    for start in [0, *(match.start() for match in re.finditer(r"\{", cleaned))]:
        try:
            value, _ = decoder.raw_decode(cleaned[start:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    raise SubmissionError("la risposta non contiene un oggetto JSON valido")


def validate_submission(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
) -> WorkflowSubmission:
    if submission.task_id != task.spec.task_id:
        raise SubmissionError(
            f"submission task_id {submission.task_id!r} != {task.spec.task_id!r}"
        )
    # File names, count and structure are part of the work product. They are
    # scored only when the public assignment asks for them; ingestion must not
    # reject an otherwise readable answer against a hidden runtime profile.
    return submission


def parse_live_submission(
    task: LoadedWorkflowTask,
    *,
    model: str,
    raw_response: str,
    metrics: dict | None = None,
) -> WorkflowSubmission:
    payload = _json_object(raw_response)
    try:
        artifacts: list[WorkflowArtifact] = []
        for item in payload["artifacts"]:
            artifact = WorkflowArtifact.model_validate(item)
            if Path(artifact.path).suffix.casefold() == ".docx":
                has_redline_markers = (
                    "[[DEL:" in artifact.content or "[[INS:" in artifact.content
                )
                with tempfile.TemporaryDirectory(prefix="legalita-one-shot-") as tmp:
                    path = Path(tmp) / Path(artifact.path).name
                    render_docx(
                        artifact.content,
                        path,
                        redline=has_redline_markers,
                        preset=str(
                            getattr(task.spec, "document_preset", None)
                            or (
                                "contract_negotiation_brief"
                                if has_redline_markers
                                else "standard_business_brief"
                            )
                        ),
                        author=task.spec.task_id,
                    )
                    raw = path.read_bytes()
                artifact = WorkflowArtifact(
                    path=artifact.path,
                    content=artifact.content,
                    media_type=DOCX_MEDIA_TYPE,
                    binary_base64=base64.b64encode(raw).decode("ascii"),
                )
            artifacts.append(artifact)
    except (KeyError, TypeError, ValueError) as exc:
        raise SubmissionError(f"protocollo artifacts non valido: {exc}") from exc
    submission = WorkflowSubmission(
        task_id=task.spec.task_id,
        model=model,
        source="live",
        execution_mode="text_bundle",
        artifacts=artifacts,
        raw_response=raw_response,
        model_call_metrics=metrics or {},
    )
    return validate_submission(task, submission)


def _docx_comments(archive: zipfile.ZipFile, namespace: str) -> dict[str, tuple[str, str]]:
    """Map comment id -> (author, text) from word/comments.xml, if present."""
    if "word/comments.xml" not in archive.namelist():
        return {}
    root = ElementTree.fromstring(archive.read("word/comments.xml"))
    comments: dict[str, tuple[str, str]] = {}
    for comment in root.iter(namespace + "comment"):
        comment_id = comment.get(namespace + "id")
        if comment_id is None:
            continue
        author = (comment.get(namespace + "author") or "").strip()
        paragraphs = []
        for paragraph in comment.iter(namespace + "p"):
            text = "".join(node.text or "" for node in paragraph.iter(namespace + "t")).strip()
            if text:
                paragraphs.append(text)
        comments[comment_id] = (author, " ".join(paragraphs))
    return comments


def _docx_text(path: Path) -> str:
    """Extract visible text, tracked changes and comments from a DOCX without SDK coupling.

    Tracked changes are rendered inline as [[AGGIUNTA: ...]] / [[ELIMINAZIONE: ...]]; Word comments as
    [[COMMENTO di <autore>: ...]] at their anchor, so that a judge reading the text sees the notes a
    reviewer would see in Word. Comments without an anchor are listed at the end.
    """
    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(path) as archive:
        document = archive.read("word/document.xml")
        comments = _docx_comments(archive, namespace)
    root = ElementTree.fromstring(document)
    anchored: set[str] = set()

    def comment_marker(comment_id: str | None) -> str:
        if comment_id is None or comment_id not in comments or comment_id in anchored:
            return ""
        anchored.add(comment_id)
        author, text = comments[comment_id]
        label = f"COMMENTO di {author}" if author else "COMMENTO"
        return f" [[{label}: {text}]]"

    def node_text(node: ElementTree.Element) -> str:
        chunks: list[str] = []
        for child in node:
            local = child.tag.rsplit("}", 1)[-1]
            if local == "ins":
                value = "".join(node_text(grandchild) for grandchild in child)
                chunks.append(f"[[AGGIUNTA: {value}]]")
            elif local == "del":
                value = "".join(node_text(grandchild) for grandchild in child)
                chunks.append(f"[[ELIMINAZIONE: {value}]]")
            elif child.tag in {namespace + "t", namespace + "delText"}:
                chunks.append(child.text or "")
            elif local == "tab":
                chunks.append("\t")
            elif local in {"br", "cr"}:
                chunks.append("\n")
            elif local == "commentReference":
                chunks.append(comment_marker(child.get(namespace + "id")))
            else:
                chunks.append(node_text(child))
        return "".join(chunks)

    paragraphs: list[str] = []
    for paragraph in root.iter(namespace + "p"):
        text = node_text(paragraph).strip()
        if text:
            paragraphs.append(text)
    orphans = [cid for cid in comments if cid not in anchored]
    if orphans:
        paragraphs.append("Commenti del documento:")
        paragraphs.extend(comment_marker(cid).strip() for cid in orphans)
    return "\n\n".join(paragraphs)


def _read_artifact(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return _docx_text(path)
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:  # pragma: no cover - release env owns dependency
            raise SubmissionError("la lettura PDF richiede pypdf") from exc
        try:
            pages = [(page.extract_text() or "").strip() for page in PdfReader(path).pages]
        except Exception as exc:
            raise SubmissionError(f"PDF illeggibile: {path}") from exc
        content = "\n\n".join(
            f"[PAGINA {index}]\n{page}"
            for index, page in enumerate(pages, start=1)
            if page
        )
        if not content.strip():
            raise SubmissionError(f"PDF senza testo estraibile: {path}")
        return content
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise SubmissionError(f"formato artifact non testuale non supportato: {path}") from exc


def import_submission(
    task: LoadedWorkflowTask,
    *,
    source: Path,
    model: str,
) -> WorkflowSubmission:
    source = source.resolve()
    if source.is_file() and source.name == "submission.json":
        submission = WorkflowSubmission.model_validate_json(
            source.read_text(encoding="utf-8")
        )
        return validate_submission(task, submission)
    if not source.is_dir():
        raise SubmissionError(
            "--submission deve essere una directory di deliverable o submission.json"
        )

    paths = sorted(
        path
        for path in source.rglob("*")
        if path.is_file()
        and path.name not in IGNORED_EXTERNAL_FILENAMES
        and not path.name.endswith(".extracted.txt")
        and path.suffix.casefold() in SUPPORTED_EXTERNAL_ARTIFACT_SUFFIXES
    )
    if not paths:
        raise SubmissionError(
            "la submission non contiene artifact leggibili "
            f"({', '.join(sorted(SUPPORTED_EXTERNAL_ARTIFACT_SUFFIXES))})"
        )

    artifacts: list[WorkflowArtifact] = []
    for path in paths:
        name = path.relative_to(source).as_posix()
        raw = path.read_bytes()
        suffix = path.suffix.casefold()
        binary = suffix in {".docx", ".pdf"}
        media_type = {
            ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ".pdf": "application/pdf",
            ".txt": "text/plain",
        }.get(suffix, "text/markdown")
        artifacts.append(
            WorkflowArtifact(
                path=name,
                content=_read_artifact(path),
                media_type=media_type,
                binary_base64=(
                    base64.b64encode(raw).decode("ascii")
                    if binary
                    else None
                ),
                sha256=hashlib.sha256(raw).hexdigest(),
            )
        )
    submission = WorkflowSubmission(
        task_id=task.spec.task_id,
        model=model,
        source="external",
        execution_mode="external_system",
        artifacts=artifacts,
    )
    return validate_submission(task, submission)


def submission_text(submission: WorkflowSubmission) -> str:
    return "\n\n".join(
        f"## DELIVERABLE: {artifact.path}\n\n{artifact.content.strip()}"
        for artifact in submission.artifacts
    )


def save_submission(submission: WorkflowSubmission, directory: Path) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    for artifact in submission.artifacts:
        path = directory / artifact.path
        path.parent.mkdir(parents=True, exist_ok=True)
        if artifact.binary_base64 is not None:
            path.write_bytes(base64.b64decode(artifact.binary_base64, validate=True))
            extracted = path.with_name(path.name + ".extracted.txt")
            extracted.write_text(artifact.content, encoding="utf-8")
        else:
            path.write_text(artifact.content, encoding="utf-8")
    return write_json_atomic(
        directory / "submission.json",
        submission.model_dump(),
    )
