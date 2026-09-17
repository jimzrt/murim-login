# Murim Login Translation Harness

Translate exactly one explicitly requested chapter. Never start the next chapter.

## Routine Trigger

For the next chapter, the preferred entry point is:

```bash
python tools/run_next.py
```

It reads the exact next chapter from `docs/STATE.md`, executes each controller
action reported by `status` through `ACCEPTED`, creates `Accept Chapter N`,
registers that commit, and stops at `COMMITTED`. Mastering is a separate queue:

```bash
python tools/run_next_mastering.py
```

It picks the oldest accepted chapter that is not yet promoted, runs the
two-model overlay, promotes the verified copy, creates `Master Chapter N`, and
registers that commit. The two runners may overlap: translation holds
`.work/run.lock`, mastering holds `.work/master.lock`, and Git commits wait on
`.work/commit.lock`. Inspect locks with `python tools/run_lock.py`. An audit
takes both work locks. The wrappers require a clean Git worktree for their own
path set; dirt owned by the other runner is ignored.

## Controller Loop

For chapter `N`, run `python tools/workflow.py status N`. Perform only the
reported next action, then run `status` again. Never infer a stage from chat
history or skip, combine, or reorder stages. Stop at `COMMITTED`, or immediately
on ambiguity, stale hashes, failed QA, an over-budget packet, invalid model JSON,
or any failed command. After `COMMITTED`, stop the translation runner; do not
begin another chapter from the same `run_next` invocation.

The controller owns retrieval, phase-specific packets, model calls, QA, review
completion, hashes, promotion, recovery, and the next action. Routine work must
not load other chapter source files, the full compendium, archive directories, or
`characters/spoilers/`.

If draft fails because the first nonblank line is not `# Chapter N`, do not
rerun the model. If `.work/NNNN/draft-raw.txt` contains the heading after a
short preamble, write the text from that heading onward into `draft.md` and run
`python tools/workflow.py drafted N`. QA reports live at
`reviews/qa/NNNN-draft.json` and `NNNN-final.json`. `translations/NNNN.md` does
not exist until `accept`.

## Model-Facing Context

- `docs/CONTEXT.json` is the bounded active state. Keep `version`, `safe_through`,
  `continuity_sources`, `active_continuity`, `open_questions`, and
  `temporary_decisions`. Keep only active continuity, unresolved questions,
  temporary decisions, and zero to two explicit `continuity_sources`. Move
  stable facts to profiles/compendium and resolved plot to summaries.
- Draft receives the source, complete rules, exact glossary matches, matching
  address pairs, matching risk notes, compact identity/voice/relationship
  fields from matching profiles, bounded active state, latest summary, and
  only the explicitly named continuity reading copies. Archived per-chapter
  profile continuity is not injected.
- Review receives the source, draft, rules, exact glossary matches, the same
  matching address pairs and risk notes, the same compact matching profiles,
  active continuity, and deterministic QA. It does not receive prior
  translations or the summary archive.
- Revision is deterministic: it applies each review finding's exact, unique
  `current` → `replacement` span to the reviewed draft. It makes no model call
  and receives no additional context.
- Summarize receives the previous block summary, this block's chapter beats,
  and bounded active state. It does not receive full reading copies.

## Gates

- The draft model drafts; deterministic QA must pass; the review model returns
  validated structured findings with exact finished replacements. Revision
  applies those replacements atomically, blocks on missing, repeated, or
  overlapping spans, and runs final QA. The mastering editor is the only
  later full-copy fluency edit and applies `POLISH.md`. Adjudication is Luna
  `:high` with a SOL-default meaning veto (`MASTERING_ADJUDICATOR.md`). The
  fidelity gate is a different model (`MASTERING_FIDELITY.md`).
- Reviews are durable JSON with generated Markdown reading reports. Checkpoint
  dispositions remain structured and unresolved critical or major checkpoint
  findings block acceptance.
- At `REVISED`, run
  `python tools/workflow.py update N`. Its bounded no-tools model call returns
  structured chapter facts; the controller validates and deterministically
  writes `docs/NAMES.md`, `docs/ADDRESS.md`, affected safe profiles, `docs/CONTEXT.json`,
  `docs/STATE.md`, and `summaries/beats/NNNN.md`. It records the packet and
  exact output under `reviews/`. Do not edit those generated updates manually.
  When status asks for it, run `python tools/workflow.py summarize N`.
- Follow configured checkpoint actions. Never substitute `/advisor`, a hub,
  task agent, nested session, or direct `omp` invocation. `run_next.py` must
  wait for each `workflow.py` command; do not background it.

## Acceptance

`accept` creates the baseline `translations/NNNN.md` and advances the primary
transaction to `ACCEPTED`. Commit the chapter, structured review, QA, metrics,
and relevant durable-context changes from `ACCEPTED`, then register the exact
commit. That registration advances the transaction to `COMMITTED`.

Mastering is not part of that commit. `python tools/run_next_mastering.py`
runs `master` on the oldest `COMMITTED` chapter that is not yet promoted,
promotes the verified copy over `translations/NNNN.md`, advances the same
transaction to `MASTERED`, commits `Master Chapter N`, and registers
`MASTERED_COMMITTED`. The pre-master snapshot remains at
`reviews/mastering/NNNN/baseline.md`. Never commit `.work/`, caches, or an
unaccepted draft.

Accept commits may only contain the deterministic accept path set for that
chapter. Mastering commits may only contain that chapter's translation, its
`reviews/mastering/NNNN/` tree, and `reviews/metrics/NNNN.json`.

Binding language policy is in `RULES.md`. Configuration is in
`docs/workflow.json`. Read `docs/WORKFLOW.md` only for recovery, profiles,
checkpoint tuning, or exports.

## Retrospective Range Audit

When the user explicitly requests a new pass over already accepted chapters,
do not reopen their normal chapter transactions. Run
`python tools/audit_range.py status START END`, follow only its reported actions,
and stop at `VERIFIED`. This maintenance flow performs deterministic QA, bounded
parallel block reviews, one patch-planning call, exact atomic replacements, and
final QA. It never advances `docs/STATE.md` or `docs/CONTEXT.json`.
