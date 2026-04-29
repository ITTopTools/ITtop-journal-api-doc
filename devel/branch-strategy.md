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
              └── collect.yml (cron + dispatch) collects data, deploys Pages + Worker
```

1. **Develop** — work in `dev` or feature branches off `dev`. Push freely.
2. **Merge** — open PR `dev → main`. Must pass `test` CI check. Blocked if red.
3. **Deploy** — `collect.yml` runs on schedule / manual from `main`, pushes to `gh-pages`.

## CI

- `ci.yml` — lint (ruff) + pytest on every push and PR
- `collect.yml` — cron (03:00 UTC daily) + manual dispatch. Uses `environment: pages` so only `main` branch can deploy to `gh-pages`. Collects API, publishes Pages, deploys Worker.

## gh-pages protection

No branch protection rules — `peaceiris/actions-gh-pages` pushes directly via git.

Instead, the `pages` GitHub Environment has a **deployment branch policy** allowing only `main`. This means:
- `collect.yml` running from `main` → deploy succeeds
- `collect.yml` running from any other branch → deploy blocked at environment level

## What not to do

- Don't push directly to `main` — it's protected
- Don't push manually to `gh-pages` — let `collect.yml` handle it
- Don't force-push any branch
