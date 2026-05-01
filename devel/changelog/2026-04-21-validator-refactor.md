# Add Pydantic models for all discovered endpoints, fix schedule path bug

## What changed
- Replaced remaining placeholder/dict models with real Pydantic schemas for all endpoints discovered from the API dataset:
  - `ProfileSettingsResponse`, `AchievementItem`, `AverageProgressItem`, `AttendanceItem`, `ChartProgressItem`
  - `ActivityItem`, `LeaderboardItem`, `LeaderPointsResponse`, `FutureExamItem`
  - `ScheduleItem`, `StudentVisitItem`, `StudentExamItem`
  - `HomeworkCountItem`, `LibraryItem`, `ReviewItem`, `EvaluateLessonItem`, `SocialReviewItem`
  - `SignalItem`, `ProblemItem`, `NewsItem`, `LanguageItem`, `TranslationsResponse`, `PublicTagItem`
- Registered all endpoint models in `MODELS` dict in `src/validator/validator.py`
- Fixed schedule endpoint path bug: `/schedule/operations/get-by-date` was incorrectly registered, now corrected in both `ENDPOINTS` and `MODELS`
- Added `/schedule/operations/get-by-date` endpoint to `ENDPOINTS` list with `date_filter` param
- Removed broken endpoint from `ENDPOINTS`
- Updated `tests/test_validator.py` to cover model registration
- Added expansion plan document

## Why
- Initial models were mostly placeholders with generic fields — real API responses had completely different structures
- Schedule endpoint path mismatch caused validation to silently skip those responses
- Without all models registered, validation passed by default for unregistered paths (by design) — real schema drifts would go undetected

## Affected files
- `src/validator/models.py`
- `src/validator/validator.py`
- `src/collector/endpoints.py`
- `tests/test_validator.py`
