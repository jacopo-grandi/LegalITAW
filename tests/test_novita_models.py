import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from legalitaw import config
from legalitaw.modeling import gateway, query
from legalitaw.modeling.runtime import (
    ANTHROPIC_STREAMING_REQUIRED_ERROR,
    ModelResponseError,
    anthropic_response_text,
)
from legalitaw.modeling.usage import ModelCallResult


class FakeCompletions:
    def __init__(self) -> None:
        self.kwargs: dict[str, object] | None = None

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.kwargs = kwargs
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content=" risposta glm ")
                )
            ]
        )


class FakeOpenAIClient:
    instances: list["FakeOpenAIClient"] = []

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.chat = SimpleNamespace(completions=FakeCompletions())
        self.responses = FakeResponses()
        self.instances.append(self)


class FakeResponses:
    response = SimpleNamespace(
        id="resp_fixture",
        status="completed",
        incomplete_details=None,
        output_text=" risposta openai ",
        usage=SimpleNamespace(
            input_tokens=10,
            output_tokens=20,
            total_tokens=30,
            output_tokens_details=SimpleNamespace(reasoning_tokens=5),
        ),
    )

    def __init__(self) -> None:
        self.kwargs: dict[str, object] | None = None

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.kwargs = kwargs
        return self.response


class FakeAnthropicStream:
    def __init__(self, response: SimpleNamespace) -> None:
        self.response = response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        return None

    def get_final_message(self) -> SimpleNamespace:
        return self.response


class FakeAnthropicMessages:
    def __init__(self, response: SimpleNamespace) -> None:
        self.response = response
        self.stream_calls: list[dict[str, object]] = []
        self.create_calls: list[dict[str, object]] = []

    def stream(self, **kwargs: object) -> FakeAnthropicStream:
        self.stream_calls.append(kwargs)
        return FakeAnthropicStream(self.response)

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.create_calls.append(kwargs)
        return self.response


class FakeAnthropicClient:
    instances: list["FakeAnthropicClient"] = []
    response = SimpleNamespace(content=[SimpleNamespace(type="text", text="ok")])

    def __init__(self) -> None:
        self.messages = FakeAnthropicMessages(self.response)
        self.instances.append(self)


class NovitaModelsTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeOpenAIClient.instances.clear()
        FakeAnthropicClient.instances.clear()
        FakeAnthropicClient.response = SimpleNamespace(
            content=[SimpleNamespace(type="text", text="ok")]
        )
        FakeResponses.response = SimpleNamespace(
            id="resp_fixture",
            status="completed",
            incomplete_details=None,
            output_text=" risposta openai ",
            usage=SimpleNamespace(
                input_tokens=10,
                output_tokens=20,
                total_tokens=30,
                output_tokens_details=SimpleNamespace(reasoning_tokens=5),
            ),
        )

    def test_glm_52_is_routed_to_novita(self) -> None:
        completion = ModelCallResult(text="ok", metrics={})
        with patch.object(
            gateway,
            "query_novita_with_metrics",
            return_value=completion,
        ) as query_novita:
            result = gateway.query_model("zai-org/glm-5.2", "Domanda", max_retries=1)

        self.assertEqual(result, "ok")
        query_novita.assert_called_once_with("zai-org/glm-5.2", "Domanda")

    def test_kimi_k3_is_routed_to_novita(self) -> None:
        completion = ModelCallResult(text="ok", metrics={})
        with patch.object(
            gateway,
            "query_novita_with_metrics",
            return_value=completion,
        ) as query_novita:
            result = gateway.query_model(
                "moonshotai/kimi-k3",
                "Domanda",
                max_retries=1,
            )

        self.assertEqual(result, "ok")
        query_novita.assert_called_once_with("moonshotai/kimi-k3", "Domanda")

    def test_gemini_is_routed_to_google(self) -> None:
        completion = ModelCallResult(text="ok", metrics={})
        with patch.object(
            gateway,
            "query_gemini_with_metrics",
            return_value=completion,
        ) as query_gemini:
            result = gateway.query_model("gemini-2.5-pro", "Domanda", max_retries=1)

        self.assertEqual(result, "ok")
        query_gemini.assert_called_once_with("gemini-2.5-pro", "Domanda")

    def test_gemini_uses_google_openai_compatible_endpoint(self) -> None:
        with patch.dict(os.environ, {"GOOGLE_API_KEY": "google-key"}, clear=False):
            with patch.object(query.openai, "OpenAI", FakeOpenAIClient):
                result = query.query_gemini("gemini-2.5-pro", "Domanda")

        self.assertEqual(result, "risposta glm")
        client = FakeOpenAIClient.instances[-1]
        self.assertEqual(client.api_key, "google-key")
        self.assertEqual(client.base_url, query.GEMINI_BASE_URL)

        kwargs = client.chat.completions.kwargs
        self.assertIsNotNone(kwargs)
        assert kwargs is not None
        self.assertEqual(kwargs["model"], "gemini-2.5-pro")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(kwargs["reasoning_effort"], "high")
        self.assertEqual(kwargs["messages"], [{"role": "user", "content": "Domanda"}])

    def test_non_reasoning_gemini_models_keep_default_request_shape(self) -> None:
        kwargs = query.default_gemini_completion_kwargs("gemini-2.0-flash", "Domanda")

        self.assertEqual(kwargs["model"], "gemini-2.0-flash")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertNotIn("reasoning_effort", kwargs)

    def test_glm_52_uses_novita_extra_body(self) -> None:
        with patch.dict(os.environ, {"NOVITA_API_KEY": "test-key"}, clear=False):
            with patch.object(query.openai, "OpenAI", FakeOpenAIClient):
                result = query.query_novita("zai-org/glm-5.2", "Domanda")

        self.assertEqual(result, "risposta glm")
        client = FakeOpenAIClient.instances[-1]
        self.assertEqual(client.base_url, query.NOVITA_BASE_URL)

        kwargs = client.chat.completions.kwargs
        self.assertIsNotNone(kwargs)
        assert kwargs is not None
        self.assertEqual(kwargs["model"], "zai-org/glm-5.2")
        self.assertEqual(kwargs["max_tokens"], query.NOVITA_GLM_52_MAX_TOKENS)
        self.assertEqual(kwargs["response_format"], {"type": "text"})
        self.assertEqual(kwargs["temperature"], 1)
        self.assertEqual(kwargs["top_p"], 1)
        self.assertEqual(kwargs["reasoning_effort"], "max")
        self.assertEqual(kwargs["presence_penalty"], 0)
        self.assertEqual(kwargs["frequency_penalty"], 0)
        self.assertEqual(
            kwargs["extra_body"],
            {
                "thinking": {"type": "enabled"},
                "top_k": 50,
                "repetition_penalty": 1,
                "min_p": 0,
            },
        )

    def test_deepseek_uses_max_reasoning_request_shape(self) -> None:
        kwargs = query.default_novita_completion_kwargs("deepseek/deepseek-v4-pro", "Domanda")

        self.assertEqual(kwargs["model"], "deepseek/deepseek-v4-pro")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(kwargs["reasoning_effort"], "max")
        self.assertEqual(kwargs["extra_body"], {"thinking": {"type": "enabled"}})
        self.assertNotIn("response_format", kwargs)

    def test_kimi_k3_uses_max_reasoning_request_shape(self) -> None:
        kwargs = query.default_novita_completion_kwargs("moonshotai/kimi-k3", "Domanda")

        self.assertEqual(kwargs["model"], "moonshotai/kimi-k3")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(kwargs["reasoning_effort"], "max")
        self.assertEqual(kwargs["extra_body"], {"thinking": {"type": "enabled"}})

    def test_non_reasoning_novita_models_keep_default_request_shape(self) -> None:
        kwargs = query.default_novita_completion_kwargs("mistralai/mistral-large", "Domanda")

        self.assertEqual(kwargs["model"], "mistralai/mistral-large")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertNotIn("reasoning_effort", kwargs)
        self.assertNotIn("extra_body", kwargs)
        self.assertNotIn("response_format", kwargs)

    def test_openai_gpt5_uses_max_completion_tokens(self) -> None:
        kwargs = query.default_openai_completion_kwargs("gpt-5.5", "Domanda")

        self.assertEqual(kwargs["model"], "gpt-5.5")
        self.assertEqual(kwargs["max_completion_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(kwargs["reasoning_effort"], "high")
        self.assertNotIn("max_tokens", kwargs)

    def test_openai_gpt5_generation_uses_responses_api(self) -> None:
        with patch.object(query.openai, "OpenAI", FakeOpenAIClient):
            result = query.query_openai_with_metrics("gpt-5.6-luna", "Domanda")

        self.assertEqual(result.text, "risposta openai")
        client = FakeOpenAIClient.instances[-1]
        kwargs = client.responses.kwargs
        self.assertIsNotNone(kwargs)
        assert kwargs is not None
        self.assertEqual(kwargs["model"], "gpt-5.6-luna")
        self.assertEqual(kwargs["input"], "Domanda")
        self.assertEqual(
            kwargs["reasoning"],
            {"effort": config.OPENAI_GENERATION_REASONING_EFFORT},
        )
        self.assertEqual(
            kwargs["max_output_tokens"],
            config.OPENAI_GENERATION_MAX_OUTPUT_TOKENS,
        )
        self.assertEqual(result.metrics["api_style"], "openai_responses")
        self.assertEqual(result.metrics["response_status"], "completed")
        self.assertEqual(result.metrics["reasoning_tokens"], 5)

    def test_openai_incomplete_response_preserves_diagnostics(self) -> None:
        FakeResponses.response = SimpleNamespace(
            id="resp_incomplete",
            status="incomplete",
            incomplete_details=SimpleNamespace(reason="max_output_tokens"),
            output_text="",
            usage=SimpleNamespace(
                input_tokens=100,
                output_tokens=32768,
                total_tokens=32868,
                output_tokens_details=SimpleNamespace(reasoning_tokens=32768),
            ),
        )
        with patch.object(query.openai, "OpenAI", FakeOpenAIClient):
            with self.assertRaises(ModelResponseError) as raised:
                query.query_openai_with_metrics("gpt-5.6-luna", "Domanda")

        error = raised.exception
        self.assertFalse(error.retryable)
        self.assertEqual(error.metrics["response_id"], "resp_incomplete")
        self.assertEqual(error.metrics["response_status"], "incomplete")
        self.assertEqual(
            error.metrics["incomplete_details"],
            {"reason": "max_output_tokens"},
        )
        self.assertEqual(error.metrics["reasoning_tokens"], 32768)

    def test_openai_legacy_models_keep_max_tokens(self) -> None:
        kwargs = query.default_openai_completion_kwargs("gpt-4o", "Domanda")

        self.assertEqual(kwargs["model"], "gpt-4o")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertNotIn("max_completion_tokens", kwargs)
        self.assertNotIn("reasoning_effort", kwargs)

    def test_openai_legacy_model_keeps_chat_completions_runtime(self) -> None:
        with patch.object(query.openai, "OpenAI", FakeOpenAIClient):
            result = query.query_openai_with_metrics("gpt-4o", "Domanda")

        self.assertEqual(result.text, "risposta glm")
        client = FakeOpenAIClient.instances[-1]
        self.assertIsNotNone(client.chat.completions.kwargs)
        self.assertIsNone(client.responses.kwargs)
        self.assertEqual(result.metrics["api_style"], "openai_chat_completions")

    def test_anthropic_answer_models_enable_max_adaptive_thinking(self) -> None:
        kwargs = query.default_anthropic_message_kwargs("claude-sonnet-4-6", "Domanda")

        self.assertEqual(kwargs["model"], "claude-sonnet-4-6")
        self.assertEqual(kwargs["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(kwargs["thinking"], {"type": "adaptive", "display": "omitted"})
        self.assertEqual(kwargs["output_config"], {"effort": "max"})

    def test_anthropic_response_text_skips_thinking_blocks(self) -> None:
        response = SimpleNamespace(
            content=[
                SimpleNamespace(type="thinking", text="hidden scratchpad"),
                SimpleNamespace(type="text", text=" risposta finale "),
            ]
        )

        self.assertEqual(anthropic_response_text(response), "risposta finale")

    def test_standard_anthropic_generation_uses_streaming_and_keeps_usage(self) -> None:
        FakeAnthropicClient.response = SimpleNamespace(
            content=[
                SimpleNamespace(type="thinking", text="hidden reasoning"),
                SimpleNamespace(type="text", text=" risposta "),
                SimpleNamespace(type="text", text="finale "),
            ],
            usage=SimpleNamespace(input_tokens=11, output_tokens=3),
        )

        with patch.object(query.anthropic, "Anthropic", FakeAnthropicClient):
            result = query.query_anthropic_with_metrics(
                "claude-sonnet-5",
                "Domanda",
            )

        self.assertEqual(result.text, "risposta finale")
        client = FakeAnthropicClient.instances[-1]
        self.assertEqual(client.messages.create_calls, [])
        self.assertEqual(len(client.messages.stream_calls), 1)
        request = client.messages.stream_calls[0]
        self.assertEqual(request["model"], "claude-sonnet-5")
        self.assertEqual(request["max_tokens"], config.MODEL_MAX_TOKENS)
        self.assertEqual(request["messages"], [{"role": "user", "content": "Domanda"}])
        self.assertEqual(result.metrics["input_tokens"], 11)
        self.assertEqual(result.metrics["output_tokens"], 3)

    def test_standard_retryable_error_still_uses_backoff(self) -> None:
        result = ModelCallResult(text="ok", metrics={})

        with patch(
            "legalitaw.modeling.gateway.query_anthropic_with_metrics",
            side_effect=[Exception("temporary network problem"), result],
        ) as mocked:
            with patch("legalitaw.modeling.query.time.sleep") as sleep:
                self.assertEqual(
                    gateway.query_model_with_metrics(
                        "claude-sonnet-5",
                        "Domanda",
                        max_retries=2,
                    ),
                    result,
                )

        self.assertEqual(mocked.call_count, 2)
        sleep.assert_called_once_with(2.0)

    def test_incomplete_model_response_is_not_retried(self) -> None:
        error = ModelResponseError(
            "incomplete",
            metrics={"response_status": "incomplete"},
            retryable=False,
        )
        with patch(
            "legalitaw.modeling.gateway.query_openai_with_metrics",
            side_effect=error,
        ) as mocked:
            with patch("legalitaw.modeling.query.time.sleep") as sleep:
                with self.assertRaises(ModelResponseError):
                    gateway.query_model_with_metrics(
                        "gpt-5.6-luna",
                        "Domanda",
                        max_retries=3,
                    )

        mocked.assert_called_once_with("gpt-5.6-luna", "Domanda")
        sleep.assert_not_called()

    def test_standard_streaming_required_error_is_not_retried(self) -> None:
        error = ValueError(ANTHROPIC_STREAMING_REQUIRED_ERROR)

        with patch(
            "legalitaw.modeling.gateway.query_anthropic_with_metrics",
            side_effect=error,
        ) as mocked:
            with patch("legalitaw.modeling.query.time.sleep") as sleep:
                self.assertIsNone(
                    gateway.query_model("claude-sonnet-5", "Domanda", max_retries=3)
                )

        mocked.assert_called_once_with("claude-sonnet-5", "Domanda")
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
