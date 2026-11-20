import io
import tempfile
import unittest
from pathlib import Path

from legalitaw.cli.v2 import build_parser
from legalitaw.cli.valuta import arbitro_provider, build_jobs, valuta

IDS = [f"WF2-{n:03d}" for n in range(1, 101)]


def parse(*extra: str):
    return build_parser().parse_args(["valuta", "gemini-4-neon", *extra])


def value(argv, flag):
    return argv[argv.index(flag) + 1]


class BuildJobsTests(unittest.TestCase):
    def test_standard_plan(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            phase1, terna, source = build_jobs(parse("--risultati", tmp), IDS, today="2026-11-20")
            self.assertEqual(source, Path(tmp) / "gemini-4-neon-low-wf2-100")
            self.assertEqual([j.label for j in phase1], ["jev", "luna p1", "luna p2"])
            jev, p1, p2 = phase1
            self.assertEqual(value(jev.argv, "--judge-a-model"), "jev-1.13.0")
            self.assertNotIn("--tasks", jev.argv)
            self.assertEqual(p1.argv[p1.argv.index("--tasks") + 1 :], IDS[:50])
            self.assertEqual(p2.argv[p2.argv.index("--tasks") + 1 :], IDS[50:])
            self.assertEqual(p1.out, Path(tmp) / "v2-scores" / "gemini-4-neon-low-wf2-100-luna-p1" / "2026-11-20")
            reuse = terna.argv[terna.argv.index("--reuse-votes") + 1 : terna.argv.index("--tie-breaker-scope")]
            self.assertEqual(reuse, [str(jev.out), str(p1.out), str(p2.out)])
            self.assertEqual(value(terna.argv, "--judge-c-model"), "claude-opus-5-5")
            self.assertEqual(value(terna.argv, "--judge-c-provider"), "anthropic")
            self.assertEqual(terna.out.parent.name, "gemini-4-neon-low-wf2-100-terna-disaccordi")

    def test_resumes_latest_folder_and_other_arbiter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            old = Path(tmp) / "v2-scores" / "neon-wf2-100-jev" / "2026-11-19"
            old.mkdir(parents=True)
            phase1, terna, _ = build_jobs(
                parse("--risultati", tmp, "--nome", "neon", "--arbitro", "gpt-6.1-sol", "--parti-luna", "1"),
                IDS,
                today="2026-11-20",
            )
            self.assertEqual(phase1[0].out, old)
            self.assertEqual([j.label for j in phase1], ["jev", "luna"])
            self.assertNotIn("--tasks", phase1[1].argv)
            self.assertEqual(value(terna.argv, "--judge-c-provider"), "openai")
            self.assertEqual(terna.out.parent.name, "neon-wf2-100-terna-gpt-6.1-sol")
            fresh, _, _ = build_jobs(parse("--risultati", tmp, "--nome", "neon", "--nuova"), IDS, today="2026-11-20")
            self.assertEqual(fresh[0].out.name, "2026-11-20")

    def test_unknown_arbiter_provider(self) -> None:
        with self.assertRaises(ValueError):
            arbitro_provider("deepseek/deepseek-v4")


class FakeProcess:
    def __init__(self, code):
        self.code = code

    def poll(self):
        return self.code

    def wait(self, timeout=None):
        return self.code


class ValutaFlowTests(unittest.TestCase):
    def _run(self, codes):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "gemini-4-neon-low-wf2-100").mkdir()
            launched = []

            def popen(argv, **kwargs):
                label = value(argv, "--judge-strategy") + ":" + value(argv, "--judge-a-model")
                launched.append(label)
                return FakeProcess(codes.get(len(launched), 0))

            out = io.StringIO()
            code = valuta(parse("--risultati", tmp), IDS, popen=popen, sleep=lambda _: None, out=out, today="2026-11-20")
            return code, launched, out.getvalue()

    def test_terna_starts_after_jev_and_luna(self) -> None:
        code, launched, text = self._run({})
        self.assertEqual(code, 0)
        self.assertEqual(launched[-1], "paired_consensus:jev-1.13.0")
        self.assertEqual(len(launched), 4)
        self.assertIn("Fase 2", text)

    def test_failed_judge_blocks_terna(self) -> None:
        code, launched, text = self._run({2: 1})
        self.assertEqual(code, 1)
        self.assertEqual(len(launched), 3)
        self.assertIn("la terna non parte", text)

    def test_missing_run_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = io.StringIO()
            self.assertEqual(valuta(parse("--risultati", tmp), IDS, out=out), 2)
            self.assertIn("non trovata", out.getvalue())


if __name__ == "__main__":
    unittest.main()
