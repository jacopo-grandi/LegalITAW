import json
import os
import unittest
from unittest.mock import patch

from legalitaw.benchmark.agentic_run import JUDGE_TOKEN_PRICES_USD_PER_MTOK
from legalitaw.modeling.usage import (
    DEFAULT_MODEL_PRICING_USD_PER_1M,
    DEFAULT_PRICE_TABLE_SOURCE,
    estimate_cost_usd,
)


class ModelPricingTest(unittest.TestCase):
    def test_builtin_table_prices_evaluated_models_without_env(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            cost, source = estimate_cost_usd(
                provider="anthropic",
                model="claude-sonnet-5-5",
                token_usage={"input_tokens": 1_000_000, "output_tokens": 100_000},
            )
        self.assertEqual(source, DEFAULT_PRICE_TABLE_SOURCE)
        self.assertAlmostEqual(cost, 2.00 + 1.00)

    def test_cached_input_is_billed_at_the_cache_rate(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            cost, _ = estimate_cost_usd(
                provider="anthropic",
                model="claude-opus-5-5",
                token_usage={
                    "input_tokens": 1_000_000,
                    "cached_input_tokens": 800_000,
                    "output_tokens": 0,
                },
            )
        self.assertAlmostEqual(cost, 0.2 * 4.00 + 0.8 * 0.40)

    def test_env_table_replaces_the_builtin_one(self) -> None:
        env = {"MODEL_PRICING_USD_PER_1M": json.dumps({"claude-sonnet-5-5": {"input": 1, "output": 1}})}
        with patch.dict(os.environ, env, clear=True):
            cost, source = estimate_cost_usd(
                provider="anthropic",
                model="claude-sonnet-5-5",
                token_usage={"input_tokens": 1_000_000, "output_tokens": 1_000_000},
            )
            missing, _ = estimate_cost_usd(
                provider="openai",
                model="gpt-5.6-luna",
                token_usage={"input_tokens": 1, "output_tokens": 1},
            )
        self.assertEqual(source, "MODEL_PRICING_USD_PER_1M")
        self.assertAlmostEqual(cost, 2.0)
        self.assertIsNone(missing)

    def test_generation_and_judge_tables_agree_on_list_prices(self) -> None:
        for model, price in DEFAULT_MODEL_PRICING_USD_PER_1M.items():
            with self.subTest(model=model):
                self.assertEqual(
                    JUDGE_TOKEN_PRICES_USD_PER_MTOK[model],
                    (price["input"], price["output"]),
                )



class AnthropicPromptCacheTest(unittest.TestCase):
    def test_breakpoints_mark_current_and_previous_user_turns(self) -> None:
        from legalitaw.modeling.tool_calling import _with_cache_breakpoints

        messages = [
            {"role": "user", "content": "incarico"},
            {"role": "assistant", "content": [{"type": "tool_use", "id": "t1", "name": "read", "input": {}}]},
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "t1", "content": "testo"}]},
        ]
        marked = _with_cache_breakpoints(messages)
        self.assertEqual(marked[0]["content"][-1]["cache_control"], {"type": "ephemeral"})
        self.assertEqual(marked[0]["content"][-1]["text"], "incarico")
        self.assertEqual(marked[2]["content"][-1]["cache_control"], {"type": "ephemeral"})
        self.assertNotIn("cache_control", str(marked[1]))
        self.assertEqual(messages[0]["content"], "incarico")  # input non modificato

    def test_anthropic_cache_tokens_are_counted_and_billed(self) -> None:
        from legalitaw.modeling.usage import build_model_call_metrics

        usage = {
            "input_tokens": 1_000,
            "cache_read_input_tokens": 90_000,
            "cache_creation_input_tokens": 9_000,
            "output_tokens": 2_000,
        }
        with patch.dict(os.environ, {}, clear=True):
            metrics = build_model_call_metrics(
                provider="anthropic", model="claude-sonnet-5-5", latency_ms_value=1, usage=usage
            )
        self.assertEqual(metrics["input_tokens"], 100_000)
        self.assertEqual(metrics["cached_input_tokens"], 90_000)
        self.assertEqual(metrics["cache_write_input_tokens"], 9_000)
        expected = (1_000 * 2.00 + 90_000 * 0.20 + 9_000 * 2.50 + 2_000 * 10.00) / 1_000_000
        self.assertAlmostEqual(metrics["estimated_cost_usd"], expected)


if __name__ == "__main__":
    unittest.main()
