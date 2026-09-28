"""Busta pubblica dei task e lettura testuale dei documenti.

Qui vivono i pezzi condivisi fra l'harness ``generic_agent`` e il contesto
completo del giudice: quali file pubblici vede il modello, gli errori di run
con le loro evidenze, l'estrazione di testo da PDF, DOCX, XLSX e file di
testo, e l'aggregazione delle metriche delle chiamate.
"""

from __future__ import annotations

import logging
import posixpath
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree
import zipfile

from .models import (
    DecisionLogEntry,
    LoadedWorkflowTask,
    WorkflowArtifact,
)


log = logging.getLogger(__name__)


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


def validate_runtime_capabilities(
    task: LoadedWorkflowTask,
    *,
    execution_mode: str,
) -> dict[str, Any]:
    """Fail before API work if a task needs a reader or writer we lack."""
    input_suffixes = {Path(item).suffix.casefold() for item in public_envelope_paths(task)}
    unsupported_inputs = sorted(input_suffixes - SUPPORTED_DOCUMENT_SUFFIXES)
    if execution_mode not in {"text_bundle", "generic_agent"}:
        raise WorkspaceError(f"modalità di esecuzione non supportata: {execution_mode}")
    if execution_mode != "generic_agent" and unsupported_inputs:
        raise WorkspaceError(
            f"{task.spec.task_id}: reader mancanti per {unsupported_inputs}"
        )

    return {
        "task_id": task.spec.task_id,
        "execution_mode": execution_mode,
        "input_readers": sorted(input_suffixes),
        "artifact_writers": sorted(SUPPORTED_ARTIFACT_SUFFIXES),
        "required_tools": [],
        "missing_tools": [],
        "native_artifact_mode": str(
            getattr(task.spec, "native_artifact_mode", None) or "markdown"
        ),
    }


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


class PublicDocumentReader:
    """Estrae il testo, per pagine, dei soli input pubblici dichiarati dal task."""

    def __init__(self, task: LoadedWorkflowTask) -> None:
        self.task = task
        self._allowed = set(public_envelope_paths(task))
        self._text_cache: dict[str, list[str]] = {}

    def _safe_public_path(self, relative: str) -> Path:
        if relative not in self._allowed or not relative.startswith("public/"):
            raise WorkspaceError(f"input fuori dalla busta pubblica: {relative!r}")
        public_root = (self.task.directory / "public").resolve()
        path = (self.task.directory / relative).resolve()
        if not path.is_relative_to(public_root) or not path.is_file():
            raise WorkspaceError(f"input pubblico non valido: {relative!r}")
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
        path = self._safe_public_path(relative)
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
        return pages

    def document_pages(self, relative: str) -> list[str]:
        """Return normalized text pages for one declared public input."""
        return list(self._pages(relative))


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
