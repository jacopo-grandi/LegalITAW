from types import SimpleNamespace
import unittest
from unittest.mock import patch

from legalitaw.config import AGENT_MAX_OUTPUT_TOKENS, AGENT_REASONING_EFFORT
from legalitaw.modeling.tool_calling import (
    DefaultNativeToolGateway,
    ToolDefinition,
    _openai_response_input,
)


TOOL = ToolDefinition(
    name="read",
    description="Read a workspace file.",
    input_schema={
        "type": "object",
        "properties": {"path": {"type": "string"}},
        "required": ["path"],
    },
)


class FakeResponses:
    def __init__(self, response) -> None:
        self.response = response
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.response


class FakeChatCompletions:
    def __init__(self, response=None) -> None:
        self.response = response
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.response is None:
            raise AssertionError("Chat Completions non deve essere chiamato")
        return self.response


class FakeOpenAIClient:
    def __init__(self, *, response=None, chat_response=None) -> None:
        self.responses = FakeResponses(response)
        self.chat = SimpleNamespace(
            completions=FakeChatCompletions(chat_response),
        )


class FakeAnthropicStream:
    def __init__(self, response) -> None:
        self.response = response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def get_final_message(self):
        return self.response


class FakeAnthropicMessages:
    def __init__(self, response) -> None:
        self.response = response
        self.calls: list[dict] = []

    def stream(self, **kwargs):
        self.calls.append(kwargs)
        return FakeAnthropicStream(self.response)


class FakeAnthropicClient:
    def __init__(self, response) -> None:
        self.messages = FakeAnthropicMessages(response)


