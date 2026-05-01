# Changelog

> Change history — both LLM-generated and human-written.

---

## Format

Each entry is a separate file: `YYYY-MM-DD-title.md`.

```
# [Title]

## What changed
- ...

## Why
- ...

## Affected files
- ...
```

---

## Entries

- [`init.md`](init.md) — Repository created from template
- [`2026-04-10-initial-setup.md`](2026-04-10-initial-setup.md) — Initial project setup and design documentation
- [`2026-04-10-mvp-pipeline.md`](2026-04-10-mvp-pipeline.md) — MVP pipeline: collector, validator, anonymizer, publisher, main entrypoint
- [`2026-04-10-auth-fixes-and-prod-models.md`](2026-04-10-auth-fixes-and-prod-models.md) — Fix auth payload and replace placeholder models with real schemas
- [`2026-04-10-array-trimmer-and-refactor.md`](2026-04-10-array-trimmer-and-refactor.md) — Add array trimmer and refactor collector/anonymizer
- [`2026-04-18-ci-gating-and-cleanup.md`](2026-04-18-ci-gating-and-cleanup.md) — CI validation gating and repository cleanup
- [`2026-04-18-openapi-enrichment.md`](2026-04-18-openapi-enrichment.md) — Enrich OpenAPI spec: auth scheme, required headers, correct response schemas
- [`2026-04-18-mock-worker.md`](2026-04-18-mock-worker.md) — Add Cloudflare Worker for mock API and proxy
- [`2026-04-21-validator-refactor.md`](2026-04-21-validator-refactor.md) — Add Pydantic models for all discovered endpoints, fix schedule path bug
- [`2026-04-21-proxy-and-server-config.md`](2026-04-21-proxy-and-server-config.md) — Add official API server, CORS proxy, and Worker updates
- [`2026-04-26-template-migration.md`](2026-04-26-template-migration.md) — Migrate to latest template and fix validator test
- [`2026-04-29-remove-schedule-count-validation.md`](2026-04-29-remove-schedule-count-validation.md) — Remove fixed count validation on schedule endpoints
- [`2026-04-29-branch-strategy-and-ci.md`](2026-04-29-branch-strategy-and-ci.md) — Add CI pipeline, branch strategy and gh-pages environment protection
- [`2026-05-01-homework-endpoints.md`](2026-05-01-homework-endpoints.md) — Add homework endpoints to main pipeline
