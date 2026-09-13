# Murim Login translation benchmark

Frozen regression items for already accepted chapters. This is a maintenance
tool, not a chapter-transaction stage: it does not draft, review, master, or
advance `docs/STATE.md`.

Each line in `items.jsonl` is one object:

- `id`, `chapter`, `category`, `source` (exact Korean span)
- `constraint` (the interpretation to preserve)
- optional `required` / `forbidden` English spans
- `origin` (review, adjudication, QA, or rules path)

Prefer forbidden traps over a single sacred English sentence. Binding
terminology may use `required`.

```bash
python tools/benchmark.py
python tools/benchmark.py --chapter 64
python tools/benchmark.py --json
```
