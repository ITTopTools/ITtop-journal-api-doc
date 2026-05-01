# CI validation gating and repository cleanup

## What changed
- Gated validation issue creation in `.github/workflows/collect.yml` by step output — only creates an Issue when validation actually fails
- Added `data/validation_issue.md` and `data/error_report.md` to `.gitignore`
- Removed leaked validation artifacts from repo (multiple cleanup commits)
- Updated design docs: marked functional requirements as completed, updated architecture pipeline details
- Documented tradeoff decisions for validation strictness and CI gating

## Why
- CI was creating GitHub Issues on every run even when validation passed — needed to gate on actual failures only
- Validation report files were accidentally committed — moved to gitignore to prevent future leaks

## Affected files
- `.github/workflows/collect.yml`
- `.gitignore`
- `docs/design/02-functional-requirements.md`
- `docs/design/05-architecture-detailed.md`
