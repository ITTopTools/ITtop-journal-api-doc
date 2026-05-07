# Text Documentation Content

## What changed
- Rewrote index, authentication, mock-server, swagger pages from stubs to full content reflecting current architecture
- Added per-endpoint documentation for all 34 endpoints across 11 API sections (auth, dashboard, homework, library, news, profile, progress, public, reviews, schedule, signals) — each with purpose, parameters, response fields, and cross-references
- Added bilingual (ru/en) documentation with language selector and flag emojis
- Restructured documentation into subdirectories: `API/auth/`, `API/dashboard/`, `API/homework/`, etc.
- Added glossary with project technical terms and journal domain terms
- Expanded mock-server documentation with full proxy flow explanation

## Why
- Stub pages had no substance — users couldn't understand the API from documentation alone
- Per-endpoint docs provide semantics that OpenAPI schemas can't express (purpose, dependencies, workflow context)
- Bilingual support matches the audience: students and developers in Russian-speaking region
- Subdirectories keep the flat file list manageable as endpoint count grows

## Affected files
- `documentation/src/index.{en,ru}.md` — full project overview, quickstart, pipeline, navigation
- `documentation/src/authentication.{en,ru}.md` — token flow, headers, Authorize button
- `documentation/src/mock-server.{en,ru}.md` — worker proxy flow, CORS, mock data
- `documentation/src/swagger.{en,ru}.md` — Swagger UI usage guide
- `documentation/src/glossary.{en,ru}.md` — terms reference
- `documentation/src/API/auth/*.{en,ru}.md` — login endpoint
- `documentation/src/API/dashboard/*.{en,ru}.md` — 8 dashboard endpoints
- `documentation/src/API/homework/*.{en,ru}.md` — 5 homework endpoints
- `documentation/src/API/library/*.{en,ru}.md` — 2 library endpoints
- `documentation/src/API/news/*.{en,ru}.md` — 2 news endpoints
- `documentation/src/API/profile/*.{en,ru}.md` — 4 profile endpoints
- `documentation/src/API/progress/*.{en,ru}.md` — 2 progress endpoints
- `documentation/src/API/public/*.{en,ru}.md` — 4 public endpoints
- `documentation/src/API/reviews/*.{en,ru}.md` — 4 review endpoints
- `documentation/src/API/schedule/*.{en,ru}.md` — 3 schedule endpoints
- `documentation/src/API/signals/*.{en,ru}.md` — 2 signal endpoints
- `mkdocs.yml` — nav structure, i18n plugin config, flag emojis
