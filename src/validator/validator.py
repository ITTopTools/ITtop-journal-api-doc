"""Validator module: validates raw API responses against Pydantic models."""

import logging
from dataclasses import dataclass, field
from typing import Any

from .models import (
    UserInfoResponse,
    ProfileSettingsResponse,
    AchievementItem,
    AverageProgressItem,
    AttendanceItem,
    ChartProgressItem,
    ActivityItem,
    LeaderboardItem,
    LeaderPointsResponse,
    FutureExamItem,
    ScheduleItem,
    StudentVisitItem,
    StudentExamItem,
    HomeworkCountItem,
    LibraryItem,
    ReviewItem,
    EvaluateLessonItem,
    SocialReviewItem,
    SignalItem,
    ProblemItem,
    NewsItem,
    LanguageItem,
    # TranslationsResponse, 
    PublicTagItem,
)

LOGGER = logging.getLogger(__name__)

# Map: endpoint path -> (model, is_list)
# is_list=True  — ответ является списком, валидируем каждый элемент отдельно
# is_list=False — ответ является словарём, валидируем целиком
MODELS: dict[str, tuple[type, bool]] = {
    "/settings/user-info":                          (UserInfoResponse,      False),
    "/profile/operations/settings":                 (ProfileSettingsResponse, False),
    "/profile/statistic/student-achievements":      (AchievementItem,       True),
    "/dashboard/chart/average-progress":            (AverageProgressItem,   True),
    "/dashboard/chart/attendance":                  (AttendanceItem,        True),
    "/dashboard/chart/progress":                    (ChartProgressItem,     True),
    "/dashboard/progress/activity":                 (ActivityItem,          True),
    "/dashboard/progress/leader-group":             (LeaderboardItem,       True),
    "/dashboard/progress/leader-stream":            (LeaderboardItem,       True),
    # leader-*-points возвращают одиночный объект, не список
    "/dashboard/progress/leader-group-points":      (LeaderPointsResponse,  False),
    "/dashboard/progress/leader-stream-points":     (LeaderPointsResponse,  False),
    "/dashboard/info/future-exams":                 (FutureExamItem,        True),
    # schedule: все три эндпоинта имеют одинаковую структуру элементов
    # /get-by-date-range может вернуть пустой список — это нормально
    "/schedule/operations/get-by-date-range":       (ScheduleItem,          True),
    "/schedule/operations/get-month":               (ScheduleItem,          True),
    "/schedule/operations/get-by-date":             (ScheduleItem,          True),
    "/progress/operations/student-visits":          (StudentVisitItem,      True),
    "/progress/operations/student-exams":           (StudentExamItem,       True),
    "/library/operations/list":                     (LibraryItem,           True),
    "/count/homework":                              (HomeworkCountItem,     True),
    "/reviews/index/list":                          (ReviewItem,            True),
    # /reviews/index/instruction возвращает null — нет смысла валидировать,
    # пропускаем (упадёт в ветку unknown path -> success=True)
    "/feedback/students/evaluate-lesson-list":      (EvaluateLessonItem,    True),
    "/feedback/social-review/get-review-list":      (SocialReviewItem,      True),
    "/signal/operations/signals-list":              (SignalItem,            True),
    "/signal/operations/problems-list":             (ProblemItem,           True),
    "/news/operations/latest-news":                 (NewsItem,              True),
    "/public/languages":                            (LanguageItem,          True),
    # /public/translations — dict строка→строка, TranslationsResponse с extra="allow"
    # поглощает все ключи без падения
    # "/public/translations":                         (TranslationsResponse,  False), !TODO!: Inspect endpoint by behavior
    "/public/tags":                                 (PublicTagItem,         True),
}


@dataclass
class ValidationResult:
    endpoint: str
    success: bool
    errors: list[str] = field(default_factory=list)


class Validator:
    def validate_all(self, raw: dict[str, Any]) -> list[ValidationResult]:
        results = []
        for path, data in raw.items():
            if path not in MODELS:
                results.append(ValidationResult(endpoint=path, success=True, errors=[]))
                continue

            if isinstance(data, dict) and "error" in data:
                results.append(ValidationResult(
                    endpoint=path,
                    success=False,
                    errors=[f"Collector Error: {data['error']}"]
                ))
                continue

            model, is_list = MODELS[path]

            try:
                if is_list:
                    if not isinstance(data, list):
                        raise TypeError(f"Expected list, but received {type(data).__name__}")
                    for item in data:
                        model.model_validate(item)
                else:
                    if not isinstance(data, dict):
                        raise TypeError(f"Expected dict, but received {type(data).__name__}")
                    model.model_validate(data)
                
                results.append(ValidationResult(endpoint=path, success=True, errors=[]))
            except Exception as e:
                results.append(ValidationResult(endpoint=path, success=False, errors=[str(e)]))

        return results

    def has_failures(self, results: list[ValidationResult]) -> bool:
        return any(not r.success for r in results)

    def format_issue_body(self, results: list[ValidationResult]) -> str:
        lines = [
            "# API schema changed — validation failed",
            "",
            "Collected payloads do not match current validation models.",
            ""
        ]
        for r in results:
            if not r.success:
                lines.append(f"### `{r.endpoint}`")
                for e in r.errors:
                    lines.append(f"* {e}")
                lines.append("")
        return "\n".join(lines)