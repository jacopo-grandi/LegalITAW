"""Collect model-call latency, token usage and cost estimates."""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any


PRICE_ENV_NAMES = (
    "MODEL_PRICING_USD_PER_1M",
    "MODEL_PRICING_USD_PER_MILLION",
)

# Listino dei modelli valutati, in USD per milione di token. Si applica quando
# nessuna delle variabili PRICE_ENV_NAMES è impostata; una variabile impostata
# lo sostituisce per intero. Senza prezzo il costo del task resta None e il
# limite --max-agent-cost-usd non si può applicare.
DEFAULT_PRICE_TABLE_SOURCE = "builtin:2026-09-29"
DEFAULT_MODEL_PRICING_USD_PER_1M: dict[str, dict[str, float]] = {
    # Anthropic, listino platform.claude.com al 29 set 2026: lettura da cache = 10%
    # dell'input, scrittura in cache (5 minuti) = 125%
    "claude-opus-5-5": {"input": 4.00, "cached_input": 0.40, "cache_write_input": 5.00, "output": 20.00},
    "claude-sonnet-5-5": {"input": 2.00, "cached_input": 0.20, "cache_write_input": 2.50, "output": 10.00},
    "claude-sonnet-4-6": {"input": 3.00, "cached_input": 0.30, "cache_write_input": 3.75, "output": 15.00},
    # OpenAI: input e output come nella tabella dei giudici; cache stimata al 10% dell'input
    "gpt-5.6-luna": {"input": 0.20, "cached_input": 0.02, "output": 1.20},
    # Novita, API /openai/models al 29 set 2026 (prezzi in 1/10.000 USD per milione);
    # prezzo della cache non pubblicato: l'input in cache si conta a prezzo pieno
    "deepseek/deepseek-v4-flash": {"input": 0.14, "output": 0.28},
    "deepseek/deepseek-v4-pro": {"input": 1.60, "output": 3.20},
    "deepseek/deepseek-v4.1-flash": {"input": 0.30, "output": 1.20},
    "openai/gpt-oss-120b": {"input": 0.05, "output": 0.25},
    "qwen/qwen3.6-35b-a3b": {"input": 0.248, "output": 1.485},
    "qwen/qwen3.6-27b": {"input": 0.60, "output": 3.60},
    "google/gemma-4-26b-a4b-it": {"input": 0.13, "output": 0.40},
    "google/gemma-4-31b-it": {"input": 0.14, "output": 0.40},
    "zai-org/glm-4.7-flash": {"input": 0.07, "output": 0.40},
    "minimax/minimax-m2.7": {"input": 0.30, "output": 1.20},
}

MODEL_CALL_SCORE_FIELDS = (
    "model_call_provider",
    "model_call_latency_ms",
    "model_call_input_tokens",
    "model_call_output_tokens",
    "model_call_total_tokens",
    "model_call_cached_input_tokens",
    "model_call_reasoning_tokens",
    "model_call_estimated_cost_usd",
    "model_call_cost_source",
    "model_call_usage",
)


@dataclass(frozen=True)
class ModelCallResult:
    text: str
    metrics: dict[str, Any]


def latency_ms(started_at: float) -> int:
    return int(round((time.perf_counter() - started_at) * 1000))


def object_to_dict(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return {
            str(key): object_to_dict(item) if _is_mapping_like(item) else item
            for key, item in value.items()
        }
    if hasattr(value, "model_dump"):
        try:
            return value.model_dump()
        except Exception:
            pass
    if hasattr(value, "to_dict"):
        try:
            return value.to_dict()
        except Exception:
            pass

    out: dict[str, Any] = {}
    for name in (
        "input_tokens",
        "output_tokens",
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "cache_creation_input_tokens",
        "cache_read_input_tokens",
        "input_tokens_details",
        "prompt_tokens_details",
        "completion_tokens_details",
        "output_tokens_details",
        "cached_tokens",
        "reasoning_tokens",
    ):
        if hasattr(value, name):
            item = getattr(value, name)
            out[name] = object_to_dict(item) if _is_mapping_like(item) else item
    return out


def _is_mapping_like(value: Any) -> bool:
    return isinstance(value, dict) or hasattr(value, "model_dump") or hasattr(value, "to_dict")


def extract_usage(response: Any) -> dict[str, Any]:
    return object_to_dict(getattr(response, "usage", None))


def normalized_token_usage(usage: dict[str, Any]) -> dict[str, int | None]:
    details_input = object_to_dict(usage.get("input_tokens_details"))
    details_prompt = object_to_dict(usage.get("prompt_tokens_details"))
    details_completion = object_to_dict(usage.get("completion_tokens_details"))
    details_output = object_to_dict(usage.get("output_tokens_details"))

    input_tokens = _int_or_none(usage.get("input_tokens"))
    if input_tokens is None:
        input_tokens = _int_or_none(usage.get("prompt_tokens"))

    output_tokens = _int_or_none(usage.get("output_tokens"))
    if output_tokens is None:
        output_tokens = _int_or_none(usage.get("completion_tokens"))

    total_tokens = _int_or_none(usage.get("total_tokens"))
    if total_tokens is None and input_tokens is not None and output_tokens is not None:
        total_tokens = input_tokens + output_tokens

    cached_input_tokens = _int_or_none(usage.get("cache_read_input_tokens"))
    cache_write_input_tokens = _int_or_none(usage.get("cache_creation_input_tokens"))
    if (cached_input_tokens is not None or cache_write_input_tokens is not None) and input_tokens is not None:
        # Anthropic conta a parte letture e scritture in cache: input_tokens è solo
        # la coda non in cache. Qui input_tokens diventa il totale letto dal modello.
        input_tokens += (cached_input_tokens or 0) + (cache_write_input_tokens or 0)
        if total_tokens is not None and output_tokens is not None:
            total_tokens = input_tokens + output_tokens
    if cached_input_tokens is None:
        cached_input_tokens = _int_or_none(details_input.get("cached_tokens"))
    if cached_input_tokens is None:
        cached_input_tokens = _int_or_none(details_prompt.get("cached_tokens"))

    reasoning_tokens = _int_or_none(details_completion.get("reasoning_tokens"))
    if reasoning_tokens is None:
        reasoning_tokens = _int_or_none(details_output.get("reasoning_tokens"))

    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "cached_input_tokens": cached_input_tokens,
        "cache_write_input_tokens": cache_write_input_tokens,
        "reasoning_tokens": reasoning_tokens,
    }