class NativeToolGatewayTest(unittest.TestCase):
    def test_openai_reasoning_model_uses_responses_with_native_tools(self) -> None:
        response = SimpleNamespace(
            id="resp_1",
            status="completed",
            output_text="",
            output=[
                SimpleNamespace(
                    type="function_call",
                    call_id="call_1",
                    name="read",
                    arguments='{"path":"documents/a.pdf"}',
                )
            ],
            usage=SimpleNamespace(input_tokens=20, output_tokens=5),
            incomplete_details=None,
        )
        client = FakeOpenAIClient(response=response)

        with patch("legalitaw.modeling.tool_calling.openai.OpenAI", return_value=client):
            turn = DefaultNativeToolGateway().complete(
                "gpt-5.6-luna",
                system_prompt="workspace",
                messages=[{"role": "user", "content": "task"}],
                tools=[TOOL],
            )

        self.assertEqual(turn.tool_calls[0].name, "read")
        self.assertEqual(turn.tool_calls[0].arguments, {"path": "documents/a.pdf"})
        self.assertEqual(turn.metrics["api_style"], "openai_responses_tool_calling")
        self.assertEqual(client.chat.completions.calls, [])
        request = client.responses.calls[0]
        self.assertEqual(request["instructions"], "workspace")
        self.assertEqual(request["tools"][0]["name"], "read")
        # Politica unica dell'agente (AGENT_REASONING_EFFORT), uguale per tutti i fornitori.
        self.assertEqual(request["reasoning"]["effort"], AGENT_REASONING_EFFORT)
        self.assertEqual(request["max_output_tokens"], AGENT_MAX_OUTPUT_TOKENS)

    def test_responses_transcript_replays_calls_and_outputs(self) -> None:
        items = _openai_response_input(
            [
                {"role": "user", "content": "task"},
                {
                    "role": "assistant",
                    "content": "",
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "name": "read",
                            "arguments": {"path": "documents/a.pdf"},
                        }
                    ],
                },
                {
                    "role": "tool",
                    "tool_call_id": "call_1",
                    "content": '{"ok":true}',
                },
            ]
        )

        self.assertEqual(items[1]["type"], "function_call")
        self.assertEqual(items[1]["call_id"], "call_1")
        self.assertEqual(items[2]["type"], "function_call_output")
        self.assertEqual(items[2]["call_id"], "call_1")

    def test_openai_legacy_model_keeps_chat_completions(self) -> None:
        chat_response = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="done", tool_calls=[]),
                    finish_reason="stop",
                )
            ],
            usage=SimpleNamespace(prompt_tokens=10, completion_tokens=2),
        )
        client = FakeOpenAIClient(chat_response=chat_response)

        with patch("legalitaw.modeling.tool_calling.openai.OpenAI", return_value=client):
            turn = DefaultNativeToolGateway().complete(
                "gpt-4o",
                system_prompt="workspace",
                messages=[{"role": "user", "content": "task"}],
                tools=[TOOL],
            )

        self.assertEqual(turn.text, "done")
        self.assertEqual(len(client.chat.completions.calls), 1)
        self.assertEqual(client.responses.calls, [])
        self.assertNotIn("reasoning_effort", client.chat.completions.calls[0])

    def test_gemini_stays_on_compatible_chat_endpoint(self) -> None:
        chat_response = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="done", tool_calls=[]),
                    finish_reason="stop",
                )
            ],
            usage=SimpleNamespace(prompt_tokens=10, completion_tokens=2),
        )
        client = FakeOpenAIClient(chat_response=chat_response)

        with patch.dict("os.environ", {"GOOGLE_API_KEY": "test"}):
            with patch("legalitaw.modeling.tool_calling.openai.OpenAI", return_value=client):
                turn = DefaultNativeToolGateway().complete(
                    "gemini-3-pro",
                    system_prompt="workspace",
                    messages=[{"role": "user", "content": "task"}],
                    tools=[TOOL],
                )

        self.assertEqual(turn.text, "done")
        request = client.chat.completions.calls[0]
        self.assertEqual(request["reasoning_effort"], "high")
        self.assertEqual(client.responses.calls, [])

    def test_novita_stays_on_compatible_chat_endpoint(self) -> None:
        chat_response = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="done", tool_calls=[]),
                    finish_reason="stop",
                )
            ],
            usage=SimpleNamespace(prompt_tokens=10, completion_tokens=2),
        )
        client = FakeOpenAIClient(chat_response=chat_response)

        with patch.dict("os.environ", {"NOVITA_API_KEY": "test"}):
            with patch("legalitaw.modeling.tool_calling.openai.OpenAI", return_value=client):
                turn = DefaultNativeToolGateway().complete(
                    "deepseek/deepseek-v4-pro",
                    system_prompt="workspace",
                    messages=[{"role": "user", "content": "task"}],
                    tools=[TOOL],
                )

        self.assertEqual(turn.text, "done")
        request = client.chat.completions.calls[0]
        self.assertEqual(request["reasoning_effort"], AGENT_REASONING_EFFORT)
        self.assertEqual(request["max_tokens"], AGENT_MAX_OUTPUT_TOKENS)
        self.assertEqual(request["extra_body"], {"thinking": {"type": "enabled"}})
        self.assertEqual(client.responses.calls, [])

    def test_anthropic_uses_native_message_tools(self) -> None:
        response = SimpleNamespace(
            content=[
                SimpleNamespace(
                    type="tool_use",
                    id="tool_1",
                    name="read",
                    input={"path": "documents/a.pdf"},
                )
            ],
            usage=SimpleNamespace(input_tokens=10, output_tokens=2),
            stop_reason="tool_use",
        )
        client = FakeAnthropicClient(response)

        with patch(
            "legalitaw.modeling.tool_calling.anthropic.Anthropic",
            return_value=client,
        ):
            turn = DefaultNativeToolGateway().complete(
                "claude-sonnet-4-6",
                system_prompt="workspace",
                messages=[{"role": "user", "content": "task"}],
                tools=[TOOL],
            )

        self.assertEqual(turn.tool_calls[0].name, "read")
        request = client.messages.calls[0]
        self.assertEqual(request["tools"][0]["name"], "read")
        self.assertEqual(request["thinking"]["type"], "adaptive")


if __name__ == "__main__":
    unittest.main()
