"""Revisioni tracciate su DOCX per l'agente generico.

Un avvocato redige un redline con il controllo revisioni di Word, non
riscrivendo l'XML del documento. Questo modulo offre all'agente la stessa
capacita': applica a un .docx sostituzioni, cancellazioni, inserimenti e
commenti come revisioni tracciate (w:ins / w:del / commenti), attiva il
controllo revisioni nelle impostazioni e scrive un nuovo file.

Il testo viene cercato nel testo visibile di ciascun paragrafo (le parti gia'
eliminate non contano). Ogni ricerca deve individuare un'unica occorrenza:
altrimenti la modifica non viene applicata e l'errore torna all'agente.
"""

from __future__ import annotations

import copy
import io
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
COMMENTS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
COMMENTS_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"
SETTINGS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings"
SETTINGS_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

ACTIONS = ("replace", "delete", "insert_after", "insert_paragraph_after", "comment")
MAX_EDITS = 300


class RedlineError(ValueError):
    pass


def w(tag: str) -> str:
    return f"{{{W_NS}}}{tag}"


def _is_deleted(node: etree._Element) -> bool:
    parent = node.getparent()
    while parent is not None:
        if parent.tag == w("del"):
            return True
        parent = parent.getparent()
    return False


def _visible_runs(paragraph: etree._Element) -> list[tuple[etree._Element, str]]:
    runs = []
    for run in paragraph.iter(w("r")):
        if _is_deleted(run):
            continue
        parts = []
        for child in run:
            if child.tag == w("t"):
                parts.append(child.text or "")
            elif child.tag == w("tab"):
                parts.append("\t")
        runs.append((run, "".join(parts)))
    return runs


def _paragraph_text(paragraph: etree._Element) -> str:
    return "".join(text for _, text in _visible_runs(paragraph))


def _text_element(tag: str, text: str) -> etree._Element:
    element = etree.Element(w(tag))
    element.text = text
    if text != text.strip() or "  " in text:
        element.set(XML_SPACE, "preserve")
    return element


def _new_run(template: etree._Element | None, text: str, *, deleted: bool = False) -> etree._Element:
    run = etree.Element(w("r"))
    if template is not None:
        properties = template.find(w("rPr"))
        if properties is not None:
            run.append(copy.deepcopy(properties))
    run.append(_text_element("delText" if deleted else "t", text))
    return run


def _simple_run(run: etree._Element) -> bool:
    """A run we can split: only rPr and text children."""
    return all(child.tag in (w("rPr"), w("t")) for child in run)


