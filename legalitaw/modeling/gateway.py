"""Provider-neutral gateway for evaluated-model completions.

The provider SDK adapters live in :mod:`legalitaw.modeling.query`; this module
owns the single routing and retry policy used by every benchmark workflow.
Adapters are constructor dependencies so unit tests and alternative runtimes do
not need to monkeypatch application modules.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass

from legalitaw.config import MODEL_RETRIES

from .query import (
    query_anthropic_with_metrics,
    query_gemini_with_metrics,
    query_novita_with_metrics,
    query_openai_with_metrics,
    require_result_text,
    run_query_with_retries,
)
from .routing import select_adapter
from .usage import ModelCallResult

ModelAdapter = Callable[[str, str], ModelCallResult]


@dataclass(frozen=True)
class ModelGateway:
    """Route one model request through an injected provider adapter."""

    anthropic: ModelAdapter
    gemini: ModelAdapter
    novita: ModelAdapter
    openai: ModelAdapter
    logger: logging.Logger

    def complete(
        self,
        model: str,
        prompt: str,
        *,
        max_retries: int = MODEL_RETRIES,
    ) -> ModelCallResult | None:
        adapter = select_adapter(
            model,
            anthropic=self.anthropic,
            gemini=self.gemini,
            novita=self.novita,
            openai=self.openai,
        )
        result = run_query_with_retries(
            adapter,
            model,
            prompt,
            max_retries=max_retries,
            log=self.logger,
            validate=require_result_text,
        )
        if result is None:
            return None
        if not isinstance(result, ModelCallResult):
            raise TypeError(
                "Un adapter modello deve restituire ModelCallResult, "
                f"non {type(result).__name__}."
            )
        return result

    def complete_text(
        self,
        model: str,
        prompt: str,
        *,
        max_retries: int = MODEL_RETRIES,
    ) -> str | None:
        result = self.complete(model, prompt, max_retries=max_retries)
        return result.text.strip() if result is not None else None


def default_gateway(*, logger: logging.Logger | None = None) -> ModelGateway:
    """Build the production gateway from the currently bound SDK adapters."""
    return ModelGateway(
        anthropic=query_anthropic_with_metrics,
        gemini=query_gemini_with_metrics,
        novita=query_novita_with_metrics,
        openai=query_openai_with_metrics,
        logger=logger or logging.getLogger(__name__),
    )


def query_model(
    model: str,
    prompt: str,
    max_retries: int = MODEL_RETRIES,
) -> str | None:
    """Convenience wrapper for callers that only need response text."""
    return default_gateway().complete_text(model, prompt, max_retries=max_retries)


def query_model_with_metrics(
    model: str,
    prompt: str,
    max_retries: int = MODEL_RETRIES,
) -> ModelCallResult | None:
    """Return the canonical completion result, including usage metrics."""
    return default_gateway().complete(model, prompt, max_retries=max_retries)
