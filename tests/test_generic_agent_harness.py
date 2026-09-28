"""Offline checks for the minimal LegalITA generic-agent harness."""

from __future__ import annotations

from copy import deepcopy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from legalitaw.agentic.generic_agent import (
    GENERIC_AGENT_TOOLS,
    GenericAgentWorkspace,
    generate_generic_agent_submission,
    generic_agent_system_prompt,
    generic_tool_definitions,
)
from legalitaw.agentic.loader import select_tasks
from legalitaw.agentic.workspace import WorkspaceRunFailure, public_envelope_paths
from legalitaw.modeling.tool_calling import (
    NativeAgentTurn,
    NativeToolCall,
    _anthropic_messages,
    _openai_messages,
)
from legalitaw.benchmark.agentic_service import persist_run


ROOT = Path(__file__).resolve().parents[1] / "task_workflow2.0"


class FixtureGateway:
    def __init__(self, task_text: str) -> None:
        self.task_text = task_text
        self.calls = 0
        self.messages = []
        self.system_prompts = []
        self.tool_names = []

    def complete(self, model, *, system_prompt, messages, tools, timeout_seconds=None):
        self.calls += 1
        self.messages.append(deepcopy(messages))
        self.system_prompts.append(system_prompt)
        self.tool_names.append([tool.name for tool in tools])
        if self.calls == 1:
            return NativeAgentTurn(
                tool_calls=[
                    NativeToolCall(
                        id="call-1",
                        name="write",
                        arguments={
                            "path": "/output/result.md",
                            "content": "# Risultato\n\nContenuto di prova.",
                        },
                    )
                ],
                metrics={"provider": "fixture", "total_tokens": 10},
                stop_reason="tool_use",
            )
        return NativeAgentTurn(
            text="Done",
            metrics={"provider": "fixture", "total_tokens": 4},
            stop_reason="stop",
        )


class CostGateway:
    def complete(
        self,
        model,
        *,
        system_prompt,
        messages,
        tools,
        timeout_seconds=None,
    ):
        return NativeAgentTurn(
            text="stop",
            metrics={
                "provider": "fixture",
                "estimated_cost_usd": 0.6,
                "total_tokens": 1,
            },
            stop_reason="stop",
        )


class GenericAgentHarnessChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.task = select_tasks(["WF2-001"], root=ROOT)[0]
        cls.task_text = (cls.task.directory / "public/01_task.md").read_text(
            encoding="utf-8"
        )

    def test_tool_surface_is_invariant_and_generic(self) -> None:
        self.assertEqual(
            tuple(tool.name for tool in generic_tool_definitions()),
            GENERIC_AGENT_TOOLS,
        )
        prompt = generic_agent_system_prompt("bare")
        self.assertNotIn(self.task.spec.task_id, prompt)
        self.assertNotIn("rubric", prompt.casefold())
        self.assertNotIn("finalization", prompt.casefold())
        self.assertNotIn("submit", prompt.casefold())
        self.assertNotIn("max_turn", prompt.casefold())
        self.assertNotIn("timeout", prompt.casefold())

    def test_normalized_transcript_uses_native_provider_tool_messages(self) -> None:
        messages = [
            {"role": "user", "content": "task"},
            {
                "role": "assistant",
                "content": "",
                "tool_calls": [
                    {"id": "c1", "name": "read", "arguments": {"path": "documents/a"}},
                    {"id": "c2", "name": "glob", "arguments": {"pattern": "*"}},
                ],
            },
            {"role": "tool", "tool_call_id": "c1", "content": "first"},
            {"role": "tool", "tool_call_id": "c2", "content": "second"},
        ]
        openai_messages = _openai_messages("system", messages)
        self.assertEqual(openai_messages[0], {"role": "system", "content": "system"})
        self.assertEqual(openai_messages[2]["tool_calls"][0]["type"], "function")
        self.assertEqual(openai_messages[3]["tool_call_id"], "c1")

        anthropic_messages = _anthropic_messages(messages)
        self.assertEqual(
            [item["role"] for item in anthropic_messages],
            ["user", "assistant", "user"],
        )
        self.assertEqual(anthropic_messages[1]["content"][0]["type"], "tool_use")
        self.assertEqual(len(anthropic_messages[2]["content"]), 2)


    def test_all_workflow2_tasks_declare_generic_agent_support(self) -> None:
        tasks = select_tasks(["all"], root=ROOT)
        self.assertEqual(len(tasks), 100)
        self.assertTrue(
            all("generic_agent" in task.spec.supported_execution_modes for task in tasks)
        )
        self.assertTrue(
            all(task.spec.output_mode == "prompt_only_free_artifacts" for task in tasks)
        )

    def test_response_templates_are_never_model_visible(self) -> None:
        tasks = select_tasks(["all"], root=ROOT)
        for task in tasks:
            with self.subTest(task_id=task.spec.task_id):
                self.assertNotIn(
                    "public/response_template.md",
                    public_envelope_paths(task),
                )
                task_text = (task.directory / "public/01_task.md").read_text(
                    encoding="utf-8"
                )
                self.assertNotIn("response_template", task_text)

        template_task = next(
            task for task in tasks if task.spec.task_id == "WF2-061"
        )
        workspace = GenericAgentWorkspace(template_task)
        try:
            listing = workspace.execute(
                "glob", {"pattern": "**/*", "path": "/documents"}
            )
            self.assertFalse(
                any("response_template" in path for path in listing["matches"])
            )
        finally:
            workspace.close()

    def test_workspace_copies_public_documents_once(self) -> None:
        class CountingWorkspace(GenericAgentWorkspace):
            copy_calls = 0

            def _copy_documents(self) -> None:
                self.copy_calls += 1
                super()._copy_documents()

        workspace = CountingWorkspace(self.task)
        try:
            self.assertEqual(workspace.copy_calls, 1)
        finally:
            workspace.close()

    def test_workspace_mounts_only_public_documents(self) -> None:
        workspace = GenericAgentWorkspace(self.task)
        try:
            listing = workspace.execute("glob", {"pattern": "**/*", "path": "/documents"})
            self.assertTrue(listing["matches"])
            self.assertFalse(any("01_task.md" in path for path in listing["matches"]))
            self.assertFalse(any("private" in path for path in listing["matches"]))
            with self.assertRaises(Exception):
                workspace.execute("read", {"path": "../private/rubric.json"})
            with self.assertRaises(Exception):
                workspace.execute(
                    "write",
                    {"path": "/documents/tamper.md", "content": "no"},
                )
            profile = workspace._sandbox_profile()
            self.assertIn("(deny network*)", profile)
            self.assertNotIn("(allow process*)", profile)
            self.assertNotIn(str(self.task.directory.resolve()), profile)
        finally:
            workspace.close()

    def test_read_extracts_text_from_matter_documents(self) -> None:
        read_tool = next(tool for tool in generic_tool_definitions() if tool.name == "read")
        self.assertIn("PDF", read_tool.description)
        cases = {
            "WF2-002": (".pdf", "[PAGINA 1]"),
            "WF2-043": (".docx", None),
            "WF2-037": (".xlsx", "[FOGLIO"),
            "WF2-041": (".eml", "From:"),
        }
        for task_id, (suffix, marker) in cases.items():
            with self.subTest(task_id=task_id, suffix=suffix):
                task = select_tasks([task_id], root=ROOT)[0]
                workspace = GenericAgentWorkspace(task)
                try:
                    matches = workspace.execute(
                        "glob", {"pattern": f"**/*{suffix}", "path": "/documents"}
                    )["matches"]
                    self.assertTrue(matches)
                    result = workspace.execute("read", {"path": matches[0], "limit": 20})
                    self.assertEqual(result["extracted_from"], suffix.lstrip("."))
                    self.assertGreater(result["total_lines"], 5)
                    self.assertNotIn("=C3=", result["content"])
                    if marker:
                        self.assertIn(marker, result["content"])
                finally:
                    workspace.close()

    def test_tool_arguments_tolerate_literal_control_characters(self) -> None:
        from legalitaw.modeling.tool_calling import _tool_arguments

        parsed = _tool_arguments(
            '{"path": "output/nota.md", "content": "# Titolo\nriga due\tfine"}',
            tool_name="write",
        )
        self.assertEqual(parsed["content"], "# Titolo\nriga due\tfine")
        self.assertEqual(
            _tool_arguments('```json\n{"path": "x"}\n```', tool_name="read"),
            {"path": "x"},
        )
        with self.assertRaisesRegex(ValueError, "argomenti JSON non validi.*inizio"):
            _tool_arguments('{"path": "a", "content": "aperto', tool_name="write")

    def test_loop_preserves_user_message_and_stops_without_submit(self) -> None:
        gateway = FixtureGateway(self.task_text)
        with patch.object(GenericAgentWorkspace, "require_safe_bash", return_value=None):
            submission = generate_generic_agent_submission(
                self.task,
                model="fixture-native-agent",
                gateway=gateway,
                max_turns=3,
                timeout_seconds=60,
            )
        self.assertEqual(submission.execution_mode, "generic_agent")
        self.assertEqual(submission.artifacts[0].path, "result.md")
        self.assertEqual(submission.raw_response, "Done")
        self.assertEqual(gateway.calls, 2)
        self.assertEqual(gateway.messages[0], [{"role": "user", "content": self.task_text}])
        self.assertEqual(gateway.tool_names[0], list(GENERIC_AGENT_TOOLS))
        self.assertEqual(
            submission.workspace_manifest["termination_reason"],
            "model_emitted_no_tool_calls",
        )
        self.assertEqual([event["tool"] for event in submission.tool_trace], ["write"])
        self.assertEqual(submission.agent_transcript[0]["content"], self.task_text)
        self.assertEqual(submission.agent_transcript[-1]["content"], "Done")
        self.assertEqual(submission.decision_log, [])
        with tempfile.TemporaryDirectory() as directory:
            run_dir = persist_run(
                self.task,
                submission,
                results_root=Path(directory),
            )
            manifest = json.loads(
                (run_dir / "run_manifest.json").read_text(encoding="utf-8")
            )
            self.assertTrue((run_dir / "agent_transcript.json").is_file())
            self.assertTrue(manifest["agent_transcript_sha256"])

    def test_truncated_empty_turn_is_not_a_voluntary_stop(self) -> None:
        class TruncatingGateway:
            def complete(self, model, *, system_prompt, messages, tools, timeout_seconds=None):
                return NativeAgentTurn(
                    tool_calls=[],
                    metrics={"output_tokens": 16000, "reasoning_tokens": 16000},
                    stop_reason="length",
                )

        with patch.object(GenericAgentWorkspace, "require_safe_bash", return_value=None):
            with self.assertRaisesRegex(Exception, "troncata al limite di token"):
                generate_generic_agent_submission(
                    self.task,
                    model="fixture-native-agent",
                    gateway=TruncatingGateway(),
                    max_turns=3,
                    timeout_seconds=60,
                )

    def test_compact_judge_context_excludes_documents(self) -> None:
        import os
        from legalitaw.evaluation.agentic import judge_task

        task = select_tasks(["WF2-002"], root=ROOT)[0]
        previous = os.environ.get("LEGALITA_JUDGE_CONTEXT")
        try:
            os.environ["LEGALITA_JUDGE_CONTEXT"] = "full"
            full = judge_task(task).query
            os.environ["LEGALITA_JUDGE_CONTEXT"] = "compact"
            compact = judge_task(task).query
            os.environ["LEGALITA_JUDGE_CONTEXT"] = "sbagliato"
            with self.assertRaises(ValueError):
                judge_task(task)
        finally:
            if previous is None:
                os.environ.pop("LEGALITA_JUDGE_CONTEXT", None)
            else:
                os.environ["LEGALITA_JUDGE_CONTEXT"] = previous
        self.assertLess(len(compact), len(full) / 2)
        self.assertIn("public/01_task.md", compact)
        self.assertNotIn("public/documents/", compact)

    def test_turn_limit_keeps_already_delivered_artifacts(self) -> None:
        class EndlessGateway:
            def __init__(self):
                self.calls = 0

            def complete(self, model, *, system_prompt, messages, tools, timeout_seconds=None):
                self.calls += 1
                name = "write" if self.calls == 1 else "glob"
                arguments = (
                    {"path": "/output/memo.md", "content": "# Memo\n\nConsegnato."}
                    if self.calls == 1
                    else {"pattern": "*", "path": "/output"}
                )
                return NativeAgentTurn(
                    tool_calls=[NativeToolCall(id=f"c{self.calls}", name=name, arguments=arguments)],
                    metrics={"output_tokens": 10},
                    stop_reason="tool_use",
                )

        with patch.object(GenericAgentWorkspace, "require_safe_bash", return_value=None):
            submission = generate_generic_agent_submission(
                self.task,
                model="fixture-native-agent",
                gateway=EndlessGateway(),
                max_turns=3,
                timeout_seconds=60,
            )
        self.assertEqual(submission.artifacts[0].path, "memo.md")
        self.assertEqual(
            submission.workspace_manifest["termination_reason"], "turn_limit_with_artifacts"
        )
        self.assertTrue(submission.workspace_manifest["external_stop"])

        class SilentLoopGateway:
            def complete(self, model, *, system_prompt, messages, tools, timeout_seconds=None):
                return NativeAgentTurn(
                    tool_calls=[NativeToolCall(id="g", name="glob", arguments={"pattern": "*"})],
                    metrics={},
                    stop_reason="tool_use",
                )

        with patch.object(GenericAgentWorkspace, "require_safe_bash", return_value=None):
            with self.assertRaisesRegex(Exception, "limite esterno"):
                generate_generic_agent_submission(
                    self.task,
                    model="fixture-native-agent",
                    gateway=SilentLoopGateway(),
                    max_turns=2,
                    timeout_seconds=60,
                )

    def test_docx_redline_writes_tracked_changes_into_output(self) -> None:
        from legalitaw.agentic.native_artifacts import docx_features
        from legalitaw.agentic.submissions import _docx_text

        workspace = GenericAgentWorkspace(self.task)
        try:
            source = next(
                path
                for path in workspace.execute("glob", {"pattern": "**/*.docx", "path": "/documents"})["matches"]
            )
            text = workspace.execute("read", {"path": source, "limit": 400})["content"]
            line = next(
                item.split(": ", 1)[1]
                for item in text.splitlines()
                if len(item.split(": ", 1)[-1]) > 80
            )
            target = line[5:45]
            result = workspace.execute(
                "docx_redline",
                {
                    "source": source,
                    "output": "/output/redline.docx",
                    "edits": [
                        {"action": "replace", "find": target, "text": "NUOVO TESTO", "comment": "motivo"},
                        {"action": "delete", "find": "testo che non esiste in alcun paragrafo"},
                    ],
                },
            )
            self.assertEqual((result["applied"], result["failed"]), (1, 1))
            written = workspace.output / "redline.docx"
            features = docx_features(written)
            self.assertTrue(features["track_revisions_enabled"])
            self.assertGreaterEqual(features["insertions"], 1)
            self.assertGreaterEqual(features["deletions"], 1)
            self.assertEqual(features["comments"], 1)
            rendered = _docx_text(written)
            self.assertIn("[[AGGIUNTA: NUOVO TESTO]]", rendered)
            self.assertRegex(rendered, r"\[\[COMMENTO[^\]]*: motivo\]\]")
            with self.assertRaises(Exception):
                workspace.execute(
                    "docx_redline",
                    {"source": source, "output": source, "edits": [{"action": "delete", "find": target}]},
                )
        finally:
            workspace.close()

    def test_external_cost_guard_is_not_injected_into_prompt(self) -> None:
        with patch.object(GenericAgentWorkspace, "require_safe_bash", return_value=None):
            with self.assertRaises(WorkspaceRunFailure) as captured:
                generate_generic_agent_submission(
                    self.task,
                    model="fixture-cost-agent",
                    gateway=CostGateway(),
                    max_turns=3,
                    timeout_seconds=60,
                    max_cost_usd=0.5,
                )
        self.assertIn("cost guard", str(captured.exception))
        self.assertNotIn("0.5", captured.exception.agent_transcript[0]["content"])

    def test_bare_and_production_profiles_are_auditable(self) -> None:
        bare = GenericAgentWorkspace(self.task, profile="bare")
        production = GenericAgentWorkspace(self.task, profile="production")
        try:
            self.assertFalse(bare.skills.exists())
            self.assertTrue((production.skills / "docx.md").is_file())
            self.assertEqual(bare.manifest["profile"], "bare")
            self.assertEqual(production.manifest["profile"], "production")
            self.assertEqual(
                set(production.manifest["skills"]),
                {"README.md", "docx.md", "pptx.md", "xlsx.md"},
            )
            self.assertTrue(production.manifest["skills_manifest_sha256"])
            self.assertTrue(bare.manifest["tool_schema_sha256"])
            self.assertNotEqual(
                bare.manifest["system_prompt_sha256"],
                production.manifest["system_prompt_sha256"],
            )
        finally:
            bare.close()
            production.close()

    def test_artifact_collector_rejects_symlinks(self) -> None:
        workspace = GenericAgentWorkspace(self.task)
        external = Path(tempfile.mkdtemp()) / "outside.txt"
        external.write_text("not an artifact", encoding="utf-8")
        try:
            (workspace.output / "leak.txt").symlink_to(external)
            with self.assertRaises(Exception):
                workspace.artifacts()
        finally:
            workspace.close()
            self.assertEqual(external.read_text(encoding="utf-8"), "not an artifact")
            external.unlink()
            external.parent.rmdir()


if __name__ == "__main__":
    unittest.main()