class _Document:
    def __init__(self, source: Path, author: str) -> None:
        with zipfile.ZipFile(source) as archive:
            self.parts = {name: archive.read(name) for name in archive.namelist()}
        if "word/document.xml" not in self.parts:
            raise RedlineError("il file non contiene word/document.xml: non e' un .docx valido")
        self.document = etree.fromstring(self.parts["word/document.xml"])
        self.body = self.document.find(w("body"))
        self.author = author or "Revisore"
        self.date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.comments: etree._Element | None = None
        if "word/comments.xml" in self.parts:
            self.comments = etree.fromstring(self.parts["word/comments.xml"])
        existing = [
            int(value)
            for tree in (self.document, self.comments)
            if tree is not None
            for value in tree.xpath("//@w:id", namespaces={"w": W_NS})
            if str(value).lstrip("-").isdigit()
        ]
        self.next_id = max(existing, default=0) + 1

    def _id(self) -> str:
        value = self.next_id
        self.next_id += 1
        return str(value)

    def _change(self, tag: str) -> etree._Element:
        element = etree.Element(w(tag))
        element.set(w("id"), self._id())
        element.set(w("author"), self.author)
        element.set(w("date"), self.date)
        return element

    # --- ricerca -------------------------------------------------------
    def locate(self, needle: str) -> tuple[etree._Element, int]:
        if not needle:
            raise RedlineError("testo da cercare vuoto")
        hits = []
        for paragraph in self.body.iter(w("p")):
            text = _paragraph_text(paragraph)
            start = text.find(needle)
            while start >= 0:
                hits.append((paragraph, start))
                start = text.find(needle, start + 1)
        if not hits:
            raise RedlineError(f"testo non trovato: {needle[:80]!r}")
        if len(hits) > 1:
            raise RedlineError(
                f"testo ambiguo ({len(hits)} occorrenze): allungare il testo cercato {needle[:80]!r}"
            )
        return hits[0]

    def isolate(self, paragraph: etree._Element, start: int, end: int) -> list[etree._Element]:
        """Split runs so that [start, end) is covered exactly by whole runs."""
        position = 0
        selected: list[etree._Element] = []
        for run, text in _visible_runs(paragraph):
            run_start, run_end = position, position + len(text)
            position = run_end
            if run_end <= start or run_start >= end or not text:
                continue
            cut_left = max(start, run_start) - run_start
            cut_right = min(end, run_end) - run_start
            if cut_left == 0 and cut_right == len(text):
                selected.append(run)
                continue
            if not _simple_run(run):
                raise RedlineError("il testo cade dentro un elemento non divisibile (tabulazione o campo)")
            parent = run.getparent()
            index = parent.index(run)
            pieces = [text[:cut_left], text[cut_left:cut_right], text[cut_right:]]
            new_runs = []
            for piece in pieces:
                new_runs.append(_new_run(run, piece) if piece else None)
            parent.remove(run)
            offset = index
            for piece_run in new_runs:
                if piece_run is not None:
                    parent.insert(offset, piece_run)
                    offset += 1
            selected.append(new_runs[1])
        if not selected:
            raise RedlineError("intervallo di testo vuoto")
        parents = {id(run.getparent()) for run in selected}
        if len(parents) > 1:
            raise RedlineError("il testo attraversa strutture diverse (es. collegamento): cercarne una parte")
        return selected

    def isolate_point(self, paragraph: etree._Element, offset: int) -> tuple[etree._Element, int]:
        """Return (parent, index) at which to insert after character offset."""
        position = 0
        for run, text in _visible_runs(paragraph):
            run_end = position + len(text)
            if position < offset < run_end:
                if not _simple_run(run):
                    raise RedlineError("punto di inserimento dentro un elemento non divisibile")
                self.isolate(paragraph, position, offset)
                return self.isolate_point(paragraph, offset)
            if run_end == offset and text:
                parent = run.getparent()
                return parent, parent.index(run) + 1
            position = run_end
        raise RedlineError("punto di inserimento non trovato")

    # --- operazioni ----------------------------------------------------
    def delete(self, needle: str) -> list[etree._Element]:
        paragraph, start = self.locate(needle)
        runs = self.isolate(paragraph, start, start + len(needle))
        parent = runs[0].getparent()
        index = parent.index(runs[0])
        deletion = self._change("del")
        for run in runs:
            parent.remove(run)
            for text in run.findall(w("t")):
                text.tag = w("delText")
            deletion.append(run)
        parent.insert(index, deletion)
        return [deletion]

    def insert_after(self, anchor: str, text: str) -> list[etree._Element]:
        if not text:
            raise RedlineError("testo da inserire vuoto")
        paragraph, start = self.locate(anchor)
        runs = self.isolate(paragraph, start, start + len(anchor))
        parent, index = self.isolate_point(paragraph, start + len(anchor))
        insertion = self._change("ins")
        insertion.append(_new_run(runs[-1], text))
        parent.insert(index, insertion)
        return [insertion]

    def replace(self, needle: str, text: str) -> list[etree._Element]:
        paragraph, start = self.locate(needle)
        runs = self.isolate(paragraph, start, start + len(needle))
        template = runs[0]
        deletion = self.delete(needle)[0]
        if not text:
            return [deletion]
        insertion = self._change("ins")
        insertion.append(_new_run(template, text))
        parent = deletion.getparent()
        parent.insert(parent.index(deletion) + 1, insertion)
        return [deletion, insertion]

    def insert_paragraph_after(self, anchor: str, text: str) -> list[etree._Element]:
        if not text:
            raise RedlineError("testo del nuovo paragrafo vuoto")
        paragraph, _ = self.locate(anchor)
        new_paragraph = etree.Element(w("p"))
        properties = paragraph.find(w("pPr"))
        new_properties = copy.deepcopy(properties) if properties is not None else etree.Element(w("pPr"))
        run_properties = new_properties.find(w("rPr"))
        if run_properties is None:
            run_properties = etree.SubElement(new_properties, w("rPr"))
        run_properties.append(self._change("ins"))
        new_paragraph.append(new_properties)
        runs = _visible_runs(paragraph)
        insertion = self._change("ins")
        insertion.append(_new_run(runs[0][0] if runs else None, text))
        new_paragraph.append(insertion)
        paragraph.addnext(new_paragraph)
        return [insertion]

    def comment(self, targets: list[etree._Element], text: str) -> None:
        if not text:
            raise RedlineError("testo del commento vuoto")
        if self.comments is None:
            self.comments = etree.Element(w("comments"), nsmap={"w": W_NS})
        comment_id = self._id()
        node = etree.SubElement(self.comments, w("comment"))
        node.set(w("id"), comment_id)
        node.set(w("author"), self.author)
        node.set(w("date"), self.date)
        node.set(w("initials"), "".join(part[:1] for part in self.author.split())[:4] or "R")
        paragraph = etree.SubElement(node, w("p"))
        run = etree.SubElement(paragraph, w("r"))
        run.append(_text_element("t", text))
        first, last = targets[0], targets[-1]
        start = etree.Element(w("commentRangeStart"))
        start.set(w("id"), comment_id)
        first.addprevious(start)
        end = etree.Element(w("commentRangeEnd"))
        end.set(w("id"), comment_id)
        last.addnext(end)
        reference_run = etree.Element(w("r"))
        reference = etree.SubElement(reference_run, w("commentReference"))
        reference.set(w("id"), comment_id)
        end.addnext(reference_run)

    def comment_on(self, needle: str, text: str) -> None:
        paragraph, start = self.locate(needle)
        runs = self.isolate(paragraph, start, start + len(needle))
        self.comment(runs, text)

    # --- scrittura -----------------------------------------------------
    def _ensure_part(self, part: str, relationship: str, content_type: str, default: bytes) -> None:
        if part not in self.parts:
            self.parts[part] = default
        rels_name = "word/_rels/document.xml.rels"
        rels = etree.fromstring(self.parts[rels_name])
        target = part.split("/", 1)[1]
        if not any(item.get("Type") == relationship for item in rels):
            used = {item.get("Id") for item in rels}
            number = 1
            while f"rId{number}" in used:
                number += 1
            item = etree.SubElement(rels, f"{{{PKG_REL_NS}}}Relationship")
            item.set("Id", f"rId{number}")
            item.set("Type", relationship)
            item.set("Target", target)
            self.parts[rels_name] = etree.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone=True)
        types = etree.fromstring(self.parts["[Content_Types].xml"])
        if not any(item.get("PartName") == f"/{part}" for item in types):
            item = etree.SubElement(types, f"{{{CT_NS}}}Override")
            item.set("PartName", f"/{part}")
            item.set("ContentType", content_type)
            self.parts["[Content_Types].xml"] = etree.tostring(types, xml_declaration=True, encoding="UTF-8", standalone=True)

    def enable_tracking(self) -> None:
        default = (
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:settings xmlns:w="{W_NS}"/>'
        ).encode("utf-8")
        self._ensure_part("word/settings.xml", SETTINGS_REL, SETTINGS_CT, default)
        settings = etree.fromstring(self.parts["word/settings.xml"])
        if settings.find(w("trackRevisions")) is None:
            settings.insert(0, etree.Element(w("trackRevisions")))
        self.parts["word/settings.xml"] = etree.tostring(settings, xml_declaration=True, encoding="UTF-8", standalone=True)

    def save(self, destination: Path) -> None:
        self.enable_tracking()
        self.parts["word/document.xml"] = etree.tostring(
            self.document, xml_declaration=True, encoding="UTF-8", standalone=True
        )
        if self.comments is not None:
            data = etree.tostring(self.comments, xml_declaration=True, encoding="UTF-8", standalone=True)
            self._ensure_part("word/comments.xml", COMMENTS_REL, COMMENTS_CT, data)
            self.parts["word/comments.xml"] = data
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
            order = ["[Content_Types].xml", *[name for name in self.parts if name != "[Content_Types].xml"]]
            for name in order:
                archive.writestr(name, self.parts[name])
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(buffer.getvalue())


