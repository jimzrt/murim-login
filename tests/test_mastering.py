from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from tools.progress import NullCall

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "mastering.py"
spec = importlib.util.spec_from_file_location("mastering", MODULE_PATH)
mastering = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(mastering)


def test_parse_chapters():
    assert mastering.parse_chapters("1-3,5,3") == [1, 2, 3, 5]


def test_parse_json_object_escapes_interior_quotes():
    raw = (
        '{\n'
        '  "chapter": 2,\n'
        '  "decisions": [{\n'
        '    "hunk_id": "H044",\n'
        '    "decision": "SOL",\n'
        '    "reason": "SOL\'s \'"> **Warning**\' heading is correct."\n'
        '  }]\n'
        '}\n'
    )
    value = mastering.parse_json_object(raw)
    assert value["chapter"] == 2
    assert "Warning" in value["decisions"][0]["reason"]


def test_parse_json_object_recovers_restarted_concatenated_payload():
    # Truncated first object spliced into a restarted complete object — the
    # outer brace span is invalid JSON, but the second object is complete.
    raw = (
        'preamble {"chapter": 13, "decisions": ['
        '{"hunk_id": "H001", "decision": "SOL", "reason": "partial"},'
        '{"chapter": 13, "decisions": ['
        '{"hunk_id": "H001", "decision": "BASE", "reason": "complete first"},'
        '{"hunk_id": "H002", "decision": "SOL", "reason": "complete second"}]}'
    )
    value = mastering.parse_json_object(raw)
    assert value["chapter"] == 13
    assert len(value["decisions"]) == 2
    assert value["decisions"][0]["decision"] == "BASE"
    assert value["decisions"][1]["reason"] == "complete second"


def test_diff_and_assemble_sol_base_repair():
    baseline = "# Chapter 1\n\nAlpha.\n\nBeta.\n\nGamma.\n"
    sol = "# Chapter 1\n\nAlpha improved.\n\nBeta improved.\n\nGamma.\n"
    diff = mastering.build_diff(baseline, sol, [])
    assert diff["hunk_count"] >= 1
    # SequenceMatcher may group adjacent changed paragraphs into one hunk.
    decisions = []
    for h in diff["hunks"]:
        decisions.append({"hunk_id": h["hunk_id"], "decision": "REPAIR", "replacement": "Alpha repaired.\n\nBeta repaired.", "reason": "test"})
    out = mastering.assemble_from_decisions(baseline, sol, {"decisions": decisions})
    assert "Alpha repaired." in out
    assert "Beta repaired." in out
    assert out.startswith("# Chapter 1")


def test_terminology_alerts_treat_slash_terms_as_alternatives():
    glossary = [{"korean": "기세", "english": "**aura** / **momentum**"}]
    switched = mastering.build_diff(
        "# Chapter 1\n\nTheir momentum returned.\n",
        "# Chapter 1\n\nAn aura pressed down.\n",
        glossary,
    )
    assert switched["global_terminology_alerts"] == []
    assert all(not h["terminology_alerts"] for h in switched["hunks"])
    dropped = mastering.build_diff(
        "# Chapter 1\n\nTheir momentum returned.\n",
        "# Chapter 1\n\nThe pressure returned.\n",
        glossary,
    )
    assert dropped["global_terminology_alerts"][0]["preferred"] == "aura / momentum"


def test_expected_live_hash_uses_promoted_copy():
    baseline = mastering.expected_live_translation_hash({"stage": "VERIFIED", "baseline_sha256": "aaa"})
    promoted = mastering.expected_live_translation_hash({"stage": "PROMOTED", "baseline_sha256": "aaa", "promoted_sha256": "bbb"})
    assert baseline == "aaa"
    assert promoted == "bbb"


def test_finish_for_commit_skips_when_already_promoted(monkeypatch):
    calls = []

    def fake_state(_number):
        return {"stage": "PROMOTED", "qa_passed": True}

    monkeypatch.setattr(mastering, "state_for", fake_state)
    monkeypatch.setattr(mastering, "command_master", lambda *_a, **_k: calls.append("master"))
    monkeypatch.setattr(mastering, "command_promote", lambda *_args: calls.append("promote"))
    mastering.command_finish_for_commit(3)
    assert calls == []


