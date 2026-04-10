"""Validator module: validates raw API responses against Pydantic models."""

from dataclasses import dataclass, field
from typing import Any
from pydantic import ValidationError

from .models import (
    UserInfoResponse,
    AverageProgressItem,
    AttendanceItem,
    LeaderboardItem,
    StudentVisitItem,
    HomeworkCountItem,
    ScheduleItem,
    ReviewItem,
    EvaluateLessonItem,
    PublicTagItem,
)

# Map: endpoint path -> (model, is_list)
MODELS: dict[str, tuple[type, bool]] = {
    "/settings/user-info":                        (UserInfoResponse,    False),
    "/dashboard/chart/average-progress":          (AverageProgressItem, True),
    "/dashboard/chart/attendance":                (AttendanceItem,      True),
    "/dashboard/progress/leader-group":           (LeaderboardItem,     True),
    "/dashboard/progress/leader-stream":          (LeaderboardItem,     True),
    "/progress/operations/student-visits":        (StudentVisitItem,    True),
    "/count/homework":                            (HomeworkCountItem,   True),
    "/schedule/operations/get-by-date":           (ScheduleItem,        True),
    "/reviews/index/list":                        (ReviewItem,          True),
    "/feedback/students/evaluate-lesson-list":    (EvaluateLessonItem,  True),
    "/public/tags":                               (PublicTagItem,       True),
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
                    # Если пути нет в MODELS, считаем это успехом, но без ошибок
                    results.append(ValidationResult(endpoint=path, success=True, errors=[]))
                    continue
    
                # Проверяем, кортеж ли это (Model, bool) или просто Model
                model_info = MODELS[path]
                if isinstance(model_info, tuple):
                    model, is_list = model_info
                else:
                    model, is_list = model_info, False
    
                try:
                    if is_list:
                        [model.model_validate(item) for item in data]
                    else:
                        model.model_validate(data)
                    results.append(ValidationResult(endpoint=path, success=True, errors=[]))
                except Exception as e:
                    results.append(ValidationResult(endpoint=path, success=False, errors=[str(e)]))
            
            return results

    def has_failures(self, results: list[ValidationResult]) -> bool:
        return any(not r.success for r in results)

    def format_issue_body(self, results: list[ValidationResult]) -> str:
        lines = ["# API schema changed — validation failed",
                 "",
                 "Collected payloads do not match current validation models.",
                 ""]
        for r in results:
            if not r.success:
                lines.append(f"`{r.endpoint}`")
                for e in r.errors:
                    lines.append(f"* {e}")
                lines.append("")
        return "\n".join(lines)