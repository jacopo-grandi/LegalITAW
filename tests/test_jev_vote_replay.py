import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from legalitaw.evaluation import judge as judge_module
from legalitaw.evaluation.judge import JEV_REPLAY_ENV, ReplayingJudge, TypeSafeJevJudge
from legalitaw.schemas import Criterion


class _Client:
    def __init__(self) -> None:
        self.payloads: list[dict] = []

    def system_one(self, payload):
        self.payloads.append(payload)
        questions = payload.get("questions") or payload.get("schema", {}).get("properties", {})
        n = len(questions) if questions else 1
        return {
            "model": "jev-1.13.0",
            "answers": {f"criterion_{i}": {"type": "noul", "noul": 0.2} for i in range(n)},
            "usage": {"input_tokens": 10, "output_tokens": 1},
        }


def _write_score(directory: Path, output: str) -> None:
    (directory / "scores").mkdir(parents=True)
    payload = {
        "task_id": "WF2-001",
        "model_output": output,
        "criteria_results": [
            {
                "id": "A.1",
                "title": "Presenza",
                "judge_votes": [
                    {"judge_id": "A", "provider": "typesafe", "model": "jev-1.13.0", "verdict": "pass",
                     "status": "ok", "probability": 0.91}
                ],
            },
            {
                "id": "A.2",
                "title": "Errore del giudice",
                "judge_votes": [
                    {"judge_id": "A", "provider": "typesafe", "model": "jev-1.13.0", "verdict": "unresolved",
                     "status": "error", "probability": None}
                ],
            },
        ],
    }
    (directory / "scores" / "WF2-001.json").write_text(json.dumps(payload), encoding="utf-8")


class JevVoteReplayTest(unittest.TestCase):
    def setUp(self) -> None:
        judge_module._JEV_REPLAY_CACHE.clear()

    def test_reuses_prior_vote_and_judges_only_the_rest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _write_score(Path(tmp), "Testo giudicato")
            client = _Client()
            judge = ReplayingJudge(TypeSafeJevJudge(client=client, max_retries=1, model="jev-1.13.0"))
            criteria = [
                Criterion(id="A.1", title="Presenza", match_criteria="PASS se presente"),
                Criterion(id="A.2", title="Errore del giudice", match_criteria="PASS se presente"),
            ]
            with patch.dict(os.environ, {JEV_REPLAY_ENV: tmp}):
                votes = judge.evaluate_batch(task_description="Q", agent_output="Testo giudicato", criteria=criteria)
            self.assertEqual(votes["A.1"].verdict, "pass")
            self.assertEqual(votes["A.1"].probability, 0.91)
            self.assertEqual(votes["A.1"].attempts, 0)
            self.assertEqual(len(client.payloads), 1)  # solo A.2, che in origine era fallito
            self.assertEqual(judge.replayed_votes, 1)

    def test_different_output_is_judged_again(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _write_score(Path(tmp), "Testo giudicato")
            client = _Client()
            judge = ReplayingJudge(TypeSafeJevJudge(client=client, max_retries=1, model="jev-1.13.0"))
            criteria = [Criterion(id="A.1", title="Presenza", match_criteria="PASS se presente")]
            with patch.dict(os.environ, {JEV_REPLAY_ENV: tmp}):
                votes = judge.evaluate_batch(task_description="Q", agent_output="Testo diverso", criteria=criteria)
            self.assertEqual(votes["A.1"].verdict, "fail")
            self.assertEqual(len(client.payloads), 1)

    def test_other_jev_model_is_not_reused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _write_score(Path(tmp), "Testo giudicato")
            client = _Client()
            judge = ReplayingJudge(TypeSafeJevJudge(client=client, max_retries=1, model="jev-2.0.0"))
            criteria = [Criterion(id="A.1", title="Presenza", match_criteria="PASS se presente")]
            with patch.dict(os.environ, {JEV_REPLAY_ENV: tmp}):
                judge.evaluate_batch(task_description="Q", agent_output="Testo giudicato", criteria=criteria)
            self.assertEqual(len(client.payloads), 1)


class _FakeJudge:
    def __init__(self, judge_id, provider, model, verdict="fail"):
        self.judge_id, self.provider, self.model, self.verdict = judge_id, provider, model, verdict
        self.calls: list[list[str]] = []

    def evaluate_batch(self, task_description, agent_output, criteria, citation_context=None):
        from legalitaw.schemas import JudgeVote

        self.calls.append([c.id for c in criteria])
        return {
            c.id: JudgeVote(judge_id=self.judge_id, provider=self.provider, model=self.model, verdict=self.verdict,
                            reasoning="live", status="ok", attempts=1)
            for c in criteria
        }


class PairedReplayTest(unittest.TestCase):
    def setUp(self) -> None:
        judge_module._JEV_REPLAY_CACHE.clear()

    def _score(self, tmp: Path, name: str, provider: str, model: str, verdicts: dict) -> None:
        d = tmp / name / "scores"
        d.mkdir(parents=True)
        results = [
            {"id": cid, "title": f"T{cid}", "judge_votes": [
                {"judge_id": "A", "provider": provider, "model": model, "verdict": v, "status": "ok",
                 "probability": None, "evidence": ["frase"] if v == "pass" else [], "evidence_status": "found" if v == "pass" else "unavailable"}]}
            for cid, v in verdicts.items()
        ]
        (d / "WF2-001.json").write_text(json.dumps({"task_id": "WF2-001", "model_output": "Testo", "criteria_results": results}))

    def test_arbiter_only_on_disagreements(self) -> None:
        from legalitaw.evaluation.judge import VOTE_REPLAY_ENV, PairedConsensusJudge

        with tempfile.TemporaryDirectory() as raw:
            tmp = Path(raw)
            self._score(tmp, "jev", "typesafe", "jev-1.13.0", {"1": "pass", "2": "pass", "3": "fail"})
            self._score(tmp, "luna", "openai", "gpt-5.6-luna", {"1": "pass", "2": "fail", "3": "fail"})
            a = _FakeJudge("A", "typesafe", "jev-1.13.0")
            b = _FakeJudge("B", "openai", "gpt-5.6-luna")
            c = _FakeJudge("C", "anthropic", "claude-opus-5-5", verdict="pass")
            env = {VOTE_REPLAY_ENV: os.pathsep.join([str(tmp / "jev"), str(tmp / "luna")]), "LEGALITA_TIE_BREAKER_SCOPE": "disagreements"}
            with patch.dict(os.environ, env):
                judge = PairedConsensusJudge(ReplayingJudge(a), ReplayingJudge(b), c, audit_sample_rate=0.0)
                criteria = [Criterion(id=i, title=f"T{i}", match_criteria="m") for i in ("1", "2", "3")]
                out = judge.evaluate_criteria(task_id="WF2-001", task_description="Q", agent_output="Testo", criteria=criteria)
            self.assertEqual(a.calls, [])
            self.assertEqual(b.calls, [])
            self.assertEqual(c.calls, [["2"]])  # solo il disaccordo; il PASS concorde senza citazione non va all'arbitro
            self.assertEqual(out["1"].verdict, "pass")
            self.assertEqual(out["2"].verdict, "pass")
            self.assertEqual(out["3"].verdict, "fail")
            self.assertEqual(judge.last_diagnostics["replayed_votes"], {"A": 3, "B": 3})


if __name__ == "__main__":
    unittest.main()
