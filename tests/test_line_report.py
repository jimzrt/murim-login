import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from tools.line_report import (
    apply_patches,
    build_evaluate_prompt,
    chapter_is_mastered,
    cheap_gates,
    format_evaluation_comment,
    format_issue_body,
    parse_apply_command,
    parse_evaluation_comment,
    parse_issue_body,
    parse_reopen_command,
    parse_revise_command,
    validate_evaluation,
)
from tools.report_server import (
    LineReportService,
    Settings,
    parse_chapter_list,
    verify_signature,
    _issue_from_pull,
)


def mark_mastered(root: Path, chapter: int) -> None:
    folder = root / "reviews" / "mastering" / f"{chapter:04d}"
    folder.mkdir(parents=True)
    (folder / "state.json").write_text(
        json.dumps({"chapter": chapter, "stage": "PROMOTED", "qa_passed": True}),
        encoding="utf-8",
    )


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
            self.assertIn("not been mastered", cheap_gates(3, "Known line.", root).lower())
            mark_mastered(root, 3)
            self.assertTrue(chapter_is_mastered(3, root))
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
        self.assertEqual(
            parse_revise_command("/revise drop hot breath; more idiomatic"),
            "drop hot breath; more idiomatic",
        )
        self.assertEqual(
            parse_revise_command("/revise\nKeep the spear, change the breath."),
            "Keep the spear, change the breath.",
        )
        self.assertEqual(parse_revise_command("/revise"), "")
        self.assertIsNone(parse_revise_command("/apply A"))
        self.assertEqual(parse_reopen_command("/reopen"), "")
        self.assertEqual(parse_reopen_command("/reopen still want alternatives"), "still want alternatives")
        self.assertIsNone(parse_reopen_command("/revise x"))

    def test_revise_prompt_includes_rejected_strategies(self):
        previous = validate_evaluation({
            "plausible": True,
            "verdict": "wording",
            "strategies": [{
                "id": "A",
                "label": "Warm breath",
                "tradeoff": "literal",
                "patches": [{
                    "path": "translations/0011.md",
                    "current": "a hot breath",
                    "replacement": "a warm breath",
                }],
            }],
        })
        prompt = build_evaluate_prompt(
            11,
            Path("/repo/translations/0011.md"),
            "# Chapter 11\n",
            "a hot breath",
            "sounds weird",
            "Korean",
            root=Path("/repo"),
            previous=previous,
            revise_note="not a synonym of hot",
        )
        self.assertIn("Maintainer revision request", prompt)
        self.assertIn("a warm breath", prompt)
        self.assertIn("not a synonym of hot", prompt)
        forced = build_evaluate_prompt(
            11,
            Path("/repo/translations/0011.md"),
            "# Chapter 11\n",
            "a hot breath",
            "sounds weird",
            "Korean",
            root=Path("/repo"),
            force=True,
        )
        self.assertIn("overrode plausibility", forced)
        self.assertNotIn("set plausible to false", forced.lower())

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
        mark_mastered(self.root, 4)
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

    def _evaluate(self, chapter, quote, note, root, previous=None, revise_note="", force=False):
        self.last_evaluate = {
            "chapter": chapter,
            "quote": quote,
            "note": note,
            "previous": previous,
            "revise_note": revise_note,
            "force": force,
        }
        replacement = "The requested line." if revise_note else "The smoother line."
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
                    "replacement": replacement,
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

    def test_unmastered_chapter_is_rejected_before_github(self):
        (self.root / "translations" / "0005.md").write_text(
            "# Chapter 5\n\nUnmastered line.\n", encoding="utf-8"
        )
        status, body = self.service.create_report(
            {"chapter": 5, "quote": "Unmastered line.", "note": "odd", "url": ""},
            "1.2.3.4",
        )
        self.assertEqual(status, 400)
        self.github.create_issue.assert_not_called()
        self.assertIn("not been mastered", body["error"].lower())

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

    def test_revise_reruns_evaluation_with_feedback(self):
        previous = self._evaluate(4, "The awkward line.", "stiff", self.root)
        self.github.list_comments.return_value = [{"body": format_evaluation_comment(previous)}]
        issue = {
            "number": 12,
            "body": format_issue_body(4, "The awkward line.", "stiff", ""),
            "labels": [{"name": "line-report"}],
        }
        self.service._revise_issue(issue, "/revise not a synonym; more idiomatic")
        self.assertEqual(self.last_evaluate["revise_note"], "not a synonym; more idiomatic")
        self.assertEqual(self.last_evaluate["previous"]["strategies"][0]["id"], "A")
        comment = self.github.comment.call_args[0][1]
        self.assertIn("/revise", comment)
        self.assertIn("The requested line.", comment)

    def test_bare_revise_asks_for_feedback(self):
        issue = {"number": 12, "body": "", "labels": [{"name": "line-report"}]}
        self.service._revise_issue(issue, "/revise")
        self.assertIn("/revise", self.github.comment.call_args[0][1])

    def test_implausible_evaluation_closes_issue(self):
        self.service.evaluate = lambda *args, **kwargs: {
            "plausible": False,
            "verdict": "already correct",
            "strategies": [],
        }
        issue = {
            "number": 12,
            "body": format_issue_body(4, "The awkward line.", "sounds weird", ""),
            "labels": [{"name": "line-report"}],
        }
        self.service._evaluate_issue(issue)
        self.github.add_labels.assert_called_with(12, ["implausible"])
        self.github.close_issue.assert_called_once_with(12)
        self.assertIn("/reopen", self.github.comment.call_args[0][1])

    def test_reopen_overrides_implausible_and_forces_strategies(self):
        issue = {
            "number": 12,
            "body": format_issue_body(4, "The awkward line.", "sounds weird", ""),
            "labels": [{"name": "line-report"}],
        }
        self.github.list_comments.return_value = []
        self.service._reopen_issue(issue, "/reopen still want other phrasings")
        self.github.reopen_issue.assert_called_once_with(12)
        self.github.remove_label.assert_called()
        self.assertTrue(self.last_evaluate["force"])
        self.assertEqual(self.last_evaluate["revise_note"], "still want other phrasings")
        self.github.close_issue.assert_not_called()
        self.assertIn("/apply", self.github.comment.call_args[0][1])

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

    def test_parse_chapter_list(self):
        self.assertEqual(parse_chapter_list(b"[160, 161]"), [160, 161])
        self.assertIsNone(parse_chapter_list(b'{"chapter": 1}'))
        self.assertIsNone(parse_chapter_list(b"[0]"))
        self.assertIsNone(parse_chapter_list(b"["))

    def test_webhook_hmac(self):
        payload = b'{"ok":true}'
        digest = "sha256=" + __import__("hmac").new(b"secret", payload, __import__("hashlib").sha256).hexdigest()
        self.assertTrue(verify_signature("secret", payload, digest))
        self.assertFalse(verify_signature("secret", payload, digest[:-1] + "0"))


if __name__ == "__main__":
    unittest.main()
