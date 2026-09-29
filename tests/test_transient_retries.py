import unittest
from unittest.mock import patch

import httpx
import openai

from legalitaw.modeling import tool_calling
from legalitaw.modeling.tool_calling import DefaultNativeToolGateway, NativeAgentTurn


def _status_error(cls, status: int, headers: dict | None = None):
    request = httpx.Request("POST", "https://api.novita.ai/openai/chat/completions")
    response = httpx.Response(status, request=request, headers=headers or {})
    return cls(f"errore {status}", response=response, body=None)


class TransientRetryTest(unittest.TestCase):
    def _run(self, errors):
        calls = {"n": 0}

        def once(self, model, **kwargs):
            calls["n"] += 1
            if errors:
                raise errors.pop(0)
            return NativeAgentTurn(text="ok")

        with patch.object(DefaultNativeToolGateway, "_complete_once", once), patch.object(
            tool_calling.time, "sleep"
        ) as sleep:
            turn = DefaultNativeToolGateway().complete(
                "deepseek/deepseek-v4-flash", system_prompt="s", messages=[], tools=[]
            )
        return turn, calls["n"], sleep

    def test_rate_limit_is_waited_out(self) -> None:
        errors = [
            _status_error(openai.RateLimitError, 429, {"retry-after": "7"}),
            _status_error(openai.InternalServerError, 503),
        ]
        turn, calls, sleep = self._run(errors)
        self.assertEqual(turn.text, "ok")
        self.assertEqual(calls, 3)
        self.assertGreaterEqual(sleep.call_args_list[0].args[0], 7)

    def test_credit_errors_are_not_retried(self) -> None:
        errors = [_status_error(openai.APIStatusError, 402)]
        with self.assertRaises(openai.APIStatusError):
            self._run(errors)

    def test_gives_up_after_the_last_attempt(self) -> None:
        errors = [
            _status_error(openai.RateLimitError, 429)
            for _ in range(tool_calling.TRANSIENT_RETRY_ATTEMPTS)
        ]
        with self.assertRaises(openai.RateLimitError):
            self._run(errors)


if __name__ == "__main__":
    unittest.main()
