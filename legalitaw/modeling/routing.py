"""Provider routing for evaluated model identifiers."""

from __future__ import annotations

from collections.abc import Callable
from typing import Literal, TypeVar

ModelProvider = Literal["anthropic", "gemini", "novita", "openai"]
Adapter = TypeVar("Adapter", bound=Callable[..., object])

NOVITA_MODEL_PREFIXES = (
    "deepseek/",
    "meta-llama/",
    "qwen/",
    "mistralai/",
    "moonshotai/",
    "zai-org/",
)
GEMINI_MODEL_PREFIX = "gemini-"
OPENAI_MODEL_PREFIXES = ("gpt", "o1", "o3", "o4")


def provider_for_model(model: str) -> ModelProvider:
    """Resolve the provider from the public model identifier."""
    if model.startswith(NOVITA_MODEL_PREFIXES):
        return "novita"
    if model.startswith(GEMINI_MODEL_PREFIX):
        return "gemini"
    if model.startswith("claude"):
        return "anthropic"
    if model.startswith(OPENAI_MODEL_PREFIXES):
        return "openai"
    raise ValueError(f"Modello non supportato: {model}")


def select_adapter(
    model: str,
    *,
    anthropic: Adapter,
    gemini: Adapter,
    novita: Adapter,
    openai: Adapter,
) -> Adapter:
    """Select an injected adapter without coupling routing to SDK clients."""
    provider = provider_for_model(model)
    return {
        "anthropic": anthropic,
        "gemini": gemini,
        "novita": novita,
        "openai": openai,
    }[provider]
