# Parked Chapter 374–375 progress

These snapshots were taken from `origin/expedition/chapter-374` after Chapters
374 and 375 were accepted, before the line was retargeted to start at 370.

- `CONTEXT-0375.json` — durable context after Chapter 375
- `STATE-0375.md` — translation state with last completed 375 / next 376

After Chapters 370–373 are committed, restore them with:

```bash
python tools/expedition.py resume-parked
```

Do not load these files into draft packets while catching up 370–373.
