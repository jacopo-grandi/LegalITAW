import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from legalitaw.evaluation import judge as judge_module
from legalitaw.evaluation.judge import JEV_REPLAY_ENV, TypeSafeJevJudge
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
            judge = TypeSafeJevJudge(client=client, max_retries=1, model="jev-1.13.0")
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
            judge = TypeSafeJevJudge(client=client, max_retries=1, model="jev-1.13.0")
            criteria = [Criterion(id="A.1", title="Presenza", match_criteria="PASS se presente")]
            with patch.dict(os.environ, {JEV_REPLAY_ENV: tmp}):
                votes = judge.evaluate_batch(task_description="Q", agent_output="Testo diverso", criteria=criteria)
            self.assertEqual(votes["A.1"].verdict, "fail")
            self.assertEqual(len(client.payloads), 1)

    def test_other_jev_model_is_not_reused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _write_score(Path(tmp), "Testo giudicato")
            client = _Client()
            judge = TypeSafeJevJudge(client=client, max_retries=1, model="jev-2.0.0")
            criteria = [Criterion(id="A.1", title="Presenza", match_criteria="PASS se presente")]
            with patch.dict(os.environ, {JEV_REPLAY_ENV: tmp}):
                judge.evaluate_batch(task_description="Q", agent_output="Testo giudicato", criteria=criteria)
            self.assertEqual(len(client.payloads), 1)


if __name__ == "__main__":
    unittest.main()
