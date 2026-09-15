# Line reports (reader → GitHub → PR)

Readers can select a passage in the web reader, describe the problem, and submit
without leaving the site. Only **mastered** chapters are accepted
(`reviews/mastering/NNNN/state.json` with `stage: PROMOTED` and `qa_passed`).
A GitHub App opens a `line-report` issue, evaluates it
with the same chapter-safe packet as `tools/refine_translation.py`, comments
strategies, and opens a pull request when you reply `/apply A`. Merging that PR
closes the issue.

Interactive local steering is unchanged:

```bash
python tools/refine_translation.py "quoted English"
```

## VPS pieces

Caddy serves these on `murim-login.com` (not under `/api`, which is Remark42):

| Path | Role |
|------|------|
| `POST /report-line` | Reader form |
| `POST /github-hooks/murim-login` | GitHub App webhook |
| `GET /health` | Worker liveness |

The Compose service `murim-report` lives in the papawellness-docker stack. It
volume-mounts a clone of this repo and a GitHub App private key.

## Create the GitHub App (after Caddy routes exist)

Do this on GitHub, then put values only in VPS `stack.env` and
`murim_report_secrets/github_app.pem`. Never commit them.

1. GitHub → Settings → Developer settings → GitHub Apps → New GitHub App.
2. Homepage URL: `https://murim-login.com`
3. Webhook URL: `https://murim-login.com/github-hooks/murim-login`
4. Webhook secret: generate a long random string.
5. Permissions:
   - Repository permissions → Issues: Read and write
   - Pull requests: Read and write
   - Contents: Read and write
   - Metadata: Read-only
6. Subscribe to events: **Issues**, **Issue comment**, **Pull request**.
7. Where can this App be installed? Only on this account.
8. Install the app on `jimzrt/murim-login`.
9. Copy into `stack.env` on the VPS:

```
GITHUB_APP_ID=
GITHUB_APP_INSTALLATION_ID=
GITHUB_WEBHOOK_SECRET=
GITHUB_REPO=jimzrt/murim-login
GITHUB_APPLY_USERS=jimzrt
GITHUB_APP_PEM_FILE=/run/secrets/github_app.pem
```

Installation ID is in the URL after you install:
`github.com/settings/installations/THIS_NUMBER`.

10. Download the App private key and save it on the VPS as
    `murim_report_secrets/github_app.pem` (mode `600`).

11. Clone this repo next to Compose as `murim-login/` so the worker can read
    translations and run `omp`.

## Models

The worker calls `omp --mode json --no-tools` like the chapter controller.
The `murim-report` image installs [omp](https://omp.sh/docs/quickstart) with the
official installer (`curl -fsSL https://omp.sh/install | sh -s -- --binary`).
Auth lives in a Compose volume at `./murim_report_omp` (`/root/.omp` in the
container) so it survives rebuilds.

On the VPS, after rebuilding `murim-report`:

```bash
docker compose exec murim-report omp --version
```

Unattended path (recommended on a server): put an OpenRouter key in `stack.env`
as `OPENROUTER_API_KEY=...` (and any other provider keys omp already honors),
then recreate the container. Fallback in [`.omp/config.yml`](../.omp/config.yml)
will use OpenRouter when Codex/Cursor are not logged in.

Interactive path (Codex/Cursor subscriptions):

```bash
docker compose exec -it murim-report omp auth-broker login
```

Pick the provider, complete the browser/device flow, then recreate is not
required; credentials are already on the volume.

Until omp can actually call a model, the GitHub issue is created but evaluation
comments fail. Redeliver the `issues` `opened` webhook for that issue after auth
works, or file a new report.

## Maintainer loop

1. Reader submits a report (or someone uses the GitHub issue form).
2. Bot comments with strategies A–E, or explains why the report is implausible
   and **closes the issue**.
3. You comment `/apply A` (allowlisted GitHub login only),
   **`/revise …`** for a new set, or **`/reopen`** (optionally with a note) to
   override an implausible close and get choices anyway.
   `/apply` always uses the latest evaluation comment.
4. Bot opens a PR that may edit `translations/*.md`, `docs/NAMES.md`,
   `docs/ADDRESS.md`, `docs/CONTEXT.json`, and `compendium.md`.
5. You merge. The worker closes the issue if GitHub has not already.
