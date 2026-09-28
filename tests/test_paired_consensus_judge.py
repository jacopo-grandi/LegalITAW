import unittest

from legalitaw.evaluation.judge import PairedConsensusJudge
from legalitaw.config import build_judge_runtime_config, validate_judge_runtime_config
from legalitaw.schemas import Criterion, JudgeVote

OUTPUT = "La clausola 6.1 limita la responsabilita' a euro 50.000."


def criteria(count, logic="required_presence"):
    return [
        Criterion(
            id=f"C-{index:03d}",
            title=f"Criterio {index}",
            match_criteria="PASS se presente.",
            category="legal",
            criterion_logic=logic,
        )
        for index in range(1, count + 1)
    ]


class FakeJudge:
    def __init__(self, judge_id, verdicts=None, *, evidence=None, errors=()):
        self.judge_id = judge_id
        self.provider = {"A": "typesafe", "B": "openai", "C": "anthropic"}[judge_id]
        self.model = f"fake-{judge_id}"
        self.verdicts = verdicts or {}
        self.evidence = evidence or {}
        self.errors = set(errors)
        self.calls = []

    def evaluate_batch(self, *, criteria, **kwargs):
        self.calls.append([item.id for item in criteria])
        votes = {}
        for item in criteria:
            if item.id in self.errors:
                votes[item.id] = JudgeVote(
                    judge_id=self.judge_id, provider=self.provider, model=self.model,
                    verdict=None, reasoning=None, status="error", error="x", attempts=1,
                )
                continue
            verdict = self.verdicts.get(item.id, "pass")
            evidence = self.evidence.get(item.id, ["clausola 6.1 limita"])
            votes[item.id] = JudgeVote(
                judge_id=self.judge_id, provider=self.provider, model=self.model,
                verdict=verdict, reasoning=verdict, status="ok", attempts=1,
                evidence=evidence,
                evidence_status="found" if evidence else "not_found",
            )
        return votes


def run(judge, items):
    return judge.evaluate_criteria(
        task_id="WF2-TEST", task_description="t", agent_output=OUTPUT, criteria=items,
    )


class PairedConsensusJudgeTest(unittest.TestCase):
    def test_agreement_is_accepted_without_arbiter(self):
        a, b, c = FakeJudge("A"), FakeJudge("B"), FakeJudge("C", {"C-001": "fail"})
        judge = PairedConsensusJudge(a, b, c, batch_size=10, audit_sample_rate=0.0)
        results = run(judge, criteria(3))
        self.assertEqual({r.consensus_method for r in results.values()}, {"initial_agreement"})
        self.assertEqual(c.calls, [])

    def test_disagreement_is_decided_by_arbiter_in_batches(self):
        items = criteria(12)
        b_verdicts = {item.id: "fail" for item in items}
        a, b = FakeJudge("A"), FakeJudge("B", b_verdicts, evidence={i.id: [] for i in items})
        c = FakeJudge("C", {item.id: "fail" for item in items})
        judge = PairedConsensusJudge(a, b, c, batch_size=10, audit_sample_rate=0.0)
        results = run(judge, items)
        self.assertTrue(all(r.verdict == "fail" for r in results.values()))
        self.assertTrue(all(r.consensus_method == "tie_breaker" for r in results.values()))
        self.assertEqual([len(call) for call in c.calls], [10, 2])
        self.assertEqual(results["C-001"].supporting_judges, ["C", "B"])

    def test_agreed_pass_with_missing_quote_goes_to_arbiter(self):
        items = criteria(2)
        b = FakeJudge("B", evidence={"C-001": ["frase che non esiste"]})
        c = FakeJudge("C", {"C-001": "fail"})
        judge = PairedConsensusJudge(FakeJudge("A"), b, c, audit_sample_rate=0.0)
        results = run(judge, items)
        self.assertEqual(results["C-001"].verdict, "fail")
        self.assertEqual(results["C-001"].consensus_method, "evidence_tie_breaker")
        self.assertEqual(results["C-002"].consensus_method, "initial_agreement")
        self.assertEqual(c.calls, [["C-001"]])

    def test_absence_criteria_do_not_need_a_quote(self):
        items = criteria(2, logic="prohibited_presence")
        b = FakeJudge("B", evidence={item.id: [] for item in items})
        c = FakeJudge("C")
        judge = PairedConsensusJudge(FakeJudge("A"), b, c, audit_sample_rate=0.0)
        results = run(judge, items)
        self.assertEqual({r.consensus_method for r in results.values()}, {"initial_agreement"})
        self.assertEqual(c.calls, [])

    def test_audit_measures_but_does_not_change_the_verdict(self):
        items = criteria(20)
        c = FakeJudge("C", {item.id: "fail" for item in items})
        judge = PairedConsensusJudge(FakeJudge("A"), FakeJudge("B"), c, audit_sample_rate=0.1)
        results = run(judge, items)
        audited = [r for r in results.values() if r.consensus_method == "agreement_audited"]
        self.assertEqual(len(audited), 2)
        self.assertTrue(all(r.verdict == "pass" for r in results.values()))
        self.assertEqual(judge.last_diagnostics["audit_disagreements"], 2)

    def test_invalid_vote_without_arbiter_is_unresolved(self):
        items = criteria(1)
        a = FakeJudge("A", errors={"C-001"})
        c = FakeJudge("C", errors={"C-001"})
        judge = PairedConsensusJudge(a, FakeJudge("B"), c, audit_sample_rate=0.0)
        self.assertEqual(run(judge, items)["C-001"].verdict, "unresolved")

    def test_strategy_is_configurable(self):
        config = build_judge_runtime_config(
            judge_strategy="paired_consensus",
            judge_a_provider="typesafe", judge_a_model="jev-1.13.0",
            judge_b_provider="openai", judge_b_model="gpt-5.6-luna",
            judge_c_provider="anthropic", judge_c_model="claude-opus-5-5",
            batch_size=10, audit_sample_rate=0.05,
        )
        validate_judge_runtime_config(
            config, api_keys={"typesafe": "x", "openai": "x", "anthropic": "x"}
        )
        self.assertEqual(config.judge_c.model, "claude-opus-5-5")


class AnthropicResponseParsingTest(unittest.TestCase):
    def test_thinking_block_before_answer_is_skipped(self):
        from types import SimpleNamespace

        from legalitaw.evaluation.judge import _anthropic_text, _raise_if_truncated

        response = SimpleNamespace(
            content=[
                SimpleNamespace(type="thinking", thinking="ragiono..."),
                SimpleNamespace(type="text", text='{"results": []}'),
            ],
            stop_reason="end_turn",
        )
        self.assertEqual(_anthropic_text(response), '{"results": []}')
        _raise_if_truncated(response)
        truncated = SimpleNamespace(
            content=[], stop_reason="max_tokens", usage=SimpleNamespace(output_tokens=6000)
        )
        with self.assertRaisesRegex(ValueError, "troncata"):
            _raise_if_truncated(truncated)


if __name__ == "__main__":
    unittest.main()
