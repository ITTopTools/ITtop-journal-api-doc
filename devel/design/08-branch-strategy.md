# Branch Strategy

## Branches

| Branch | Purpose | Protection |
|--------|---------|------------|
| `dev` | Development. Free push, CI runs but doesn't block. | None |
| `main` | Stable code. Only merged via PR with green CI. | Direct push blocked, requires `test` check, requires PR |
| `gh-pages` | Auto-generated Swagger UI deploy. | `pages` environment restricts deploys to `main` only |

## Workflow

```
dev  ──PR──>  main  ──schedule/manual──>  gh-pages
              │
              └── pipeline.yml (cron + dispatch) → tests → collect → validate → anonymize → publish/worker + mkdocs
```

1. **Develop** — work in `dev` or feature branches off `dev`. Push freely.
2. **Merge** — open PR `dev → main`. Must pass `test` CI check. Blocked if red.
3. **Deploy** — `pipeline.yml` runs on schedule / manual from `main`, triggers reusable workflows for each step, pushes to `gh-pages`.

## CI

- `ci.yml` — lint (ruff) + pytest on every push and PR
- `pipeline.yml` — cron (03:00 UTC daily) + manual dispatch. Orchestrates reusable workflows:
  - `_tests.yml` — lint + pytest gate (main branch only)
  - `_collect.yml` — API collection, uploads raw-data artifact
  - `_validate.yml` — Pydantic validation, soft fail (always exit 0), creates Issue on failure, outputs `validation_failed`
  - `_anonymize.yml` — Faker anonymization (skipped if validation failed, falls back to committed examples)
  - `_publish.yml` — OpenAPI build + gh-pages deploy
  - `_worker.yml` — Cloudflare Worker deploy
  - `_mkdocs.yml` — MkDocs site build + deploy to gh-pages/docs

## gh-pages protection

No branch protection rules — `peaceiris/actions-gh-pages` pushes directly via git.

Instead, the `pages` GitHub Environment has a **deployment branch policy** allowing only `main`. This means:
- `pipeline.yml` running from `main` → deploy succeeds
- `pipeline.yml` running from any other branch → deploy blocked at environment level

## What not to do

- Don't push directly to `main` — it's protected
- Don't push manually to `gh-pages` — let `pipeline.yml` handle it
- Don't force-push any branch
