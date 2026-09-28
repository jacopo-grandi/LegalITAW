"""Build a deterministic, public-only text bundle for evaluated models."""

from __future__ import annotations

from .models import LoadedWorkflowTask
from .workspace import (
    MatterWorkspace,
    public_envelope_paths,
    validate_runtime_capabilities,
)


def _fallback_by_stem(task: LoadedWorkflowTask) -> dict[str, str]:
    return {
        fallback.rsplit("/", 1)[-1].rsplit(".", 1)[0]: fallback
        for fallback in task.spec.fallback_paths
    }


def public_text_paths(task: LoadedWorkflowTask) -> list[str]:
    """Return canonical textual counterparts for every declared public input."""
    fallbacks = _fallback_by_stem(task)
    selected: list[str] = []
    for relative in public_envelope_paths(task):
        if relative.lower().endswith(".docx"):
            stem = relative.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            fallback = fallbacks.get(stem)
            if fallback is None:
                raise ValueError(f"fallback Markdown mancante per {relative}")
            relative = fallback
        if relative not in selected:
            selected.append(relative)
    return selected


def build_public_bundle(task: LoadedWorkflowTask) -> str:
    validate_runtime_capabilities(task, execution_mode="text_bundle")
    files: list[str] = []
    workspace = MatterWorkspace(task)
    try:
        for relative in public_envelope_paths(task):
            pages = workspace.document_pages(relative)
            content = "\n\n".join(
                f"[PAGINA {index}]\n{page}"
                for index, page in enumerate(pages, start=1)
            )
            files.append(
                f'<public_file path="{relative}">\n{content.strip()}\n</public_file>'
            )
    finally:
        workspace.close()

    protocol = f"""<output_protocol>
Restituisci esclusivamente un oggetto JSON valido, senza markdown esterno e senza
testo prima o dopo il JSON, con questa forma:
{{
  "artifacts": [
    {{"path": "nome-scelto.md", "content": "..."}}
  ]
}}
Scegli liberamente nomi, numero e struttura degli artifact in base all'incarico.
Ogni `content` deve contenere il testo completo dell'artifact. Sono supportate le
estensioni `.md`, `.txt` e `.docx`; eventuali richieste su formato o numero dei file
valgono soltanto se compaiono nei file pubblici.
</output_protocol>"""

    return "\n\n".join(
        [
            f'<legalita_workflow_task id="{task.spec.task_id}">',
            *files,
            protocol,
            "</legalita_workflow_task>",
        ]
    )
