# Mastering Queue and Overlay

Mastering is a separate, lagging FIFO queue after a chapter has been accepted and committed. It is not part of the ordinary translation transaction.

The normal commands are:

```bash
python tools/run_next.py
python tools/run_next_mastering.py
```

`run_next.py` processes exactly one chapter through acceptance, creates `Accept Chapter N`, registers the commit, and stops at `COMMITTED`. `run_next_mastering.py` selects the oldest `COMMITTED` chapter that is not yet promoted, runs the mastering overlay, promotes the verified copy into `translations/`, creates `Master Chapter N`, registers it, and stops at `MASTERED_COMMITTED`.

The pre-master accepted copy remains at `reviews/mastering/NNNN/baseline.md`.

## Overlay stages

```text
accepted translation
       ↓
mastering editor
       ↓
paragraph-aware deterministic diff
       ↓
meaning adjudicator: SOL / BASE / REPAIR per changed hunk
       ↓
assembled candidate
       ↓
deterministic QA
       ↓
independent fidelity gate
       ↓
bounded fidelity repair rounds, when required
       ↓
final QA and verification
       ↓
promote into translations/ and register MASTERED_COMMITTED
```

The overlay has three model roles, not two:

1. **Mastering editor** — performs the full-copy fluency edit.
2. **Adjudicator** — evaluates each changed hunk and chooses `SOL`, `BASE`, or `REPAIR`; the current configured model is Luna `:high` with a SOL-default meaning veto.
3. **Fidelity gate** — independently checks the assembled chapter against the Korean source and accepted baseline; the current configured model is GPT-4.1 Mini.

The fidelity gate may produce bounded automatic repairs. Invalid gate JSON is treated as a failed round. If verification still fails, the controller can re-adjudicate once and remaster once according to `docs/mastering.json`. It stays on the same chapter and never skips ahead.

## Current configuration

Primary selectors live in `docs/mastering.json`:

```json
{
  "models": {
    "master": "openai-codex/gpt-5.6-sol:medium",
    "adjudicator": "openai-codex/gpt-5.6-luna:high",
    "quality_gate": "openrouter/openai/gpt-4.1-mini"
  },
  "quality_gate_max_rounds": 3,
  "qa_retry_readjudicate": 1,
  "qa_retry_remaster": 1,
  "run_until_mastering_retries": 2,
  "run_until_mastering_retry_delay_seconds": 30
}
```

The actual file also configures packet limits, timeouts, OMP configuration files, context lookback, safe-profile injection, and fidelity confidence thresholds. Change model identifiers only when your local OMP configuration requires different names.

Sol is requested through the configured OMP chain. The adjudicator and fidelity gate use their configured OMP/provider paths; inspect `.omp/*.yml` and `docs/mastering.json` for local routing.

## Manual commands

The controller-integrated queue is preferred, but the lower-level mastering CLI remains useful for inspection, reruns, and retrospective work:

```bash
python tools/mastering.py doctor
python tools/mastering.py status 1-10
python tools/mastering.py report 1-10
python tools/mastering.py run 1-10
```

`doctor` checks installation and model configuration without making a paid model call. `run` performs the complete lower-level mastering workflow and promotes verified results. Individual stages can be run separately:

```bash
python tools/mastering.py master 1
python tools/mastering.py adjudicate 1
python tools/mastering.py assemble 1
python tools/mastering.py qa 1
```

Individual stage commands do not replace `translations/` until a verified `run` or explicit `promote` is performed. Use `--force` only on paid model stages when deliberately paying for a rerun:

```bash
python tools/mastering.py adjudicate 1 --force
```

Manual promotion of an already-verified chapter remains available:

```bash
python tools/mastering.py promote 1 --confirm REPLACE_TRANSLATIONS
```

For a bounded queue run through a target chapter, use:

```bash
python tools/run_until_mastering.py 58
```

It retries the same chapter according to the configured limits and stops when retries are exhausted. It does not skip failed chapters.