def test_validate_adjudication_requires_exact_hunks():
    diff = {"hunks": [{"hunk_id": "H001"}, {"hunk_id": "H002"}]}
    value = {
        "chapter": 7,
        "decisions": [
            {"hunk_id": "H001", "decision": "SOL", "reason": "better"},
            {"hunk_id": "H002", "decision": "BASE", "reason": "faithful"},
        ],
    }
    normalized = mastering.validate_adjudication(value, 7, diff)
    assert [d["decision"] for d in normalized["decisions"]] == ["SOL", "BASE"]


def test_normalize_strips_single_fence():
    value = "```markdown\n# Chapter 2\n\nText.\n```"
    assert mastering.normalize_chapter(value) == "# Chapter 2\n\nText.\n"


def test_apply_fidelity_repairs_only_major_findings():
    text = "# Chapter 1\n\nCounter (2 / 100).\n\nKeep this.\n"
    review = {
        "findings": [
            {
                "id": "F01",
                "severity": "major",
                "current": "Counter (2 / 100).",
                "replacement": "Successful repetitions (2 / 100).",
            },
            {
                "id": "F02",
                "severity": "minor",
                "current": "Keep this.",
                "replacement": "Keep that.",
            },
        ]
    }
    repaired, count = mastering.apply_fidelity_repairs(text, review, 0.98)
    assert count == 1
    assert "Successful repetitions (2 / 100)." in repaired
    assert "Keep this." in repaired


def test_apply_fidelity_repairs_skips_missing_current_span():
    text = "# Chapter 1\n\nAlpha phrase.\n"
    review = {
        "findings": [{
            "id": "F01",
            "severity": "major",
            "current": "Missing span.",
            "replacement": "Replacement.",
        }]
    }
    repaired, count = mastering.apply_fidelity_repairs(text, review, 0.9)
    assert count == 0
    assert repaired == mastering.normalize_chapter(text)


def test_filter_fidelity_findings_drops_absent_and_glossary_regressions():
    text = "# Chapter 62\n\n*One Annihilation.*\n\nGunggwimun waited.\n"
    glossary = [
        {"korean": "일섬", "english": "**One Annihilation**"},
        {"korean": "궁귀문", "english": "**Gunggui Sect**"},
    ]
    findings = [
        {
            "id": "F01",
            "severity": "major",
            "current": "One Annihilation.",
            "replacement": "One Flash.",
        },
        {
            "id": "F02",
            "severity": "major",
            "current": "the Gunggui Sect",
            "replacement": "Gunggwimun",
        },
        {
            "id": "F03",
            "severity": "major",
            "current": "Gunggwimun waited.",
            "replacement": "Gunggui Sect waited.",
        },
    ]
    kept, dropped = mastering.filter_fidelity_findings(text, findings, glossary)
    assert [item["id"] for item in kept] == ["F03"]
    assert any("glossary regression" in note for note in dropped)
    assert any("current span absent" in note for note in dropped)


