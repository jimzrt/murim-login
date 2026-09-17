# Korean source chapters

Licensed originals are **not** stored in the public repository. They live in
the private companion [jimzrt/murim-login-source](https://github.com/jimzrt/murim-login-source)
as `NNNN.txt` files. GitHub Pages and the ebook build do not need them.

On a translation machine, clone that repo **directly into** `source/`:

```bash
python tools/sync_source.py
```

The first run clones `jimzrt/murim-login-source` into `source/`. Later runs
`git fetch` and fast-forward. `gh auth login` is enough; the script uses
`gh auth token` when `gh` is available.

That also refreshes `reader/src/generated/source-count.ts` when the chapter set
changes. Commit the generated file if the total changed.

The VPS worker still uses a **sibling** clone (`murim-login-source/` next to
Compose) bind-mounted over `/app/source`. See `docs/LINE_REPORT.md`.
