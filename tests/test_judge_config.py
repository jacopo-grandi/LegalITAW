import os
import unittest
from unittest.mock import patch

from legalitaw.config import build_judge_runtime_config, validate_judge_runtime_config


class JudgeConfigTest(unittest.TestCase):
    def test_defaults_are_adaptive_sonnet_gpt_opus(self) -> None:
        env = {
            "ANTHROPIC_API_KEY": "dummy",
            "OPENAI_API_KEY": "dummy",
        }
        with patch.dict(os.environ, env, clear=True):
            config = build_judge_runtime_config()
            validate_judge_runtime_config(config)

        self.assertEqual(config.strategy, "adaptive_majority")
        self.assertEqual(config.judge_a.provider, "anthropic")
        self.assertEqual(config.judge_a.model, "claude-sonnet-4-6")
        self.assertEqual(config.judge_b.provider, "openai")
        self.assertEqual(config.judge_b.model, "gpt-5.5")
        self.assertEqual(config.judge_c.provider, "anthropic")
        self.assertEqual(config.judge_c.model, "claude-opus-4-8")

    def test_single_strategy_override_does_not_require_openai_key(self) -> None:
        env = {
            "ANTHROPIC_API_KEY": "dummy",
            "JUDGE_STRATEGY": "single",
        }
        with patch.dict(os.environ, env, clear=True):
            config = build_judge_runtime_config()
            validate_judge_runtime_config(config)

        self.assertEqual(config.strategy, "single")
        self.assertEqual(config.judge_a.provider, "anthropic")

    def test_identical_a_b_warns(self) -> None:
        env = {
            "ANTHROPIC_API_KEY": "dummy",
            "JUDGE_STRATEGY": "adaptive_majority",
            "JUDGE_A_PROVIDER": "anthropic",
            "JUDGE_A_MODEL": "claude-sonnet-4-6",
            "JUDGE_B_PROVIDER": "anthropic",
            "JUDGE_B_MODEL": "claude-sonnet-4-6",
            "JUDGE_C_PROVIDER": "anthropic",
            "JUDGE_C_MODEL": "claude-sonnet-4-6",
        }
        with patch.dict(os.environ, env, clear=True):
            config = build_judge_runtime_config()
            with self.assertLogs("legalitaw.config", level="WARNING") as logs:
                validate_judge_runtime_config(config)

        self.assertIn("stesso provider e modello", " ".join(logs.output))

    def test_registered_openai_compatible_provider_accepts_its_own_key(self) -> None:
        config = build_judge_runtime_config(
            judge_a_provider="novita",
            judge_a_model="deepseek/deepseek-v4-pro",
            judge_b_provider="gemini",
            judge_b_model="gemini-3-pro",
            judge_c_provider="anthropic",
            judge_c_model="claude-opus-4-8",
        )

        validate_judge_runtime_config(
            config,
            api_keys={
                "novita": "novita-secret",
                "gemini": "google-secret",
                "anthropic": "anthropic-secret",
            },
        )

        self.assertEqual(config.judge_a.provider, "novita")
        self.assertEqual(config.judge_b.provider, "gemini")

    def test_targeted_audit_requires_only_primary_and_reviewer_keys(self) -> None:
        config = build_judge_runtime_config(
            judge_strategy="targeted_audit",
            judge_a_provider="openai",
            judge_a_model="gpt-5.6-luna",
            judge_b_provider="anthropic",
            judge_b_model="claude-sonnet-4-6",
            batch_size=10,
            audit_sample_rate=0.10,
        )

        validate_judge_runtime_config(
            config,
            api_keys={"openai": "openai-secret", "anthropic": "anthropic-secret"},
        )

        self.assertEqual(config.strategy, "targeted_audit")
        self.assertEqual(config.batch_size, 10)
        self.assertEqual(config.audit_sample_rate, 0.10)


if __name__ == "__main__":
    unittest.main()
