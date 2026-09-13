# Chapter 374 Expedition

This branch is a temporary, intentionally gapped translation line. It starts
with Chapter 374 and must not be merged wholesale into `master`.

## Continuity contract

- Chapters 0–64 are accepted local translations and remain available as an
  anchor.
- Chapters 65–370 are skipped. Their Korean source exists, but there is no
  accepted English continuity for them in this branch.
- Chapters 371–373 have source-grounded bridge summaries under
  `summaries/0369-0373.md` and `summaries/beats/`. They are orientation only,
  not translations or proof of every intervening fact.
- Chapter 374 starts the normal transaction workflow. From Chapter 374 onward,
  `workflow.py update`, summaries, profiles, names, QA, hashes, and mastering
  are authoritative for this branch.
- If a later chapter requires a fact from the skipped range, record the
  uncertainty and prefer the current Korean source over guesses or web-fan
  summaries. Do not backfill skipped chapters silently.

## Running the expedition

From this worktree:

```bash
python tools/expedition.py check
python tools/workflow.py status 374 --json
python tools/run_next.py
python tools/run_until.py 378
```

`run_next.py` reads the expedition `docs/STATE.md`; after Chapter 374 is
committed it advances normally to 375 and so on. Do not edit `STATE.md` or
`CONTEXT.json` manually after the first expedition chapter. Use the normal
workflow update stage.

## Publication

The Pages publication is built by the separate repository
`jimzrt/murim-login-expedition-pages`. The source branch dispatches a build
only after `translations/0374.md` exists. The rolling expedition ebook release
uses the tag `expedition-ebook`, never the canonical `ebook` release.

The source repository needs an `EXPEDITION_PAGES_TOKEN` secret with permission
to dispatch workflows in the Pages repository. The Pages repository must have
GitHub Pages configured with **GitHub Actions** as its source.

The public reader labels the skipped range so readers do not mistake the
expedition edition for a complete chronological release.
