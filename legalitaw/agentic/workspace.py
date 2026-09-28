"""Tool-mediated, public-only workspace for agentic workflow runs."""

from __future__ import annotations

import base64
import hashlib
from importlib.metadata import PackageNotFoundError, version
import json
import logging
import math
import mimetypes
import posixpath
import re
import shutil
import tempfile
import time
import zipfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from legalitaw.modeling.gateway import ModelGateway, default_gateway

from .native_artifacts import DOCX_MEDIA_TYPE, docx_features, render_docx
from .models import (
    DecisionLogEntry,
    LoadedWorkflowTask,
    WorkflowArtifact,
    WorkflowSubmission,
    safe_relative_path,
)


log = logging.getLogger(__name__)


IMPLEMENTED_WORKSPACE_TOOLS = frozenset(
    {
        "list_files",
        "search_documents",
        "open_document",
        "inspect_metadata",
        "record_decision",
        "write_artifact",
        "submit",
    }
)
MODEL_WORKSPACE_TOOLS = IMPLEMENTED_WORKSPACE_TOOLS - {"record_decision"}
SUPPORTED_DOCUMENT_SUFFIXES = frozenset(
    {".pdf", ".docx", ".xlsx", ".md", ".txt", ".eml", ".csv", ".json"}
)
SUPPORTED_ARTIFACT_SUFFIXES = frozenset({".md", ".txt", ".docx"})
MODEL_HIDDEN_PUBLIC_INPUTS = frozenset({"public/response_template.md"})


class WorkspaceError(RuntimeError):
    """The isolated matter workspace or its tool protocol failed."""


class WorkspaceRunFailure(WorkspaceError):
    """A failed run together with the evidence needed to audit it."""

    def __init__(
        self,
        message: str,
        *,
        task_id: str,
        model: str,
        error_type: str,
        artifacts: list[WorkflowArtifact],
        tool_trace: list[dict[str, Any]],
        decision_log: list[DecisionLogEntry],
        workspace_manifest: dict[str, Any],
        model_call_metrics: dict[str, Any],
        raw_response: str | None,
        agent_transcript: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.task_id = task_id
        self.model = model
        self.error_type = error_type
        self.artifacts = artifacts
        self.tool_trace = tool_trace
        self.decision_log = decision_log
        self.workspace_manifest = workspace_manifest
        self.model_call_metrics = model_call_metrics
        self.raw_response = raw_response
        self.agent_transcript = list(agent_transcript or [])
        self.created_at = datetime.now(timezone.utc).isoformat()


def public_envelope_paths(task: LoadedWorkflowTask) -> list[str]:
    """Return model-visible inputs, excluding authoring-only benchmark aids."""
    paths = [
        path
        for path in task.spec.public_inputs
        if path not in MODEL_HIDDEN_PUBLIC_INPUTS
    ]
    task_path = task.directory / "public/01_task.md"
    task_text = task_path.read_text(encoding="utf-8")
    public_root = task.directory / "public"
    for candidate in sorted(public_root.iterdir()):
        if not candidate.is_file() or candidate.name == "01_task.md":
            continue
        relative = f"public/{candidate.name}"
        if relative in MODEL_HIDDEN_PUBLIC_INPUTS:
            continue
        if candidate.name in task_text and relative not in paths:
            paths.append(relative)
    # l'elenco chiuso delle fonti fa parte della consegna anche quando il prompt non ne scrive il nome
    # (17 task lo avevano in public/ senza che arrivasse al modello)
    sources = "public/03_legal_sources.md"
    if (task.directory / sources).is_file() and sources not in paths and sources not in MODEL_HIDDEN_PUBLIC_INPUTS:
        paths.append(sources)
    return paths


def required_workspace_tools(task: LoadedWorkflowTask) -> set[str]:
    """Derive the model-facing tools needed by this task's declared contract."""
    required = {"write_artifact", "submit"}
    documents = [
        relative
        for relative in public_envelope_paths(task)
        if relative not in {"public/01_task.md", "public/02_reference_pack.md"}
    ]
    if documents:
        required.update({"list_files", "open_document"})
    if len(documents) > 1:
        required.add("search_documents")
    if any(
        Path(relative).suffix.casefold() not in {".md", ".txt"}
        for relative in documents
    ):
        required.add("inspect_metadata")
    return required


def model_workspace_tools(task: LoadedWorkflowTask) -> set[str]:
    """Return the neutral tool surface exposed to the evaluated model."""

    return set(task.spec.tool_allowlist) & set(MODEL_WORKSPACE_TOOLS)


def validate_runtime_capabilities(
    task: LoadedWorkflowTask,
    *,
    execution_mode: str,
) -> dict[str, Any]:
    """Fail before API work if a task needs a reader, writer or tool we lack."""
    input_suffixes = {Path(item).suffix.casefold() for item in public_envelope_paths(task)}
    unsupported_inputs = sorted(input_suffixes - SUPPORTED_DOCUMENT_SUFFIXES)
    if execution_mode != "generic_agent" and unsupported_inputs:
        raise WorkspaceError(
            f"{task.spec.task_id}: reader mancanti per {unsupported_inputs}"
        )

    required_tools: set[str] = set()
    missing_tools: set[str] = set()
    if execution_mode == "agentic_workspace":
        required_tools = required_workspace_tools(task)
        unknown_tools = set(task.spec.tool_allowlist) - IMPLEMENTED_WORKSPACE_TOOLS
        if unknown_tools:
            raise WorkspaceError(
                f"{task.spec.task_id}: tool dichiarati ma non implementati: "
                + ", ".join(sorted(unknown_tools))
            )
        missing_tools = required_tools - set(task.spec.tool_allowlist)
        if missing_tools:
            raise WorkspaceError(
                f"{task.spec.task_id}: tool necessari non autorizzati: "
                + ", ".join(sorted(missing_tools))
            )
    elif execution_mode not in {"text_bundle", "generic_agent"}:
        raise WorkspaceError(f"modalità di esecuzione non supportata: {execution_mode}")

    return {
        "task_id": task.spec.task_id,
        "execution_mode": execution_mode,
        "input_readers": sorted(input_suffixes),
        "artifact_writers": sorted(SUPPORTED_ARTIFACT_SUFFIXES),
        "required_tools": sorted(required_tools),
        "missing_tools": sorted(missing_tools),
        "native_artifact_mode": str(
            getattr(task.spec, "native_artifact_mode", None) or "markdown"
        ),
    }


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json_object(text: str) -> dict[str, Any]:
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
    raise WorkspaceError("la risposta del modello non contiene un tool call JSON")


_XLSX_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_XLSX_REL_NS = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
)
_PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
_BUILTIN_DATE_FORMATS = {*range(14, 23), *range(27, 37), *range(45, 48), *range(50, 59)}


