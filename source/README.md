# Korean source chapters

Licensed originals are **not** stored in the public repository.

Place `NNNN.txt` files (zero-padded chapter numbers) in this directory on
machines that draft, review, master, or evaluate line reports. GitHub Pages and
the ebook build do not need them.

Typical local layout after cloning a private companion repo:

```bash
git clone git@github.com:<you>/murim-login-source.git source
```

If `source/` already exists as this placeholder directory, clone into a sibling
folder and copy or replace these files. Rebuild the reader progress total with
`npm run sync-source-count` in `reader/` when the chapter set changes.
