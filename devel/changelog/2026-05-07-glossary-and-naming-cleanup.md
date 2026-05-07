# Glossary Restructure and Naming Cleanup

## What changed
- Restructured glossary (ru/en) into categorized sections: Project Terms (Infrastructure, Security, Data Processing, Documentation) and Journal Domain Terms (Organizational Structure, Academic Process)
- Added new glossary entry: "Homework Evaluation Tags" / "Теги оценки ДЗ" with anchor `#evaluation-tags`
- Replaced "ИТ Top Академия" with "IT Top Academy" in Russian localization (`index.ru.md`)
- Updated OpenAPI title from "IT Top Journal API" to "IT Top Academy Journal API"
- Renamed "self-assessment tags" / "self-evaluation tags" / "теги самооценки" to "homework evaluation tags" / "теги оценки ДЗ" across all docs, source code, and OpenAPI specs

## Why
- Flat glossary made it hard to distinguish project infrastructure from journal domain concepts — categorization clarifies the boundary
- College name was inconsistently localized (Russian in ru docs, English in en docs) — using English name universally is clearer and matches the API/brand identity
- "Self-assessment tags" was confusing: the endpoint is `/homework/evaluation/operations/get-tags` and the tags are for evaluating homework, not a separate "self-assessment" concept — the new name directly reflects the endpoint purpose

## Affected files
- `documentation/src/glossary.ru.md` — restructured into sections, added evaluation-tags entry
- `documentation/src/glossary.en.md` — restructured into sections, added evaluation-tags entry
- `documentation/src/index.ru.md` — "ИТ Top Академия" → "IT Top Academy"
- `documentation/src/index.en.md` — no changes (already English)
- `documentation/src/openapi.json` — title update, tag description, endpoint summary/description
- `documentation/site/openapi.json` — same changes as src/openapi.json
- `documentation/src/API/homework/evaluation-tags.ru.md` — "теги самооценки" → "теги оценки ДЗ"
- `documentation/src/API/homework/evaluation-tags.en.md` — "self-assessment tags" → "homework evaluation tags"
- `documentation/src/API/homework/index.ru.md` — "теги самооценки" → "теги оценки ДЗ" (2 places)
- `documentation/src/API/homework/index.en.md` — "self-evaluation tags" → "homework evaluation tags" (2 places)
- `documentation/src/API/homework/list.ru.md` — "Теги самооценки" → "Теги оценки ДЗ"
- `documentation/src/API/homework/list.en.md` — added "homework evaluation" clarification
- `README.md` — "Теги для самооценки ДЗ" → "Теги оценки ДЗ"
- `src/collector/endpoints.py` — summary and description for get-tags endpoint
- `src/publisher/builder.py` — homework tag description
