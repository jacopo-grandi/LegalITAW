"""Provider-neutral native tool-calling for evaluated agent runs.

The normalized transcript is deliberately small.  Provider-specific adapters
only translate messages and tool calls; strategy remains entirely with the
model and the harness never rewrites the conversation.
"""

from __future__ import annotations

import json
import re
import logging
import os
import random
import time
from dataclasses import dataclass, field
from typing import Any, Protocol

import anthropic
import openai

from legalitaw import config as benchmark_config
from legalitaw.config import (
    AGENT_MAX_OUTPUT_TOKENS,
    AGENT_REASONING_EFFORT,
)

from .query import GEMINI_BASE_URL, NOVITA_BASE_URL
from .request_config import (
    ANTHROPIC_REASONING_PREFIXES,
    GEMINI_REASONING_PREFIXES,
    NOVITA_REASONING_PREFIXES,
    OPENAI_REASONING_PREFIXES,
    openai_uses_responses,
)
from .routing import provider_for_model
from .runtime import ModelResponseError, log_anthropic_request_diagnostics
from .usage import (
    build_model_call_metrics,
    extract_usage,
    latency_ms,
    object_to_dict,
)


log = logging.getLogger(__name__)


@dataclass(frozen=True)
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]


@dataclass(frozen=True)
class NativeToolCall:
    id: str
    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class NativeAgentTurn:
    text: str = ""
    tool_calls: list[NativeToolCall] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    stop_reason: str | None = None


class NativeToolGateway(Protocol):
    def complete(
        self,
        model: str,
        *,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None = None,
    ) -> NativeAgentTurn: ...


def _agent_max_output_tokens() -> int:
    """Budget di output dell'agente; MODEL_MAX_TOKENS esplicito resta un override."""
    explicit = os.environ.get("MODEL_MAX_TOKENS")
    return int(explicit) if explicit else AGENT_MAX_OUTPUT_TOKENS


def _agent_reasoning_effort() -> str:
    return os.environ.get("AGENT_REASONING_EFFORT", AGENT_REASONING_EFFORT).strip()


def _tool_arguments(value: object, *, tool_name: str) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    raw = str(value or "{}").strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, flags=re.DOTALL)
    if fenced:
        raw = fenced.group(1)
    try:
        # strict=False ammette caratteri di controllo (a-capo, tab) scritti
        # letteralmente dentro le stringhe: alcuni modelli OpenAI-compatible li
        # emettono negli argomenti dei tool, e il contenuto resta identico.
        decoded = json.loads(raw or "{}", strict=False)
    except json.JSONDecodeError as exc:
        snippet = raw[:240] + ("..." if len(raw) > 240 else "")
        raise ValueError(
            f"argomenti JSON non validi per il tool {tool_name}: {exc.msg} "
            f"(carattere {exc.pos} di {len(raw)}); inizio: {snippet!r}"
        ) from exc
    if not isinstance(decoded, dict):
        raise ValueError(f"gli argomenti del tool {tool_name} devono essere un oggetto")
    return decoded


def _openai_tools(tools: list[ToolDefinition]) -> list[dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.input_schema,
            },
        }
        for tool in tools
    ]


def _openai_response_tools(tools: list[ToolDefinition]) -> list[dict[str, Any]]:
    """Translate the common tool schema to the Responses API shape."""
    return [
        {
            "type": "function",
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.input_schema,
            "strict": False,
        }
        for tool in tools
    ]


