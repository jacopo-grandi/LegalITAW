"""Deterministic native artifact brokers for agentic Workflow 2.0 runs."""

from __future__ import annotations

import io
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


DOCX_MEDIA_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
_W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
_MARKER_RE = re.compile(r"\[\[(DEL|INS|NOTE):\s*(.*?)\]\]")
_TABLE_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$"
)


class NativeArtifactError(ValueError):
    """The model-authored source cannot be rendered as a valid native artifact."""


def _set_run_font(
    run: Any,
    *,
    name: str = "Calibri",
    size: float = 11,
    color: str = "000000",
    bold: bool | None = None,
    italic: bool | None = None,
) -> None:
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def _configure_styles(document: Document, *, preset: str) -> None:
    if preset not in {"standard_business_brief", "contract_negotiation_brief"}:
        raise NativeArtifactError(f"preset DOCX non supportato: {preset}")
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.right_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)

    normal = document.styles["Normal"]
    normal.font.name = "Calibri"
    normal._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Calibri")
    normal._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Calibri")
    normal.font.size = Pt(11)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.10 if preset == "standard_business_brief" else 1.25

    heading_tokens = {
        "Heading 1": (16, "2E74B5", 14 if preset == "contract_negotiation_brief" else 16, 8),
        "Heading 2": (13, "2E74B5", 11 if preset == "contract_negotiation_brief" else 12, 6),
        "Heading 3": (12, "1F4D78", 8, 4),
    }
    for style_name, (size, color, before, after) in heading_tokens.items():
        style = document.styles[style_name]
        style.font.name = "Calibri"
        style._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Calibri")
        style._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Calibri")
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor.from_string(color)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True

    for style_name in ("List Bullet", "List Number"):
        style = document.styles[style_name]
        style.font.name = "Calibri"
        style._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Calibri")
        style._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Calibri")
        style.font.size = Pt(11)
        style.paragraph_format.left_indent = (
            Inches(0.375) if preset == "contract_negotiation_brief" else Inches(0.5)
        )
        style.paragraph_format.first_line_indent = (
            Inches(-0.188) if preset == "contract_negotiation_brief" else Inches(-0.25)
        )
        style.paragraph_format.space_after = (
            Pt(4) if preset == "contract_negotiation_brief" else Pt(8)
        )


def _enable_track_revisions(document: Document) -> None:
    settings = document.settings.element
    if settings.find(qn("w:trackRevisions")) is None:
        settings.insert(0, OxmlElement("w:trackRevisions"))


def _revision_element(
    kind: str,
    text: str,
    *,
    revision_id: int,
    author: str,
) -> OxmlElement:
    wrapper = OxmlElement("w:ins" if kind == "INS" else "w:del")
    wrapper.set(qn("w:id"), str(revision_id))
    wrapper.set(qn("w:author"), author)
    wrapper.set(qn("w:date"), datetime.now(timezone.utc).isoformat())
    run = OxmlElement("w:r")
    properties = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "Calibri")
    fonts.set(qn("w:hAnsi"), "Calibri")
    properties.append(fonts)
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), "22")
    properties.append(size)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "1F4D78" if kind == "INS" else "C00000")
    properties.append(color)
    if kind == "INS":
        underline = OxmlElement("w:u")
        underline.set(qn("w:val"), "single")
        properties.append(underline)
    else:
        properties.append(OxmlElement("w:strike"))
    run.append(properties)
    value = OxmlElement("w:t" if kind == "INS" else "w:delText")
    value.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    value.text = text
    run.append(value)
    wrapper.append(run)
    return wrapper


def _add_inline_content(
    document: Document,
    paragraph: Any,
    text: str,
    *,
    redline: bool,
    author: str,
    revision_counter: list[int],
) -> dict[str, int]:
    counts = {"insertions": 0, "deletions": 0, "comments": 0}
    cursor = 0
    comments: list[str] = []
    for marker in _MARKER_RE.finditer(text):
        prefix = text[cursor : marker.start()]
        if prefix:
            run = paragraph.add_run(prefix)
            _set_run_font(run)
        kind, value = marker.group(1), marker.group(2).strip()
        if not value:
            raise NativeArtifactError(f"marker {kind} senza contenuto")
        if kind == "NOTE":
            comments.append(value)
        else:
            if not redline:
                raise NativeArtifactError(
                    "marker INS/DEL ammesso soltanto per un output redline"
                )
            revision_counter[0] += 1
            paragraph._p.append(
                _revision_element(
                    kind,
                    value,
                    revision_id=revision_counter[0],
                    author=author,
                )
            )
            counts["insertions" if kind == "INS" else "deletions"] += 1
        cursor = marker.end()
    suffix = text[cursor:]
    if suffix:
        run = paragraph.add_run(suffix)
        _set_run_font(run)
    if "[[" in _MARKER_RE.sub("", text):
        raise NativeArtifactError("marker DOCX non riconosciuto o non chiuso")

    for comment_text in comments:
        anchor = paragraph.add_run("\u200b")
        _set_run_font(anchor)
        document.add_comment(
            runs=anchor,
            text=comment_text,
            author=author,
            initials="AI",
        )
        counts["comments"] += 1
    return counts


