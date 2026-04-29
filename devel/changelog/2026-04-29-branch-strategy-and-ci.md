# Add CI pipeline, branch strategy and gh-pages environment protection

## What changed
- Added `.github/workflows/ci.yml` — lint (ruff) + pytest on every push and PR
- Created `dev` branch for development, protected `main` (direct push blocked, requires PR + `test` check)
- Created `pages` GitHub Environment with deployment branch policy allowing only `main` to deploy to `gh-pages`
- Added `environment: pages` to `collect.yml` deploy job
- Removed branch protection from `gh-pages` (was blocking `peaceiris/actions-gh-pages` direct push)
- Deleted `ci/add-test-pipeline` branch (merged via PR #18)
- Wrote `devel/branch-strategy.md` documenting the full setup

## Why
- CI was not running on push — broken code could land on main without checks
- No branch structure — direct pushes to main, no isolation between development and stable code
- `gh-pages` branch protection via PR blocked the deploy action; environment-based restriction achieves the same goal (only main deploys) without breaking the workflow

## Affected files
- `.github/workflows/ci.yml` (created)
- `.github/workflows/collect.yml` (added `environment: pages`)
- `devel/branch-strategy.md` (created)