def test_command_qa_applies_blocking_repairs_before_final_gate():
    work = Path(tempfile.mkdtemp())
    source = work / "source.txt"
    baseline = work / "baseline.md"
    final = work / "final.md"
    source.write_text("원문\n", encoding="utf-8")
    baseline.write_text("# Chapter 9\n\nWe hold it down.\n", encoding="utf-8")
    final.write_text("# Chapter 9\n\nWe hold it down.\n", encoding="utf-8")
    paths = {
        "final": final,
        "source": source,
        "baseline": baseline,
        "qa": work / "qa.json",
        "fidelity_packet": work / "fidelity-packet.md",
        "fidelity_review": work / "fidelity-review.json",
        "state": work / "state.json",
        "metrics": work / "metrics.json",
        "logs": work / "omp",
    }
    paths["logs"].mkdir()
    state = {"stage": "ASSEMBLED", "version": 1, "chapter": 9}
    gate_calls = {"n": 0}

    def fake_gate(_number, _source, current_final, *_args, **_kwargs):
        gate_calls["n"] += 1
        if "We hold it down." in current_final:
            return {
                "summary": "blocked",
                "findings": [{
                    "id": "F01",
                    "severity": "major",
                    "current": "We hold it down.",
                    "replacement": "That thing must be held off.",
                    "confidence": 0.99,
                }],
            }
        return {"summary": "clean", "findings": []}

    with (
        patch.object(mastering, "create_or_verify_state", return_value=(state, paths)),
        patch.object(mastering, "run_qa", return_value={"passed": True, "errors": [], "warnings": []}),
        patch.object(mastering, "run_fidelity_gate", side_effect=fake_gate),
        patch.object(mastering, "load_config", return_value={
            "quality_gate_min_auto_confidence": 0.9,
            "quality_gate_max_rounds": 3,
        }),
        patch.object(mastering, "exact_glossary", return_value=[]),
        patch.object(mastering, "validate_chapter", lambda *_a, **_k: None),
    ):
        mastering.command_qa(9)
    assert gate_calls["n"] == 2
    assert "That thing must be held off." in final.read_text(encoding="utf-8")
    recorded = json.loads(paths["state"].read_text(encoding="utf-8"))
    assert recorded["stage"] == "VERIFIED"
    assert recorded["qa_passed"] is True
    assert recorded["fidelity_repairs"] == 1


def test_command_qa_applies_repairs_on_final_round():
    work = Path(tempfile.mkdtemp())
    source = work / "source.txt"
    baseline = work / "baseline.md"
    final = work / "final.md"
    source.write_text("원문\n", encoding="utf-8")
    baseline.write_text("# Chapter 9\n\nWe hold it down.\n", encoding="utf-8")
    final.write_text("# Chapter 9\n\nWe hold it down.\n", encoding="utf-8")
    paths = {
        "final": final,
        "source": source,
        "baseline": baseline,
        "qa": work / "qa.json",
        "fidelity_packet": work / "fidelity-packet.md",
        "fidelity_review": work / "fidelity-review.json",
        "state": work / "state.json",
        "metrics": work / "metrics.json",
        "logs": work / "omp",
    }
    paths["logs"].mkdir()
    state = {"stage": "ASSEMBLED", "version": 1, "chapter": 9}
    gate_calls = {"n": 0}

    def fake_gate(_number, _source, current_final, *_args, **_kwargs):
        gate_calls["n"] += 1
        if "We hold it down." in current_final:
            return {
                "summary": "blocked",
                "findings": [{
                    "id": "F01",
                    "severity": "major",
                    "current": "We hold it down.",
                    "replacement": "That thing must be held off.",
                    "confidence": 0.99,
                }],
            }
        return {"summary": "clean", "findings": []}

    with (
        patch.object(mastering, "create_or_verify_state", return_value=(state, paths)),
        patch.object(mastering, "run_qa", return_value={"passed": True, "errors": [], "warnings": []}),
        patch.object(mastering, "run_fidelity_gate", side_effect=fake_gate),
        patch.object(mastering, "load_config", return_value={
            "quality_gate_min_auto_confidence": 0.9,
            "quality_gate_max_rounds": 1,
        }),
        patch.object(mastering, "exact_glossary", return_value=[]),
        patch.object(mastering, "validate_chapter", lambda *_a, **_k: None),
    ):
        mastering.command_qa(9)
    assert gate_calls["n"] == 2
    assert "That thing must be held off." in final.read_text(encoding="utf-8")
    recorded = json.loads(paths["state"].read_text(encoding="utf-8"))
    assert recorded["stage"] == "VERIFIED"
    assert recorded["qa_passed"] is True


def test_apply_fidelity_repairs_rejects_truncated_model_replacement():
    review = {
        "findings": [{
            "id": "F01",
            "severity": "critical",
            "confidence": 1.0,
            "current": "Keep this.",
            "replacement": "[Showing lines 1-300 of 389. Use :301 to continue]",
        }]
    }
    try:
        mastering.apply_fidelity_repairs("# Chapter 1\n\nKeep this.\n", review, 0.95)
    except ValueError as error:
        assert "pagination marker" in str(error)
    else:
        raise AssertionError("truncated replacement was accepted")