def _xlsx_xml(archive: zipfile.ZipFile, member: str) -> ElementTree.Element:
    try:
        return ElementTree.fromstring(archive.read(member))
    except KeyError as exc:
        raise WorkspaceError(f"XLSX senza componente obbligatorio: {member}") from exc
    except ElementTree.ParseError as exc:
        raise WorkspaceError(f"XML non valido nel componente XLSX {member}: {exc}") from exc


def _xlsx_shared_strings(archive: zipfile.ZipFile) -> list[str]:
    try:
        root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    except ElementTree.ParseError as exc:
        raise WorkspaceError(f"sharedStrings.xml non valido: {exc}") from exc
    return [
        "".join(node.text or "" for node in item.iter(f"{{{_XLSX_NS}}}t"))
        for item in root.findall(f"{{{_XLSX_NS}}}si")
    ]


def _xlsx_date_styles(archive: zipfile.ZipFile) -> set[int]:
    try:
        root = ElementTree.fromstring(archive.read("xl/styles.xml"))
    except KeyError:
        return set()
    except ElementTree.ParseError as exc:
        raise WorkspaceError(f"styles.xml non valido: {exc}") from exc

    custom_formats = {
        int(node.attrib["numFmtId"]): node.attrib.get("formatCode", "")
        for node in root.findall(
            f"{{{_XLSX_NS}}}numFmts/{{{_XLSX_NS}}}numFmt"
        )
        if node.attrib.get("numFmtId", "").isdigit()
    }
    date_format_ids = set(_BUILTIN_DATE_FORMATS)
    for format_id, code in custom_formats.items():
        normalized = re.sub(r'"[^"]*"|\\.|\[[^]]*\]', "", code).casefold()
        if any(marker in normalized for marker in ("yy", "dd", "mm/", "/mm", "hh:")):
            date_format_ids.add(format_id)

    cell_xfs = root.find(f"{{{_XLSX_NS}}}cellXfs")
    if cell_xfs is None:
        return set()
    return {
        index
        for index, node in enumerate(cell_xfs.findall(f"{{{_XLSX_NS}}}xf"))
        if int(node.attrib.get("numFmtId", "0")) in date_format_ids
    }


def _xlsx_scalar(
    cell: ElementTree.Element,
    *,
    shared_strings: list[str],
    date_styles: set[int],
    date_1904: bool,
) -> str:
    cell_type = cell.attrib.get("t")
    value_node = cell.find(f"{{{_XLSX_NS}}}v")
    raw = value_node.text if value_node is not None and value_node.text is not None else ""
    if cell_type == "inlineStr":
        return "".join(
            node.text or "" for node in cell.iter(f"{{{_XLSX_NS}}}t")
        )
    if cell_type == "s":
        try:
            return shared_strings[int(raw)]
        except (ValueError, IndexError):
            return f"[shared-string non risolta: {raw}]"
    if cell_type == "b":
        return "TRUE" if raw == "1" else "FALSE"
    if cell_type == "e":
        return f"[errore Excel: {raw}]"
    if cell_type in {"str", "d"}:
        return raw

    style = cell.attrib.get("s")
    if style is not None and style.isdigit() and int(style) in date_styles and raw:
        try:
            epoch = datetime(1904, 1, 1) if date_1904 else datetime(1899, 12, 30)
            parsed = epoch + timedelta(days=float(raw))
            if parsed.time() == datetime.min.time():
                return parsed.date().isoformat()
            return parsed.isoformat(sep=" ", timespec="seconds")
        except ValueError:
            pass
    return raw


def _chunk_text_lines(lines: list[str], *, target_chars: int) -> list[str]:
    pages: list[str] = []
    current: list[str] = []
    current_chars = 0
    for line in lines:
        added = len(line) + (1 if current else 0)
        if current and current_chars + added > target_chars:
            pages.append("\n".join(current))
            current = []
            current_chars = 0
        current.append(line)
        current_chars += len(line) + (1 if current_chars else 0)
    if current:
        pages.append("\n".join(current))
    return pages or [""]


