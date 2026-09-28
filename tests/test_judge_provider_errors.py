"""Errori dei fornitori dei giudici: credito finito interrompe, 404 si ritenta, checkpoint in errore si rifanno."""
from __future__ import annotations

import io
from urllib.error import HTTPError

import pytest

from legalitaw.benchmark.agentic_v2 import _has_judge_errors
from legalitaw.evaluation.judge import JudgeProviderFatalError, TypeSafeJevJudge
from legalitaw.schemas import Criterion


class _Client:
    def __init__(self, codes):
        self.codes = list(codes)
        self.calls = 0

    def system_one(self, payload):
        self.calls += 1
        code = self.codes.pop(0)
        if code == 200:
            return {"answers": {q: {"type": "noul", "noul": 0.9} for q in payload["questions"]}}
        raise HTTPError("https://api.typesafe.ai/v1/systemone", code, "err", {}, io.BytesIO(b'{"error":"x"}'))


def _judge(codes):
    return TypeSafeJevJudge(client=_Client(codes), base_delay=0, max_retries=3)


CRITERIA = [Criterion(id="A.1", title="t", match_criteria="m")]


def test_payment_required_interrompe():
    judge = _judge([402])
    with pytest.raises(JudgeProviderFatalError):
        judge.evaluate_batch(task_description="d", agent_output="o", criteria=CRITERIA)
    assert judge.client.calls == 1


def test_404_viene_ritentato():
    judge = _judge([404, 200])
    votes = judge.evaluate_batch(task_description="d", agent_output="o", criteria=CRITERIA)
    assert votes["A.1"].status == "ok" and judge.client.calls == 2


def test_errore_riporta_il_corpo_della_risposta():
    judge = _judge([400])
    votes = judge.evaluate_batch(task_description="d", agent_output="o", criteria=CRITERIA)
    assert votes["A.1"].status == "error" and '"error"' in (votes["A.1"].error or "")


def test_checkpoint_con_voti_in_errore_va_rifatto():
    ok = {"criteria_results": [{"judge_votes": [{"status": "ok"}, {"status": "ok"}]}]}
    ko = {"criteria_results": [{"judge_votes": [{"status": "ok"}, {"status": "error"}]}]}
    assert not _has_judge_errors(ok)
    assert _has_judge_errors(ko)


def test_credito_finito_interrompe_anche_dentro_la_terna():
    from legalitaw.evaluation.judge import PairedConsensusJudge
    from tests.test_paired_consensus_judge import FakeJudge, criteria, run

    a = _judge([402])
    b, c = FakeJudge("B"), FakeJudge("C")
    with pytest.raises(JudgeProviderFatalError):
        run(PairedConsensusJudge(a, b, c, batch_size=10, audit_sample_rate=0.0), criteria(3))
    assert c.calls == []


def test_i_token_dei_giudici_finiscono_nei_diagnostici_e_nel_riepilogo():
    from legalitaw.benchmark.agentic_v2 import _judge_usage
    from legalitaw.evaluation.judge import PairedConsensusJudge, _record_usage
    from tests.test_paired_consensus_judge import FakeJudge, criteria, run

    class Counting(FakeJudge):
        def evaluate_batch(self, **kwargs):
            _record_usage(self, {"usage": {"input_tokens": 1000, "output_tokens": 10}})
            return super().evaluate_batch(**kwargs)

    a, b, c = Counting("A"), Counting("B"), Counting("C")
    a.model, b.model = "jev-1.13.0", "gpt-5.6-luna"
    judge = PairedConsensusJudge(a, b, c, batch_size=10, audit_sample_rate=0.0)
    run(judge, criteria(3))
    usage = judge.last_diagnostics["usage"]
    assert usage["A"]["input_tokens"] == 1000 and usage["B"]["calls"] == 1
    summary = _judge_usage([{"judge_diagnostics": {"targeted_audit": judge.last_diagnostics}}, {}])
    assert summary["tasks_with_usage"] == 1 and summary["tasks_without_usage"] == 1
    assert summary["per_judge"]["A"]["input_tokens"] == 1000
    assert summary["per_judge"]["B"]["estimated_cost_usd"] > 0
