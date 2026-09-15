import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from tools.line_report import (
    apply_patches,
    cheap_gates,
    format_evaluation_comment,
    format_issue_body,
    parse_apply_command,
    parse_evaluation_comment,
    parse_issue_body,
    validate_evaluation,
)
from tools.report_server import LineReportService, Settings, verify_signature, _issue_from_pull


class LineReportTest(unittest.TestCase):
    def test_issue_body_roundtrip(self):
        body = format_issue_body(62, 'He said "--> wait"', "awkward cadence", "https://murim-login.com/chapter/62/")
        parsed = parse_issue_body(body)
        self.assertEqual(parsed["chapter"], 62)
        self.assertEqual(parsed["quote"], 'He said "--> wait"')
        self.assertEqual(parsed["note"], "awkward cadence")
        self.assertIn("https://murim-login.com/chapter/62/", parsed["url"])

    def test_github_form_body(self):
        parsed = parse_issue_body(
            "### Chapter\n\n7\n\n### Quoted line\n\nAwkward title.\n\n### What's wrong\n\nSounds off.\n"
        )
        self.assertEqual(parsed["chapter"], 7)
        self.assertEqual(parsed["quote"], "Awkward title.")
        self.assertEqual(parsed["note"], "Sounds off.")

    def test_cheap_gates_require_exact_quote(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            translations = root / "translations"
            translations.mkdir()
            (translations / "0003.md").write_text("# Chapter 3\n\nKnown line.\n", encoding="utf-8")
            self.assertIsNone(cheap_gates(3, "Known line.", root))
            self.assertIn("not found", cheap_gates(3, "Missing.", root).lower())
            self.assertIn("not an accepted", cheap_gates(9, "Known line.", root).lower())

    def test_rejects_disallowed_patch_paths(self):
        with self.assertRaises(ValueError):
            validate_evaluation({
                "plausible": True,
                "verdict": "ok",
                "strategies": [{
                    "id": "A",
                    "label": "bad",
                    "tradeoff": "no",
                    "patches": [{"path": "source/0001.txt", "current": "a", "replacement": "b"}],
                }],
            })

    def test_apply_patches_requires_unique_non_overlapping_spans(self):
        files = {"translations/0001.md": "# Chapter 1\n\nHello world.\nHello there.\n"}
        patches = [
            {"path": "translations/0001.md", "current": "Hello world.", "replacement": "Hi world."},
            {"path": "translations/0001.md", "current": "Hello there.", "replacement": "Hi there."},
        ]
        updated = apply_patches(files, patches)
        self.assertEqual(updated["translations/0001.md"], "# Chapter 1\n\nHi world.\nHi there.\n")
        with self.assertRaises(ValueError):
            apply_patches(files, [
                {"path": "translations/0001.md", "current": "Hello", "replacement": "Hi"},
            ])

    def test_evaluation_comment_roundtrip_and_apply_command(self):
        evaluation = validate_evaluation({
            "plausible": True,
            "verdict": "wrong title",
            "strategies": [{
                "id": "A",
                "label": "Fix title",
                "tradeoff": "Matches source.",
                "patches": [{
                    "path": "docs/NAMES.md",
                    "current": "| 검 | **Sword** |",
                    "replacement": "| 검 | **Blade** |",
                }],
            }],
        })
        comment = format_evaluation_comment(evaluation)
        self.assertEqual(parse_evaluation_comment(comment), evaluation)
        self.assertEqual(parse_apply_command("/apply A"), "A")
        self.assertEqual(parse_apply_command("/apply b please"), "B")
        self.assertIsNone(parse_apply_command("please apply A"))

    def test_implausible_evaluation_has_no_strategies(self):
        value = validate_evaluation({"plausible": False, "verdict": "already correct", "strategies": []})
        self.assertFalse(value["plausible"])
        with self.assertRaises(ValueError):
            validate_evaluation({"plausible": False, "verdict": "no", "strategies": [{
                "id": "A", "label": "x", "tradeoff": "y",
                "patches": [{"path": "compendium.md", "current": "a", "replacement": "b"}],
            }]})


class ReportServerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        translations = self.root / "translations"
        translations.mkdir()
        (translations / "0004.md").write_text("# Chapter 4\n\nThe awkward line.\n", encoding="utf-8")
        self.github = MagicMock()
        self.github.create_issue.return_value = {"number": 12, "html_url": "https://github.com/x/y/issues/12"}
        self.settings = Settings({
            "MURIM_ROOT": str(self.root),
            "GITHUB_APPLY_USERS": "jimzrt",
            "REPORT_LINE_RATE": "50",
            "GITHUB_WEBHOOK_SECRET": "secret",
        })
        self.service = LineReportService(self.settings, self.github, evaluate=self._evaluate)

    def tearDown(self):
        self.temp.cleanup()

    def _evaluate(self, chapter, quote, note, root):
        return {
            "plausible": True,
            "verdict": "local wording",
            "strategies": [{
                "id": "A",
                "label": "Smoother",
                "tradeoff": "Closer to source cadence.",
                "patches": [{
                    "path": "translations/0004.md",
                    "current": "The awkward line.",
                    "replacement": "The smoother line.",
                }],
            }],
        }

    def test_create_report_opens_labeled_issue(self):
        status, body = self.service.create_report(
            {
                "chapter": 4,
                "quote": "The awkward line.",
                "note": "stiff",
                "url": "https://murim-login.com/chapter/4/",
            },
            "1.2.3.4",
        )
        self.assertEqual(status, 201)
        self.assertEqual(body["number"], 12)
        args = self.github.create_issue.call_args[0]
        self.assertEqual(args[0], "Chapter 4: report line")
        self.assertEqual(args[2], ["line-report"])
        self.assertEqual(parse_issue_body(args[1])["quote"], "The awkward line.")

    def test_unknown_quote_is_rejected_before_github(self):
        status, body = self.service.create_report(
            {"chapter": 4, "quote": "not in the file", "note": "", "url": ""},
            "1.2.3.4",
        )
        self.assertEqual(status, 400)
        self.github.create_issue.assert_not_called()
        self.assertIn("not found", body["error"].lower())

    def test_evaluate_issue_comments_strategies(self):
        issue = {
            "number": 12,
            "body": format_issue_body(4, "The awkward line.", "stiff", ""),
            "labels": [{"name": "line-report"}],
        }
        self.github.list_comments.return_value = []
        self.service._evaluate_issue(issue)
        comment = self.github.comment.call_args[0][1]
        self.assertIn("/apply", comment)
        parsed = parse_evaluation_comment(comment)
        self.assertEqual(parsed["strategies"][0]["id"], "A")

    def test_apply_opens_pr_with_patched_files(self):
        evaluation = self._evaluate(4, "The awkward line.", "", self.root)
        self.github.list_comments.return_value = [{"body": format_evaluation_comment(evaluation)}]
        self.github.default_branch.return_value = "master"
        self.github.get_ref_sha.return_value = "abc"
        self.github.get_file.side_effect = [
            ("# Chapter 4\n\nThe awkward line.\n", "blob1"),
            ("# Chapter 4\n\nThe smoother line.\n", "blob2"),
        ]
        self.github.create_pull.return_value = {"html_url": "https://github.com/x/y/pull/3"}
        issue = {
            "number": 12,
            "node_id": "I_1",
            "body": format_issue_body(4, "The awkward line.", "", ""),
            "labels": [{"name": "line-report"}],
        }
        self.service._apply_strategy(12, "A", issue)
        self.github.create_branch.assert_called_once()
        put = self.github.put_file.call_args[0]
        self.assertEqual(put[0], "translations/0004.md")
        self.assertIn("The smoother line.", put[1])
        self.github.create_pull.assert_called_once()
        self.assertIn("report-line-12-A", self.github.create_pull.call_args[0][1])

    def test_apply_ignored_for_unknown_user_via_comment_gate(self):
        payload = {
            "action": "created",
            "comment": {"body": "/apply A", "user": {"type": "User"}},
            "issue": {"number": 12, "labels": [{"name": "line-report"}]},
            "sender": {"login": "stranger"},
        }
        self.service._on_comment(payload)
        self.github.create_pull.assert_not_called()

    def test_merged_pull_closes_issue(self):
        self.github.get_issue.return_value = {"state": "open"}
        self.service._on_pull_closed({
            "pull_request": {
                "merged": True,
                "head": {"ref": "report-line-44-A"},
                "body": "<!-- line-report-issue 44 -->",
            }
        })
        self.github.close_issue.assert_called_once_with(44)

    def test_issue_number_from_branch_and_marker(self):
        self.assertEqual(_issue_from_pull({"head": {"ref": "report-line-9-B"}, "body": ""}), 9)
        self.assertEqual(_issue_from_pull({"head": {"ref": "other"}, "body": "<!-- line-report-issue 77 -->"}), 77)

    def test_webhook_hmac(self):
        payload = b'{"ok":true}'
        digest = "sha256=" + __import__("hmac").new(b"secret", payload, __import__("hashlib").sha256).hexdigest()
        self.assertTrue(verify_signature("secret", payload, digest))
        self.assertFalse(verify_signature("secret", payload, digest[:-1] + "0"))


if __name__ == "__main__":
    unittest.main()
