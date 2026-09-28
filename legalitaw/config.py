"""
Configurazione globale di LegalITA-W.
Tutte le costanti condivise tra i moduli stanno qui.
"""

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Mapping


log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths - tutti relativi alla root del progetto
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT_DIR / "results"
WORKFLOW2_TASKS_DIR = ROOT_DIR / "task_workflow2.0"
AGENTIC_TASKS_DIR = WORKFLOW2_TASKS_DIR
AGENTIC_RESULTS_DIR = RESULTS_DIR / "agentic"

# ---------------------------------------------------------------------------
# Evaluation - parametri del judge
# ---------------------------------------------------------------------------

JUDGE_TEMPERATURE: float = 0.0
JUDGE_MAX_TOKENS: int = int(os.environ.get("JUDGE_MAX_TOKENS", "3000"))
JUDGE_RETRIES: int = 3
TARGETED_AUDIT_BATCH_SIZE: int = int(os.environ.get("JUDGE_BATCH_SIZE", "10"))
TARGETED_AUDIT_SAMPLE_RATE: float = float(
    os.environ.get("JUDGE_AUDIT_SAMPLE_RATE", "0.05")
)

JUDGE_MODEL: str = "claude-sonnet-4-6"      # valutazione delle risposte

JudgeStrategy = Literal[
    "single",
    "batched_single",
    "adaptive_majority",
    "targeted_audit",
    "paired_consensus",
]
JudgeProvider = str
JudgeId = Literal["A", "B", "C"]
JudgeAPIStyle = Literal[
    "anthropic",
    "openai_responses",
    "openai_compatible",
    "typesafe_system_one",
]


@dataclass(frozen=True)
class JudgeProviderConfig:
    provider: str
    label: str
    api_key_env: str
    api_style: JudgeAPIStyle
    endpoint_label: str
    models: tuple[str, ...]
    base_url: str | None = None