def _xlsx_pages(path: Path, *, target_chars: int = 8000) -> list[str]:
    """Extract XLSX cells without macros, external links or formula evaluation."""
    try:
        with zipfile.ZipFile(path) as archive:
            workbook = _xlsx_xml(archive, "xl/workbook.xml")
            relationships = _xlsx_xml(archive, "xl/_rels/workbook.xml.rels")
            targets = {
                node.attrib["Id"]: node.attrib.get("Target", "")
                for node in relationships.findall(f"{{{_PACKAGE_REL_NS}}}Relationship")
                if node.attrib.get("TargetMode") != "External"
            }
            shared_strings = _xlsx_shared_strings(archive)
            date_styles = _xlsx_date_styles(archive)
            workbook_properties = workbook.find(f"{{{_XLSX_NS}}}workbookPr")
            date_1904 = (
                workbook_properties is not None
                and workbook_properties.attrib.get("date1904", "").casefold()
                in {"1", "true"}
            )

            pages: list[str] = []
            sheets = workbook.find(f"{{{_XLSX_NS}}}sheets")
            if sheets is None:
                raise WorkspaceError(f"XLSX senza fogli: {path.name}")
            for sheet in sheets.findall(f"{{{_XLSX_NS}}}sheet"):
                relation_id = sheet.attrib.get(f"{{{_XLSX_REL_NS}}}id", "")
                target = targets.get(relation_id, "")
                if not target:
                    raise WorkspaceError(
                        f"relazione del foglio XLSX non risolta: {sheet.attrib.get('name')}"
                    )
                member = (
                    target.lstrip("/")
                    if target.startswith("/")
                    else posixpath.normpath(posixpath.join("xl", target))
                )
                worksheet = _xlsx_xml(archive, member)
                lines = [f"[FOGLIO {sheet.attrib.get('name', relation_id)}]"]
                for row in worksheet.findall(
                    f".//{{{_XLSX_NS}}}sheetData/{{{_XLSX_NS}}}row"
                ):
                    values: list[str] = []
                    for cell in row.findall(f"{{{_XLSX_NS}}}c"):
                        reference = cell.attrib.get("r", "?")
                        scalar = _xlsx_scalar(
                            cell,
                            shared_strings=shared_strings,
                            date_styles=date_styles,
                            date_1904=date_1904,
                        )
                        formula = cell.find(f"{{{_XLSX_NS}}}f")
                        if formula is not None and formula.text:
                            values.append(
                                f"{reference}=={formula.text} -> {scalar or '[vuoto]'}"
                            )
                        elif scalar:
                            values.append(f"{reference}={scalar}")
                    if values:
                        lines.append(" | ".join(values))
                pages.extend(_chunk_text_lines(lines, target_chars=target_chars))
            return pages or [""]
    except zipfile.BadZipFile as exc:
        raise WorkspaceError(f"XLSX illeggibile {path.name}: {exc}") from exc


