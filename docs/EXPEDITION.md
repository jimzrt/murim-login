# Chapter 374 Expedition (catch-up from 370)

This branch is a temporary, intentionally gapped translation line. The Git
branch name remains `expedition/chapter-374`. It must not be merged wholesale
into `master`.

The first expedition pass started at Chapter 374 and accepted 374–375. Those
reading copies stay in the tree. The line now backfills 370–373 against the
Chapter 65 master anchor, then resumes at 376 without redoing 374–375.

## Continuity contract

- Chapters 0–65 are accepted local translations and remain available as an
  anchor.
- Chapters 66–369 are skipped. Their Korean source exists, but there is no
  accepted English continuity for them in this branch.
- Chapters 370–373 are the current catch-up translations. Run the normal
  transaction workflow for each of them.
- Chapters 374–375 are parked accepted translations. After Chapter 373 is
  committed, run `python tools/expedition.py resume-parked` before `run_next`.
  That restores the parked 375 `STATE`/`CONTEXT` and sets next chapter to 376.
- If a later chapter requires a fact from the skipped range, record the
  uncertainty and prefer the current Korean source over guesses, parked later
  chapters, or web-fan summaries. Do not backfill skipped chapters silently.

Do not put 371–375 plot into `docs/CONTEXT.json` or `docs/EXPEDITION_SEED.md`
while drafting 370. Parked snapshots live under `docs/expedition-parked/`.

## Running the expedition

From this worktree:

```bash
python tools/expedition.py check
python tools/workflow.py status 370 --json
python tools/run_next.py
python tools/run_until.py 373
python tools/expedition.py resume-parked
python tools/run_next.py
```

`run_next.py` reads `docs/STATE.md`. Do not edit `STATE.md` or `CONTEXT.json`
manually after catch-up chapters start, except via `resume-parked` at the 373/374
boundary. Use the normal workflow update stage.

## Publication

The Pages publication is built by the separate repository
`jimzrt/murim-login-expedition-pages`. The source branch dispatches a build
only after `translations/0374.md` exists. The rolling expedition ebook release
uses the tag `expedition-ebook`, never the canonical `ebook` release.

The source repository needs an `EXPEDITION_PAGES_TOKEN` secret with permission
to dispatch workflows in the Pages repository. The Pages repository must have
GitHub Pages configured with **GitHub Actions** as its source.

The public reader should label the skipped range so readers do not mistake the
expedition edition for a complete chronological release.