def test_fuzzy_alignment_does_not_collapse_fully_edited_chapter():
    baseline = "# Chapter 1\n\nThe hunter walked home.\n\nHe opened the door.\n\nThe room was empty.\n"
    sol = "# Chapter 1\n\nThe hunter headed home.\n\nHe pushed the door open.\n\nNo one was inside.\n"
    diff = mastering.build_diff(baseline, sol, [])
    # Heading remains an anchor and edited prose is adjudicable in small units.
    assert diff["hunk_count"] == 3
    assert all(len(h["baseline_range"]) == 2 for h in diff["hunks"])


def test_master_packet_owns_full_copy_polish():
    packet = mastering.master_packet(
        1,
        "＃1화\n\n원문.\n",
        "# Chapter 1\n\nBaseline.\n",
        [],
    )
    assert "## Project polish guidance" in packet
    assert "Translate the thought, not the Korean sentence structure" in packet
    assert "## Current accepted English baseline" in packet
    assert "## Matched address pairs" in packet
    assert "## Matched risk notes" in packet


def test_fidelity_gate_packet_includes_baseline_regression_anchor():
    work = Path(tempfile.mkdtemp())
    paths = mastering.chapter_paths(1)
    paths["fidelity_packet"] = work / "fidelity-packet.md"
    packet_source = "＃1화\n\n원문.\n"
    # Build the packet without invoking OMP; the helper writes the packet
    # immediately before its model call.
    with patch.object(mastering, "run_omp", return_value=(
        '{"findings":[]}', {"requests": 1}, NullCall()
    )):
        with patch.object(mastering, "atomic_json"):
            with patch.object(mastering, "save_metric"):
                mastering.run_fidelity_gate(
                    1,
                    packet_source,
                    "# Chapter 1\n\nFinal.\n",
                    {"passed": True},
                    paths,
                    baseline="# Chapter 1\n\nBaseline.\n",
                )
    assert "## Accepted baseline for regression comparison" in paths["fidelity_packet"].read_text()
    assert "Baseline." in paths["fidelity_packet"].read_text()


def test_adjudicator_packet_is_compact():
    source = "＃1화\n\n“쓰레기네.”\n\n진호가 말했다.\n"
    baseline = "# Chapter 1\n\n“It’s garbage.”\n\nJinho spoke.\n"
    sol = "# Chapter 1\n\n“It’s garbage.”\n\nJinho said it.\n"
    diff = mastering.build_diff(baseline, sol, [], source)
    assert diff["hunk_count"] == 1
    hunk = diff["hunks"][0]
    assert hunk["baseline_paragraphs"] == "P3"
    assert hunk["sol_paragraphs"] == "P3"
    assert hunk["korean_lines"] == "5"
    assert "context_before_baseline" not in hunk
    packet = mastering.adjudicator_packet(1, source, baseline, sol, [], diff)
    assert "## Complete numbered SOL English" in packet
    assert "BASE context before" not in packet
    assert "SOL context after" not in packet
    assert "Baseline paragraphs: P3" in packet
    assert "SOL paragraphs: P3" in packet
    assert "Korean lines: 5" in packet
    assert "[P1]" in packet
    assert "1|＃1화" in packet
    assert packet.count("Jinho spoke.") == 2
    assert packet.count("Jinho said it.") == 2
    hunk_section = packet.split("## Numbered diff hunks", 1)[1]
    assert "Jinho spoke." in hunk_section
    assert "Jinho said it." in hunk_section
    sections = [
        "## Korean source",
        "## Complete BASELINE English",
        "## Complete numbered SOL English",
        "## Exact glossary matches for this Korean chapter",
        "## Adjudicator rules",
        "## Critical binding translation rules",
        "## Numbered diff hunks",
    ]
    indexes = [packet.index(name) for name in sections]
    assert indexes == sorted(indexes)