class MatterWorkspace:
    """A copied public envelope reachable only through an explicit tool broker."""

    def __init__(self, task: LoadedWorkflowTask) -> None:
        self.task = task
        self.root = Path(tempfile.mkdtemp(prefix=f"legalita-{task.short_id}-"))
        self.matter = self.root / "matter"
        self.work = self.root / "work"
        self.matter.mkdir(mode=0o700)
        self.work.mkdir(mode=0o700)
        self.trace: list[dict[str, Any]] = []
        self.decision_log: list[DecisionLogEntry] = []
        self._text_cache: dict[str, list[str]] = {}
        self._page_counts: dict[str, int] = {}
        self._opened_pages: dict[str, set[int]] = defaultdict(set)
        self._completed_pages: dict[str, set[int]] = defaultdict(set)
        self._searched_pages: dict[str, set[int]] = defaultdict(set)
        self._artifact_sources: dict[str, str] = {}
        self._submitted: str | None = None
        self._submitted_paths: list[str] = []
        self._artifact_revision = 0
        self._copy_public_envelope()
        self._observed_documents = (
            {"public/01_task.md"}
            if (self.matter / "public/01_task.md").is_file()
            else set()
        )
        self.manifest = self._build_manifest()

    def close(self) -> None:
        if not self.root.exists():
            return
        for path in self.root.rglob("*"):
            try:
                path.chmod(0o700 if path.is_dir() else 0o600)
            except OSError:
                pass
        self.root.chmod(0o700)
        shutil.rmtree(self.root)

    def _copy_public_envelope(self) -> None:
        for relative in public_envelope_paths(self.task):
            if not relative.startswith("public/"):
                raise WorkspaceError(f"input fuori dalla busta pubblica: {relative}")
            source = (self.task.directory / relative).resolve()
            public_root = (self.task.directory / "public").resolve()
            if not source.is_relative_to(public_root) or not source.is_file():
                raise WorkspaceError(f"input pubblico non valido: {relative}")
            destination = self.matter / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            destination.chmod(0o400)
        for directory in sorted(
            (path for path in self.matter.rglob("*") if path.is_dir()),
            reverse=True,
        ):
            directory.chmod(0o500)
        self.matter.chmod(0o500)

    def _build_manifest(self) -> dict[str, Any]:
        try:
            pypdf_version = version("pypdf")
        except PackageNotFoundError:
            pypdf_version = None
        inputs = {
            path.relative_to(self.matter).as_posix(): {
                "sha256": _sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in sorted(self.matter.rglob("*"))
            if path.is_file()
        }
        return {
            "workspace_contract": "public_only_prompt_and_documents_v1",
            "task_id": self.task.spec.task_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "matter_mode": "read_only_copy",
            "work_mode": "write_only_through_allowlisted_tools",
            "private_envelope_mounted": False,
            "shell_available": False,
            "workspace_network_available": False,
            "tool_allowlist": list(self.task.spec.tool_allowlist),
            "document_readers": {
                "pdf": {"package": "pypdf", "version": pypdf_version},
                "docx": {"package": "python-docx"},
                "xlsx": {
                    "package": "python-standard-library",
                    "mode": "static_ooxml_extraction",
                    "formula_evaluation": False,
                    "macros_executed": False,
                    "external_links_followed": False,
                },
            },
            "public_inputs": inputs,
            "submission_policy": "free_artifacts",
            "supported_artifact_suffixes": sorted(SUPPORTED_ARTIFACT_SUFFIXES),
            "decision_log_contract": {
                "schema_version": "decision_log_v1",
                "provenance": "model_authored_structured_summary",
                "contains_hidden_chain_of_thought": False,
                "required_before_first_write": False,
                "required_after_last_write": False,
            },
        }

    def _safe_matter_path(self, relative: str) -> Path:
        path = (self.matter / relative).resolve()
        if not path.is_relative_to(self.matter.resolve()) or not path.is_file():
            raise WorkspaceError(f"file del matter non accessibile: {relative!r}")
        return path

    def _safe_output_path(self, relative: str) -> Path:
        try:
            normalized = safe_relative_path(relative, label="artifact path")
        except ValueError as exc:
            raise WorkspaceError(str(exc)) from exc
        suffix = Path(normalized).suffix.casefold()
        if suffix not in SUPPORTED_ARTIFACT_SUFFIXES:
            raise WorkspaceError(
                f"formato artifact non supportato: {suffix or '[senza estensione]'}"
            )
        path = (self.work / normalized).resolve()
        if not path.is_relative_to(self.work.resolve()):
            raise WorkspaceError(f"percorso artifact non sicuro: {relative!r}")
        return path

    def _pdf_pages(self, path: Path) -> list[str]:
        try:
            from pypdf import PdfReader
        except ImportError as exc:  # pragma: no cover - release env owns dependency
            raise WorkspaceError(
                "la lettura PDF richiede pypdf; installare le dipendenze del progetto"
            ) from exc
        try:
            reader = PdfReader(path)
            return [(page.extract_text() or "").strip() for page in reader.pages]
        except Exception as exc:
            raise WorkspaceError(f"PDF illeggibile {path.name}: {exc}") from exc

    def _docx_pages(self, path: Path, *, target_chars: int = 8000) -> list[str]:
        try:
            from docx import Document
            from docx.table import Table
        except ImportError as exc:  # pragma: no cover
            raise WorkspaceError("la lettura DOCX richiede python-docx") from exc
        document = Document(path)
        blocks: list[str] = []
        for item in document.iter_inner_content():
            if isinstance(item, Table):
                rows = [
                    " | ".join(cell.text.strip() for cell in row.cells)
                    for row in item.rows
                ]
                value = "\n".join(row for row in rows if row.strip())
            else:
                value = item.text.strip()
            if value:
                blocks.append(value)

        pages: list[str] = []
        current: list[str] = []
        current_chars = 0
        for block in blocks:
            added = len(block) + (1 if current else 0)
            if current and current_chars + added > target_chars:
                pages.append("\n".join(current))
                current = []
                current_chars = 0
            if len(block) <= target_chars:
                current.append(block)
                current_chars += len(block) + (1 if current_chars else 0)
                continue
            for start in range(0, len(block), target_chars):
                if current:
                    pages.append("\n".join(current))
                    current = []
                    current_chars = 0
                pages.append(block[start : start + target_chars])
        if current:
            pages.append("\n".join(current))
        return pages or [""]

    def _pages(self, relative: str) -> list[str]:
        if relative in self._text_cache:
            return self._text_cache[relative]
        path = self._safe_matter_path(relative)
        suffix = path.suffix.casefold()
        if suffix == ".pdf":
            pages = self._pdf_pages(path)
        elif suffix == ".docx":
            pages = self._docx_pages(path)
        elif suffix == ".xlsx":
            pages = _xlsx_pages(path)
        elif suffix in {".md", ".txt", ".eml", ".csv", ".json"}:
            pages = [path.read_text(encoding="utf-8", errors="replace")]
        else:
            raise WorkspaceError(f"formato non supportato dal reader: {suffix}")
        self._text_cache[relative] = pages
        self._page_counts[relative] = len(pages)
        return pages

    def document_pages(self, relative: str) -> list[str]:
        """Return normalized text pages for one declared public input."""
        return list(self._pages(relative))

    def _tool_list_files(self, arguments: dict[str, Any]) -> dict[str, Any]:
        files = []
        for path in sorted(self.matter.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(self.matter).as_posix()
            media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            files.append(
                {
                    "path": relative,
                    "bytes": path.stat().st_size,
                    "media_type": media_type,
                    "sha256": _sha256_file(path),
                }
            )
        return {"files": files, "count": len(files)}

    def _tool_search_documents(self, arguments: dict[str, Any]) -> dict[str, Any]:
        query = str(arguments.get("query") or "").strip()
        if len(query) < 2:
            raise WorkspaceError("search_documents richiede query di almeno 2 caratteri")
        limit = min(max(int(arguments.get("limit", 20)), 1), 50)
        needle = query.casefold()
        hits: list[dict[str, Any]] = []
        for path in sorted(self.matter.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(self.matter).as_posix()
            try:
                pages = self._pages(relative)
            except WorkspaceError:
                continue
            for page_number, page in enumerate(pages, start=1):
                folded = page.casefold()
                start = folded.find(needle)
                if start < 0:
                    continue
                left = max(0, start - 240)
                right = min(len(page), start + len(query) + 360)
                hits.append(
                    {
                        "path": relative,
                        "page": page_number,
                        "snippet": page[left:right].strip(),
                    }
                )
                self._observed_documents.add(relative)
                self._searched_pages[relative].add(page_number)
                if len(hits) >= limit:
                    return {"query": query, "hits": hits, "truncated": True}
        return {"query": query, "hits": hits, "truncated": False}

    def _tool_open_document(self, arguments: dict[str, Any]) -> dict[str, Any]:
        relative = str(arguments.get("path") or "")
        pages = self._pages(relative)
        requested = arguments.get("page")
        max_chars = min(max(int(arguments.get("max_chars", 10000)), 500), 20000)
        if requested is not None:
            page_number = int(requested)
            if page_number < 1 or page_number > len(pages):
                raise WorkspaceError(
                    f"pagina fuori intervallo: {page_number}; pagine={len(pages)}"
                )
            text = pages[page_number - 1]
            selected: int | str = page_number
            content = text[:max_chars]
            opened_pages = {page_number}
            completed_pages = {page_number} if len(text) <= max_chars else set()
        else:
            blocks = [
                f"[PAGINA {index}]\n{page}"
                for index, page in enumerate(pages, start=1)
            ]
            spans: list[tuple[int, int, int]] = []
            cursor = 0
            for page_number, block in enumerate(blocks, start=1):
                if page_number > 1:
                    cursor += 2
                start = cursor
                cursor += len(block)
                spans.append((page_number, start, cursor))
            text = "\n\n".join(blocks)
            selected = "all"
            content = text[:max_chars]
            opened_pages = {
                page_number
                for page_number, start, _ in spans
                if start < len(content)
            }
            completed_pages = {
                page_number
                for page_number, _, end in spans
                if end <= len(content)
            }
        self._observed_documents.add(relative)
        self._opened_pages[relative].update(opened_pages)
        self._completed_pages[relative].update(completed_pages)
        return {
            "path": relative,
            "page": selected,
            "page_count": len(pages),
            "opened_pages": sorted(opened_pages),
            "fully_read_pages": sorted(completed_pages),
            "content": content,
            "truncated": len(text) > max_chars,
        }

    def _tool_inspect_metadata(self, arguments: dict[str, Any]) -> dict[str, Any]:
        relative = str(arguments.get("path") or "")
        path = self._safe_matter_path(relative)
        result: dict[str, Any] = {
            "path": relative,
            "bytes": path.stat().st_size,
            "sha256": _sha256_file(path),
            "suffix": path.suffix.casefold(),
            "media_type": mimetypes.guess_type(path.name)[0]
            or "application/octet-stream",
        }
        if path.suffix.casefold() in {
            ".pdf",
            ".docx",
            ".xlsx",
            ".md",
            ".txt",
            ".eml",
        }:
            result["page_count"] = len(self._pages(relative))
        return result

    def _tool_record_decision(self, arguments: dict[str, Any]) -> dict[str, Any]:
        reserved = {
            "schema_version",
            "sequence",
            "timestamp",
            "tool_sequence",
            "artifact_revision",
        }
        supplied_reserved = reserved.intersection(arguments)
        if supplied_reserved:
            raise WorkspaceError(
                "record_decision non accetta campi runtime: "
                + ", ".join(sorted(supplied_reserved))
            )
        try:
            entry = DecisionLogEntry.model_validate(
                {
                    **arguments,
                    "schema_version": "decision_log_v1",
                    "sequence": len(self.decision_log) + 1,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "tool_sequence": len(self.trace) + 1,
                    "artifact_revision": self._artifact_revision,
                }
            )
        except ValueError as exc:
            raise WorkspaceError(f"record_decision non valido: {exc}") from exc

        evidence_paths = {item.document for item in entry.evidence}
        for relative in sorted(evidence_paths):
            self._safe_matter_path(relative)
        unseen_evidence = evidence_paths - self._observed_documents
        if unseen_evidence:
            raise WorkspaceError(
                "record_decision cita documenti non ancora osservati: "
                + ", ".join(sorted(unseen_evidence))
            )
        for relative in entry.documents_not_reviewed:
            self._safe_matter_path(relative)
        already_reviewed = set(entry.documents_not_reviewed) & self._observed_documents
        if already_reviewed:
            raise WorkspaceError(
                "documents_not_reviewed contiene documenti già osservati: "
                + ", ".join(sorted(already_reviewed))
            )
        if entry.stage == "final_check" and self._artifact_revision == 0:
            raise WorkspaceError("final_check richiede un artifact già scritto")

        self.decision_log.append(entry)
        serialized = json.dumps(
            entry.model_dump(),
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
        return {
            "recorded": entry.sequence,
            "stage": entry.stage,
            "artifact_revision": entry.artifact_revision,
            "sha256": _sha256_bytes(serialized),
        }

    def _tool_write_artifact(self, arguments: dict[str, Any]) -> dict[str, Any]:
        relative = str(arguments.get("path") or "")
        content = str(arguments.get("content") or "")
        if not content.strip():
            raise WorkspaceError("write_artifact rifiuta contenuto vuoto")
        path = self._safe_output_path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        suffix = path.suffix.casefold()
        native_features: dict[str, Any] | None = None
        if suffix == ".md":
            path.write_text(content, encoding="utf-8")
        elif suffix == ".docx":
            has_redline_markers = "[[DEL:" in content or "[[INS:" in content
            try:
                render_docx(
                    content,
                    path,
                    redline=has_redline_markers,
                    preset=str(
                        getattr(self.task.spec, "document_preset", None)
                        or (
                            "contract_negotiation_brief"
                            if has_redline_markers
                            else "standard_business_brief"
                        )
                    ),
                    author=self.task.spec.task_id,
                )
                native_features = docx_features(path)
            except (OSError, ValueError, zipfile.BadZipFile) as exc:
                raise WorkspaceError(f"DOCX non generabile: {exc}") from exc
        else:
            raise WorkspaceError(f"formato artifact non supportato: {suffix}")
        self._artifact_sources[relative] = content
        self._artifact_revision += 1
        result = {
            "path": relative,
            "bytes": path.stat().st_size,
            "sha256": _sha256_file(path),
            "artifact_revision": self._artifact_revision,
        }
        if native_features is not None:
            result["native_features"] = native_features
        return result

    def _tool_submit(self, arguments: dict[str, Any]) -> dict[str, Any]:
        raw_paths = arguments.get("paths")
        if raw_paths is not None:
            if not isinstance(raw_paths, list) or not raw_paths:
                raise WorkspaceError("submit.paths deve essere una lista non vuota")
            relatives = [str(item) for item in raw_paths]
        else:
            relative = str(arguments.get("path") or "")
            relatives = [relative] if relative else []
        if len(set(relatives)) != len(relatives):
            raise WorkspaceError("submit contiene artifact duplicati")
        if not relatives:
            raise WorkspaceError("submit richiede almeno un artifact")
        paths = [self._safe_output_path(relative) for relative in relatives]
        for relative, path in zip(relatives, paths, strict=True):
            source = self._artifact_sources.get(relative, "")
            if not path.is_file() or not source.strip():
                raise WorkspaceError(f"artifact non scritto o vuoto: {relative}")
        self._submitted_paths = relatives
        self._submitted = relatives[0]
        return {
            "submitted": relatives[0] if len(relatives) == 1 else relatives,
            "sha256": (
                _sha256_file(paths[0])
                if len(relatives) == 1
                else {
                    relative: _sha256_file(path)
                    for relative, path in zip(relatives, paths, strict=True)
                }
            ),
        }

    def execute(
        self,
        tool: str,
        arguments: dict[str, Any],
        *,
        allowed_tools: set[str] | None = None,
    ) -> dict[str, Any]:
        handlers = {
            "list_files": self._tool_list_files,
            "search_documents": self._tool_search_documents,
            "open_document": self._tool_open_document,
            "inspect_metadata": self._tool_inspect_metadata,
            "record_decision": self._tool_record_decision,
            "write_artifact": self._tool_write_artifact,
            "submit": self._tool_submit,
        }
        started = time.perf_counter()
        sanitized_arguments = dict(arguments)
        if tool == "record_decision":
            serialized_decision = json.dumps(
                arguments,
                ensure_ascii=False,
                sort_keys=True,
            ).encode("utf-8")
            sanitized_arguments = {
                "stage": arguments.get("stage"),
                "confidence": arguments.get("confidence"),
                "objective_chars": len(str(arguments.get("objective") or "")),
                "evidence_count": len(arguments.get("evidence") or []),
                "documents_not_reviewed_count": len(
                    arguments.get("documents_not_reviewed") or []
                ),
                "alternatives_count": len(
                    arguments.get("alternatives_considered") or []
                ),
                "missing_information_count": len(
                    arguments.get("missing_information") or []
                ),
                "checks_performed_count": len(
                    arguments.get("checks_performed") or []
                ),
                "decision_payload_sha256": _sha256_bytes(serialized_decision),
            }
        elif "content" in sanitized_arguments:
            content = str(sanitized_arguments.pop("content"))
            sanitized_arguments["content_chars"] = len(content)
            sanitized_arguments["content_sha256"] = _sha256_bytes(content.encode())
        event: dict[str, Any] = {
            "sequence": len(self.trace) + 1,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tool": tool,
            "arguments": sanitized_arguments,
            "arguments_sha256": _sha256_bytes(
                json.dumps(arguments, ensure_ascii=False, sort_keys=True).encode()
            ),
        }
        try:
            if tool not in self.task.spec.tool_allowlist:
                raise WorkspaceError(f"tool non autorizzato per il task: {tool}")
            if allowed_tools is not None and tool not in allowed_tools:
                raise WorkspaceError(
                    f"tool {tool!r} non ammesso nella fase corrente; "
                    f"consentiti={sorted(allowed_tools)}"
                )
            if tool not in handlers:
                raise WorkspaceError(f"tool non implementato: {tool}")
            result = handlers[tool](arguments)
            serialized = json.dumps(result, ensure_ascii=False, sort_keys=True)
            event.update(
                {
                    "status": "ok",
                    "result_sha256": _sha256_bytes(serialized.encode()),
                    "result_chars": len(serialized),
                }
            )
            return result
        except Exception as exc:
            event.update({"status": "error", "error": str(exc)})
            raise
        finally:
            event["latency_ms"] = int(round((time.perf_counter() - started) * 1000))
            self.trace.append(event)

    def document_coverage(self) -> dict[str, Any]:
        """Return runtime-authored source coverage, independent of model claims."""
        prompt_embedded = {"public/01_task.md"}
        sources = sorted(
            relative
            for relative in public_envelope_paths(self.task)
            if relative not in prompt_embedded
        )
        opened_sources = {
            relative for relative in sources if self._opened_pages.get(relative)
        }
        searched_sources = {
            relative for relative in sources if self._searched_pages.get(relative)
        }
        observed_sources = opened_sources | searched_sources
        unopened_sources = sorted(set(sources) - opened_sources)
        unseen_sources = sorted(set(sources) - observed_sources)
        search_only_sources = sorted(searched_sources - opened_sources)

        by_source: list[dict[str, Any]] = []
        known_page_total = 0
        opened_page_total = 0
        completed_page_total = 0
        for relative in sources:
            page_count = self._page_counts.get(relative)
            opened_pages = sorted(self._opened_pages.get(relative, set()))
            completed_pages = sorted(self._completed_pages.get(relative, set()))
            searched_pages = sorted(self._searched_pages.get(relative, set()))
            if page_count is not None:
                known_page_total += page_count
                opened_page_total += len(opened_pages)
                completed_page_total += len(completed_pages)
            by_source.append(
                {
                    "path": relative,
                    "page_count": page_count,
                    "opened_pages": opened_pages,
                    "fully_read_pages": completed_pages,
                    "searched_pages": searched_pages,
                    "opened": bool(opened_pages),
                    "observed_via_search": bool(searched_pages),
                }
            )

        final_check = next(
            (
                item
                for item in reversed(self.decision_log)
                if item.stage == "final_check"
            ),
            None,
        )
        declared_unreviewed = (
            sorted(
                set(final_check.documents_not_reviewed).intersection(sources)
            )
            if final_check is not None
            else None
        )
        declaration_matches_runtime = (
            declared_unreviewed == unopened_sources
            if declared_unreviewed is not None
            else None
        )
        reader_errors = [
            {
                "sequence": event["sequence"],
                "tool": event["tool"],
                "path": event.get("arguments", {}).get("path"),
                "error": event.get("error"),
            }
            for event in self.trace
            if event.get("status") == "error"
            and event.get("tool")
            in {"search_documents", "open_document", "inspect_metadata"}
        ]
        source_count = len(sources)
        return {
            "schema_version": "document_coverage_v1",
            "policy": str(
                getattr(self.task.spec, "document_coverage_policy", None)
                or "observe_only"
            ),
            "scope": (
                "all_public_inputs_except_prompt_embedded_task"
            ),
            "source_count": source_count,
            "opened_source_count": len(opened_sources),
            "observed_source_count": len(observed_sources),
            "document_open_rate": (
                len(opened_sources) / source_count if source_count else 1.0
            ),
            "all_sources_opened": not unopened_sources,
            "unopened_sources": unopened_sources,
            "unseen_sources": unseen_sources,
            "search_only_sources": search_only_sources,
            "known_page_count": known_page_total,
            "opened_known_page_count": opened_page_total,
            "fully_read_known_page_count": completed_page_total,
            "known_page_open_rate": (
                opened_page_total / known_page_total
                if known_page_total
                else None
            ),
            "known_page_full_read_rate": (
                completed_page_total / known_page_total
                if known_page_total
                else None
            ),
            "declared_unreviewed_sources": declared_unreviewed,
            "declaration_matches_runtime": declaration_matches_runtime,
            "undeclared_unopened_sources": (
                sorted(set(unopened_sources) - set(declared_unreviewed or []))
                if declared_unreviewed is not None
                else None
            ),
            "reader_errors": reader_errors,
            "by_source": by_source,
        }

    @property
    def submitted_path(self) -> str | None:
        return self._submitted

    @property
    def has_prewrite_decision(self) -> bool:
        return any(
            item.stage in {"analysis", "decision"} for item in self.decision_log
        )

    @property
    def has_current_final_check(self) -> bool:
        return any(
            item.stage == "final_check"
            and item.artifact_revision == self._artifact_revision
            for item in self.decision_log
        )


    def submitted_artifacts(self) -> list[WorkflowArtifact]:
        artifacts: list[WorkflowArtifact] = []
        for relative in self._submitted_paths:
            path = self._safe_output_path(relative)
            content = self._artifact_sources.get(relative, "")
            binary = path.read_bytes() if path.suffix.casefold() == ".docx" else None
            artifacts.append(
                WorkflowArtifact(
                    path=relative,
                    content=content,
                    media_type=(
                        DOCX_MEDIA_TYPE if binary is not None else "text/markdown"
                    ),
                    binary_base64=(
                        base64.b64encode(binary).decode("ascii")
                        if binary is not None
                        else None
                    ),
                    sha256=_sha256_file(path),
                )
            )
        return artifacts

    def partial_artifacts(self) -> list[WorkflowArtifact]:
        artifacts: list[WorkflowArtifact] = []
        for relative in self._artifact_sources:
            path = self._safe_output_path(relative)
            if not path.is_file():
                continue
            content = self._artifact_sources.get(relative, "")
            if not content.strip():
                continue
            binary = path.read_bytes() if path.suffix.casefold() == ".docx" else None
            artifacts.append(
                WorkflowArtifact(
                    path=relative,
                    content=content,
                    media_type=(
                        DOCX_MEDIA_TYPE if binary is not None else "text/markdown"
                    ),
                    binary_base64=(
                        base64.b64encode(binary).decode("ascii")
                        if binary is not None
                        else None
                    ),
                    sha256=_sha256_file(path),
                )
            )
        return artifacts


def _tool_documentation(task: LoadedWorkflowTask) -> str:
    return f"""Tool disponibili (restituisci una sola chiamata JSON per turno):
- {{"tool":"list_files","arguments":{{}}}}
- {{"tool":"search_documents","arguments":{{"query":"...","limit":20}}}}
- {{"tool":"open_document","arguments":{{"path":"public/documents/...","page":1,"max_chars":10000}}}}
- {{"tool":"inspect_metadata","arguments":{{"path":"public/documents/..."}}}}
- {{"tool":"write_artifact","arguments":{{"path":"nome-scelto.md","content":"..."}}}}
- {{"tool":"submit","arguments":{{"paths":["nome-scelto.md"]}}}}

Contratto tecnico della consegna:
- scegli liberamente nomi, numero e struttura degli artifact in base all'incarico;
- sono supportati artifact `.md`, `.txt` e `.docx`;
- `submit` deve indicare almeno un artifact già scritto e può indicarne più di uno;
- eventuali richieste su formato, contenuto o numero dei file valgono soltanto se
  compaiono nell'incarico o nei documenti pubblici.
"""


def build_workspace_prompt(
    task: LoadedWorkflowTask,
    transcript: list[dict[str, Any]] | None = None,
    *,
    current_step: int | None = None,
    max_steps: int | None = None,
    finalization_phase: bool = False,
    allowed_tools: set[str] | None = None,
    artifact_written: bool = False,
) -> str:
    task_text = (task.directory / "public/01_task.md").read_text(encoding="utf-8")
    history = ""
    if transcript:
        history = "\n\n<tool_history>\n" + "\n".join(
            json.dumps(item, ensure_ascii=False) for item in transcript
        ) + "\n</tool_history>"
    budget = ""
    if current_step is not None and max_steps is not None:
        remaining = max_steps - current_step + 1
        phase = "finalization" if finalization_phase else "exploration"
        permitted = ", ".join(sorted(allowed_tools or model_workspace_tools(task)))
        if finalization_phase:
            phase_instruction = (
                "La fase di esplorazione è chiusa. Non leggere o cercare altri "
                "documenti. Usa soltanto i tool consentiti per produrre e "
                "sottoporre gli artifact con le evidenze già raccolte."
            )
        else:
            phase_instruction = (
                "Esplora in modo selettivo. Concludi la raccolta prima della fase "
                "finale, che sarà riservata alla scrittura e alla submission."
            )
        budget = f"""

<run_budget current_step="{current_step}" max_steps="{max_steps}"
  remaining_steps_including_current="{remaining}" phase="{phase}"
  artifact_written="{str(artifact_written).lower()}">
Tool consentiti in questo turno: {permitted}.
{phase_instruction}
</run_budget>"""
    return f"""<legalita_agentic_workspace task_id="{task.spec.task_id}">
Sei l'agente incaricato del matter. Non hai accesso a shell, rete o filesystem
esterni: usa esclusivamente i tool elencati. I documenti non sono inclusi in
questo prompt e devono essere individuati e letti attraverso i tool.

<public_task>
{task_text.strip()}
</public_task>

{_tool_documentation(task).strip()}
{budget}
{history}

Restituisci esclusivamente il prossimo oggetto JSON di tool call. Non aggiungere
testo o markdown esterno al JSON.
</legalita_agentic_workspace>"""


def _aggregate_metrics(items: list[dict[str, Any]], model: str) -> dict[str, Any]:
    def total(name: str) -> int | None:
        values = [
            item.get(name)
            for item in items
            if isinstance(item.get(name), (int, float))
        ]
        return int(sum(values)) if values else None

    costs = [
        item.get("estimated_cost_usd")
        for item in items
        if isinstance(item.get("estimated_cost_usd"), (int, float))
    ]
    return {
        "provider": next(
            (item.get("provider") for item in items if item.get("provider")),
            None,
        ),
        "model": model,
        "call_count": len(items),
        "latency_ms": total("latency_ms"),
        "input_tokens": total("input_tokens"),
        "output_tokens": total("output_tokens"),
        "total_tokens": total("total_tokens"),
        "cached_input_tokens": total("cached_input_tokens"),
        "reasoning_tokens": total("reasoning_tokens"),
        "estimated_cost_usd": sum(costs) if costs else None,
        "per_call": items,
    }


def _finalization_steps(max_steps: int) -> int:
    return min(max_steps, max(2, math.ceil(max_steps * 0.15)))


def _step_policy(
    workspace: MatterWorkspace,
    *,
    step: int,
    max_steps: int,
) -> tuple[bool, set[str]]:
    remaining = max_steps - step + 1
    finalization = remaining <= _finalization_steps(max_steps)
    if not finalization:
        return False, model_workspace_tools(workspace.task)
    if remaining == 1:
        return True, {"submit"}
    if not workspace.partial_artifacts():
        return True, {"write_artifact"}
    return True, {"write_artifact", "submit"}


def generate_workspace_submission(
    task: LoadedWorkflowTask,
    *,
    model: str,
    gateway: ModelGateway | None = None,
    max_steps: int = 40,
    timeout_seconds: int = 900,
) -> WorkflowSubmission:
    if "agentic_workspace" not in task.spec.supported_execution_modes:
        raise WorkspaceError(f"{task.spec.task_id} non supporta agentic_workspace")
    if max_steps < 2:
        raise WorkspaceError("max_steps deve essere almeno 2 per scrittura e submission")
    if timeout_seconds < 1:
        raise WorkspaceError("timeout_seconds deve essere positivo")
    workspace = MatterWorkspace(task)
    transcript: list[dict[str, Any]] = []
    metrics: list[dict[str, Any]] = []
    raw_response: str | None = None
    started = time.monotonic()
    active_gateway = gateway or default_gateway()
    try:
        for step in range(1, max_steps + 1):
            if time.monotonic() - started > timeout_seconds:
                raise WorkspaceError(
                    f"timeout workspace dopo {timeout_seconds} secondi"
                )
            finalization, allowed_tools = _step_policy(
                workspace,
                step=step,
                max_steps=max_steps,
            )
            prompt = build_workspace_prompt(
                task,
                transcript,
                current_step=step,
                max_steps=max_steps,
                finalization_phase=finalization,
                allowed_tools=allowed_tools,
                artifact_written=bool(workspace.partial_artifacts()),
            )
            result = active_gateway.complete(model, prompt)
            if result is None:
                raise WorkspaceError("il modello non ha restituito una risposta")
            raw_response = result.text
            metrics.append(dict(result.metrics or {}))
            call = _json_object(result.text)
            tool = str(call.get("tool") or "")
            arguments = call.get("arguments") or {}
            if not isinstance(arguments, dict):
                raise WorkspaceError("arguments del tool call deve essere un oggetto")
            remaining = max_steps - step
            log.info(
                "[%s] Agent step=%d/%d — phase=%s — tool=%s — remaining=%d",
                task.short_id,
                step,
                max_steps,
                "finalization" if finalization else "exploration",
                tool or "<missing>",
                remaining,
            )
            try:
                observation = workspace.execute(
                    tool,
                    arguments,
                    allowed_tools=allowed_tools,
                )
            except Exception as exc:
                observation = {"error": str(exc)}
                log.warning(
                    "[%s] Agent tool error — step=%d tool=%s error=%s",
                    task.short_id,
                    step,
                    tool or "<missing>",
                    exc,
                )
            transcript.append(
                {
                    "step": step,
                    "tool": tool,
                    "arguments": (
                        {key: value for key, value in arguments.items() if key != "content"}
                        | (
                            {"content_chars": len(str(arguments.get("content") or ""))}
                            if "content" in arguments
                            else {}
                        )
                    ),
                    "observation": observation,
                }
            )
            if tool == "submit" and workspace.submitted_path is not None:
                artifacts = workspace.submitted_artifacts()
                manifest = {
                    **workspace.manifest,
                    "run_status": "completed",
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                    "steps": step,
                    "timeout_seconds": timeout_seconds,
                    "max_steps": max_steps,
                    "finalization_steps": _finalization_steps(max_steps),
                    "decision_log_entries": len(workspace.decision_log),
                    "artifact_revisions": workspace._artifact_revision,
                    "document_coverage": workspace.document_coverage(),
                }
                return WorkflowSubmission(
                    task_id=task.spec.task_id,
                    model=model,
                    source="live",
                    execution_mode="agentic_workspace",
                    artifacts=artifacts,
                    raw_response=raw_response,
                    model_call_metrics=_aggregate_metrics(metrics, model),
                    tool_trace=list(workspace.trace),
                    decision_log=list(workspace.decision_log),
                    workspace_manifest=manifest,
                )
        raise WorkspaceError(f"nessuna submission dopo {max_steps} step")
    except Exception as exc:
        failure_manifest = {
            **workspace.manifest,
            "run_status": "failed",
            "failed_at": datetime.now(timezone.utc).isoformat(),
            "termination_reason": str(exc),
            "error_type": type(exc).__name__,
            "steps": len(metrics),
            "tool_events": len(workspace.trace),
            "timeout_seconds": timeout_seconds,
            "max_steps": max_steps,
            "finalization_steps": _finalization_steps(max_steps),
            "decision_log_entries": len(workspace.decision_log),
            "artifact_revisions": workspace._artifact_revision,
            "document_coverage": workspace.document_coverage(),
        }
        raise WorkspaceRunFailure(
            str(exc),
            task_id=task.spec.task_id,
            model=model,
            error_type=type(exc).__name__,
            artifacts=workspace.partial_artifacts(),
            tool_trace=list(workspace.trace),
            decision_log=list(workspace.decision_log),
            workspace_manifest=failure_manifest,
            model_call_metrics=_aggregate_metrics(metrics, model),
            raw_response=raw_response,
        ) from exc
    finally:
        workspace.close()
