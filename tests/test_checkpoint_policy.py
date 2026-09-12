import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import context, workflow


class CheckpointPolicyTest(unittest.TestCase):
    def test_missing_disposition_is_recorded_as_advisory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs").mkdir()
            (root / "docs" / "STATE.md").write_text(
                "# Translation State\n\n- Last completed: 0\n- Next chapter: 1\n",
                encoding="utf-8",
            )
            (root / "docs" / "NAMES.md").write_text("# Names\n", encoding="utf-8")
            (root / "docs" / "workflow.json").write_text(
                json.dumps(workflow.DEFAULT_CONFIG), encoding="utf-8"
            )
            with (
                patch.object(workflow, "ROOT", root),
                patch.object(workflow, "source_hash", return_value="source"),
            ):
                state, paths = workflow.load(1)
                paths["revised"].parent.mkdir(parents=True, exist_ok=True)
                paths["revised"].write_text(
                    "# Chapter 1\n\nFinished.\n", encoding="utf-8"
                )
                workflow.atomic_json(paths["checkpoint_json"], {
                    "version": 1,
                    "summary": "Finding",
                    "findings": [{
                        "id": "C01",
                        "severity": "major",
                        "source": "Chapter 1",
                        "current": "Finished.",
                        "defect": "Follow-up needed.",
                        "replacement": "Finished.",
                        "rationale": "Defer to retrofit.",
                        "confidence": 0.9,
                    }],
                })
                state["stage"] = "CHECKPOINT_REVIEWED"
                state["artifacts"]["checkpoint_report_sha256"] = workflow.digest(
                    paths["checkpoint_json"]
                )
                workflow.atomic_json(paths["state"], state)
                with (
                    patch.object(context, "chapter_text", return_value="source"),
                    patch.object(context, "exact_glossary_entries", return_value=[]),
                    patch(
                        "tools.qa.run_qa",
                        return_value={"passed": True, "errors": [], "warnings": []},
                    ),
                ):
                    workflow.command_checkpointed(1)
                disposition = json.loads(
                    paths["checkpoint_disposition"].read_text(encoding="utf-8")
                )
                recorded = json.loads(paths["state"].read_text(encoding="utf-8"))

        self.assertEqual(disposition["dispositions"][0]["status"], "unresolved")
        self.assertEqual(recorded["stage"], "CHECKPOINT_APPLIED")


if __name__ == "__main__":
    unittest.main()
