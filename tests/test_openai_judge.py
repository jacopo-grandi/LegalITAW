from types import SimpleNamespace
import unittest

import httpx
import openai

from legalitaw.evaluation.judge import (
    BatchCriterionDecision,
    BatchJudgeDecision,
    JudgeDecision,
    OpenAIJudge,
)
from legalitaw.schemas import Criterion


INPUTS = {
    "task_description": "Q",
    "agent_output": "A",
    "criterion_title": "C",
    "match_criteria": "PASS se ok. FAIL se no.",
    "citation_context": None,
}


class FakeResponse:
    def __init__(self, output_parsed=None, output=None):
        self.output_parsed = output_parsed
        self.output = output or []


class FakeResponses:
    def __init__(self, items):
        self.items = list(items)
        self.calls = []

    def parse(self, **kwargs):
        self.calls.append(kwargs)
        item = self.items.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


class FakeClient:
    def __init__(self, items):
        self.responses = FakeResponses(items)


def judge(items, *, max_retries=1):
    return OpenAIJudge(
        judge_id="B",
        model="fake-openai",
        client=FakeClient(items),
        max_retries=max_retries,
        base_delay=0,
    )


def request() -> httpx.Request:
    return httpx.Request("POST", "https://api.openai.com/v1/responses")


class OpenAIJudgeTest(unittest.TestCase):
    def test_batch_returns_one_vote_per_criterion(self) -> None:
        adapter = OpenAIJudge(
            judge_id="A",
            model="gpt-5.6-luna",
            client=FakeClient(
                [
                    FakeResponse(
                        BatchJudgeDecision(
                            results=[
                                BatchCriterionDecision(
                                    criterion_id="C-001",
                                    verdict="pass",
                                    reasoning="ok",
                                    evidence_status="found",
                                    evidence=["A"],
                                ),
                                BatchCriterionDecision(
                                    criterion_id="C-002",
                                    verdict="fail",
                                    reasoning="omesso",
                                    evidence_status="not_found",
                                ),
                            ]
                        )
                    )
                ]
            ),
            max_retries=1,
            base_delay=0,
        )

        votes = adapter.evaluate_batch(
            task_description="Q",
            agent_output="A",
            criteria=[
                Criterion(id="C-001", title="Uno", match_criteria="PASS se A"),
                Criterion(id="C-002", title="Due", match_criteria="PASS se B"),
            ],
        )

        self.assertEqual(votes["C-001"].verdict, "pass")
        self.assertEqual(votes["C-002"].verdict, "fail")
        call = adapter.client.responses.calls[0]
        self.assertEqual(call["text_format"], BatchJudgeDecision)
        self.assertEqual(call["reasoning"], {"effort": "none"})

    def test_luna_uses_no_reasoning_and_stable_prompt_cache_key(self) -> None:
        adapter = OpenAIJudge(
            judge_id="A",
            model="gpt-5.6-luna",
            client=FakeClient(
                [FakeResponse(JudgeDecision(verdict="pass", reasoning="ok"))]
            ),
            max_retries=1,
            base_delay=0,
        )

        adapter.evaluate(**INPUTS)

        call = adapter.client.responses.calls[0]
        self.assertEqual(call["reasoning"], {"effort": "none"})
        self.assertTrue(call["prompt_cache_key"].startswith("legalita-judge-"))

    def test_valid_parsed_output(self) -> None:
        adapter = judge(
            [
                FakeResponse(
                    JudgeDecision(
                        verdict="pass",
                        reasoning="ok",
                        evidence_status="found",
                        evidence=["A"],
                    )
                )
            ]
        )

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertEqual(vote.verdict, "pass")
        self.assertEqual(vote.evidence_status, "found")
        self.assertEqual(vote.evidence, ["A"])
        call = adapter.client.responses.calls[0]
        self.assertFalse(call["store"])
        self.assertNotIn("tools", call)
        self.assertNotIn("previous_response_id", call)
        self.assertEqual(call["text_format"], JudgeDecision)

    def test_prompt_requires_exact_response_evidence(self) -> None:
        adapter = judge(
            [
                FakeResponse(
                    JudgeDecision(
                        verdict="fail",
                        reasoning="omesso",
                        evidence_status="not_found",
                        evidence=[],
                    )
                )
            ]
        )

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.evidence_status, "not_found")
        payload = str(adapter.client.responses.calls[0]["input"])
        self.assertIn("estratti brevi, continui e testuali", payload)
        self.assertIn('evidence_status="not_found"', payload)
        self.assertIn(
            "mancata menzione soddisfa il criterio e comporta PASS",
            payload,
        )
        self.assertIn(
            "ricevere FAIL soltanto con evidence_status=\"found\"",
            payload,
        )

    def test_invalid_verdict_returns_error(self) -> None:
        adapter = judge([FakeResponse({"verdict": "maybe", "reasoning": "bad"})])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIsNone(vote.verdict)

    def test_output_parsed_absent_returns_error(self) -> None:
        adapter = judge([FakeResponse(None)])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIn("output_parsed", vote.error or "")

    def test_refusal_returns_error(self) -> None:
        refusal_output = [
            SimpleNamespace(content=[SimpleNamespace(refusal="cannot comply")])
        ]
        adapter = judge([FakeResponse(JudgeDecision(verdict="pass", reasoning="ok"), refusal_output)])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIn("refusal", (vote.error or "").lower())

    def test_rate_limit_returns_error(self) -> None:
        response = httpx.Response(429, request=request())
        adapter = judge([openai.RateLimitError("rate", response=response, body=None)])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIn("RateLimitError", vote.error or "")

    def test_timeout_returns_error(self) -> None:
        adapter = judge([openai.APITimeoutError(request())])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIn("APITimeoutError", vote.error or "")

    def test_api_error_returns_error(self) -> None:
        adapter = judge([openai.APIError("api", request(), body=None)])

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "error")
        self.assertIn("APIError", vote.error or "")

    def test_retry_succeeds(self) -> None:
        adapter = judge(
            [
                openai.APIError("api", request(), body=None),
                FakeResponse({"verdict": "fail", "reasoning": "no"}),
            ],
            max_retries=2,
        )

        vote = adapter.evaluate(**INPUTS)

        self.assertEqual(vote.status, "ok")
        self.assertEqual(vote.verdict, "fail")
        self.assertEqual(vote.attempts, 2)
        self.assertEqual(len(adapter.client.responses.calls), 2)

    def test_prompt_contains_no_prior_judge_data(self) -> None:
        adapter = judge([FakeResponse({"verdict": "pass", "reasoning": "ok"})])

        adapter.evaluate(**INPUTS)

        payload = str(adapter.client.responses.calls[0]["input"])
        self.assertNotIn("SECRET_A_REASONING", payload)
        self.assertNotIn("A=PASS", payload)
        self.assertNotIn("B=FAIL", payload)


if __name__ == "__main__":
    unittest.main()