def apply_redline(source: Path, destination: Path, edits: list[dict[str, Any]], author: str = "") -> dict[str, Any]:
    if not isinstance(edits, list) or not edits:
        raise RedlineError("edits deve essere una lista non vuota")
    if len(edits) > MAX_EDITS:
        raise RedlineError(f"massimo {MAX_EDITS} modifiche per chiamata")
    document = _Document(source, author)
    report = []
    for number, edit in enumerate(edits, start=1):
        action = str((edit or {}).get("action") or "")
        find = str(edit.get("find") or "")
        text = str(edit.get("text") or "")
        note = str(edit.get("comment") or "")
        try:
            if action not in ACTIONS:
                raise RedlineError(f"azione non valida: {action!r} (ammesse: {', '.join(ACTIONS)})")
            if action == "replace":
                targets = document.replace(find, text)
            elif action == "delete":
                targets = document.delete(find)
            elif action == "insert_after":
                targets = document.insert_after(find, text)
            elif action == "insert_paragraph_after":
                targets = document.insert_paragraph_after(find, text)
            else:
                document.comment_on(find, note or text)
                targets = []
            if note and action != "comment":
                document.comment(targets, note)
            report.append({"edit": number, "action": action, "status": "applied"})
        except RedlineError as exc:
            report.append({"edit": number, "action": action, "status": "error", "error": str(exc)})
    applied = sum(item["status"] == "applied" for item in report)
    if applied:
        document.save(destination)
    return {
        "applied": applied,
        "failed": len(report) - applied,
        "written": bool(applied),
        "report": report,
    }
