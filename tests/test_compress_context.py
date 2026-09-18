import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import compress_context
from tools import workflow


class CompressContextTest(unittest.TestCase):
    def test_compression_due_is_false_under_thresholds(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "characters").mkdir()
            (root / "docs" / "workflow.json").write_text(json.dumps({
                "profile_compress_trigger_bytes": 4096,
                "context_thresholds": {
                    "bytes": 12000,
                    "active_continuity": 12,
                    "open_questions": 5,
                    "temporary_decisions": 5,
                },
            }), encoding="utf-8")
            (root / "docs" / "CONTEXT.json").write_text(json.dumps({
                "version": 1,
                "safe_through": 1,
                "continuity_sources": [1],
                "active_continuity": ["One."],
                "open_questions": ["Why?"],
                "temporary_decisions": ["Keep."],
            }), encoding="utf-8")
            (root / "characters" / "Hero.md").write_text("# Hero (주인공)\n\n- **Role:** Lead\n", encoding="utf-8")
            with patch.object(compress_context, "ROOT", root), patch.object(compress_context, "workflow_config", return_value=json.loads((root / "docs" / "workflow.json").read_text())):
                self.assertFalse(compress_context.compression_due())

    def test_compression_due_when_context_lists_exceed_limits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "characters").mkdir()
            cfg = {
                "profile_compress_trigger_bytes": 4096,
                "context_thresholds": {
                    "bytes": 12000,
                    "active_continuity": 2,
                    "open_questions": 5,
                    "temporary_decisions": 5,
                },
            }
            (root / "docs" / "workflow.json").write_text(json.dumps(cfg), encoding="utf-8")
            (root / "docs" / "CONTEXT.json").write_text(json.dumps({
                "version": 1,
                "safe_through": 1,
                "continuity_sources": [1],
                "active_continuity": ["A.", "B.", "C."],
                "open_questions": [],
                "temporary_decisions": [],
            }), encoding="utf-8")
            with patch.object(compress_context, "ROOT", root), patch.object(compress_context, "workflow_config", return_value=cfg):
                self.assertTrue(compress_context.context_compression_due())
                self.assertTrue(compress_context.compression_due())

    def test_run_compression_is_noop_when_not_due(self):
        with patch.object(compress_context, "compression_due", return_value=False):
            self.assertEqual(compress_context.run_compression(9), [])


class CompressWorkflowTest(unittest.TestCase):
    def test_ready_prepare_when_compression_not_due(self):
        state = {"chapter": 1, "stage": "READY"}
        with patch("tools.compress_context.compression_due", return_value=False):
            self.assertEqual(
                workflow.next_action(state, {}),
                "python tools/workflow.py prepare 1",
            )

    def test_ready_compress_when_over_threshold(self):
        state = {"chapter": 1, "stage": "READY"}
        with patch("tools.compress_context.compression_due", return_value=True):
            self.assertEqual(
                workflow.next_action(state, {}),
                "python tools/workflow.py compress 1",
            )

    def test_command_compress_skips_model_when_not_due(self):
        state = {"chapter": 1, "stage": "READY"}
        paths = {"work": Path("/tmp"), "compress_files": Path("/tmp/compress-files.json")}
        with (
            patch.object(workflow, "load", return_value=(state, paths)),
            patch.object(workflow, "require"),
            patch("tools.compress_context.compression_due", return_value=False),
            patch("tools.compress_context.run_compression") as run,
            patch("tools.progress.step"),
        ):
            workflow.command_compress(1)
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