def build_model_call_metrics(
    *,
    provider: str,
    model: str,
    latency_ms_value: int,
    usage: dict[str, Any],
) -> dict[str, Any]:
    tokens = normalized_token_usage(usage)
    cost, source = estimate_cost_usd(provider=provider, model=model, token_usage=tokens)
    return {
        "provider": provider,
        "model": model,
        "latency_ms": latency_ms_value,
        "usage": usage,
        **tokens,
        "estimated_cost_usd": cost,
        "cost_source": source,
    }


def score_update_from_model_call(metrics: dict[str, Any] | None) -> dict[str, Any]:
    if not metrics:
        return {}
    return {
        "model_call_provider": metrics.get("provider"),
        "model_call_latency_ms": metrics.get("latency_ms"),
        "model_call_input_tokens": metrics.get("input_tokens"),
        "model_call_output_tokens": metrics.get("output_tokens"),
        "model_call_total_tokens": metrics.get("total_tokens"),
        "model_call_cached_input_tokens": metrics.get("cached_input_tokens"),
        "model_call_reasoning_tokens": metrics.get("reasoning_tokens"),
        "model_call_estimated_cost_usd": metrics.get("estimated_cost_usd"),
        "model_call_cost_source": metrics.get("cost_source"),
        "model_call_usage": metrics.get("usage") or {},
    }


def with_model_call_metrics(score: Any, metrics: dict[str, Any] | None) -> Any:
    update = score_update_from_model_call(metrics)
    if not update:
        return score
    if hasattr(score, "model_copy"):
        return score.model_copy(update=update)
    for key, value in update.items():
        setattr(score, key, value)
    return score


def estimate_cost_usd(
    *,
    provider: str,
    model: str,
    token_usage: dict[str, int | None],
) -> tuple[float | None, str | None]:
    price, source = _lookup_price(provider, model)
    if not price:
        return None, None

    input_tokens = token_usage.get("input_tokens") or 0
    output_tokens = token_usage.get("output_tokens") or 0
    cached_input_tokens = min(token_usage.get("cached_input_tokens") or 0, input_tokens)
    cache_write_tokens = min(
        token_usage.get("cache_write_input_tokens") or 0,
        max(0, input_tokens - cached_input_tokens),
    )
    regular_input_tokens = input_tokens

    input_price = _price_value(price, "input")
    output_price = _price_value(price, "output")
    cached_input_price = _price_value(price, "cached_input")
    cache_write_price = _price_value(price, "cache_write_input")

    cost = 0.0
    if cached_input_price is not None:
        regular_input_tokens = max(0, input_tokens - cached_input_tokens)
        cost += cached_input_tokens / 1_000_000 * cached_input_price
    if cache_write_price is not None:
        regular_input_tokens = max(0, regular_input_tokens - cache_write_tokens)
        cost += cache_write_tokens / 1_000_000 * cache_write_price
    if input_price is not None:
        cost += regular_input_tokens / 1_000_000 * input_price
    if output_price is not None:
        cost += output_tokens / 1_000_000 * output_price

    return round(cost, 8), source


def _lookup_price(provider: str, model: str) -> tuple[dict[str, Any] | None, str | None]:
    table, source = _load_price_table()
    if not table:
        return None, None
    keys = (
        model,
        model.replace("/", "-"),
        f"{provider}/{model}",
        f"{provider}:{model}",
        provider,
    )
    for key in keys:
        value = table.get(key)
        if isinstance(value, dict):
            return value, source
    return None, None


def _load_price_table() -> tuple[dict[str, Any], str | None]:
    for name in PRICE_ENV_NAMES:
        raw = os.environ.get(name)
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return {}, name
        if isinstance(parsed, dict):
            return parsed, name
    return DEFAULT_MODEL_PRICING_USD_PER_1M, DEFAULT_PRICE_TABLE_SOURCE


def _price_value(price: dict[str, Any], name: str) -> float | None:
    for key in (name, f"{name}_per_1m", f"{name}_per_million"):
        value = price.get(key)
        if value is None:
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
    return None


def _int_or_none(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


