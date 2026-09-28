"""Minimal, provider-neutral agent harness for LegalITA v2.

The harness provides a filesystem, six generic tools and external safety
limits.  It does not prescribe phases, coverage, deliverable names or a
submission action: a run ends when the model stops requesting tools.
"""

from __future__ import annotations

import base64
import fnmatch
import hashlib
import json
import mimetypes
import os
import re
import shlex
import shutil
import subprocess
import sys
import sysconfig
import tempfile
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from xml.etree import ElementTree

from legalitaw.modeling.tool_calling import (
    NativeToolGateway,
    ToolDefinition,
    default_native_tool_gateway,
)

from legalitaw.config import AGENT_MAX_OUTPUT_TOKENS, AGENT_REASONING_EFFORT

from .models import LoadedWorkflowTask, WorkflowArtifact, WorkflowSubmission
from .coverage import generic_document_coverage
from .submissions import _read_artifact
from .workspace import (
    WorkspaceError,
    WorkspaceRunFailure,
    _aggregate_metrics,
    public_envelope_paths,
)


GENERIC_AGENT_TOOLS = ("bash", "read", "write", "edit", "glob", "grep", "docx_redline")
GENERIC_AGENT_PROFILES = ("bare", "production")
MAX_TOOL_OUTPUT_CHARS = 100_000
MAX_TEXT_WRITE_CHARS = 5_000_000
MAX_ARTIFACT_BYTES = 100_000_000


def generic_tool_definitions() -> list[ToolDefinition]:
    """Return the invariant tool surface exposed on every turn."""
    object_schema = {"type": "object", "additionalProperties": False}
    return [
        ToolDefinition(
            "bash",
            "Run a shell command from the isolated workspace root. Network is disabled.",
            {
                **object_schema,
                "properties": {
                    "command": {"type": "string"},
                    "timeout_seconds": {"type": "integer", "minimum": 1, "maximum": 120},
                },
                "required": ["command"],
            },
        ),
        ToolDefinition(
            "read",
            "Read a workspace file by line range. Text files are returned as-is; "
            "PDF, DOCX, XLSX and EML documents are returned as extracted text "
            "(PDF pages are marked [PAGINA n]).",
            {
                **object_schema,
                "properties": {
                    "path": {"type": "string"},
                    "offset": {"type": "integer", "minimum": 1},
                    "limit": {"type": "integer", "minimum": 1, "maximum": 5000},
                },
                "required": ["path"],
            },
        ),
        ToolDefinition(
            "write",
            "Create or replace a UTF-8 file under scratch/ or output/.",
            {
                **object_schema,
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        ),
        ToolDefinition(
            "edit",
            "Replace exact text in a UTF-8 file under scratch/ or output/.",
            {
                **object_schema,
                "properties": {
                    "path": {"type": "string"},
                    "old_text": {"type": "string"},
                    "new_text": {"type": "string"},
                    "replace_all": {"type": "boolean"},
                },
                "required": ["path", "old_text", "new_text"],
            },
        ),
        ToolDefinition(
            "glob",
            "List workspace files matching a glob pattern.",
            {
                **object_schema,
                "properties": {
                    "pattern": {"type": "string"},
                    "path": {"type": "string"},
                },
                "required": ["pattern"],
            },
        ),
        ToolDefinition(
            "grep",
            "Search UTF-8 workspace files with a regular expression.",
            {
                **object_schema,
                "properties": {
                    "pattern": {"type": "string"},
                    "path": {"type": "string"},
                    "glob": {"type": "string"},
                    "case_sensitive": {"type": "boolean"},
                    "max_results": {"type": "integer", "minimum": 1, "maximum": 1000},
                },
                "required": ["pattern"],
            },
        ),
        ToolDefinition(
            "docx_redline",
            (
                "Write a copy of a .docx with tracked changes (Word revisions) and comments. "
                "Each edit locates text by exact match inside one paragraph of the current "
                "document; the match must be unique. Actions: replace (find -> text), delete "
                "(find), insert_after (text after find), insert_paragraph_after (new paragraph "
                "after the paragraph containing find), comment (comment on find). Any edit may "
                "add a comment. Failed edits are reported and skipped; the file is written if "
                "at least one edit applies. To continue, call again using the output as source."
            ),
            {
                **object_schema,
                "properties": {
                    "source": {"type": "string"},
                    "output": {"type": "string"},
                    "author": {"type": "string"},
                    "edits": {
                        "type": "array",
                        "minItems": 1,
                        "maxItems": 300,
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "action": {
                                    "type": "string",
                                    "enum": [
                                        "replace",
                                        "delete",
                                        "insert_after",
                                        "insert_paragraph_after",
                                        "comment",
                                    ],
                                },
                                "find": {"type": "string"},
                                "text": {"type": "string"},
                                "comment": {"type": "string"},
                            },
                            "required": ["action", "find"],
                        },
                    },
                },
                "required": ["source", "output", "edits"],
            },
        ),
    ]


