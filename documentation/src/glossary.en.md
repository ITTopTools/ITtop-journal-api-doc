# Glossary

Terms and concepts used throughout this documentation.

## Project Terms

Technical terms and tools used in this documentation project.

### Infrastructure

<a id="worker"></a>
### Worker
[Cloudflare Worker](mock-server.md) — a serverless proxy between Swagger UI and the real API. Adds CORS headers, injects `Origin`/`Referer`, and serves mock data when no token is provided.

<a id="pipeline"></a>
### Pipeline
The automated data collection and publishing process: `tests → collect → validate → anonymize → publish → worker → mkdocs`. Runs nightly via GitHub Actions.

<a id="cors"></a>
### CORS
Cross-Origin Resource Sharing — a browser security mechanism. The Journal API does not allow cross-origin requests, so the [worker](#worker) adds CORS headers to responses.

### Security & Authorization

<a id="bearer-token"></a>
### Bearer token
An HTTP authorization format. After login, the `access_token` is sent as `Authorization: Bearer <token>` with every request. See [Authentication](authentication.md).

### Data Processing

<a id="anonymization"></a>
### Anonymization
The process of replacing real personal data (names, IDs, dates) with generated values using [Faker](#faker). Ensures no sensitive data appears in the public repository or mock server.

<a id="faker"></a>
### Faker
A Python library (`faker`) for generating fake data. Used in the `anonymize` pipeline step to replace names with random ones, shift dates, etc.

<a id="pydantic"></a>
### Pydantic
A Python data validation library. Models in `src/validator/models.py` define the expected structure of each API response. When the API changes, validation fails and triggers a GitHub Issue.

### Documentation

<a id="swagger-ui"></a>
### Swagger UI
An interactive API documentation interface embedded in this site. Powered by `openapi.json` and the `mkdocs-swagger-ui-tag` plugin. See [Swagger UI](swagger.md).

## Journal Domain Terms

Concepts describing the internal structure and organization of the IT Top Academy Journal.

### Organizational Structure

<a id="stream"></a>
### Stream
An academic cohort — a group of students studying together. A stream contains multiple [groups](#group). Identified by `stream_id` and `stream_name`.

<a id="group"></a>
### Group
A class within a [stream](#stream). Students in the same group share a schedule and homework. Identified by `group_id` or `current_group_id`.

<a id="spec"></a>
### Spec
Subject (discipline) in the curriculum. Appears in API as `spec_id`, `spec_name`, `id_spec`, `name_spec`. Used in homework, progress, and schedule endpoints.

### Academic Process

<a id="dz"></a>
### DZ
Homework assignment (from Russian "домашнее задание"). In the UI — the "ДЗ" tab. API uses `type=0` for regular DZ, `type=1` for lab work.

<a id="evaluation-tags"></a>
### Homework Evaluation Tags
Tags shown to the student after submitting homework — the student selects tags that describe their confidence and effort level. Returned by the `/homework/evaluation/operations/get-tags` endpoint.
