from types import SimpleNamespace
import unittest

from legalitaw.evaluation.judge import OpenAICompatibleJudge


class FakeChatCompletions:
    def __init__(self, content: str) -> None:
        self.content = content
        self.calls: list[dict[str, object]] = []

    def create(self, **kwargs: object) -> object:
        self.calls.append(kwargs)
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=self.content))]
        )


class FakeChatClient:
    def __init__(self, content: str) -> None:
        self.chat = SimpleNamespace(completions=FakeChatCompletions(content))


class OpenAICompatibleJudgesTest(unittest.TestCase):
    def test_novita_reasoning_judge_uses_chat_completions(self) -> None:
        client = FakeChatClient('{"verdict":"pass","reasoning":"corretto"}')
        judge = OpenAICompatibleJudge(
            judge_id="B",
            provider="novita",
            model="deepseek/deepseek-v4-pro",
            client=client,
            max_retries=1,
        )

        vote = judge.evaluate(
            task_description="Quesito",
            agent_output="Risposta",
            criterion_title="Criterio",
            match_criteria="PASS se corretto.",
        )

        self.assertEqual(vote.status, "ok")
        self.assertEqual(vote.provider, "novita")
        call = client.chat.completions.calls[0]
        self.assertEqual(call["model"], "deepseek/deepseek-v4-pro")
        self.assertEqual(call["reasoning_effort"], "max")


if __name__ == "__main__":
    unittest.main()