def generic_agent_system_prompt(profile: str) -> str:
    if profile not in GENERIC_AGENT_PROFILES:
        raise WorkspaceError(f"profilo generic_agent non supportato: {profile}")
    skills = (
        " Technical document skills are available under skills/; consult them "
        "when they are relevant."
        if profile == "production"
        else ""
    )
    return (
        "You are working in an isolated matter workspace. The task is the user "
        "message. The workspace root is the current directory for bash and all "
        "paths below are relative to it. Source documents are read-only under "
        "documents/. Use scratch/ for notes and intermediate work, and place "
        "every deliverable under output/. You may choose your own strategy, "
        "tools, file names, formats, "
        "iterations, and stopping point. The available tools are bash, read, "
        "write, edit, glob, grep, and docx_redline. Network access is disabled. Do not attempt "
        "to access files outside the workspace or hidden benchmark data."
        + skills
    )


class GenericAgentWorkspace:
    """Public-only workspace and generic tool broker."""

    def __init__(self, task: LoadedWorkflowTask, *, profile: str = "bare") -> None:
        if profile not in GENERIC_AGENT_PROFILES:
            raise WorkspaceError(f"profilo generic_agent non supportato: {profile}")
        self.task = task
        self.profile = profile
        self.root = Path(
            tempfile.mkdtemp(prefix=f"legalita-generic-{task.short_id}-")
        ).resolve()
        self.documents = self.root / "documents"
        self.scratch = self.root / "scratch"
        self.output = self.root / "output"
        self.skills = self.root / "skills"
        for path in (self.documents, self.scratch, self.output):
            path.mkdir(mode=0o700)
        self.trace: list[dict[str, Any]] = []
        self._sandbox_verified = False
        self._copy_documents()
        if profile == "production":
            self._copy_production_skills()
        self.sandbox_backend = self._detect_sandbox_backend()
        self.manifest = self._build_manifest()

    def close(self) -> None:
        if not self.root.exists():
            return
        for path in self.root.rglob("*"):
            try:
                if path.is_symlink():
                    path.unlink()
                    continue
                path.chmod(0o700 if path.is_dir() else 0o600)
            except OSError:
                pass
        shutil.rmtree(self.root)

    def _copy_documents(self) -> None:
        public_root = (self.task.directory / "public").resolve()
        for relative in public_envelope_paths(self.task):
            if relative == "public/01_task.md":
                continue
            source = (self.task.directory / relative).resolve()
            resolved = source.resolve()
            if not resolved.is_relative_to(public_root) or not resolved.is_file():
                raise WorkspaceError(f"input pubblico non valido: {source}")
            destination = self.documents / resolved.relative_to(public_root)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(resolved, destination)
            destination.chmod(0o400)
        for directory in sorted(self.documents.rglob("*"), reverse=True):
            if directory.is_dir():
                directory.chmod(0o500)
        self.documents.chmod(0o500)

    def _copy_production_skills(self) -> None:
        source = Path(__file__).with_name("production_skills")
        if not source.is_dir():
            raise WorkspaceError(f"skill production mancanti: {source}")
        shutil.copytree(source, self.skills)
        for path in self.skills.rglob("*"):
            path.chmod(0o500 if path.is_dir() else 0o400)
        self.skills.chmod(0o500)

    @staticmethod
    def _detect_sandbox_backend() -> str | None:
        requested = os.environ.get("LEGALITA_GENERIC_AGENT_BASH_BACKEND", "auto")
        if requested == "disabled":
            return None
        if requested not in {"auto", "sandbox-exec"}:
            raise WorkspaceError(
                "LEGALITA_GENERIC_AGENT_BASH_BACKEND deve essere auto, "
                "sandbox-exec o disabled"
            )
        executable = shutil.which("sandbox-exec")
        if executable:
            return "sandbox-exec"
        if requested == "sandbox-exec":
            raise WorkspaceError("sandbox-exec richiesto ma non disponibile")
        return None

    def require_safe_bash(self) -> None:
        if self.sandbox_backend is None:
            raise WorkspaceError(
                "generic_agent richiede un backend OS per il tool bash; "
                "su questa piattaforma sandbox-exec non è disponibile"
            )
        if self._sandbox_verified:
            return
        profile_path = self.root / ".sandbox-probe.sb"
        profile_path.write_text(self._sandbox_profile(), encoding="utf-8")
        forbidden = shlex.quote(str(self.task.rubric_path.resolve()))
        python = shlex.quote(str(Path(sys.executable).resolve()))
        probe_command = "set -x; " + " ".join(
            [
                "test -r documents",
                "&& touch scratch/.sandbox-write-probe",
                "&& rm scratch/.sandbox-write-probe",
                f"&& test ! -r {forbidden}",
                f"&& {python} -c 'import sys'",
                f"&& {python} -c 'import errno,socket; "
                "assert socket.socket().connect_ex((\"127.0.0.1\",9)) "
                "== errno.EPERM'",
            ]
        )
        probe = subprocess.run(
            [
                shutil.which("sandbox-exec") or "/usr/bin/sandbox-exec",
                "-f",
                str(profile_path),
                "/bin/bash",
                "--noprofile",
                "--norc",
                "-c",
                probe_command,
            ],
            cwd=self.root,
            env=self._bash_environment(),
            text=True,
            capture_output=True,
            stdin=subprocess.DEVNULL,
            timeout=10,
            check=False,
        )
        if probe.returncode != 0:
            raise WorkspaceError(
                "il backend sandbox-exec è presente ma non applicabile: "
                + (probe.stderr or f"exit {probe.returncode}").strip()
            )
        self._sandbox_verified = True

    def _bash_environment(self) -> dict[str, str]:
        (self.scratch / "tmp").mkdir(exist_ok=True)
        return {
            "HOME": str(self.scratch),
            "TMPDIR": str(self.scratch / "tmp"),
            "PATH": f"{Path(sys.executable).parent}:/usr/bin:/bin:/usr/sbin:/sbin",
            "LANG": "C.UTF-8",
            "LC_ALL": "C.UTF-8",
        }

    def _build_manifest(self) -> dict[str, Any]:
        inputs = {
            path.relative_to(self.documents).as_posix(): {
                "sha256": _sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in sorted(self.documents.rglob("*"))
            if path.is_file()
        }
        skills = (
            {
                path.relative_to(self.skills).as_posix(): {
                    "sha256": _sha256_file(path),
                    "bytes": path.stat().st_size,
                }
                for path in sorted(self.skills.rglob("*"))
                if path.is_file()
            }
            if self.skills.is_dir()
            else {}
        )
        system_prompt = generic_agent_system_prompt(self.profile)
        tool_schema = [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema,
            }
            for tool in generic_tool_definitions()
        ]
        return {
            "workspace_contract": "generic_agent_v1",
            "task_id": self.task.spec.task_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "profile": self.profile,
            "matter_mode": "read_only_copy",
            "scratch_mode": "read_write",
            "output_mode": "read_write_free_artifacts",
            "private_envelope_mounted": False,
            "shell_available": True,
            "workspace_network_available": False,
            "sandbox_backend": self.sandbox_backend,
            "tool_allowlist": list(GENERIC_AGENT_TOOLS),
            "native_tool_calling": True,
            "stop_policy": "model_emits_no_tool_calls",
            "agent_reasoning_effort": os.environ.get(
                "AGENT_REASONING_EFFORT", AGENT_REASONING_EFFORT
            ),
            "agent_max_output_tokens": int(
                os.environ.get("MODEL_MAX_TOKENS") or AGENT_MAX_OUTPUT_TOKENS
            ),
            "system_prompt_sha256": hashlib.sha256(system_prompt.encode()).hexdigest(),
            "tool_schema_sha256": hashlib.sha256(
                json.dumps(
                    tool_schema,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest(),
            "user_message_sha256": _sha256_file(
                self.task.directory / "public/01_task.md"
            ),
            "public_inputs": inputs,
            "skills": skills,
            "skills_manifest_sha256": (
                hashlib.sha256(
                    json.dumps(
                        skills,
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode()
                ).hexdigest()
                if skills
                else None
            ),
            "evaluation_separated": True,
        }

    def _resolve(self, value: str, *, writable: bool = False) -> Path:
        normalized = value.replace("\\", "/").strip()
        if normalized.startswith("/workspace/"):
            normalized = normalized[len("/workspace/") :]
        elif normalized == "/workspace":
            normalized = "."
        elif normalized.startswith("/"):
            normalized = normalized[1:]
        pure = PurePosixPath(normalized or ".")
        if ".." in pure.parts:
            raise WorkspaceError(f"percorso non sicuro: {value!r}")
        path = (self.root / pure.as_posix()).resolve()
        if not path.is_relative_to(self.root.resolve()):
            raise WorkspaceError(f"percorso fuori workspace: {value!r}")
        if writable and not (
            path.is_relative_to(self.scratch.resolve())
            or path.is_relative_to(self.output.resolve())
        ):
            raise WorkspaceError("scrittura consentita soltanto in /scratch e /output")
        return path

    def _display_path(self, path: Path) -> str:
        return "/" + path.relative_to(self.root).as_posix()

    def execute(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
        started = time.perf_counter()
        sanitized = dict(arguments)
        if "content" in sanitized:
            content = str(sanitized.pop("content"))
            sanitized["content_chars"] = len(content)
            sanitized["content_sha256"] = hashlib.sha256(content.encode()).hexdigest()
        if "new_text" in sanitized:
            value = str(sanitized.pop("new_text"))
            sanitized["new_text_chars"] = len(value)
        event: dict[str, Any] = {
            "sequence": len(self.trace) + 1,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tool": tool,
            "arguments": sanitized,
        }
        try:
            handlers = {
                "bash": self._bash,
                "read": self._read,
                "write": self._write,
                "edit": self._edit,
                "glob": self._glob,
                "grep": self._grep,
                "docx_redline": self._docx_redline,
            }
            if tool not in handlers:
                raise WorkspaceError(f"tool non disponibile: {tool}")
            result = handlers[tool](arguments)
            encoded = json.dumps(result, ensure_ascii=False, sort_keys=True)
            event.update(
                {
                    "status": "ok",
                    "result_chars": len(encoded),
                    "result_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                }
            )
            return result
        except Exception as exc:
            event.update({"status": "error", "error": str(exc)})
            raise
        finally:
            event["latency_ms"] = int(round((time.perf_counter() - started) * 1000))
            self.trace.append(event)

    def _read(self, arguments: dict[str, Any]) -> dict[str, Any]:
        path = self._resolve(str(arguments.get("path") or ""))
        if not path.is_file():
            raise WorkspaceError(f"file non trovato: {arguments.get('path')!r}")
        offset = int(arguments.get("offset") or 1)
        limit = min(int(arguments.get("limit") or 500), 5000)
        if offset < 1 or limit < 1:
            raise WorkspaceError("offset e limit devono essere positivi")
        extracted_from = None
        if path.suffix.casefold() in READABLE_DOCUMENT_SUFFIXES:
            text = _document_text(path)
            extracted_from = path.suffix.casefold().lstrip(".")
        else:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                raise WorkspaceError(
                    "read supporta testo UTF-8 e documenti PDF, DOCX, XLSX, EML; "
                    "usa bash e un programma adatto per gli altri file binari"
                ) from exc
        lines = text.splitlines()
        selected = lines[offset - 1 : offset - 1 + limit]
        content = "\n".join(
            f"{number}: {line}"
            for number, line in enumerate(selected, start=offset)
        )
        return {
            "path": self._display_path(path),
            "offset": offset,
            "lines": len(selected),
            "total_lines": len(lines),
            "content": content[:MAX_TOOL_OUTPUT_CHARS],
            "truncated": len(content) > MAX_TOOL_OUTPUT_CHARS,
            **({"extracted_from": extracted_from} if extracted_from else {}),
        }

    def _docx_redline(self, arguments: dict[str, Any]) -> dict[str, Any]:
        from .docx_redline import RedlineError, apply_redline

        source = self._resolve(str(arguments.get("source") or ""))
        if not source.is_file() or source.suffix.casefold() != ".docx":
            raise WorkspaceError(f"source deve essere un file .docx esistente: {arguments.get('source')!r}")
        destination = self._resolve(str(arguments.get("output") or ""), writable=True)
        if destination.suffix.casefold() != ".docx":
            raise WorkspaceError("output deve avere estensione .docx")
        try:
            result = apply_redline(
                source,
                destination,
                list(arguments.get("edits") or []),
                author=str(arguments.get("author") or ""),
            )
        except RedlineError as exc:
            raise WorkspaceError(str(exc)) from exc
        return {
            "source": self._display_path(source),
            "output": self._display_path(destination) if result["written"] else None,
            **result,
        }

    def _write(self, arguments: dict[str, Any]) -> dict[str, Any]:
        path = self._resolve(str(arguments.get("path") or ""), writable=True)
        content = str(arguments.get("content") or "")
        if len(content) > MAX_TEXT_WRITE_CHARS:
            raise WorkspaceError("contenuto write oltre il limite di sicurezza")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return {"path": self._display_path(path), "bytes": path.stat().st_size}

    def _edit(self, arguments: dict[str, Any]) -> dict[str, Any]:
        path = self._resolve(str(arguments.get("path") or ""), writable=True)
        if not path.is_file():
            raise WorkspaceError(f"file non trovato: {arguments.get('path')!r}")
        old = str(arguments.get("old_text") or "")
        new = str(arguments.get("new_text") or "")
        if not old:
            raise WorkspaceError("old_text non può essere vuoto")
        content = path.read_text(encoding="utf-8")
        count = content.count(old)
        if count == 0:
            raise WorkspaceError("old_text non trovato")
        replace_all = bool(arguments.get("replace_all", False))
        if count > 1 and not replace_all:
            raise WorkspaceError("old_text non univoco; usa replace_all=true")
        updated = content.replace(old, new, -1 if replace_all else 1)
        if len(updated) > MAX_TEXT_WRITE_CHARS:
            raise WorkspaceError("file risultante oltre il limite di sicurezza")
        path.write_text(updated, encoding="utf-8")
        return {
            "path": self._display_path(path),
            "replacements": count if replace_all else 1,
            "bytes": path.stat().st_size,
        }

    def _glob(self, arguments: dict[str, Any]) -> dict[str, Any]:
        pattern = str(arguments.get("pattern") or "")
        if not pattern or ".." in PurePosixPath(pattern).parts:
            raise WorkspaceError("pattern glob non sicuro o vuoto")
        base = self._resolve(str(arguments.get("path") or "/workspace"))
        if not base.is_dir():
            raise WorkspaceError("glob.path deve essere una directory")
        matches = sorted(
            self._display_path(path)
            for path in base.glob(pattern)
            if path.is_file() and path.resolve().is_relative_to(self.root.resolve())
        )
        return {"matches": matches[:5000], "truncated": len(matches) > 5000}

    def _grep(self, arguments: dict[str, Any]) -> dict[str, Any]:
        pattern = str(arguments.get("pattern") or "")
        if not pattern:
            raise WorkspaceError("pattern grep vuoto")
        flags = 0 if bool(arguments.get("case_sensitive", True)) else re.IGNORECASE
        try:
            expression = re.compile(pattern, flags)
        except re.error as exc:
            raise WorkspaceError(f"regex non valida: {exc}") from exc
        base = self._resolve(str(arguments.get("path") or "/workspace"))
        glob_pattern = str(arguments.get("glob") or "*")
        maximum = min(int(arguments.get("max_results") or 200), 1000)
        paths = [base] if base.is_file() else sorted(base.rglob("*"))
        matches: list[dict[str, Any]] = []
        for path in paths:
            if not path.is_file() or not fnmatch.fnmatch(path.name, glob_pattern):
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (UnicodeDecodeError, OSError):
                continue
            for line_number, line in enumerate(lines, start=1):
                if expression.search(line):
                    matches.append(
                        {
                            "path": self._display_path(path),
                            "line": line_number,
                            "text": line[:2000],
                        }
                    )
                    if len(matches) >= maximum:
                        return {"matches": matches, "truncated": True}
        return {"matches": matches, "truncated": False}

    def _sandbox_profile(self) -> str:
        read_roots = {
            "/System",
            "/usr",
            "/bin",
            "/sbin",
            "/dev",
            str(self.root),
            str(Path(sys.executable).resolve().parent.parent),
        }
        for key in ("stdlib", "platstdlib", "purelib", "platlib"):
            value = sysconfig.get_path(key)
            if value:
                read_roots.add(str(Path(value).resolve()))
        rules = "\n".join(
            "\n".join(
                [
                    f'(allow file-read* (subpath {json.dumps(path)}))',
                    "(allow file-read-metadata file-test-existence "
                    f"(path-ancestors {json.dumps(path)}))",
                ]
            )
            for path in sorted(read_roots)
        )
        return "\n".join(
            [
                "(version 1)",
                "(deny default)",
                '(import "system.sb")',
                "(allow process-exec)",
                "(allow process-fork)",
                "(allow signal (target self))",
                "(allow sysctl-read)",
                "(allow file-ioctl)",
                rules,
                f'(allow file-write* (subpath {json.dumps(str(self.scratch))}))',
                f'(allow file-write* (subpath {json.dumps(str(self.output))}))',
                "(deny network*)",
            ]
        )

    def _bash(self, arguments: dict[str, Any]) -> dict[str, Any]:
        self.require_safe_bash()
        command = str(arguments.get("command") or "")
        if not command:
            raise WorkspaceError("bash.command vuoto")
        timeout = min(max(int(arguments.get("timeout_seconds") or 30), 1), 120)
        profile_path = self.root / ".sandbox.sb"
        profile_path.write_text(self._sandbox_profile(), encoding="utf-8")
        environment = self._bash_environment()
        try:
            completed = subprocess.run(
                [
                    shutil.which("sandbox-exec") or "/usr/bin/sandbox-exec",
                    "-f",
                    str(profile_path),
                    "/bin/bash",
                    "--noprofile",
                    "--norc",
                    "-c",
                    command,
                ],
                cwd=self.root,
                env=environment,
                text=True,
                capture_output=True,
                stdin=subprocess.DEVNULL,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise WorkspaceError(f"bash timeout dopo {timeout} secondi") from exc
        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
        total = len(stdout) + len(stderr)
        return {
            "exit_code": completed.returncode,
            "stdout": stdout[:MAX_TOOL_OUTPUT_CHARS],
            "stderr": stderr[:MAX_TOOL_OUTPUT_CHARS],
            "truncated": total > MAX_TOOL_OUTPUT_CHARS,
        }

    def artifacts(self) -> list[WorkflowArtifact]:
        candidates = sorted(self.output.rglob("*"))
        symlinks = [path for path in candidates if path.is_symlink()]
        if symlinks:
            raise WorkspaceError(
                "symlink non ammessi in output/: "
                + ", ".join(self._display_path(path) for path in symlinks[:20])
            )
        paths = [
            path
            for path in candidates
            if path.is_file()
            and path.resolve().is_relative_to(self.output.resolve())
        ]
        artifacts: list[WorkflowArtifact] = []
        for path in paths:
            if path.stat().st_size > MAX_ARTIFACT_BYTES:
                raise WorkspaceError(f"artifact oltre 100 MB: {self._display_path(path)}")
            relative = path.relative_to(self.output).as_posix()
            raw = path.read_bytes()
            suffix = path.suffix.casefold()
            media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            if suffix in {".md", ".txt", ".csv", ".json", ".html", ".xml"}:
                content = path.read_text(encoding="utf-8")
                binary = False
            elif suffix in {".docx", ".pdf"}:
                content = _read_artifact(path)
                binary = True
            elif suffix == ".xlsx":
                from .workspace import _xlsx_pages

                content = "\n\n".join(_xlsx_pages(path))
                binary = True
            elif suffix == ".pptx":
                content = _pptx_text(path)
                binary = True
            else:
                try:
                    content = raw.decode("utf-8")
                    media_type = "text/plain"
                    binary = False
                except UnicodeDecodeError:
                    content = (
                        f"[binary artifact: {relative}; media_type={media_type}; "
                        f"bytes={len(raw)}; sha256={hashlib.sha256(raw).hexdigest()}]"
                    )
                    binary = True
            artifacts.append(
                WorkflowArtifact(
                    path=relative,
                    content=content,
                    media_type=media_type,
                    binary_base64=base64.b64encode(raw).decode("ascii") if binary else None,
                    sha256=hashlib.sha256(raw).hexdigest(),
                )
            )
        return artifacts


# Un turno chiuso per limite di lunghezza non e' una scelta del modello di fermarsi.
TRUNCATION_STOP_REASONS = frozenset({"length", "max_tokens", "incomplete"})
READABLE_DOCUMENT_SUFFIXES = frozenset({".pdf", ".docx", ".xlsx", ".eml"})


def _document_text(path: Path) -> str:
    """Extract plain text from a document the model must be able to read.

    Extraction runs in the harness on the read-only copy, so the sandbox
    stays unchanged; it reuses the extractors already used for submissions.
    """
    suffix = path.suffix.casefold()
    try:
        if suffix in {".pdf", ".docx"}:
            return _read_artifact(path)
        if suffix == ".xlsx":
            from .workspace import _xlsx_pages

            return "\n\n".join(_xlsx_pages(path))
        if suffix == ".eml":
            return _eml_text(path)
    except WorkspaceError:
        raise
    except Exception as exc:
        raise WorkspaceError(
            f"impossibile estrarre il testo da {path.name}: {exc}"
        ) from exc
    raise WorkspaceError(f"formato documento non supportato: {path.name}")


def _eml_text(path: Path) -> str:
    """Headers and decoded text parts of an email; attachments are listed."""
    from email import policy
    from email.parser import BytesParser

    message = BytesParser(policy=policy.default).parse(path.open("rb"))
    lines = [
        f"{name}: {message[name]}"
        for name in ("From", "To", "Cc", "Date", "Subject")
        if message[name]
    ]
    bodies: list[str] = []
    attachments: list[str] = []
    for part in message.walk():
        if part.is_multipart():
            continue
        filename = part.get_filename()
        if filename:
            attachments.append(filename)
        elif part.get_content_type() == "text/plain":
            bodies.append(part.get_content().strip())
    if attachments:
        lines.append("Allegati: " + ", ".join(attachments))
    return "\n".join(lines) + "\n\n" + "\n\n".join(bodies)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _pptx_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as archive:
            names = sorted(
                (
                    name
                    for name in archive.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
                ),
                key=lambda name: int(re.search(r"\d+", Path(name).stem).group()),
            )
            slides = []
            for index, name in enumerate(names, start=1):
                root = ElementTree.fromstring(archive.read(name))
                text = "\n".join(
                    node.text or ""
                    for node in root.iter()
                    if node.tag.rsplit("}", 1)[-1] == "t" and (node.text or "").strip()
                )
                slides.append(f"[SLIDE {index}]\n{text}")
    except (zipfile.BadZipFile, ElementTree.ParseError) as exc:
        raise WorkspaceError(f"PPTX illeggibile: {path.name}") from exc
    content = "\n\n".join(slides).strip()
    if not content:
        raise WorkspaceError(f"PPTX senza testo estraibile: {path.name}")
    return content


def _transcript_assistant(turn: Any) -> dict[str, Any]:
    return {
        "role": "assistant",
        "content": turn.text,
        "tool_calls": [
            {"id": call.id, "name": call.name, "arguments": call.arguments}
            for call in turn.tool_calls
        ],
    }


def generate_generic_agent_submission(
    task: LoadedWorkflowTask,
    *,
    model: str,
    gateway: NativeToolGateway | None = None,
    max_turns: int = 150,
    timeout_seconds: int = 3600,
    profile: str = "bare",
    max_cost_usd: float | None = None,
) -> WorkflowSubmission:
    """Run the minimal shuttle loop until the model emits no tool calls."""
    if "generic_agent" not in task.spec.supported_execution_modes:
        raise WorkspaceError(f"{task.spec.task_id} non supporta generic_agent")
    if max_turns < 1:
        raise WorkspaceError("max_turns deve essere positivo")
    if timeout_seconds < 1:
        raise WorkspaceError("timeout_seconds deve essere positivo")
    if max_cost_usd is not None and max_cost_usd <= 0:
        raise WorkspaceError("max_cost_usd deve essere positivo")
    workspace = GenericAgentWorkspace(task, profile=profile)
    messages: list[dict[str, Any]] = [
        {
            "role": "user",
            "content": (task.directory / "public/01_task.md").read_text(encoding="utf-8"),
        }
    ]
    metrics: list[dict[str, Any]] = []
    raw_response: str | None = None
    started = time.monotonic()
    active_gateway = gateway or default_native_tool_gateway()
    external_stop: tuple[str, str] = ("turn_limit", "")

    def _completed(
        termination_reason: str,
        turns: int,
        artifacts: list[WorkflowArtifact],
        raw_text: str | None,
    ) -> WorkflowSubmission:
        manifest = {
            **workspace.manifest,
            "run_status": "completed",
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "turns": turns,
            "tool_events": len(workspace.trace),
            "document_coverage": generic_document_coverage(
                (workspace.manifest.get("public_inputs") or {}).keys(), workspace.trace
            ),
            "max_turns": max_turns,
            "timeout_seconds": timeout_seconds,
            "max_cost_usd": max_cost_usd,
            "termination_reason": termination_reason,
            "external_stop": termination_reason.endswith("_with_artifacts"),
            "elapsed_seconds": round(time.monotonic() - started, 1),
            "artifact_count": len(artifacts),
        }
        return WorkflowSubmission(
            task_id=task.spec.task_id,
            model=model,
            source="live",
            execution_mode="generic_agent",
            artifacts=artifacts,
            raw_response=raw_text,
            model_call_metrics=_aggregate_metrics(metrics, model),
            agent_transcript=list(messages),
            tool_trace=list(workspace.trace),
            decision_log=[],
            workspace_manifest=manifest,
        )

    try:
        workspace.require_safe_bash()
        for turn_number in range(1, max_turns + 1):
            elapsed = time.monotonic() - started
            if elapsed > timeout_seconds:
                external_stop = ("timeout", f"timeout generic_agent dopo {timeout_seconds} secondi")
                break
            turn = active_gateway.complete(
                model,
                system_prompt=generic_agent_system_prompt(profile),
                messages=messages,
                tools=generic_tool_definitions(),
                timeout_seconds=max(1.0, timeout_seconds - elapsed),
            )
            raw_response = turn.text or raw_response
            metrics.append(dict(turn.metrics or {}))
            if max_cost_usd is not None and not isinstance(
                (turn.metrics or {}).get("estimated_cost_usd"),
                (int, float),
            ):
                raise WorkspaceError(
                    "cost guard generic_agent non applicabile: "
                    "prezzo o usage del modello non disponibile"
                )
            accumulated_cost = sum(
                float(item["estimated_cost_usd"])
                for item in metrics
                if isinstance(item.get("estimated_cost_usd"), (int, float))
            )
            messages.append(_transcript_assistant(turn))
            if max_cost_usd is not None and accumulated_cost > max_cost_usd:
                external_stop = (
                    "cost_limit",
                    f"cost guard generic_agent superato: "
                    f"${accumulated_cost:.6f} > ${max_cost_usd:.6f}",
                )
                break
            if not turn.tool_calls:
                truncated = str(turn.stop_reason or "").casefold() in TRUNCATION_STOP_REASONS
                artifacts = workspace.artifacts()
                if not artifacts:
                    if truncated:
                        last = turn.metrics or {}
                        raise WorkspaceError(
                            "risposta del modello troncata al limite di token di output "
                            f"(stop_reason={turn.stop_reason}, output_tokens="
                            f"{last.get('output_tokens')}, reasoning_tokens="
                            f"{last.get('reasoning_tokens')}) prima di creare artifact in "
                            "/output: aumentare MODEL_MAX_TOKENS"
                        )
                    raise WorkspaceError(
                        "il modello ha terminato senza creare artifact in /output"
                    )
                return _completed(
                    "model_output_truncated" if truncated else "model_emitted_no_tool_calls",
                    turn_number,
                    artifacts,
                    turn.text,
                )
            for call in turn.tool_calls:
                try:
                    observation = workspace.execute(call.name, call.arguments)
                    payload = {"ok": True, "result": observation}
                except Exception as exc:
                    payload = {"ok": False, "error": str(exc)}
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "name": call.name,
                        "content": json.dumps(payload, ensure_ascii=False),
                    }
                )
        else:
            external_stop = ("turn_limit", f"limite esterno raggiunto dopo {max_turns} turni")
        # Freno di emergenza (turni, tempo o spesa). Se il modello ha gia'
        # consegnato un deliverable in /output lo si valuta, segnalando la
        # chiusura esterna; altrimenti la run fallisce come prima.
        kind, message = external_stop
        artifacts = workspace.artifacts()
        if artifacts:
            return _completed(f"{kind}_with_artifacts", len(metrics), artifacts, raw_response)
        raise WorkspaceError(message)
    except Exception as exc:
        failure_manifest = {
            **workspace.manifest,
            "run_status": "failed",
            "failed_at": datetime.now(timezone.utc).isoformat(),
            "termination_reason": str(exc),
            "error_type": type(exc).__name__,
            "turns": len(metrics),
            "tool_events": len(workspace.trace),
            "document_coverage": generic_document_coverage(
                (workspace.manifest.get("public_inputs") or {}).keys(), workspace.trace
            ),
            "max_turns": max_turns,
            "timeout_seconds": timeout_seconds,
            "max_cost_usd": max_cost_usd,
        }
        failure = WorkspaceRunFailure(
            str(exc),
            task_id=task.spec.task_id,
            model=model,
            error_type=type(exc).__name__,
            artifacts=workspace.artifacts(),
            tool_trace=list(workspace.trace),
            decision_log=[],
            workspace_manifest=failure_manifest,
            model_call_metrics=_aggregate_metrics(metrics, model),
            raw_response=raw_response,
            agent_transcript=list(messages),
        )
        failure.execution_mode = "generic_agent"
        raise failure from exc
    finally:
        workspace.close()


def validate_generic_agent_runtime(
    task: LoadedWorkflowTask,
    *,
    profile: str = "bare",
) -> dict[str, Any]:
    """Verify the OS sandbox and selected skill profile before any API call."""
    workspace = GenericAgentWorkspace(task, profile=profile)
    try:
        workspace.require_safe_bash()
        return {
            "task_id": task.spec.task_id,
            "execution_mode": "generic_agent",
            "profile": profile,
            "sandbox_backend": workspace.sandbox_backend,
            "tool_allowlist": list(GENERIC_AGENT_TOOLS),
        }
    finally:
        workspace.close()
