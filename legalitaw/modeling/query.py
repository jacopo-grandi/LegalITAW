"""
Layer condiviso di interrogazione dei modelli sotto esame.

Contiene gli adapter SDK per Anthropic, OpenAI, Gemini via endpoint
OpenAI-compatibile e Novita, oltre alla policy di retry condivisa. Il routing
provider-neutral vive nel gateway; i servizi applicativi non importano SDK né
riesportano alias degli adapter.
"""

import logging
import os
import time
from collections.abc import Callable

import anthropic
import openai

from legalitaw import config as benchmark_config
from legalitaw.config import (
    MODEL_MAX_TOKENS,
    OPENAI_GENERATION_MAX_OUTPUT_TOKENS,
    OPENAI_GENERATION_REASONING_EFFORT,
)

from .request_config import (
    anthropic_message_kwargs,
    gemini_completion_kwargs,
    novita_completion_kwargs,
    openai_completion_kwargs,
    openai_response_kwargs,
    openai_uses_responses,
    request_config_for_summary,
)
from .routing import provider_for_model
from .runtime import (
    ModelResponseError,
    anthropic_response_text,
    is_non_retryable_model_error,
    stream_anthropic_message,
)
from .usage import (
    ModelCallResult,
    build_model_call_metrics,
    extract_usage,
    latency_ms,
    object_to_dict,
)

log = logging.getLogger(__name__)

NOVITA_BASE_URL = "https://api.novita.ai/openai"
NOVITA_GLM_52_MAX_TOKENS = 65536
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


def run_query_with_retries(
    adapter: Callable[[str, str], object],
    model: str,
    query: str,
    *,
    max_retries: int,
    log: logging.Logger,
    validate: Callable[[object], None] | None = None,
) -> object | None:
    """
    Esegue adapter(model, query) con retry e backoff esponenziale.

    `validate` puo' sollevare per forzare il retry su risposte non valide.
    Gli errori non recuperabili interrompono subito i tentativi; un
    `ModelResponseError` viene propagato per conservarne la diagnostica,
    mentre gli altri fallimenti restituiscono None per compatibilita'.
    """
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            result = adapter(model, query)
            if validate is not None:
                validate(result)
            return result
        except Exception as exc:
            last_error = exc
            if is_non_retryable_model_error(exc):
                log.error(
                    "Errore non recuperabile query %s (tentativo %d/%d): %s",
                    model,
                    attempt,
                    max_retries,
                    exc,
                )
                if isinstance(exc, ModelResponseError):
                    raise
                return None
            if attempt >= max_retries:
                log.warning(
                    "Errore ritentabile query %s (tentativo %d/%d): %s; tentativi esauriti",
                    model,
                    attempt,
                    max_retries,
                    exc,
                )
                break
            delay = 2.0 * (2 ** (attempt - 1))
            log.warning(
                "Errore ritentabile query %s (tentativo %d/%d): %s; attendo %.1fs",
                model,
                attempt,
                max_retries,
                exc,
                delay,
            )
            time.sleep(delay)

    log.error("Query fallita dopo %d tentativi: %s", max_retries, model)
    if isinstance(last_error, ModelResponseError):
        raise last_error
    return None


def require_result_text(result: ModelCallResult) -> None:
    if not result.text:
        raise ValueError("Risposta vuota dal modello.")


def query_anthropic(model: str, query: str) -> str:
    return query_anthropic_with_metrics(model, query).text


def query_anthropic_with_metrics(model: str, query: str) -> ModelCallResult:
    client = anthropic.Anthropic()
    started_at = time.perf_counter()
    request = default_anthropic_message_kwargs(model, query)
    response = stream_anthropic_message(
        client,
        logger=log,
        config_module=benchmark_config,
        model=model,
        model_max_tokens=MODEL_MAX_TOKENS,
        request=request,
    )
    text = anthropic_response_text(response)
    if not text:
        content_types = [
            getattr(block, "type", type(block).__name__)
            for block in getattr(response, "content", []) or []
        ]
        raise ValueError(
            "Risposta Anthropic priva di blocchi testuali finali "
            f"(content_types={content_types})."
        )
    return ModelCallResult(
        text=text,
        metrics=build_model_call_metrics(
            provider="anthropic",
            model=model,
            latency_ms_value=latency_ms(started_at),
            usage=extract_usage(response),
        ),
    )


def default_anthropic_message_kwargs(model: str, query: str) -> dict[str, object]:
    return anthropic_message_kwargs(model, query, MODEL_MAX_TOKENS)


def query_openai(model: str, query: str) -> str:
    return query_openai_with_metrics(model, query).text


