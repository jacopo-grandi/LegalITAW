"""Bridge from workflow rubrics to the existing binary three-judge engine."""

from __future__ import annotations

import base64
import logging
import os
import re
from typing import Any

from legalitaw.agentic.bundle import build_public_bundle
from legalitaw.agentic.native_artifacts import docx_features
from legalitaw.agentic.models import (
    LoadedWorkflowTask,
    WorkflowArtifact,
    WorkflowCriterion,
    WorkflowSubmission,
)
from legalitaw.agentic.submissions import submission_text, validate_submission
from legalitaw.modeling.usage import with_model_call_metrics
from legalitaw.progress import progress_heartbeat
from legalitaw.schemas import (
    Criterion,
    CriterionResult,
    ResponseEvidence,
    TaskScore,
    WorkflowJudgeTask,
)

from .scoring import score_task


log = logging.getLogger(__name__)



_EVIDENCE_CHARACTER_EQUIVALENTS = str.maketrans(
    {
        "’": "'",
        "‘": "'",
        "ʼ": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "−": "-",
    }
)


def _normalize_with_offsets(value: str) -> tuple[str, list[int]]:
    """Normalize harmless typography and whitespace, retaining source offsets."""
    normalized: list[str] = []
    offsets: list[int] = []
    pending_space = False
    pending_offset = 0
    for index, character in enumerate(value):
        if character.isspace():
            if normalized and not pending_space:
                pending_space = True
                pending_offset = index
            continue
        if pending_space:
            normalized.append(" ")
            offsets.append(pending_offset)
            pending_space = False
        normalized.append(character.translate(_EVIDENCE_CHARACTER_EQUIVALENTS))
        offsets.append(index)
    return "".join(normalized), offsets


def _find_quote_span(content: str, quote: str) -> tuple[int, int] | None:
    exact = content.find(quote)
    if exact >= 0:
        return exact, exact + len(quote)

    normalized_content, offsets = _normalize_with_offsets(content)
    normalized_quote, _ = _normalize_with_offsets(quote)
    if not normalized_quote:
        return None
    start = normalized_content.find(normalized_quote)
    if start < 0:
        return None
    end = start + len(normalized_quote)
    return offsets[start], offsets[end - 1] + 1


def _locate_response_quotes(
    submission: WorkflowSubmission,
    quotes: list[str],
) -> tuple[list[ResponseEvidence], list[str]]:
    located: list[ResponseEvidence] = []
    invalid: list[str] = []
    seen: set[tuple[str, int, int]] = set()
    for raw_quote in quotes:
        quote = raw_quote.strip()
        if not quote:
            continue
        match: tuple[WorkflowArtifact, int, int] | None = None
        for artifact in submission.artifacts:
            span = _find_quote_span(artifact.content, quote)
            if span is not None:
                match = artifact, span[0], span[1]
                break
        if match is None:
            invalid.append(quote)
            continue
        artifact, start, end = match
        key = (artifact.path, start, end)
        if key in seen:
            continue
        seen.add(key)
        exact_quote = artifact.content[start:end]
        located.append(
            ResponseEvidence(
                artifact=artifact.path,
                quote=exact_quote,
                char_start=start,
                char_end=end,
                line_start=artifact.content.count("\n", 0, start) + 1,
                line_end=artifact.content.count("\n", 0, end) + 1,
            )
        )
    return located, invalid


def _evidence_within_scope(
    submission: WorkflowSubmission,
    criterion: WorkflowCriterion,
    evidence: list[ResponseEvidence],
) -> tuple[list[ResponseEvidence], list[str]]:
    if criterion.evaluation_scope != "section":
        return evidence, []
    assert criterion.scope_locator is not None
    artifacts = {item.path: item.content for item in submission.artifacts}
    accepted: list[ResponseEvidence] = []
    rejected: list[str] = []
    for item in evidence:
        content = artifacts.get(item.artifact)
        span = _section_span(content, criterion.scope_locator) if content is not None else None
        if span is not None and span[0] <= item.char_start and item.char_end <= span[1]:
            accepted.append(item)
        else:
            rejected.append(item.quote)
    return accepted, rejected


def _matching_lines(content: str, pattern: str) -> list[str]:
    return [
        line.strip()
        for line in content.splitlines()
        if re.search(pattern, line, flags=re.IGNORECASE)
    ]


