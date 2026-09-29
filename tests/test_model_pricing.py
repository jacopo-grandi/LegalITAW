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


if __name__ == "__main__":
    unittest.main()