def _openai_response_input(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Replay the normalized transcript as Responses API input items."""
    result: list[dict[str, Any]] = []
    for message in messages:
        role = message["role"]
        if role in {"system", "developer"}:
            continue
        if role == "assistant":
            content = message.get("content") or ""
            if content:
                result.append({"role": "assistant", "content": content})
            result.extend(
                {
                    "type": "function_call",
                    "call_id": call["id"],
                    "name": call["name"],
                    "arguments": json.dumps(
                        call.get("arguments") or {},
                        ensure_ascii=False,
                    ),
                }
                for call in message.get("tool_calls") or []
            )
            continue
        if role == "tool":
            result.append(
                {
                    "type": "function_call_output",
                    "call_id": message["tool_call_id"],
                    "output": message.get("content") or "",
                }
            )
            continue
        result.append({"role": "user", "content": message.get("content") or ""})
    return result


def _openai_messages(
    system_prompt: str,
    messages: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = [{"role": "system", "content": system_prompt}]
    for message in messages:
        role = message["role"]
        if role in {"system", "developer"}:
            continue
        if role == "assistant":
            item: dict[str, Any] = {
                "role": "assistant",
                "content": message.get("content") or None,
            }
            calls = message.get("tool_calls") or []
            if calls:
                item["tool_calls"] = [
                    {
                        "id": call["id"],
                        "type": "function",
                        "function": {
                            "name": call["name"],
                            "arguments": json.dumps(
                                call.get("arguments") or {},
                                ensure_ascii=False,
                            ),
                        },
                    }
                    for call in calls
                ]
            result.append(item)
        elif role == "tool":
            result.append(
                {
                    "role": "tool",
                    "tool_call_id": message["tool_call_id"],
                    "content": message.get("content") or "",
                }
            )
        else:
            result.append({"role": "user", "content": message.get("content") or ""})
    return result


def _anthropic_tools(tools: list[ToolDefinition]) -> list[dict[str, Any]]:
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_schema,
        }
        for tool in tools
    ]


def _anthropic_messages(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    index = 0
    while index < len(messages):
        message = messages[index]
        role = message["role"]
        if role == "assistant":
            blocks: list[dict[str, Any]] = []
            if message.get("content"):
                blocks.append({"type": "text", "text": message["content"]})
            blocks.extend(
                {
                    "type": "tool_use",
                    "id": call["id"],
                    "name": call["name"],
                    "input": call.get("arguments") or {},
                }
                for call in message.get("tool_calls") or []
            )
            result.append({"role": "assistant", "content": blocks})
            index += 1
            continue
        if role == "tool":
            blocks = []
            while index < len(messages) and messages[index]["role"] == "tool":
                tool_message = messages[index]
                blocks.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_message["tool_call_id"],
                        "content": tool_message.get("content") or "",
                    }
                )
                index += 1
            result.append({"role": "user", "content": blocks})
            continue
        if role == "user":
            result.append({"role": "user", "content": message.get("content") or ""})
        index += 1
    return result


def _with_cache_breakpoints(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Mark the conversation prefix for Anthropic prompt caching.

    Each agent turn resends the whole conversation. A breakpoint on the last
    message writes the prefix to the cache; one on the message that was last in
    the previous turn (three positions back) reads what that turn wrote. The
    content the model sees does not change, only how the input is billed.
    """
    result = [dict(message) for message in messages]
    for position in (len(result) - 1, len(result) - 3):
        if position < 0 or result[position]["role"] != "user":
            continue
        content = result[position]["content"]
        blocks = (
            [{"type": "text", "text": content}]
            if isinstance(content, str)
            else [dict(block) for block in content]
        )
        if not blocks or (blocks[-1].get("type") == "text" and not blocks[-1].get("text")):
            continue
        blocks[-1] = {**blocks[-1], "cache_control": {"type": "ephemeral"}}
        result[position] = {**result[position], "content": blocks}
    return result


# Rate limit (429), sovraccarico (529) ed errori 5xx o di rete: l'harness aspetta
# e riprova invece di far fallire il task. Le librerie dei provider riprovano già
# 2 volte in pochi secondi; qui l'attesa arriva a qualche minuto. Gli errori di
# credito o di autenticazione (401, 402, 403) non si ritentano.
TRANSIENT_RETRY_ATTEMPTS = 10
TRANSIENT_RETRY_MAX_DELAY_SECONDS = 120.0
TRANSIENT_PROVIDER_ERRORS = (
    anthropic.RateLimitError,
    anthropic.APIConnectionError,
    anthropic.InternalServerError,
    anthropic.APIStatusError,
    openai.RateLimitError,
    openai.APIConnectionError,
    openai.InternalServerError,
    openai.APIStatusError,
)


def _retry_delay_seconds(exc: BaseException, attempt: int) -> float:
    response = getattr(exc, "response", None)
    headers = getattr(response, "headers", None) or {}
    try:
        retry_after = float(headers.get("retry-after"))
    except (TypeError, ValueError):
        retry_after = None
    backoff = min(TRANSIENT_RETRY_MAX_DELAY_SECONDS, 5.0 * 2 ** (attempt - 1))
    jitter = random.uniform(0, backoff * 0.25)
    if retry_after is not None:
        return min(TRANSIENT_RETRY_MAX_DELAY_SECONDS, max(retry_after, 1.0)) + jitter
    return backoff + jitter


class DefaultNativeToolGateway:
    """Translate one normalized turn to the selected provider's native API."""

    def complete(
        self,
        model: str,
        *,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None = None,
    ) -> NativeAgentTurn:
        """Call the provider, waiting out rate limits and transient outages."""
        for attempt in range(1, TRANSIENT_RETRY_ATTEMPTS + 1):
            try:
                return self._complete_once(
                    model,
                    system_prompt=system_prompt,
                    messages=messages,
                    tools=tools,
                    timeout_seconds=timeout_seconds,
                )
            except TRANSIENT_PROVIDER_ERRORS as exc:
                status = getattr(exc, "status_code", None)
                if isinstance(exc, (anthropic.APIStatusError, openai.APIStatusError)) and not (
                    status == 429 or (status is not None and status >= 500)
                ):
                    raise
                if attempt == TRANSIENT_RETRY_ATTEMPTS:
                    raise
                delay = _retry_delay_seconds(exc, attempt)
                log.warning(
                    "%s: errore transitorio del provider (%s, tentativo %d/%d), nuovo tentativo tra %.0f s",
                    model,
                    status or type(exc).__name__,
                    attempt,
                    TRANSIENT_RETRY_ATTEMPTS,
                    delay,
                )
                time.sleep(delay)
        raise AssertionError("unreachable")  # pragma: no cover

    def _complete_once(
        self,
        model: str,
        *,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None = None,
    ) -> NativeAgentTurn:
        provider = provider_for_model(model)
        if provider == "anthropic":
            return self._anthropic(
                model,
                system_prompt,
                messages,
                tools,
                timeout_seconds,
            )
        if provider == "openai" and openai_uses_responses(model):
            return self._openai_responses(
                model,
                system_prompt,
                messages,
                tools,
                timeout_seconds,
            )
        return self._openai_compatible(
            provider,
            model,
            system_prompt,
            messages,
            tools,
            timeout_seconds,
        )

    def _anthropic(
        self,
        model: str,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None,
    ) -> NativeAgentTurn:
        client = anthropic.Anthropic(timeout=timeout_seconds)
        request: dict[str, Any] = {
            "model": model,
            "max_tokens": _agent_max_output_tokens(),
            "system": system_prompt,
            "messages": _with_cache_breakpoints(_anthropic_messages(messages)),
            "tools": _anthropic_tools(tools),
        }
        if model.strip().lower().startswith(
            (*ANTHROPIC_REASONING_PREFIXES, "claude-opus-5", "claude-sonnet-5")
        ):
            request["thinking"] = {"type": "adaptive", "display": "omitted"}
            request["output_config"] = {"effort": _agent_reasoning_effort()}
        log_anthropic_request_diagnostics(
            log,
            config_module=benchmark_config,
            model=model,
            model_max_tokens=request["max_tokens"],
            request=request,
        )
        started = time.perf_counter()
        with client.messages.stream(**request) as stream:
            response = stream.get_final_message()
        calls = [
            NativeToolCall(
                id=str(block.id),
                name=str(block.name),
                arguments=_tool_arguments(block.input, tool_name=str(block.name)),
            )
            for block in response.content
            if getattr(block, "type", None) == "tool_use"
        ]
        text = "".join(
            getattr(block, "text", "")
            for block in response.content
            if getattr(block, "type", None) == "text"
        ).strip()
        return NativeAgentTurn(
            text=text,
            tool_calls=calls,
            metrics=build_model_call_metrics(
                provider="anthropic",
                model=model,
                latency_ms_value=latency_ms(started),
                usage=extract_usage(response),
            ),
            stop_reason=getattr(response, "stop_reason", None),
        )

    def _openai_responses(
        self,
        model: str,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None,
    ) -> NativeAgentTurn:
        """Use native Responses tool calling for current OpenAI models."""
        client = openai.OpenAI(timeout=timeout_seconds)
        max_output_tokens = int(
            os.environ.get("OPENAI_GENERATION_MAX_OUTPUT_TOKENS") or _agent_max_output_tokens()
        )
        reasoning_effort = (
            os.environ.get("OPENAI_GENERATION_REASONING_EFFORT") or _agent_reasoning_effort()
        ).strip()
        request: dict[str, Any] = {
            "model": model,
            "instructions": system_prompt,
            "input": _openai_response_input(messages),
            "tools": _openai_response_tools(tools),
            "tool_choice": "auto",
            "parallel_tool_calls": True,
            "max_output_tokens": max_output_tokens,
        }
        if model.strip().lower().startswith(OPENAI_REASONING_PREFIXES):
            request["reasoning"] = {"effort": reasoning_effort}

        started = time.perf_counter()
        response = client.responses.create(**request)
        calls = [
            NativeToolCall(
                id=str(getattr(item, "call_id")),
                name=str(getattr(item, "name")),
                arguments=_tool_arguments(
                    getattr(item, "arguments", "{}"),
                    tool_name=str(getattr(item, "name")),
                ),
            )
            for item in (getattr(response, "output", None) or [])
            if getattr(item, "type", None) == "function_call"
        ]
        text = (getattr(response, "output_text", None) or "").strip()
        status = getattr(response, "status", None)
        incomplete_value = getattr(response, "incomplete_details", None)
        incomplete_details = object_to_dict(incomplete_value)
        if incomplete_value is not None and "reason" not in incomplete_details:
            reason = getattr(incomplete_value, "reason", None)
            if reason is not None:
                incomplete_details["reason"] = reason
        metrics = build_model_call_metrics(
            provider="openai",
            model=model,
            latency_ms_value=latency_ms(started),
            usage=extract_usage(response),
        )
        metrics.update(
            {
                "api_style": "openai_responses_tool_calling",
                "response_id": getattr(response, "id", None),
                "response_status": status,
                "incomplete_details": incomplete_details,
            }
        )
        if not calls and not text:
            reason = incomplete_details.get("reason") or "no_output"
            raise ModelResponseError(
                "Risposta OpenAI priva di testo e function call "
                f"(status={status or 'unknown'}, reason={reason}).",
                metrics=metrics,
                retryable=status in {None, "completed"},
            )
        return NativeAgentTurn(
            text=text,
            tool_calls=calls,
            metrics=metrics,
            stop_reason="tool_use" if calls else status,
        )

    def _openai_compatible(
        self,
        provider: str,
        model: str,
        system_prompt: str,
        messages: list[dict[str, Any]],
        tools: list[ToolDefinition],
        timeout_seconds: float | None,
    ) -> NativeAgentTurn:
        if provider == "gemini":
            api_key = os.environ.get("GOOGLE_API_KEY")
            if not api_key:
                raise RuntimeError("GOOGLE_API_KEY non impostata in .env")
            client = openai.OpenAI(
                api_key=api_key,
                base_url=GEMINI_BASE_URL,
                timeout=timeout_seconds,
            )
        elif provider == "novita":
            api_key = os.environ.get("NOVITA_API_KEY")
            if not api_key:
                raise RuntimeError("NOVITA_API_KEY non impostata in .env")
            client = openai.OpenAI(
                api_key=api_key,
                base_url=NOVITA_BASE_URL,
                timeout=timeout_seconds,
            )
        else:
            client = openai.OpenAI(timeout=timeout_seconds)

        normalized = model.strip().lower()
        token_parameter = (
            "max_completion_tokens"
            if normalized.startswith(OPENAI_REASONING_PREFIXES)
            else "max_tokens"
        )
        request: dict[str, Any] = {
            "model": model,
            token_parameter: _agent_max_output_tokens(),
            "messages": _openai_messages(system_prompt, messages),
            "tools": _openai_tools(tools),
            "tool_choice": "auto",
        }
        if normalized.startswith(OPENAI_REASONING_PREFIXES):
            request["reasoning_effort"] = _agent_reasoning_effort()
        elif normalized.startswith(GEMINI_REASONING_PREFIXES):
            request["reasoning_effort"] = _agent_reasoning_effort()
        if provider == "novita" and normalized.startswith(NOVITA_REASONING_PREFIXES):
            request["reasoning_effort"] = _agent_reasoning_effort()
            request["extra_body"] = {"thinking": {"type": "enabled"}}
        if provider == "novita" and normalized.startswith("zai-org/"):
            request.update(
                {
                    "max_tokens": 65536,
                    "temperature": 1,
                    "top_p": 1,
                    "presence_penalty": 0,
                    "frequency_penalty": 0,
                    "response_format": {"type": "text"},
                }
            )
            request.pop("max_completion_tokens", None)
            extra_body = dict(request.get("extra_body") or {})
            extra_body.update(
                {
                    "top_k": 50,
                    "repetition_penalty": 1,
                    "min_p": 0,
                }
            )
            request["extra_body"] = extra_body

        started = time.perf_counter()
        response = client.chat.completions.create(**request)
        choice = response.choices[0]
        message = choice.message
        calls = [
            NativeToolCall(
                id=str(call.id),
                name=str(call.function.name),
                arguments=_tool_arguments(
                    call.function.arguments,
                    tool_name=str(call.function.name),
                ),
            )
            for call in (getattr(message, "tool_calls", None) or [])
        ]
        metrics = build_model_call_metrics(
            provider={"gemini": "google"}.get(provider, provider),
            model=model,
            latency_ms_value=latency_ms(started),
            usage=extract_usage(response),
        )
        metrics.update(
            {
                "api_style": "native_tool_calling_chat_completions",
                "finish_reason": getattr(choice, "finish_reason", None),
            }
        )
        return NativeAgentTurn(
            text=(message.content or "").strip(),
            tool_calls=calls,
            metrics=metrics,
            stop_reason=getattr(choice, "finish_reason", None),
        )


def default_native_tool_gateway() -> DefaultNativeToolGateway:
    return DefaultNativeToolGateway()