_D_LGS_REFERENCE_RE = re.compile(
    r"\bartt?\.?\s+(?P<articles>\d+(?:\s*(?:,|e)\s*\d+)*)\s+"
    r"(?:del\s+)?D\.?\s*Lgs\.?\s*(?:n\.?\s*)?(?P<number>\d+)\s*/\s*(?P<year>\d{4})",
    flags=re.IGNORECASE,
)
_D_LGS_REVERSE_RE = re.compile(
    r"\bD\.?\s*Lgs\.?\s*(?:n\.?\s*)?(?P<number>\d+)\s*/\s*(?P<year>\d{4})"
    r"\s*,?\s*(?:artt?\.?\s+)(?P<articles>\d+(?:\s*(?:,|e)\s*\d+)*)",
    flags=re.IGNORECASE,
)
_D_LGS_INSTRUMENT_RE = re.compile(
    r"\bD\.?\s*Lgs\.?\s*(?:n\.?\s*)?(?P<number>\d+)\s*/\s*(?P<year>\d{4})",
    flags=re.IGNORECASE,
)
_CODE_REFERENCE_RE = re.compile(
    r"\bartt?\.?\s+(?P<articles>\d+(?:\s*(?:,|e)\s*\d+)*)\s+"
    r"(?P<code>c\.?\s*c\.?|c\.?\s*p\.?\s*c\.?|c\.?\s*p\.?)"
    r"(?=$|\s|[,;)])",
    flags=re.IGNORECASE,
)
_OTHER_NORMATIVE_INSTRUMENT_RE = re.compile(
    r"\b(?:D\.?\s*P\.?\s*R\.?|D\.?\s*L\.?|Legge|L\.)\s*"
    r"(?:n\.?\s*)?\d+(?:\s*/\s*\d{2,4})?"
    r"|\b(?:Regolamento|Reg\.)\s*\((?:UE|CE)\)\s*(?:n\.?\s*)?\d+(?:\s*/\s*\d{2,4})?",
    flags=re.IGNORECASE,
)


def _line_at(content: str, start: int, end: int) -> str:
    line_start = content.rfind("\n", 0, start) + 1
    next_newline = content.find("\n", end)
    line_end = len(content) if next_newline < 0 else next_newline
    return content[line_start:line_end].strip()


def _normative_references(content: str) -> list[tuple[str, str]]:
    """Extract deterministic normative citations without treating contract articles as law."""
    references: list[tuple[str, str]] = []
    covered_d_lgs_spans: list[tuple[int, int]] = []
    for pattern in (_D_LGS_REFERENCE_RE, _D_LGS_REVERSE_RE):
        for match in pattern.finditer(content):
            covered_d_lgs_spans.append(match.span())
            line = _line_at(content, match.start(), match.end())
            for article in re.findall(r"\d+", match.group("articles")):
                references.append(
                    (
                        f"d.lgs.{int(match.group('number'))}/{match.group('year')}#{int(article)}",
                        line,
                    )
                )

    for match in _D_LGS_INSTRUMENT_RE.finditer(content):
        if any(start <= match.start() and match.end() <= end for start, end in covered_d_lgs_spans):
            continue
        references.append(
            (
                f"d.lgs.{int(match.group('number'))}/{match.group('year')}#*",
                _line_at(content, match.start(), match.end()),
            )
        )

    for match in _CODE_REFERENCE_RE.finditer(content):
        code = re.sub(r"\s+", "", match.group("code").casefold())
        line = _line_at(content, match.start(), match.end())
        for article in re.findall(r"\d+", match.group("articles")):
            references.append((f"{code}#{int(article)}", line))

    for match in _OTHER_NORMATIVE_INSTRUMENT_RE.finditer(content):
        normalized = re.sub(r"\s+", "", match.group(0).casefold())
        normalized = re.sub(r"^reg\.\(", "regolamento(", normalized)
        normalized = re.sub(r"^legge", "l.", normalized)
        references.append((normalized, _line_at(content, match.start(), match.end())))

    unique: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in references:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def _artifact_check_evidence(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
    check_id: str,
    *,
    passed: bool,
) -> tuple[list[str], bool]:
    """Return exact response excerpts, or declare a whole-artifact check."""
    check = next(item for item in task.spec.artifact_checks if item.id == check_id)
    content = _artifact_content(submission, check.artifact)
    if content is None:
        return [], True
    if check.type == "required_markdown_headings":
        quotes = _matching_lines(content, r"^\s{0,3}#{1,6}\s+")
        return quotes, not passed
    if check.type == "ordered_markdown_blocks":
        assert check.block_heading_pattern is not None
        return _matching_lines(content, check.block_heading_pattern), not passed
    if check.type == "repeated_block_required_fields":
        labels = "|".join(re.escape(item) for item in check.required_fields)
        quotes = _matching_lines(content, rf"^\s*[-*+]\s+(?:\*\*)?(?:{labels})")
        if not passed:
            assert check.block_heading_pattern is not None
            quotes.extend(_matching_lines(content, check.block_heading_pattern))
        return quotes, not passed and not quotes
    if check.type in {"labeled_value_allowlist", "labeled_source_locator"}:
        assert check.label is not None
        quotes = _matching_lines(
            content,
            rf"^\s*[-*+]\s+(?:\*\*)?{re.escape(check.label)}",
        )
        return quotes, not passed and not quotes
    if check.type == "normative_reference_allowlist":
        allowed = {item.casefold() for item in check.allowed_values}
        invalid_lines = [
            line for key, line in _normative_references(content) if key not in allowed
        ]
        return list(dict.fromkeys(invalid_lines)), passed
    if check.type == "required_regex":
        quotes: list[str] = []
        for pattern in check.patterns:
            match = re.search(pattern, content, flags=re.IGNORECASE | re.MULTILINE)
            if match is not None:
                quotes.append(match.group(0))
        return quotes, not passed
    if check.type == "docx_features":
        return _matching_lines(content, r"\[\[(?:INS|DEL|NOTE):"), not passed
    if check.section:
        quotes = _matching_lines(
            content,
            rf"^\s{{0,3}}#{{1,6}}\s+{re.escape(check.section)}\s*$",
        )
        return quotes, True
    return [], True


