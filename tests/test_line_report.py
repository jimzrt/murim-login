import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from tools.line_report import (
    apply_patches,
    asks_for_corpus,
    build_evaluate_prompt,
    corpus_gap,
    corpus_hits,
    match_korean_term,
    require_applicable,
    UnapplicableStrategy,
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
    retry_delay,
    sync_git,
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
        with self.assertRaises(ValueError) as caught:
            apply_patches(files, [
                {"path": "translations/0001.md", "current": "Hello", "replacement": "Hi"},
            ])
        self.assertIn("Hello", str(caught.exception))

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
        self.assertIn("verbatim", prompt)

    def test_corpus_revision_lists_other_chapters(self):
        self.assertTrue(asks_for_corpus("", "use qinggong. every usage, not just this one."))
        self.assertFalse(asks_for_corpus("Can translate as Qinggong?", ""))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            translations = root / "translations"
            translations.mkdir()
            (translations / "0247.md").write_text(
                "the finest lightness technique\n", encoding="utf-8"
            )
            (translations / "0249.md").write_text(
                "ahead in lightness skills\n\ninto lightness skills\n", encoding="utf-8"
            )
            (translations / "0516.md").write_text(
                "a welcome lightness in my body\n", encoding="utf-8"
            )
            hits, total = corpus_hits("lightness", root)
            self.assertEqual(total, 4)
            prompt = build_evaluate_prompt(
                247,
                root / "translations" / "0247.md",
                "the finest lightness technique\n",
                "lightness",
                "Can translate as Qinggong?",
                "Korean",
                root=root,
                revise_note="every usage, not just this one",
                hits=hits,
                hit_total=total,
                corpus_requested=True,
            )
            self.assertIn("translations/0249.md", prompt)
            self.assertIn("translations/0516.md", prompt)
            self.assertIn("not only the anchor", prompt)
            anchor_only = {
                "plausible": True,
                "strategies": [{
                    "id": "A",
                    "patches": [{"path": "translations/0247.md"}],
                }],
            }
            gap = corpus_gap(anchor_only, hits, 247)
            self.assertIn("0249", gap)
            covered = {
                "plausible": True,
                "strategies": [{
                    "id": "A",
                    "patches": [
                        {"path": "translations/0247.md"},
                        {"path": "translations/0249.md"},
                        {"path": "translations/0516.md"},
                    ],
                }],
            }
            self.assertIsNone(corpus_gap(covered, hits, 247))

    def test_korean_term_includes_other_renderings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source").mkdir()
            (root / "translations").mkdir()
            (root / "source" / "0001.txt").write_text("경공술이 가장 뛰어나다\n", encoding="utf-8")
            (root / "translations" / "0001.md").write_text(
                "the finest lightness technique\n", encoding="utf-8"
            )
            (root / "source" / "0002.txt").write_text("나는 경공(輕功)을 발휘했다\n", encoding="utf-8")
            (root / "translations" / "0002.md").write_text(
                "I used light-body arts\n", encoding="utf-8"
            )
            (root / "source" / "0003.txt").write_text("경신술을 발휘했다\n", encoding="utf-8")
            (root / "translations" / "0003.md").write_text(
                "using lightness skill\n", encoding="utf-8"
            )
            (root / "source" / "0004.txt").write_text("경공술에 몰빵했냐\n", encoding="utf-8")
            (root / "translations" / "0004.md").write_text(
                "Did you put everything into lightness skills?\n", encoding="utf-8"
            )
            matched = match_korean_term("lightness", 1, root)
            self.assertEqual(matched["term"], "경공술")
            self.assertIn("경공", matched["forms"])
            chapters = {hit["chapter"] for hit in matched["hits"]}
            self.assertEqual(chapters, {1, 2, 4})
            prompt = build_evaluate_prompt(
                1,
                root / "translations" / "0001.md",
                "the finest lightness technique\n",
                "lightness",
                "use qinggong",
                "Korean",
                root=root,
                revise_note="every usage, not just this one",
                hits=matched["hits"],
                hit_total=matched["total"],
                corpus_requested=True,
            )
            self.assertIn("경공술", prompt)
            self.assertIn("light-body arts", prompt)
            self.assertNotIn("경신술", prompt)
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

    def test_truncated_quote_is_not_applicable(self):
        text = "“Chengdu. A military conference has been convened.”\n"
        evaluation = validate_evaluation({
            "plausible": True,
            "verdict": "needs a gloss",
            "strategies": [{
                "id": "A",
                "label": "Footnote",
                "tradeoff": "Keeps the line.",
                "patches": [
                    {
                        "path": "translations/0394.md",
                        "current": "“Chengdu.”",
                        "replacement": "“Chengdu.”\n\n[^1]: A note.",
                    },
                ],
            }],
        })
        with self.assertRaises(UnapplicableStrategy) as caught:
            require_applicable(evaluation, {"translations/0394.md": text})
        self.assertIn("occurs 0 times", str(caught.exception))
        fixed = validate_evaluation({
            "plausible": True,
            "verdict": "needs a gloss",
            "strategies": [{
                "id": "A",
                "label": "Footnote",
                "tradeoff": "Keeps the line.",
                "patches": [{
                    "path": "translations/0394.md",
                    "current": text.strip(),
                    "replacement": text.strip() + "\n\n[^1]: A note.",
                }],
            }],
        })
        applied = require_applicable(fixed, {"translations/0394.md": text})
        self.assertEqual(applied["strategies"][0]["id"], "A")

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
        self.github.comment.return_value = {"id": 501}
        self.github.list_comments.return_value = []
        self.settings = Settings({
            "MURIM_ROOT": str(self.root),
            "GITHUB_APPLY_USERS": "jimzrt",
            "REPORT_LINE_RATE": "50",
            "GITHUB_WEBHOOK_SECRET": "secret",
        })
        self.service = LineReportService(self.settings, self.github, evaluate=self._evaluate)
        self.service._spawn = lambda target, args: target(*args)

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
        pending = self.github.comment.call_args[0][1]
        self.assertIn("Evaluating this report", pending)
        self.assertIn("line-report-status pending", pending)
        comment = self.github.update_comment.call_args[0][1]
        self.assertIn("/apply", comment)
        parsed = parse_evaluation_comment(comment)
        self.assertEqual(parsed["strategies"][0]["id"], "A")
        self.assertEqual(self.github.update_comment.call_args[0][0], 501)

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
        self.assertIn("Revising strategies", self.github.comment.call_args[0][1])
        comment = self.github.update_comment.call_args[0][1]
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
        self.assertIn("/reopen", self.github.update_comment.call_args[0][1])

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
        self.assertIn("Reopening this report", self.github.comment.call_args[0][1])
        self.assertIn("/apply", self.github.update_comment.call_args[0][1])

    def test_retry_delay_caps_at_fifteen_minutes(self):
        self.assertEqual(retry_delay(1), 60)
        self.assertEqual(retry_delay(2), 120)
        self.assertEqual(retry_delay(5), 900)
        self.assertEqual(retry_delay(20), 900)

    def test_model_outage_updates_placeholder_and_sweep_waits(self):
        def boom(*_args, **_kwargs):
            raise SystemExit("no tokens available")

        self.service.evaluate = boom
        issue = {
            "number": 60,
            "body": format_issue_body(4, "The awkward line.", "stiff", ""),
            "labels": [{"name": "line-report"}],
        }
        self.service._evaluate_issue(issue)
        body = self.github.update_comment.call_args[0][1]
        self.assertIn("no tokens available", body)
        self.assertIn("line-report-status retry", body)
        self.assertIn("60", self.service._retry_state)
        self.github.update_comment.reset_mock()
        self.github.comment.reset_mock()
        self.github.list_issues.return_value = [issue]
        self.github.list_comments.return_value = [{"id": 501, "body": body}]
        self.service.sweep_open_reports()
        self.github.comment.assert_not_called()
        self.github.update_comment.assert_not_called()

    def test_sweep_evaluates_open_issue_that_never_got_a_comment(self):
        issue = {
            "number": 59,
            "body": format_issue_body(4, "The awkward line.", "nickname", ""),
            "labels": [{"name": "line-report"}],
        }
        self.github.list_issues.return_value = [issue]
        self.service.sweep_open_reports()
        self.assertIn("Evaluating this report", self.github.comment.call_args[0][1])
        published = self.github.update_comment.call_args[0][1]
        self.assertIn("line-report-eval", published)
        self.assertNotIn("59", self.service._retry_state)

    def test_sweep_skips_a_finished_evaluation(self):
        issue = {"number": 8, "labels": [{"name": "line-report"}]}
        self.github.list_issues.return_value = [issue]
        self.github.list_comments.return_value = [{"body": "<!-- line-report-eval\n{}\n-->"}]
        self.service.sweep_open_reports()
        self.github.comment.assert_not_called()
        self.github.update_comment.assert_not_called()

    def test_unreadable_issue_is_not_retried(self):
        issue = {"number": 12, "body": "not a report", "labels": [{"name": "line-report"}]}
        self.service._evaluate_issue(issue)
        failed = self.github.update_comment.call_args[0][1]
        self.assertIn("line-report-status failed", failed)
        self.github.update_comment.reset_mock()
        self.github.list_issues.return_value = [issue]
        self.github.list_comments.return_value = [{"id": 501, "body": failed}]
        self.service.sweep_open_reports()
        self.github.update_comment.assert_not_called()

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
        self.assertEqual(parse_chapter_list(b"[0, 160]"), [0, 160])
        self.assertIsNone(parse_chapter_list(b"[-1]"))
        self.assertIsNone(parse_chapter_list(b"["))
        self.assertEqual(parse_chapter_list(b"[" + b",".join(b"1" for _ in range(501)) + b"]"), [1] * 501)
        self.assertIsNone(parse_chapter_list(b"[" + b",".join(b"1" for _ in range(5001)) + b"]"))

    def test_webhook_hmac(self):
        payload = b'{"ok":true}'
        digest = "sha256=" + __import__("hmac").new(b"secret", payload, __import__("hashlib").sha256).hexdigest()
        self.assertTrue(verify_signature("secret", payload, digest))
        self.assertFalse(verify_signature("secret", payload, digest[:-1] + "0"))


class GitSyncTest(unittest.TestCase):
    def test_sync_git_noops_without_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            sync_git(Path(directory))

    def test_sync_git_hard_resets_to_origin_master(self):
        import subprocess

        with tempfile.TemporaryDirectory() as directory:
            remote = Path(directory) / "remote"
            clone = Path(directory) / "clone"
            remote.mkdir()
            subprocess.run(["git", "init", "-b", "master"], cwd=remote, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=remote, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=remote, check=True)
            (remote / "chapter.txt").write_text("one\n", encoding="utf-8")
            subprocess.run(["git", "add", "chapter.txt"], cwd=remote, check=True)
            subprocess.run(["git", "commit", "-m", "one"], cwd=remote, check=True, capture_output=True)
            subprocess.run(["git", "clone", str(remote), str(clone)], check=True, capture_output=True)
            (clone / "chapter.txt").write_text("dirty\n", encoding="utf-8")
            (remote / "chapter.txt").write_text("two\n", encoding="utf-8")
            subprocess.run(["git", "add", "chapter.txt"], cwd=remote, check=True)
            subprocess.run(["git", "commit", "-m", "two"], cwd=remote, check=True, capture_output=True)
            sync_git(clone)
            self.assertEqual((clone / "chapter.txt").read_text(encoding="utf-8"), "two\n")


if __name__ == "__main__":
    unittest.main()