def _table_cells(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [item.strip() for item in value.split("|")]


def _set_table_geometry(table: Any, column_count: int) -> None:
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    table_width = 9360
    column_widths = [table_width // column_count] * column_count
    column_widths[-1] += table_width - sum(column_widths)
    properties = table._tbl.tblPr
    width = properties.first_child_found_in("w:tblW")
    if width is None:
        width = OxmlElement("w:tblW")
        properties.append(width)
    width.set(qn("w:type"), "dxa")
    width.set(qn("w:w"), str(table_width))
    indent = properties.first_child_found_in("w:tblInd")
    if indent is None:
        indent = OxmlElement("w:tblInd")
        properties.append(indent)
    indent.set(qn("w:type"), "dxa")
    indent.set(qn("w:w"), "120")
    layout = properties.first_child_found_in("w:tblLayout")
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        properties.append(layout)
    layout.set(qn("w:type"), "fixed")

    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for column_width in column_widths:
        node = OxmlElement("w:gridCol")
        node.set(qn("w:w"), str(column_width))
        grid.append(node)
    for row in table.rows:
        for index, cell in enumerate(row.cells):
            cell.width = Inches(column_widths[index] / 1440)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell_properties = cell._tc.get_or_add_tcPr()
            cell_width = cell_properties.first_child_found_in("w:tcW")
            cell_width.set(qn("w:type"), "dxa")
            cell_width.set(qn("w:w"), str(column_widths[index]))
            margins = cell_properties.first_child_found_in("w:tcMar")
            if margins is None:
                margins = OxmlElement("w:tcMar")
                cell_properties.append(margins)
            for side, value in (
                ("top", 80),
                ("bottom", 80),
                ("start", 120),
                ("end", 120),
            ):
                node = margins.find(qn(f"w:{side}"))
                if node is None:
                    node = OxmlElement(f"w:{side}")
                    margins.append(node)
                node.set(qn("w:w"), str(value))
                node.set(qn("w:type"), "dxa")


def render_docx(
    source: str,
    destination: Path,
    *,
    redline: bool,
    preset: str,
    author: str,
) -> dict[str, int]:
    """Render bounded Markdown plus INS/DEL/NOTE markers to a native DOCX."""
    if not source.strip():
        raise NativeArtifactError("sorgente DOCX vuota")
    if redline and not _MARKER_RE.search(source):
        raise NativeArtifactError("il redline richiede marker INS/DEL/NOTE")

    document = Document()
    _configure_styles(document, preset=preset)
    if redline:
        _enable_track_revisions(document)

    counts = {"insertions": 0, "deletions": 0, "comments": 0}
    revision_counter = [0]
    lines = source.splitlines()
    index = 0
    first_heading = True
    while index < len(lines):
        line = lines[index].rstrip()
        if not line.strip():
            index += 1
            continue
        if (
            line.lstrip().startswith("|")
            and index + 1 < len(lines)
            and _TABLE_SEPARATOR_RE.match(lines[index + 1])
        ):
            raw_rows = [_table_cells(line)]
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                raw_rows.append(_table_cells(lines[index]))
                index += 1
            column_count = len(raw_rows[0])
            if column_count < 2 or any(len(row) != column_count for row in raw_rows):
                raise NativeArtifactError("tabella Markdown con numero colonne incoerente")
            table = document.add_table(rows=len(raw_rows), cols=column_count)
            table.style = "Table Grid"
            for row_index, values in enumerate(raw_rows):
                for cell, value in zip(table.rows[row_index].cells, values):
                    paragraph = cell.paragraphs[0]
                    local = _add_inline_content(
                        document,
                        paragraph,
                        value,
                        redline=redline,
                        author=author,
                        revision_counter=revision_counter,
                    )
                    for key, value_count in local.items():
                        counts[key] += value_count
                    if row_index == 0:
                        for run in paragraph.runs:
                            run.bold = True
            _set_table_geometry(table, column_count)
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        bullet = re.match(r"^\s*[-*+]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            paragraph = document.add_paragraph(
                style="Heading 1" if level == 1 else f"Heading {level}"
            )
            if first_heading and level == 1:
                paragraph.paragraph_format.space_before = Pt(0)
                first_heading = False
            text = heading.group(2)
        elif bullet:
            paragraph = document.add_paragraph(style="List Bullet")
            text = bullet.group(1)
        elif numbered:
            paragraph = document.add_paragraph(style="List Number")
            text = numbered.group(1)
        else:
            paragraph = document.add_paragraph()
            text = line
        local = _add_inline_content(
            document,
            paragraph,
            text,
            redline=redline,
            author=author,
            revision_counter=revision_counter,
        )
        for key, value_count in local.items():
            counts[key] += value_count
        index += 1

    if redline and (
        counts["insertions"] == 0
        or counts["deletions"] == 0
        or counts["comments"] == 0
    ):
        raise NativeArtifactError(
            "il redline richiede almeno una inserzione, una eliminazione e un commento"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    document.save(destination)
    return counts


def docx_features(value: bytes | Path) -> dict[str, Any]:
    """Inspect the OOXML features used by deterministic artifact checks."""
    raw = value.read_bytes() if isinstance(value, Path) else value
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        document_xml = archive.read("word/document.xml")
        settings_xml = archive.read("word/settings.xml")
        names = set(archive.namelist())
        comments_xml = (
            archive.read("word/comments.xml") if "word/comments.xml" in names else b""
        )
    document = ElementTree.fromstring(document_xml)
    settings = ElementTree.fromstring(settings_xml)
    namespace = {"w": _W_NS}
    comments = (
        ElementTree.fromstring(comments_xml).findall("w:comment", namespace)
        if comments_xml
        else []
    )
    return {
        "valid_package": True,
        "track_revisions_enabled": (
            settings.find("w:trackRevisions", namespace) is not None
        ),
        "insertions": len(document.findall(".//w:ins", namespace)),
        "deletions": len(document.findall(".//w:del", namespace)),
        "comment_range_starts": len(
            document.findall(".//w:commentRangeStart", namespace)
        ),
        "comment_range_ends": len(
            document.findall(".//w:commentRangeEnd", namespace)
        ),
        "comment_references": len(
            document.findall(".//w:commentReference", namespace)
        ),
        "comments": len(comments),
    }