def test_expected_live_hash_uses_promoted_copy():
    baseline = mastering.expected_live_translation_hash({"stage": "VERIFIED", "baseline_sha256": "aaa"})
    promoted = mastering.expected_live_translation_hash(
        {"stage": "PROMOTED", "baseline_sha256": "aaa", "promoted_sha256": "bbb"}
    )
    assert baseline == "aaa"
    assert promoted == "bbb"


def test_run_skips_when_already_promoted():
    calls: list[str] = []
    with patch.object(mastering, "state_for", return_value={"stage": "PROMOTED", "qa_passed": True}):
        with patch.object(mastering, "command_master", lambda *_a, **_k: calls.append("master")):
            with patch.object(mastering, "command_adjudicate", lambda *_a, **_k: calls.append("adjudicate")):
                with patch.object(mastering, "command_assemble", lambda *_a, **_k: calls.append("assemble")):
                    with patch.object(mastering, "command_qa", lambda *_a, **_k: calls.append("qa")):
                        with patch.object(mastering, "command_promote", lambda *_a, **_k: calls.append("promote")):
                            mastering.command_run(11)
    assert calls == []


def test_run_promotes_when_already_verified():
    calls: list[str] = []

    def fake_state(_number):
        if "promote" in calls:
            return {"stage": "PROMOTED", "qa_passed": True}
        return {"stage": "VERIFIED", "qa_passed": True}

    with patch.object(mastering, "state_for", side_effect=fake_state):
        with patch.object(mastering, "chapter_paths", return_value={"qa": Path("reviews/mastering/0011/qa.json")}):
            with patch.object(mastering, "command_master", lambda *_a, **_k: calls.append("master")):
                with patch.object(mastering, "command_qa", lambda *_a, **_k: calls.append("qa")):
                    with patch.object(
                        mastering,
                        "command_promote",
                        lambda number, confirm: calls.append(f"promote:{confirm}"),
                    ):
                        mastering.command_run(11)
    assert calls == ["promote:REPLACE_TRANSLATIONS"]


def test_run_escalates_from_readjudicate_to_remaster():
    calls: list[str] = []
    qa_results = iter([
        {"stage": "QA_FAILED", "qa_passed": False},
        {"stage": "QA_FAILED", "qa_passed": False},
        {"stage": "QA_FAILED", "qa_passed": False},
        {"stage": "VERIFIED", "qa_passed": True},
        {"stage": "VERIFIED", "qa_passed": True},
    ])

    def fake_state(_number):
        return next(qa_results)

    def track(name):
        def _inner(*_args, **kwargs):
            force = kwargs.get("force")
            calls.append(f"{name}:force" if force else name)
        return _inner

    with (
        patch.object(mastering, "state_for", side_effect=fake_state),
        patch.object(mastering, "chapter_paths", return_value={
            "qa": Path("reviews/mastering/0011/qa.json"),
            "fidelity_review": Path("reviews/mastering/0011/fidelity-review.json"),
            "state": Path("reviews/mastering/0011/state.json"),
        }),
        patch.object(mastering, "load_config", return_value={
            "qa_retry_readjudicate": 1,
            "qa_retry_remaster": 1,
        }),
        patch.object(mastering, "command_master", side_effect=track("master")),
        patch.object(mastering, "command_adjudicate", side_effect=track("adjudicate")),
        patch.object(mastering, "command_assemble", side_effect=track("assemble")),
        patch.object(mastering, "command_qa", side_effect=track("qa")),
        patch.object(mastering, "command_promote", side_effect=track("promote")),
        patch.object(mastering, "update_state", lambda *_a, **_k: None),
    ):
        mastering.command_run(11)
    assert calls == [
        "master",
        "adjudicate",
        "assemble",
        "qa",
        "adjudicate:force",
        "assemble",
        "qa",
        "master:force",
        "adjudicate:force",
        "assemble",
        "qa",
        "promote",
    ]