def _uses_prompt_only_free_artifacts(task: LoadedWorkflowTask) -> bool:
    return (
        getattr(task.spec, "submission_contract", None)
        == "prompt_only_free_artifacts_v1"
    )


def judge_task(task: LoadedWorkflowTask) -> WorkflowJudgeTask:
    default_deliverables = task.spec.deliverable_names
    prompt_only_free_artifacts = _uses_prompt_only_free_artifacts(task)
    criteria = [
        Criterion(
            id=item.id,
            title=item.normalized_title,
            match_criteria=item.normalized_match_criteria,
            deliverables=item.deliverables or default_deliverables,
            scoring_type="required",
            category=item.category,
            criterion_type=item.criterion_type,
            criterion_logic=item.criterion_logic,
            verification_class=item.verification_class,
            evaluation_scope=item.evaluation_scope,
            scope_locator=item.scope_locator,
        )
        for item in task.rubric.criteria
        if prompt_only_free_artifacts or item.evaluation_mode == "judge"
    ]
    return WorkflowJudgeTask(
        task_id=task.spec.task_id,
        query=_judge_context(task),
        criteria=criteria,
    )


JUDGE_CONTEXT_ENV = "LEGALITA_JUDGE_CONTEXT"
JUDGE_CONTEXT_MODES = ("full", "compact")


def judge_context_mode() -> str:
    """Judge context policy: ``compact`` (default) or ``full`` (public bundle).

    ``compact`` sends only the public markdown inputs (assignment, reference
    pack, legal sources), never the documents: it keeps judge requests small
    enough for providers with a hard request limit and costs about half as much.
    """
    mode = os.environ.get(JUDGE_CONTEXT_ENV, "compact").strip().casefold() or "compact"
    if mode not in JUDGE_CONTEXT_MODES:
        raise ValueError(
            f"{JUDGE_CONTEXT_ENV}={mode!r} non valido: usare {', '.join(JUDGE_CONTEXT_MODES)}"
        )
    return mode


def _judge_context(task: LoadedWorkflowTask) -> str:
    """Use the assignment, not the whole data room, as repeated judge context.

    Each private criterion already states the gold proposition, pass/fail rule,
    and source anchor. Repeating all source documents for every criterion would
    add cost without changing the binary comparison and would conflate rubric
    scoring with a separate source-grounding audit.
    """
    if judge_context_mode() == "full" and not (
        "agentic_workspace" in task.spec.supported_execution_modes
        and "text_bundle" not in task.spec.supported_execution_modes
    ):
        context = build_public_bundle(task)
        if not _uses_prompt_only_free_artifacts(task):
            return context
        return context + "\n" + "\n".join(
            [
                "<evaluation_boundary>",
                "Il prompt e i documenti pubblici sono l'unica fonte dei requisiti ",
                "di output. Se il criterio legacy prescrive un nome di file, ",
                "un'estensione, un'intestazione, un'etichetta o una sintassi più ",
                "restrittivi del contratto pubblico, non penalizzare il mero ",
                "scostamento formale: valuta se la sostanza pubblicamente richiesta ",
                "è presente, corretta e utilizzabile.",
                "</evaluation_boundary>",
            ]
        )
    from legalitaw.agentic.workspace import public_envelope_paths

    public_context: list[str] = []
    # il giudice vede gli stessi file testuali della consegna che vede il modello (prompt, reference
    # pack, elenco delle fonti), non il template nascosto al modello
    for relative in public_envelope_paths(task):
        if not relative.endswith(".md") or relative.startswith("public/documents/"):
            continue
        content = (task.directory / relative).read_text(encoding="utf-8")
        public_context.extend(
            [
                f'<public_context path="{relative}">',
                content.strip(),
                "</public_context>",
            ]
        )
    public_contract_boundary = (
        [
            "Il prompt e i documenti pubblici sono l'unica fonte dei requisiti ",
            "di output. Se il criterio legacy prescrive un nome di file, ",
            "un'estensione, un'intestazione, un'etichetta o una sintassi più ",
            "restrittivi del contratto pubblico, non penalizzare il mero ",
            "scostamento formale: valuta se la sostanza pubblicamente richiesta ",
            "è presente, corretta e utilizzabile.",
        ]
        if _uses_prompt_only_free_artifacts(task)
        else []
    )
    return "\n".join(
        [
            f'<legalita_judge_context task_id="{task.spec.task_id}">',
            *public_context,
            "<evaluation_boundary>",
            "Valuta la risposta rispetto al singolo criterio gold fornito.",
            *public_contract_boundary,
            "La verifica indipendente delle fonti del fascicolo è un audit separato.",
            "</evaluation_boundary>",
            "</legalita_judge_context>",
        ]
    )


