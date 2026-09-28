from types import SimpleNamespace
import unittest

from legalitaw.evaluation.judge import AnthropicJudge, JudgeDecision, OpenAIJudge


STANDARD_INPUTS = {
    "task_description": "Q",
    "agent_output": "A",
    "criterion_title": "C",
    "match_criteria": "PASS se ok. FAIL se no.",
    "citation_context": None,
}


class FakeAnthropicMessages:
    def __init__(self, text: str) -> None:
        self.text = text
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(content=[SimpleNamespace(text=self.text)])


class FakeAnthropicClient:
    def __init__(self, text: str) -> None:
        self.messages = FakeAnthropicMessages(text)


class FakeResponses:
    def __init__(self, parsed) -> None:
        self.parsed = parsed
        self.calls: list[dict] = []

    def parse(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(output_parsed=self.parsed, output=[])


class FakeOpenAIClient:
    def __init__(self, parsed) -> None:
        self.responses = FakeResponses(parsed)


class JudgeTemperatureTest(unittest.TestCase):
    def test_standard_openai_gpt5_omits_temperature(self) -> None:
        client = FakeOpenAIClient(JudgeDecision(verdict="pass", reasoning="ok"))
        judge = OpenAIJudge(
            judge_id="B",
            model="gpt-5.5",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(**STANDARD_INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertNotIn("temperature", client.responses.calls[0])

    def test_standard_openai_legacy_keeps_temperature(self) -> None:
        client = FakeOpenAIClient(JudgeDecision(verdict="pass", reasoning="ok"))
        judge = OpenAIJudge(
            judge_id="B",
            model="gpt-4o",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(**STANDARD_INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertIn("temperature", client.responses.calls[0])

    def test_standard_anthropic_opus4_omits_temperature(self) -> None:
        client = FakeAnthropicClient('{"verdict": "pass", "reasoning": "ok"}')
        judge = AnthropicJudge(
            judge_id="C",
            model="claude-opus-4-8",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(**STANDARD_INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertNotIn("temperature", client.messages.calls[0])

    def test_standard_anthropic_sonnet_keeps_temperature(self) -> None:
        client = FakeAnthropicClient('{"verdict": "pass", "reasoning": "ok"}')
        judge = AnthropicJudge(
            judge_id="A",
            model="claude-sonnet-4-6",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(**STANDARD_INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertIn("temperature", client.messages.calls[0])

    def test_standard_anthropic_generation5_omits_temperature(self) -> None:
        for model in ("claude-opus-5", "claude-sonnet-5"):
            with self.subTest(model=model):
                client = FakeAnthropicClient(
                    '{"verdict": "pass", "reasoning": "ok"}'
                )
                judge = AnthropicJudge(
                    judge_id="A",
                    model=model,
                    client=client,
                    max_retries=1,
                )

                vote = judge.evaluate(**STANDARD_INPUTS)

                self.assertEqual(vote.status, "ok")
                self.assertNotIn("temperature", client.messages.calls[0])

    def test_standard_anthropic_parses_fenced_json_with_prose(self) -> None:
        client = FakeAnthropicClient(
            'Ecco il verdetto:\n```json\n{"verdict": "PASS", "reasoning": "ok"}\n```'
        )
        judge = AnthropicJudge(
            judge_id="A",
            model="claude-sonnet-4-6",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(**STANDARD_INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertEqual(vote.verdict, "pass")


if __name__ == "__main__":
    unittest.main()