def test_run_stops_after_bounded_retries():
    calls: list[str] = []

    def fake_state(_number):
        return {"stage": "QA_FAILED", "qa_passed": False}

    def track(name):
        def _inner(*_args, **kwargs):
            force = kwargs.get("force")
            calls.append(f"{name}:force" if force else name)
        return _inner

    with (
        patch.object(mastering, "state_for", side_effect=fake_state),
        patch.object(mastering, "chapter_paths", return_value={
            "qa": mastering.ROOT / "reviews/mastering/0011/qa.json",
            "fidelity_review": mastering.ROOT / "reviews/mastering/0011/fidelity-review.json",
        }),
        patch.object(mastering, "load_config", return_value={
            "qa_retry_readjudicate": 1,
            "qa_retry_remaster": 1,
        }),
        patch.object(mastering, "command_master", side_effect=track("master")),
        patch.object(mastering, "command_adjudicate", side_effect=track("adjudicate")),
        patch.object(mastering, "command_assemble", side_effect=track("assemble")),
        patch.object(mastering, "command_qa", side_effect=track("qa")),
        patch.object(mastering, "command_promote", side_effect=track("promote")),
    ):
        try:
            mastering.command_run(11)
            assert False, "expected exhaustion error"
        except ValueError as error:
            assert "after 1 re-adjudicate and 1 remaster" in str(error)
    assert "promote" not in calls
    assert calls.count("master:force") == 1
    assert calls.count("adjudicate:force") == 2


def test_assemble_skips_existing_final_after_verified():
    work = Path(tempfile.mkdtemp())
    number = 11
    final = work / "final.md"
    final.write_text("# Chapter 11\n\nDone.\n", encoding="utf-8")
    sol = work / "sol.md"
    sol.write_text("# Chapter 11\n\nDone.\n", encoding="utf-8")
    adjudication = work / "adjudication.json"
    adjudication.write_text('{"decisions":[]}\n', encoding="utf-8")
    paths = {
        "final": final,
        "sol": sol,
        "adjudication": adjudication,
        "baseline": work / "baseline.md",
        "state": work / "state.json",
    }
    state = {"stage": "VERIFIED", "qa_passed": True, "final_sha256": "x"}
    with patch.object(mastering, "create_or_verify_state", return_value=(state, paths)):
        with patch.object(mastering, "assemble_from_decisions", side_effect=AssertionError("should skip")):
            mastering.command_assemble(number)
    assert final.read_text(encoding="utf-8") == "# Chapter 11\n\nDone.\n"


def test_qa_skips_when_already_verified():
    work = Path(tempfile.mkdtemp())
    final_text = "# Chapter 11\n\nDone.\n"
    final = work / "final.md"
    final.write_text(final_text, encoding="utf-8")
    paths = {"final": final, "source": work / "source.txt", "qa": work / "qa.json"}
    state = {
        "stage": "VERIFIED",
        "qa_passed": True,
        "final_sha256": mastering.sha256_text(mastering.normalize_chapter(final_text)),
    }
    with patch.object(mastering, "create_or_verify_state", return_value=(state, paths)):
        with patch.object(mastering, "run_fidelity_gate", side_effect=AssertionError("should skip")):
            mastering.command_qa(11)


def test_adjudicator_run_omp_passes_deepseek_overlay():
    work = Path(tempfile.mkdtemp())
    packet = work / "packet.md"
    packet.write_text("x", encoding="utf-8")
    captured: dict[str, list[str]] = {}

    def fake_run(command, **_kwargs):
        captured["command"] = command
        return "# Chapter 1\n", {"exact": True}

    with patch("tools.omp_json.run_json_command", fake_run):
        mastering.run_omp(
            packet,
            "cursor/cursor-grok-4.6:low",
            120,
            work / "log.jsonl",
            extra_configs=[".omp/adjudicator-overlay.yml"],
        )
    configs = [item for i, item in enumerate(captured["command"]) if captured["command"][i - 1] == "--config"]
    assert any(str(item).endswith("review-overlay.yml") for item in configs)
    assert any(str(item).endswith("adjudicator-overlay.yml") for item in configs)
    assert captured["command"][captured["command"].index("--model") + 1] == "cursor/cursor-grok-4.6:low"
