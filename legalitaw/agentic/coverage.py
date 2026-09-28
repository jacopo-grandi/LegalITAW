"""Copertura documentale del generic_agent ricavata dalla traccia degli strumenti.

Misura che cosa il sistema ha effettivamente aperto della busta pubblica, indipendentemente da quello che
dichiara nel deliverable. Un file conta come aperto se:
- ``read``: lo strumento read e' stato chiamato su quel file;
- ``shell``: un comando bash lo nomina, o nomina un pattern (``documents/documents/*.pdf``) o una cartella
  che lo contiene insieme a un comando che legge o converte (cat, pdftotext, python, for ...);
- ``grep``: grep lo ha attraversato ed e' un file di testo (grep non legge PDF, DOCX, XLSX).
Il prompt (01_task.md) e' fuori perimetro: il sistema lo riceve come messaggio.
"""
from __future__ import annotations

import fnmatch
import re
from pathlib import PurePosixPath
from typing import Any, Iterable, Mapping

TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json"}
_READERS = re.compile(r"\b(cat|head|tail|less|more|pdftotext|pdftohtml|pandoc|textutil|python3?|unzip|"
                      r"docx2txt|libreoffice|soffice|xlsx2csv|strings|sed|awk|grep|rg|wc|for)\b")


def _norm(path: str) -> str:
    path = (path or "").strip().strip("'\"")
    for prefix in ("/workspace/", "workspace/", "./", "/"):
        if path.startswith(prefix):
            path = path[len(prefix):]
    return path


def _tokens(command: str) -> list[str]:
    # separatori di shell e virgolette: "documents/documents/*.pdf;" -> "documents/documents/*.pdf"
    return [t for t in re.split(r"[\s;|&()<>`'\",]+", command) if t]


def generic_document_coverage(sources: Iterable[str], trace: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """``sources``: percorsi relativi alla cartella documents/ (le chiavi di workspace_manifest.public_inputs)."""
    wanted = {f"documents/{_norm(s)}": _norm(s) for s in sources if _norm(s) and not s.endswith("01_task.md")}
    via: dict[str, set[str]] = {path: set() for path in wanted}
    first_seq: dict[str, int] = {}

    def mark(path: str, how: str, seq: int) -> None:
        via[path].add(how)
        first_seq.setdefault(path, seq)

    for event in trace:
        if event.get("status") not in (None, "ok"):
            continue
        tool, args, seq = event.get("tool"), event.get("arguments") or {}, int(event.get("sequence") or 0)
        if tool == "read":
            target = _norm(str(args.get("path") or ""))
            for path in wanted:
                if target == path or target == wanted[path]:
                    mark(path, "read", seq)
        elif tool == "grep":
            base = _norm(str(args.get("path") or ""))
            name_glob = str(args.get("glob") or "*")
            for path in wanted:
                if PurePosixPath(path).suffix.lower() not in TEXT_SUFFIXES:
                    continue
                inside = not base or base in ("documents", ".") or path == base or path.startswith(base.rstrip("/") + "/")
                if inside and fnmatch.fnmatch(PurePosixPath(path).name, name_glob):
                    mark(path, "grep", seq)
        elif tool == "bash":
            command = str(args.get("command") or "")
            reads = bool(_READERS.search(command))
            for token in _tokens(command):
                token = _norm(token.split("=", 1)[-1] if token.startswith("--") else token)
                if "documents" not in token and not any(PurePosixPath(p).name in token for p in wanted):
                    continue
                for path in wanted:
                    name = PurePosixPath(path).name
                    if token == path or token == wanted[path] or token.endswith("/" + name) or token == name:
                        mark(path, "shell", seq)
                    elif any(ch in token for ch in "*?[") and (fnmatch.fnmatch(path, token)
                                                                or fnmatch.fnmatch(wanted[path], token)):
                        mark(path, "shell", seq)
                    elif reads and token.rstrip("/") in ("documents", "documents/documents") and \
                            path.startswith(token.rstrip("/") + "/") and ("-r" in command or "for " in command
                                                                          or "rglob" in command or "walk" in command
                                                                          or "listdir" in command or "glob" in command):
                        mark(path, "shell", seq)

    opened = sorted(p for p, how in via.items() if how & {"read", "shell"})
    grep_only = sorted(p for p, how in via.items() if how == {"grep"})
    unopened = sorted(p for p, how in via.items() if not how & {"read", "shell"})
    by_source = [{"path": wanted[p], "opened": bool(via[p] & {"read", "shell"}), "via": sorted(via[p]),
                  "first_event": first_seq.get(p)} for p in sorted(wanted)]
    count = len(wanted)

    def flag(name: str) -> bool | None:
        match = [p for p in wanted if PurePosixPath(p).name == name]
        return None if not match else all(p in opened for p in match)

    return {
        "schema_version": "generic_document_coverage_v1",
        "source_count": count,
        "opened_count": len(opened),
        "open_rate": round(len(opened) / count, 4) if count else 1.0,
        "read_tool_count": sum(1 for p in via if "read" in via[p]),
        "grep_only": [wanted[p] for p in grep_only],
        "unopened": [wanted[p] for p in unopened],
        "reference_pack_opened": flag("02_reference_pack.md"),
        "legal_sources_opened": flag("03_legal_sources.md"),
        "by_source": by_source,
    }