def _word_count(text: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÿ'’-]+\b", text, flags=re.UNICODE))


def _heading_name(line: str) -> str | None:
    match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
    return match.group(1).strip() if match else None


def _section_span(text: str, section: str) -> tuple[int, int] | None:
    lines = text.splitlines(keepends=True)
    wanted = section.strip().casefold()
    start_line: int | None = None
    for index, line in enumerate(lines):
        heading = _heading_name(line)
        if heading is not None and heading.casefold() == wanted:
            start_line = index + 1
            break
    if start_line is None:
        return None
    end_line = len(lines)
    for index in range(start_line, len(lines)):
        if _heading_name(lines[index]) is not None:
            end_line = index
            break
    start = sum(len(line) for line in lines[:start_line])
    end = sum(len(line) for line in lines[:end_line])
    return start, end


def _section_text(text: str, section: str) -> str | None:
    span = _section_span(text, section)
    if span is None:
        return None
    return text[span[0] : span[1]].strip()


def _artifact_for_declared_path(
    submission: WorkflowSubmission,
    path: str,
) -> WorkflowArtifact | None:
    """Resolve a private routing label without making it an ingestion contract."""
    exact = next(
        (artifact for artifact in submission.artifacts if artifact.path == path),
        None,
    )
    if exact is not None:
        return exact
    if len(submission.artifacts) == 1:
        return submission.artifacts[0]
    suffix = path.rsplit(".", 1)[-1].casefold() if "." in path else ""
    same_type = [
        artifact
        for artifact in submission.artifacts
        if artifact.path.casefold().endswith(f".{suffix}")
    ]
    return same_type[0] if len(same_type) == 1 else None


def _artifact_content(submission: WorkflowSubmission, path: str) -> str | None:
    artifact = _artifact_for_declared_path(submission, path)
    if artifact is not None:
        return artifact.content
    if not submission.artifacts:
        return None
    return "\n\n".join(
        f"## ARTIFACT: {item.path}\n\n{item.content}"
        for item in submission.artifacts
    )


def _artifact_binary(submission: WorkflowSubmission, path: str) -> bytes | None:
    artifact = _artifact_for_declared_path(submission, path)
    encoded = artifact.binary_base64 if artifact is not None else None
    return (
        base64.b64decode(encoded, validate=True)
        if encoded is not None
        else None
    )


def _markdown_blocks(text: str, pattern: str) -> list[tuple[int, str]]:
    matches = list(re.finditer(pattern, text, flags=re.MULTILINE | re.IGNORECASE))
    blocks: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        raw_number = match.groupdict().get("number")
        if raw_number is None:
            raise ValueError("block_heading_pattern deve esporre il gruppo 'number'")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((int(raw_number), text[match.start() : end]))
    return blocks


def _labeled_value(block: str, label: str) -> str | None:
    match = re.search(
        rf"(?im)^\s*[-*+]\s+(?:\*\*)?{re.escape(label)}(?:\*\*)?\s*:\s*(.+?)\s*$",
        block,
    )
    return match.group(1).strip() if match else None


def _run_artifact_check(task: LoadedWorkflowTask, submission: WorkflowSubmission, check_id: str) -> tuple[bool, str]:
    check = next(item for item in task.spec.artifact_checks if item.id == check_id)
    content = _artifact_content(submission, check.artifact)
    if content is None:
        return False, f"{check.id}: artifact {check.artifact} mancante"

    if check.type == "required_markdown_headings":
        present = {
            heading.casefold()
            for line in content.splitlines()
            if (heading := _heading_name(line)) is not None
        }
        missing = [item for item in check.headings if item.casefold() not in present]
        return (
            not missing,
            f"{check.id}: "
            + ("tutte le sezioni presenti" if not missing else f"sezioni mancanti {missing}"),
        )

    if check.type == "max_words":
        count = _word_count(content)
        assert check.value is not None
        return count <= check.value, f"{check.id}: parole={count}, massimo={check.value}"

    if check.type == "ordered_markdown_blocks":
        assert check.block_heading_pattern is not None and check.minimum is not None
        blocks = _markdown_blocks(content, check.block_heading_pattern)
        numbers = [number for number, _ in blocks]
        expected = list(range(1, len(numbers) + 1))
        passed = len(blocks) >= check.minimum and numbers == expected
        return (
            passed,
            f"{check.id}: blocchi={len(blocks)}, numerazione={numbers}",
        )

    if check.type == "repeated_block_required_fields":
        assert check.block_heading_pattern is not None
        blocks = _markdown_blocks(content, check.block_heading_pattern)
        missing = {
            number: [
                field
                for field in check.required_fields
                if not (_labeled_value(block, field) or "").strip()
            ]
            for number, block in blocks
        }
        missing = {number: fields for number, fields in missing.items() if fields}
        passed = bool(blocks) and not missing
        return passed, f"{check.id}: campi mancanti={missing or 'nessuno'}"

    if check.type == "labeled_value_allowlist":
        assert check.block_heading_pattern is not None and check.label is not None
        blocks = _markdown_blocks(content, check.block_heading_pattern)
        invalid: dict[int, str | None] = {}
        allowed = [value.casefold() for value in check.allowed_values]
        for number, block in blocks:
            value = _labeled_value(block, check.label)
            if value is None or not any(value.casefold().startswith(item) for item in allowed):
                invalid[number] = value
        passed = bool(blocks) and not invalid
        return passed, f"{check.id}: valori non ammessi={invalid or 'nessuno'}"

    if check.type == "labeled_source_locator":
        assert check.block_heading_pattern is not None and check.label is not None
        blocks = _markdown_blocks(content, check.block_heading_pattern)
        invalid: dict[int, str | None] = {}
        for number, block in blocks:
            value = _labeled_value(block, check.label)
            has_document = bool(
                value and re.search(r"\.(?:pdf|docx|xlsx|eml)\b", value, re.IGNORECASE)
            )
            has_locator = bool(
                value
                and re.search(
                    r"\b(?:art(?:icolo)?|clausola|pag(?:ina)?|voce|sezione|allegato|riga)\b|§",
                    value,
                    re.IGNORECASE,
                )
            )
            if not (has_document and has_locator):
                invalid[number] = value
        passed = bool(blocks) and not invalid
        return passed, f"{check.id}: fonti senza documento/locator={invalid or 'nessuna'}"

    if check.type == "normative_reference_allowlist":
        references = _normative_references(content)
        allowed = {item.casefold() for item in check.allowed_values}
        invalid = [key for key, _ in references if key not in allowed]
        passed = not invalid
        observed = [key for key, _ in references]
        return (
            passed,
            f"{check.id}: riferimenti={observed or 'nessuno'}; "
            f"fuori allowlist={invalid or 'nessuno'}",
        )

    if check.type == "required_regex":
        matched = [
            bool(re.search(pattern, content, flags=re.IGNORECASE | re.MULTILINE))
            for pattern in check.patterns
        ]
        missing = [
            pattern for pattern, found in zip(check.patterns, matched) if not found
        ]
        return (
            not missing,
            f"{check.id}: pattern mancanti={missing or 'nessuno'}",
        )

    if check.type == "docx_features":
        binary = _artifact_binary(submission, check.artifact)
        if binary is None:
            return False, f"{check.id}: artifact DOCX binario mancante"
        try:
            observed = docx_features(binary)
        except Exception as exc:
            return False, f"{check.id}: DOCX non valido: {exc}"
        feature_pass = {
            "valid_package": bool(observed["valid_package"]),
            "track_revisions": bool(observed["track_revisions_enabled"]),
            "insertions": int(observed["insertions"]) > 0,
            "deletions": int(observed["deletions"]) > 0,
            "comments": (
                int(observed["comments"]) > 0
                and observed["comments"] == observed["comment_range_starts"]
                and observed["comments"] == observed["comment_range_ends"]
                and observed["comments"] == observed["comment_references"]
            ),
            "comments_cover_changes": (
                int(observed["comments"])
                >= max(int(observed["insertions"]), int(observed["deletions"]))
            ),
            "comments_reference_norm": all(
                re.search(
                    r"\b(?:art\.?|articolo|regolamento|d\.?\s*lgs\.?)\b",
                    note,
                    flags=re.IGNORECASE,
                )
                for note in re.findall(
                    r"\[\[NOTE:\s*(.*?)\]\]",
                    content,
                    flags=re.IGNORECASE,
                )
            )
            and bool(re.search(r"\[\[NOTE:", content, flags=re.IGNORECASE)),
        }
        unknown = set(check.required_features) - set(feature_pass)
        if unknown:
            raise ValueError(
                f"{check.id}: feature DOCX sconosciute {sorted(unknown)}"
            )
        failed = [
            feature
            for feature in check.required_features
            if not feature_pass[feature]
        ]
        missing_patterns = [
            pattern
            for pattern in check.patterns
            if not re.search(
                pattern,
                content,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        ]
        return (
            not failed and not missing_patterns,
            f"{check.id}: feature={observed}; mancanti={failed or 'nessuna'}; "
            f"pattern mancanti={missing_patterns or 'nessuno'}",
        )

    assert check.section is not None
    section = _section_text(content, check.section)
    if section is None:
        return False, f"{check.id}: sezione {check.section!r} mancante"

    if check.type == "section_max_words":
        count = _word_count(section)
        assert check.value is not None
        return count <= check.value, f"{check.id}: parole={count}, massimo={check.value}"

    if check.type == "section_list_items_range":
        count = sum(
            1
            for line in section.splitlines()
            if re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", line)
        )
        assert check.minimum is not None and check.maximum is not None
        return (
            check.minimum <= count <= check.maximum,
            f"{check.id}: elementi={count}, intervallo={check.minimum}-{check.maximum}",
        )

    raise ValueError(f"artifact check non supportato: {check.type}")


def _deterministic_results(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
) -> tuple[list[CriterionResult], dict[str, list[str]]]:
    results: list[CriterionResult] = []
    diagnostics: dict[str, list[str]] = {}
    for criterion in task.rubric.criteria:
        if criterion.evaluation_mode != "deterministic":
            continue
        outcomes = [
            _run_artifact_check(task, submission, check_id)
            for check_id in criterion.deterministic_checks
        ]
        passed = all(outcome for outcome, _ in outcomes)
        messages = [message for _, message in outcomes]
        quotes: list[str] = []
        full_scope = False
        for check_id, (outcome, _) in zip(criterion.deterministic_checks, outcomes):
            check_quotes, check_full_scope = _artifact_check_evidence(
                task,
                submission,
                check_id,
                passed=outcome,
            )
            quotes.extend(check_quotes)
            full_scope = full_scope or check_full_scope
        response_evidence, invalid_quotes = _locate_response_quotes(submission, quotes)
        if response_evidence:
            evidence_status = "found"
            evidence_scope = None
        elif full_scope:
            evidence_status = (
                "global_scan"
                if criterion.evaluation_scope == "all_deliverables"
                else "not_found"
            )
            evidence_scope = criterion.normalized_evidence_scope
        elif invalid_quotes:
            evidence_status = "invalid"
            evidence_scope = None
        else:
            evidence_status = "unavailable"
            evidence_scope = None
        diagnostics[criterion.id] = messages
        results.append(
            CriterionResult(
                id=criterion.id,
                title=criterion.normalized_title,
                verdict="pass" if passed else "fail",
                reasoning="; ".join(messages),
                verification_class=criterion.verification_class,
                criterion_type=criterion.criterion_type,
                criterion_logic=criterion.criterion_logic,
                evaluation_scope=criterion.evaluation_scope,
                scope_locator=criterion.scope_locator,
                evidence_status=evidence_status,
                response_evidence=response_evidence,
                evidence_scope=evidence_scope,
                evidence_notes=[
                    f"Estratto deterministico non localizzato: {item[:160]}"
                    for item in invalid_quotes
                ],
                scoring_type=criterion.scoring_type,
                category=criterion.category,
                consensus_method="deterministic",
                supporting_judges=["deterministic"],
            )
        )
    return results, diagnostics


def _merge_deterministic_results(
    task: LoadedWorkflowTask,
    score: TaskScore,
    deterministic: list[CriterionResult],
    diagnostics: dict[str, list[str]],
) -> TaskScore:
    if not deterministic:
        return score
    by_id = {item.id: item for item in [*score.criteria_results, *deterministic]}
    ordered = [by_id[item.id] for item in task.rubric.criteria]
    required = [item for item in ordered if item.scoring_type == "required"]
    bonus = [item for item in ordered if item.scoring_type == "bonus"]
    n_required_unresolved = sum(item.verdict == "unresolved" for item in required)
    complete = n_required_unresolved == 0
    n_required_passed = sum(item.verdict == "pass" for item in required)
    n_passed = sum(item.verdict == "pass" for item in ordered)
    n_unresolved = sum(item.verdict == "unresolved" for item in ordered)
    all_pass = complete and bool(required) and n_required_passed == len(required)
    summary = (
        f"Reasoning: {n_required_passed}/{len(required)} criteri required superati. "
        + ("ALL PASS." if all_pass else f"FALLITI {len(required) - n_required_passed} REQUIRED.")
    )
    if not complete:
        summary += f" VALUTAZIONE INCOMPLETA: {n_required_unresolved} required unresolved."
    judge_diagnostics = dict(score.judge_diagnostics)
    judge_diagnostics["deterministic_artifact_checks"] = diagnostics
    return score.model_copy(
        update={
            "score": (1.0 if all_pass else 0.0) if complete else None,
            "all_pass": all_pass if complete else None,
            "reasoning_score": (1.0 if all_pass else 0.0) if complete else None,
            "reasoning_all_pass": all_pass if complete else None,
            "content_all_pass": all_pass if complete else None,
            "reasoning_scoring_status": "complete" if complete else "incomplete",
            "scoring_status": "complete" if complete else "incomplete",
            "n_criteria": len(ordered),
            "n_passed": n_passed,
            "n_unresolved": n_unresolved,
            "n_required": len(required),
            "n_required_passed": n_required_passed,
            "n_required_unresolved": n_required_unresolved,
            "n_bonus": len(bonus),
            "n_bonus_passed": sum(item.verdict == "pass" for item in bonus),
            "n_bonus_unresolved": sum(item.verdict == "unresolved" for item in bonus),
            "required_pass_rate": (
                n_required_passed / len(required) if complete and required else None
            ),
            "bonus_pass_rate": (
                sum(item.verdict == "pass" for item in bonus) / len(bonus)
                if bonus
                else None
            ),
            "unresolved_rate": n_unresolved / len(ordered) if ordered else 0.0,
            "summary": summary,
            "criteria_results": ordered,
            "judge_diagnostics": judge_diagnostics,
        }
    )


def _anchor_judge_results(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
    score: TaskScore,
) -> TaskScore:
    """Validate judge quotes against the frozen submission and add line spans."""
    criteria = {item.id: item for item in task.rubric.criteria}
    anchored: list[CriterionResult] = []
    for result in score.criteria_results:
        criterion = criteria[result.id]
        if result.consensus_method == "deterministic":
            anchored.append(result)
            continue

        supporting = set(result.supporting_judges)
        votes = [
            vote
            for vote in result.judge_votes
            if vote.status == "ok"
            and vote.verdict == result.verdict
            and (not supporting or vote.judge_id in supporting)
        ]
        quotes = [quote for vote in votes for quote in vote.evidence]
        response_evidence, invalid_quotes = _locate_response_quotes(submission, quotes)
        response_evidence, outside_scope_quotes = _evidence_within_scope(
            submission,
            criterion,
            response_evidence,
        )
        reported_not_found = any(vote.evidence_status == "not_found" for vote in votes)
        reported_unavailable = any(
            vote.evidence_status == "unavailable" for vote in votes
        ) or not votes

        evidence_scope: str | None = None
        notes = [
            f"Estratto del judge non presente testualmente nella submission: {item[:160]}"
            for item in invalid_quotes
        ]
        notes.extend(
            f"Estratto del judge fuori dall'ambito {criterion.normalized_evidence_scope}: "
            f"{item[:160]}"
            for item in outside_scope_quotes
        )
        if response_evidence:
            evidence_status = "found"
        elif invalid_quotes or outside_scope_quotes:
            evidence_status = "invalid"
        elif reported_not_found:
            if (
                criterion.verification_class == "scansione"
                and result.verdict == "pass"
                and criterion.evaluation_scope == "all_deliverables"
            ):
                evidence_status = "global_scan"
            else:
                evidence_status = "not_found"
            evidence_scope = criterion.normalized_evidence_scope
        elif reported_unavailable:
            evidence_status = "unavailable"
            notes.append(
                "Il judge non ha restituito il contratto di evidenza response_span_v1."
            )
        else:
            evidence_status = "unavailable"

        anchored.append(
            result.model_copy(
                update={
                    "verification_class": criterion.verification_class,
                    "criterion_type": criterion.criterion_type,
                    "criterion_logic": criterion.criterion_logic,
                    "evaluation_scope": criterion.evaluation_scope,
                    "scope_locator": criterion.scope_locator,
                    "evidence_status": evidence_status,
                    "response_evidence": response_evidence,
                    "evidence_scope": evidence_scope,
                    "evidence_notes": notes,
                }
            )
        )
    return score.model_copy(update={"criteria_results": anchored})


def _diagnostic_breakdown(task: LoadedWorkflowTask, score: TaskScore) -> dict[str, Any]:
    results = {item.id: item for item in score.criteria_results}
    categories: dict[str, dict[str, int | float | None]] = {}
    for item in score.criteria_results:
        bucket = categories.setdefault(
            item.category,
            {"passed": 0, "evaluated": 0, "unresolved": 0, "rate": None},
        )
        if item.verdict == "unresolved":
            bucket["unresolved"] = int(bucket["unresolved"]) + 1
        else:
            bucket["evaluated"] = int(bucket["evaluated"]) + 1
            if item.verdict == "pass":
                bucket["passed"] = int(bucket["passed"]) + 1
    for bucket in categories.values():
        evaluated = int(bucket["evaluated"])
        bucket["rate"] = int(bucket["passed"]) / evaluated if evaluated else None

    verification_classes: dict[str, dict[str, int | float | None]] = {}
    criterion_by_id = {item.id: item for item in task.rubric.criteria}
    for result in score.criteria_results:
        verification_class = criterion_by_id[result.id].verification_class
        bucket = verification_classes.setdefault(
            verification_class,
            {"passed": 0, "evaluated": 0, "unresolved": 0, "rate": None},
        )
        if result.verdict == "unresolved":
            bucket["unresolved"] = int(bucket["unresolved"]) + 1
        else:
            bucket["evaluated"] = int(bucket["evaluated"]) + 1
            if result.verdict == "pass":
                bucket["passed"] = int(bucket["passed"]) + 1
    for bucket in verification_classes.values():
        evaluated = int(bucket["evaluated"])
        bucket["rate"] = int(bucket["passed"]) / evaluated if evaluated else None

    evidence_status_counts: dict[str, int] = {}
    evidence_issues: dict[str, list[str]] = {}
    for result in score.criteria_results:
        evidence_status_counts[result.evidence_status] = (
            evidence_status_counts.get(result.evidence_status, 0) + 1
        )
        if result.evidence_status in {"invalid", "unavailable"}:
            evidence_issues[result.id] = list(result.evidence_notes)

    absence_fail_not_found = [
        result.id
        for result in score.criteria_results
        if criterion_by_id[result.id].criterion_logic == "prohibited_presence"
        and result.verdict == "fail"
        and result.evidence_status == "not_found"
    ]
    conditional_fail_not_found = [
        result.id
        for result in score.criteria_results
        if criterion_by_id[result.id].criterion_logic == "conditional_if_mentioned"
        and result.verdict == "fail"
        and result.evidence_status == "not_found"
    ]
    scoped_fail_without_in_scope_evidence = [
        result.id
        for result in score.criteria_results
        if criterion_by_id[result.id].evaluation_scope == "section"
        and result.verdict == "fail"
        and result.evidence_status in {"invalid", "not_found", "unavailable"}
        and criterion_by_id[result.id].criterion_logic != "required_presence"
    ]
    evidence_review_required = bool(
        evidence_issues
        or absence_fail_not_found
        or conditional_fail_not_found
        or scoped_fail_without_in_scope_evidence
    )

    judge_votes = [
        vote
        for result in score.criteria_results
        for vote in result.judge_votes
        if vote.status == "ok"
    ]
    judge_providers = sorted({vote.provider for vote in judge_votes})
    judge_models = sorted({vote.model for vote in judge_votes})

    def model_family(model: str) -> str:
        lowered = model.casefold()
        match = re.match(r"(gpt-\d+(?:\.\d+)?)", lowered)
        if match:
            return match.group(1)
        for prefix in ("claude", "gemini", "mistral", "llama", "deepseek"):
            if lowered.startswith(prefix):
                return prefix
        return lowered.split(":", 1)[0]

    agent_family = model_family(score.model)
    same_model_family_judges = [
        model for model in judge_models if model_family(model) == agent_family
    ]
    panel_warnings: list[str] = []
    if score.judge_strategy in {"single", "batched_single"}:
        panel_warnings.append(
            "Strategia single-judge: risultato diagnostico, non idoneo al reporting benchmark finale."
        )
    if same_model_family_judges:
        panel_warnings.append(
            "Almeno un judge appartiene alla stessa famiglia del modello valutato."
        )
    if (
        score.model_call_provider
        and judge_providers
        and set(judge_providers) == {score.model_call_provider}
    ):
        panel_warnings.append(
            "Il panel usa soltanto lo stesso provider del modello valutato."
        )

    clusters: dict[str, Any] = {}
    for cluster in task.rubric.diagnostic_clusters:
        clusters[cluster.id] = {
            "entry_criteria": {
                criterion_id: results[criterion_id].verdict
                for criterion_id in cluster.entry_criteria
            },
            "dependent_criteria": {
                criterion_id: results[criterion_id].verdict
                for criterion_id in cluster.dependent_criteria
            },
            "hypothesized_edges": [list(edge) for edge in cluster.hypothesized_edges],
            "interpretation": cluster.interpretation,
            "non_additive": True,
        }
    return {
        "rubric_version": task.rubric.rubric_version,
        "methodology_version": task.spec.methodology_version,
        "category_rates": categories,
        "verification_class_rates": verification_classes,
        "criterion_evidence": {
            "contract": "response_span_v1",
            "status_counts": dict(sorted(evidence_status_counts.items())),
            "issues": evidence_issues,
            "review_required": evidence_review_required,
            "review_flags": {
                "absence_fail_without_positive_evidence": absence_fail_not_found,
                "conditional_fail_without_trigger_evidence": conditional_fail_not_found,
                "scoped_fail_without_in_scope_evidence": (
                    scoped_fail_without_in_scope_evidence
                ),
            },
        },
        "judge_panel": {
            "reporting_status": (
                "diagnostic_only"
                if score.judge_strategy in {"single", "batched_single"}
                else (
                    "review_required"
                    if evidence_review_required
                    else "panel_evaluation"
                )
            ),
            "agent_provider": score.model_call_provider,
            "agent_model_family": agent_family,
            "judge_providers": judge_providers,
            "judge_models": judge_models,
            "same_model_family_judges": same_model_family_judges,
            "warnings": panel_warnings,
        },
        "diagnostic_clusters": clusters,
    }


def evaluate_submission(
    task: LoadedWorkflowTask,
    submission: WorkflowSubmission,
    *,
    judge: Any,
) -> TaskScore:
    validate_submission(task, submission)
    log.info(
        "[%s] Evaluation avviata — criteri=%d, strategia=%s, judge=%s",
        task.short_id,
        len(task.rubric.criteria),
        getattr(judge, "strategy", "single"),
        getattr(judge, "judge_models", {"A": getattr(judge, "model", "unknown")}),
    )
    with progress_heartbeat(
        log,
        f"[{task.short_id}] Evaluation ancora in corso",
    ):
        score = score_task(
            judge_task(task),
            submission_text(submission),
            submission.model,
            judge=judge,
        )
    legacy_check_ids = [
        check_id
        for criterion in task.rubric.criteria
        if criterion.evaluation_mode == "deterministic"
        for check_id in criterion.deterministic_checks
    ]
    if _uses_prompt_only_free_artifacts(task):
        deterministic: list[CriterionResult] = []
        diagnostics: dict[str, list[str]] = {}
    else:
        deterministic, diagnostics = _deterministic_results(task, submission)
        score = _merge_deterministic_results(task, score, deterministic, diagnostics)
    score = _anchor_judge_results(task, submission, score)
    score = with_model_call_metrics(score, submission.model_call_metrics)
    legacy_check_diagnostics = (
        {
            "legacy_artifact_checks": {
                "status": "diagnostic_only_not_applied",
                "contract": "prompt_only_free_artifacts_v1",
                "count": len(legacy_check_ids),
                "check_ids": legacy_check_ids,
            }
        }
        if _uses_prompt_only_free_artifacts(task)
        else {}
    )
    submission_contract = getattr(task.spec, "submission_contract", None)
    criterion_routing_contract = (
        "all_criteria_semantic_judge_v1"
        if _uses_prompt_only_free_artifacts(task)
        else "legacy_mixed_routing_v1"
    )
    score = score.model_copy(
        update={
            "judge_diagnostics": {
                **score.judge_diagnostics,
                "submission_contract": submission_contract,
                "criterion_routing_contract": criterion_routing_contract,
                **legacy_check_diagnostics,
                **_diagnostic_breakdown(task, score),
            }
        }
    )
    log.info(
        "[%s] Evaluation completata — all_pass=%s, criterion_rate=%s, unresolved=%d",
        task.short_id,
        score.all_pass,
        score.required_pass_rate,
        score.n_unresolved,
    )
    return score


def evaluation_payload(score: TaskScore) -> dict[str, Any]:
    payload = score.model_dump()
    payload["criterion_rate"] = score.required_pass_rate
    payload["evaluation_contract"] = "all_pass_and_criterion_rate"
    payload["criterion_evidence_contract"] = "response_span_v1"
    payload["submission_contract"] = score.judge_diagnostics.get(
        "submission_contract"
    )
    payload["criterion_routing_contract"] = score.judge_diagnostics.get(
        "criterion_routing_contract"
    )
    payload["citation_grounding"] = "not_applicable"
    return payload
