# Branch Strategy

## Branches

| Branch | Purpose | Protection |
|--------|---------|------------|
| `dev` | Development. Free push, CI runs but doesn't block. | None |
| `main` | Stable code. Only merged via PR with green CI. | Direct push blocked, requires `test` check, requires PR |
| `gh-pages` | Auto-generated Swagger UI deploy. | Direct push blocked, requires PR + approval |

## Workflow

```
dev  ──PR──>  main  ──schedule/manual──>  gh-pages
              │
              └── collect.yml (cron + dispatch) collects data, deploys Pages + Worker
```

1. **Develop** — work in `dev` or feature branches off `dev`. Push freely.
2. **Merge** — open PR `dev → main`. Must pass `test` CI check. Blocked if red.
3. **Deploy** — `collect.yml` runs on schedule / manual from `main`, pushes to `gh-pages`.

## CI

- `ci.yml` — lint (ruff) + pytest on every push and PR
- `collect.yml` — cron (03:00 UTC daily) + manual dispatch. Collects API, publishes Pages, deploys Worker

## What not to do

- Don't push directly to `main` — it's protected
- Don't push directly to `gh-pages` — it's protected, let CI handle it
- Don't force-push any branch