def query_openai_with_metrics(model: str, query: str) -> ModelCallResult:
    client = openai.OpenAI()
    started_at = time.perf_counter()
    if not openai_uses_responses(model):
        request = default_openai_completion_kwargs(model, query)
        response = client.chat.completions.create(**request)
        content = (response.choices[0].message.content or "").strip()
        metrics = build_model_call_metrics(
            provider="openai",
            model=model,
            latency_ms_value=latency_ms(started_at),
            usage=extract_usage(response),
        )
        metrics.update(
            {
                "api_style": "openai_chat_completions",
                "request": request_config_for_summary(request),
                "finish_reason": getattr(response.choices[0], "finish_reason", None),
            }
        )
        if not content:
            raise ModelResponseError(
                "Risposta OpenAI Chat Completions senza testo finale "
                f"(finish_reason={metrics.get('finish_reason') or 'unknown'}).",
                metrics=metrics,
                retryable=metrics.get("finish_reason") not in {"length", "content_filter"},
            )
        return ModelCallResult(text=content, metrics=metrics)

    request = default_openai_response_kwargs(model, query)
    response = client.responses.create(**request)
    content = (getattr(response, "output_text", None) or "").strip()
    status = getattr(response, "status", None)
    incomplete_value = getattr(response, "incomplete_details", None)
    incomplete_details = object_to_dict(incomplete_value)
    if incomplete_value is not None and "reason" not in incomplete_details:
        reason_value = getattr(incomplete_value, "reason", None)
        if reason_value is not None:
            incomplete_details["reason"] = reason_value
    metrics = build_model_call_metrics(
        provider="openai",
        model=model,
        latency_ms_value=latency_ms(started_at),
        usage=extract_usage(response),
    )
    metrics.update(
        {
            "api_style": "openai_responses",
            "request": request_config_for_summary(request),
            "response_id": getattr(response, "id", None),
            "response_status": status,
            "incomplete_details": incomplete_details,
        }
    )
    if not content:
        reason = incomplete_details.get("reason") or "no_output_text"
        raise ModelResponseError(
            "Risposta OpenAI senza testo finale "
            f"(status={status or 'unknown'}, reason={reason}, "
            f"output_tokens={metrics.get('output_tokens')}, "
            f"reasoning_tokens={metrics.get('reasoning_tokens')}).",
            metrics=metrics,
            retryable=status in {None, "completed"},
        )
    return ModelCallResult(
        text=content.strip(),
        metrics=metrics,
    )


def default_openai_completion_kwargs(model: str, query: str) -> dict[str, object]:
    return openai_completion_kwargs(model, query, MODEL_MAX_TOKENS)


def default_openai_response_kwargs(model: str, query: str) -> dict[str, object]:
    max_output_tokens = int(
        os.environ.get(
            "OPENAI_GENERATION_MAX_OUTPUT_TOKENS",
            str(OPENAI_GENERATION_MAX_OUTPUT_TOKENS),
        )
    )
    reasoning_effort = os.environ.get(
        "OPENAI_GENERATION_REASONING_EFFORT",
        OPENAI_GENERATION_REASONING_EFFORT,
    ).strip()
    return openai_response_kwargs(
        model,
        query,
        max_output_tokens,
        reasoning_effort,
    )


def query_gemini(model: str, query: str) -> str:
    return query_gemini_with_metrics(model, query).text


def default_gemini_completion_kwargs(model: str, query: str) -> dict[str, object]:
    return gemini_completion_kwargs(model, query, MODEL_MAX_TOKENS)


def query_gemini_with_metrics(model: str, query: str) -> ModelCallResult:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY non impostata in .env")

    client = openai.OpenAI(api_key=api_key, base_url=GEMINI_BASE_URL)
    started_at = time.perf_counter()
    response = client.chat.completions.create(**default_gemini_completion_kwargs(model, query))
    choice = response.choices[0]
    if getattr(choice, "finish_reason", None) == "length":
        log.warning("Risposta %s troncata dal provider: finish_reason=length", model)
    content = choice.message.content
    if content is None:
        raise ValueError("Risposta Gemini priva di contenuto testuale.")
    return ModelCallResult(
        text=content.strip(),
        metrics=build_model_call_metrics(
            provider="google",
            model=model,
            latency_ms_value=latency_ms(started_at),
            usage=extract_usage(response),
        ),
    )


def default_novita_completion_kwargs(model: str, query: str) -> dict[str, object]:
    return novita_completion_kwargs(
        model,
        query,
        max_tokens=MODEL_MAX_TOKENS,
        glm_max_tokens=NOVITA_GLM_52_MAX_TOKENS,
    )


def query_novita(model: str, query: str) -> str:
    return query_novita_with_metrics(model, query).text


def query_novita_with_metrics(model: str, query: str) -> ModelCallResult:
    api_key = os.environ.get("NOVITA_API_KEY")
    if not api_key:
        raise RuntimeError("NOVITA_API_KEY non impostata in .env")

    client = openai.OpenAI(api_key=api_key, base_url=NOVITA_BASE_URL)
    started_at = time.perf_counter()
    response = client.chat.completions.create(**default_novita_completion_kwargs(model, query))
    choice = response.choices[0]
    if getattr(choice, "finish_reason", None) == "length":
        log.warning("Risposta %s troncata dal provider: finish_reason=length", model)
    content = choice.message.content
    if content is None:
        raise ValueError("Risposta Novita priva di contenuto testuale.")
    return ModelCallResult(
        text=content.strip(),
        metrics=build_model_call_metrics(
            provider="novita",
            model=model,
            latency_ms_value=latency_ms(started_at),
            usage=extract_usage(response),
        ),
    )


def model_request_kwargs_for_summary(model: str) -> dict[str, object]:
    try:
        provider = provider_for_model(model)
    except ValueError:
        return {"model": model}
    if provider == "novita":
        return default_novita_completion_kwargs(model, "")
    if provider == "gemini":
        return default_gemini_completion_kwargs(model, "")
    if provider == "anthropic":
        return default_anthropic_message_kwargs(model, "")
    return default_openai_completion_kwargs(model, "")
