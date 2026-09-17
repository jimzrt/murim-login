# Korean source chapters

Licensed originals are **not** stored in the public repository.

Place `NNNN.txt` files (zero-padded chapter numbers) in this directory on
machines that draft, review, master, or evaluate line reports. GitHub Pages and
the ebook build do not need them.

Typical local layout after cloning the private companion repo:

```bash
git clone git@github.com:jimzrt/murim-login-source.git source
```

On the VPS, clone it as a sibling of the public repo (`murim-login-source/`)
with host `gh` (`gh repo clone jimzrt/murim-login-source murim-login-source`)
and let Compose mount it at `/app/source`. If `source/` already exists as this
placeholder directory, clone into a sibling folder and copy or replace these
files. Rebuild the reader progress total with `npm run sync-source-count` in
`reader/` when the chapter set changes.