## Runtime artifacts

Mastering artifacts are stored under:

```text
reviews/mastering/0001/
    baseline.md               # immutable accepted-English snapshot
    master-packet.md
    sol.md                    # editor output
    sol-qa.json
    diff.json
    diff.md
    adjudicator-packet.md
    adjudication.json
    final.md
    qa.json
    metrics.json
    omp/
```

The Korean source is snapshotted and hashed during the transaction; it is not copied into the normal public reading output. The accepted `translations/0001.md` is replaced only after mastering verification succeeds. The baseline remains available for regression comparison.

The mastering commit may contain only the chapter translation, its mastering review tree, and its metrics file. It must not include `.work/`, caches, unrelated chapters, or an unverified draft.

## Retrospective context safety

Do not feed present-day `docs/CONTEXT.json` blindly into an old chapter: it may contain future plot facts.

The mastering packet uses:

* exact glossary rows matched to the current Korean source;
* the latest summary whose end chapter is strictly earlier than the chapter being mastered;
* tails of up to two prior chapters;
* a mastered final from a prior chapter when it has already been verified, otherwise its accepted translation;
* compact identity, voice, and relationship fields only from profiles safe strictly before the chapter being mastered.

Archived chapter-by-chapter profile continuity is not injected. Set `include_safe_profiles` to `false` in `docs/mastering.json` to disable profile injection entirely.

## Diff and adjudication semantics

The diff is paragraph-aware. A hunk can contain one or several adjacent paragraphs when the editor restructures them.

The adjudicator receives:

* the complete Korean source with line numbers;
* the complete accepted baseline English with paragraph labels;
* the complete editor output with paragraph labels;
* exact glossary rows and project fidelity rules;
* numbered changed hunks containing the exact BASE/SOL prose, paragraph references, and Korean citations;
* terminology-risk annotations when a preferred baseline term disappears.

Each hunk must resolve to exactly one of:

* `SOL` — keep the mastering editor's edit;
* `BASE` — revert to the accepted baseline;
* `REPAIR` — neither version is satisfactory; use a narrowly bounded replacement.

The default policy is to preserve the baseline when the editor changes meaning, terminology, formatting, or source-specific texture. Sol is kept when the improvement is concrete and faithful.

After assembly, deterministic QA is followed by the separate whole-chapter fidelity gate. The gate receives the Korean source and accepted baseline so it can detect both newly introduced mistranslations and regressions. High-confidence minor findings and major/critical findings may be repaired automatically within the configured round limit. Unresolved major or critical findings block promotion.

## Safety and state transitions

At the start of mastering, the controller snapshots and hashes the Korean source and accepted English. Later stages abort if either live file changes. After promotion, the live translation must match the promoted final.

The authoritative state is the primary workflow transaction:

```text
COMMITTED
    ↓ workflow master / mastering overlay
MASTERED
    ↓ Master Chapter N commit and registration
MASTERED_COMMITTED
```

`python tools/workflow.py status N` reports the exact next action. Do not edit transaction JSON or manually advance hashes. `run_next_mastering.py` uses the mastering lock; translation uses the separate run lock, and Git commits wait for `.work/commit.lock`.

## Inspecting results

Useful files for a chapter include:

```text
reviews/mastering/0001/baseline.md
reviews/mastering/0001/sol.md
reviews/mastering/0001/diff.md
reviews/mastering/0001/adjudication.json
reviews/mastering/0001/final.md
reviews/mastering/0001/qa.json
reviews/metrics/0001.json
```

Use the project cost report for provider-reported usage and workload metrics:

```bash
python tools/cost_report.py --chapter 1
python tools/cost_report.py --chapter 1 --json
```

For a frozen comparison without promotion, use:

```bash
python tools/mastering_ab.py 1
```

The report separates editor, adjudicator, and fidelity-gate work where provider metrics are available, and records hunk decisions as `SOL`, `BASE`, or `REPAIR`.