JUDGE_PROVIDER_CONFIGS: tuple[JudgeProviderConfig, ...] = (
    JudgeProviderConfig(
        provider="anthropic",
        label="Anthropic",
        api_key_env="ANTHROPIC_API_KEY",
        api_style="anthropic",
        endpoint_label="Anthropic Messages API",
        models=(
            "claude-opus-5-5",
            "claude-opus-5",
            "claude-sonnet-5",
            "claude-opus-4-8",
            "claude-sonnet-4-6",
            "claude-sonnet-4-5-20250929",
        ),
    ),
    JudgeProviderConfig(
        provider="openai",
        label="OpenAI",
        api_key_env="OPENAI_API_KEY",
        api_style="openai_responses",
        endpoint_label="OpenAI Responses API",
        models=("gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", "gpt-5.5"),
    ),
    JudgeProviderConfig(
        provider="novita",
        label="Novita AI",
        api_key_env="NOVITA_API_KEY",
        api_style="openai_compatible",
        endpoint_label="Novita OpenAI-compatible API",
        models=(
            "deepseek/deepseek-v4-pro",
            "deepseek/deepseek-v4-flash-0731",
            "deepseek/deepseek-v4-flash",
            "zai-org/glm-5.2",
            "moonshotai/kimi-k3",
            "mistralai/mistral-large",
        ),
        base_url="https://api.novita.ai/openai",
    ),
    JudgeProviderConfig(
        provider="gemini",
        label="Google Gemini",
        api_key_env="GOOGLE_API_KEY",
        api_style="openai_compatible",
        endpoint_label="Gemini OpenAI-compatible API",
        models=("gemini-3-pro", "gemini-2.5-pro", "gemini-2.0-flash"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    ),
    JudgeProviderConfig(
        provider="typesafe",
        label="TypeSafe AI",
        api_key_env="TYPESAFE_API_KEY",
        api_style="typesafe_system_one",
        endpoint_label="TypeSafe System One API",
        models=("jev-latest", "jev-1.13.0"),
        base_url="https://api.typesafe.ai",
    ),
)

JUDGE_PROVIDER_CONFIG_BY_ID: dict[str, JudgeProviderConfig] = {
    item.provider: item for item in JUDGE_PROVIDER_CONFIGS
}

SUPPORTED_JUDGE_STRATEGIES: tuple[str, ...] = (
    "single",
    "batched_single",
    "adaptive_majority",
    "targeted_audit",
    "paired_consensus",
)
SUPPORTED_JUDGE_PROVIDERS: tuple[str, ...] = tuple(JUDGE_PROVIDER_CONFIG_BY_ID)
# Terna validata (audit del 26 settembre 2026): Jev e Luna giudicano tutti i
# criteri, Opus arbitra disaccordi, PASS con citazione non ritrovata e un
# campione di audit del 5%. Vedi docs/AUDIT_TERNA_2026-09-26.md.
DEFAULT_JUDGE_STRATEGY: JudgeStrategy = "paired_consensus"
DEFAULT_JUDGE_A_PROVIDER: JudgeProvider = "typesafe"
DEFAULT_JUDGE_A_MODEL: str = "jev-1.13.0"
DEFAULT_JUDGE_B_PROVIDER: JudgeProvider = "openai"
DEFAULT_JUDGE_B_MODEL: str = "gpt-5.6-luna"
DEFAULT_JUDGE_C_PROVIDER: JudgeProvider = "anthropic"
DEFAULT_JUDGE_C_MODEL: str = "claude-opus-5-5"


@dataclass(frozen=True)
class JudgeEndpointConfig:
    judge_id: JudgeId
    provider: JudgeProvider
    model: str


@dataclass(frozen=True)
class JudgeRuntimeConfig:
    strategy: JudgeStrategy
    judge_a: JudgeEndpointConfig
    judge_b: JudgeEndpointConfig
    judge_c: JudgeEndpointConfig
    batch_size: int = TARGETED_AUDIT_BATCH_SIZE
    audit_sample_rate: float = TARGETED_AUDIT_SAMPLE_RATE


def _env_value(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        return default
    return value.strip()


def _provider(value: str | None, default: str) -> JudgeProvider:
    provider = (value or default).strip().lower()
    if provider not in SUPPORTED_JUDGE_PROVIDERS:
        # Il messaggio completo viene costruito dalla validazione runtime.
        return provider
    return provider


def judge_provider_config(provider: str) -> JudgeProviderConfig:
    try:
        return JUDGE_PROVIDER_CONFIG_BY_ID[provider]
    except KeyError as exc:
        raise ValueError(f"Provider judge non supportato: {provider}") from exc


def build_judge_runtime_config(
    *,
    judge_strategy: str | None = None,
    judge_a_provider: str | None = None,
    judge_a_model: str | None = None,
    judge_b_provider: str | None = None,
    judge_b_model: str | None = None,
    judge_c_provider: str | None = None,
    judge_c_model: str | None = None,
    legacy_judge_model: str | None = None,
    batch_size: int | None = None,
    audit_sample_rate: float | None = None,
) -> JudgeRuntimeConfig:
    """Legge configurazione judge da override espliciti e variabili ambiente."""
    strategy = (
        judge_strategy
        or _env_value("JUDGE_STRATEGY")
        or DEFAULT_JUDGE_STRATEGY
    ).strip().lower()

    a_model = (
        judge_a_model
        or _env_value("JUDGE_A_MODEL")
        or legacy_judge_model
        or DEFAULT_JUDGE_A_MODEL
    )

    return JudgeRuntimeConfig(
        strategy=strategy,  # type: ignore[arg-type]
        judge_a=JudgeEndpointConfig(
            judge_id="A",
            provider=_provider(
                judge_a_provider or _env_value("JUDGE_A_PROVIDER"),
                DEFAULT_JUDGE_A_PROVIDER,
            ),
            model=a_model.strip(),
        ),
        judge_b=JudgeEndpointConfig(
            judge_id="B",
            provider=_provider(
                judge_b_provider or _env_value("JUDGE_B_PROVIDER"),
                DEFAULT_JUDGE_B_PROVIDER,
            ),
            model=(
                judge_b_model
                or _env_value("JUDGE_B_MODEL")
                or DEFAULT_JUDGE_B_MODEL
            ).strip(),
        ),
        judge_c=JudgeEndpointConfig(
            judge_id="C",
            provider=_provider(
                judge_c_provider or _env_value("JUDGE_C_PROVIDER"),
                DEFAULT_JUDGE_C_PROVIDER,
            ),
            model=(
                judge_c_model
                or _env_value("JUDGE_C_MODEL")
                or DEFAULT_JUDGE_C_MODEL
            ).strip(),
        ),
        batch_size=(
            batch_size
            if batch_size is not None
            else int(_env_value("JUDGE_BATCH_SIZE", str(TARGETED_AUDIT_BATCH_SIZE)))
        ),
        audit_sample_rate=(
            audit_sample_rate
            if audit_sample_rate is not None
            else float(
                _env_value(
                    "JUDGE_AUDIT_SAMPLE_RATE",
                    str(TARGETED_AUDIT_SAMPLE_RATE),
                )
            )
        ),
    )


def validate_judge_runtime_config(
    config: JudgeRuntimeConfig,
    *,
    api_keys: Mapping[str, str] | None = None,
) -> None:
    """Valida strategia, provider, modelli e credenziali senza esporre secret."""
    if config.strategy not in SUPPORTED_JUDGE_STRATEGIES:
        raise RuntimeError(
            "Strategia judge non supportata: "
            f"{config.strategy!r}. Valori ammessi: {', '.join(SUPPORTED_JUDGE_STRATEGIES)}"
        )

    if config.batch_size < 1 or config.batch_size > 50:
        raise RuntimeError("JUDGE_BATCH_SIZE deve essere compreso tra 1 e 50")
    if not 0.0 <= config.audit_sample_rate <= 1.0:
        raise RuntimeError("JUDGE_AUDIT_SAMPLE_RATE deve essere compreso tra 0 e 1")

    endpoints = [config.judge_a]
    if config.strategy in {"adaptive_majority", "targeted_audit", "paired_consensus"}:
        endpoints.append(config.judge_b)
    if config.strategy in {"adaptive_majority", "paired_consensus"}:
        endpoints.append(config.judge_c)

    errors: list[str] = []
    for endpoint in endpoints:
        if endpoint.provider not in SUPPORTED_JUDGE_PROVIDERS:
            errors.append(
                f"JUDGE_{endpoint.judge_id}_PROVIDER={endpoint.provider!r} non supportato"
            )
        if not endpoint.model:
            errors.append(f"JUDGE_{endpoint.judge_id}_MODEL mancante")
        key_name = _api_key_name(endpoint.provider)
        key_available = (
            bool(api_keys.get(endpoint.provider))
            if api_keys is not None
            else bool(key_name and os.environ.get(key_name))
        )
        if key_name and not key_available:
            errors.append(f"{key_name} mancante per Judge {endpoint.judge_id}")

    if errors:
        raise RuntimeError("Configurazione judge non valida: " + "; ".join(errors))

    if (
        config.strategy in {"adaptive_majority", "targeted_audit", "paired_consensus"}
        and config.judge_a.provider == config.judge_b.provider
        and config.judge_a.model == config.judge_b.model
    ):
        log.warning(
            "Judge A e Judge B usano stesso provider e modello (%s/%s): "
            "la maggioranza non e metodologicamente eterogenea.",
            config.judge_a.provider,
            config.judge_a.model,
        )


def _api_key_name(provider: str) -> str | None:
    definition = JUDGE_PROVIDER_CONFIG_BY_ID.get(provider)
    return definition.api_key_env if definition is not None else None

# ---------------------------------------------------------------------------
# Run - parametri dei modelli sotto esame
# ---------------------------------------------------------------------------

# Budget di output identico per tutti i modelli valutati.
# Include eventuali thinking/reasoning tokens per i modelli che li espongono.
MODEL_MAX_TOKENS: int = int(os.environ.get("MODEL_MAX_TOKENS", "16000"))

# GPT-5 reasoning and visible text share the same output budget. One-shot
# workflow deliverables need more headroom than short workspace tool calls.
OPENAI_GENERATION_MAX_OUTPUT_TOKENS: int = int(
    os.environ.get("OPENAI_GENERATION_MAX_OUTPUT_TOKENS", "32768")
)
OPENAI_GENERATION_REASONING_EFFORT: str = os.environ.get(
    "OPENAI_GENERATION_REASONING_EFFORT",
    "medium",
).strip()

# Politica unica per l'agente generico (tool calling), uguale per tutti i
# fornitori: stesso livello di ragionamento e stesso budget di output, in cui
# ragionamento e risposta si sommano. "high" e' accettato da OpenAI, Anthropic
# e dai modelli OpenAI-compatible di Novita/Gemini. Sovrascrivibili da env.
AGENT_REASONING_EFFORT: str = os.environ.get("AGENT_REASONING_EFFORT", "high").strip()
AGENT_MAX_OUTPUT_TOKENS: int = int(os.environ.get("AGENT_MAX_OUTPUT_TOKENS", "32768"))

# Numero massimo di tentativi per query a un modello sotto esame.
MODEL_RETRIES: int = 3
