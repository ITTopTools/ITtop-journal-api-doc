# Reusable Workflow Pipeline

## What changed
- Added `--step` CLI argument to `main.py` (collect/validate/anonymize/publish) — no-arg still runs full pipeline
- Replaced monolithic `collect.yml` with 8 reusable workflows: `pipeline.yml` (orchestrator) + `_tests.yml`, `_collect.yml`, `_validate.yml`, `_anonymize.yml`, `_publish.yml`, `_worker.yml`, `_mkdocs.yml`
- `--step validate` always exits 0 (soft fail) and writes `validation_failed=true` to `GITHUB_OUTPUT`
- `--step anonymize` gracefully handles missing raw data (exit 0)
- When validation fails, anonymize is skipped and committed examples are used as fallback
- Updated documentation: README.md, devel/design/05-architecture-detailed.md, devel/design/08-branch-strategy.md

## Why
- Reusable workflows decouple each pipeline step into independent jobs with artifact-based data flow
- Soft-fail validation prevents the entire pipeline from blocking on API schema changes
- Fallback to committed examples ensures documentation is always published, even when collection or validation encounters issues

## Affected files
- `main.py` — added argparse, step functions, kept backward compat
- `.github/workflows/collect.yml` — deleted
- `.github/workflows/pipeline.yml` — new orchestrator
- `.github/workflows/_tests.yml` — new reusable
- `.github/workflows/_collect.yml` — new reusable
- `.github/workflows/_validate.yml` — new reusable
- `.github/workflows/_anonymize.yml` — new reusable
- `.github/workflows/_publish.yml` — new reusable
- `.github/workflows/_worker.yml` — new reusable
- `.github/workflows/_mkdocs.yml` — new reusable
- `README.md` — updated pipeline description, --step usage, soft-fail behavior
- `devel/design/05-architecture-detailed.md` — updated workflow structure and pipeline diagram
- `devel/design/08-branch-strategy.md` — updated references from collect.yml to pipeline.yml
