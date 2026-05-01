from dataclasses import dataclass
from datetime import date

BASE_API_URL = "https://msapi.top-academy.ru/api/v2"
LOGIN_PATH = "/auth/login"

@dataclass(slots=True, frozen=True)
class Endpoint:
    path: str
    method: str
    params: dict | None = None
    anonymize: bool = True
    max_items: int | None = None
    validate_count: bool = False
    expected_max_items: int | None = None

ENDPOINTS: list[Endpoint] = [
    Endpoint(path=LOGIN_PATH, method="POST", params={
        "application_key": "6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6",
        "id_city": None,
        "username": "<login>",
        "password": "<password>",
    }),

    # ── Profile / Settings ──
    Endpoint(path="/settings/user-info", method="GET"),
    Endpoint(path="/profile/operations/settings", method="GET"),
    Endpoint(path="/profile/statistic/student-achievements", method="GET"),

    # ── Dashboard ──
    Endpoint(path="/dashboard/chart/average-progress", method="GET"),
    Endpoint(path="/dashboard/chart/attendance", method="GET"),
    Endpoint(path="/dashboard/chart/progress", method="GET"),
    Endpoint(path="/dashboard/progress/activity", method="GET"),
    Endpoint(path="/dashboard/progress/leader-group", method="GET"),
    Endpoint(path="/dashboard/progress/leader-stream", method="GET"),
    Endpoint(path="/dashboard/progress/leader-group-points", method="GET"),
    Endpoint(path="/dashboard/progress/leader-stream-points", method="GET"),
    Endpoint(path="/dashboard/info/future-exams", method="GET"),

    # ── Schedule ── count varies by number of classes per day, no fixed limit
    Endpoint(
        path="/schedule/operations/get-by-date",
        method="GET",
        params={"date_filter": date.today().isoformat()},
    ),
    Endpoint(
        path="/schedule/operations/get-by-date-range",
        method="GET",
        params={
            "date_start": date.today().isoformat(),
            "date_end": date.today().isoformat(),
        },
    ),
    Endpoint(
        path="/schedule/operations/get-month",
        method="GET",
        params={"date_filter": date.today().isoformat()},
    ),

    # ── Progress ──
    Endpoint(path="/progress/operations/student-visits", method="GET"),
    Endpoint(path="/progress/operations/student-exams", method="GET"),

    # ── Library / Homework ──
    # material_type=2, filter_type=0, recommended_type=0 — default filter values
    # observed in the UI; exact meaning unknown, but these return non-empty data.
    Endpoint(path="/library/operations/list", method="GET", params={
        "material_type": 2,
        "filter_type": 0,
        "recommended_type": 0,
    }),
    # Returns counters per homework status type. counter_type meanings:
    #   0 — overdue (deadline passed, auto-fail grade assigned)
    #   1 — reviewed by teacher (has a grade)
    #   2 — submitted, awaiting teacher review
    #   3 — current (not yet submitted by student)
    #   4 — total across all types
    #   5 — deleted by teacher (was submitted but rejected)
    Endpoint(path="/count/homework", method="GET"),

    # ── Homework (DZ) ──
    # List of student's groups with their subjects — shown in the group switcher in the DZ tab.
    # Not used to resolve group_id for homework requests; group_id comes from
    # current_group_id in /settings/user-info.
    Endpoint(path="/homework/settings/group-history", method="GET"),
    # Subjects (specs) linked to the current group.
    Endpoint(path="/settings/group-specs", method="GET"),
    # Tags for the homework self-evaluation form (shown after submitting HW).
    Endpoint(path="/homework/evaluation/operations/get-tags", method="GET"),
    # group_id=4 — current_group_id from /settings/user-info.
    # status=1 — "reviewed by teacher" (counter_type 1, 457 items at collection time);
    #            chosen because status=0 (overdue) and status=3 (current) had 0 items.
    # type=0 — regular HW; type=1 is lab work, identical response structure, same model.
    Endpoint(
        path="/homework/operations/list",
        method="GET",
        params={
            "page": 1,
            "status": 1,
            "type": 0,
            "group_id": 4,
        },
    ),

    # ── Reviews / Feedback ──
    Endpoint(path="/reviews/index/list", method="GET"),
    Endpoint(path="/reviews/index/instruction", method="GET"),
    Endpoint(path="/feedback/students/evaluate-lesson-list", method="GET"),
    Endpoint(path="/feedback/social-review/get-review-list", method="GET"),

    # ── Signals ──
    Endpoint(path="/signal/operations/signals-list", method="GET"),
    Endpoint(path="/signal/operations/problems-list", method="GET"),

    # ── News ──
    Endpoint(path="/news/operations/latest-news", method="GET"),

    # ── Public (not sensitive, anonymize=False) ──
    Endpoint(path="/public/languages", method="GET", anonymize=False),
    # language=ru — only Russian locale collected; other locales share the same schema.
    Endpoint(path="/public/translations", method="GET", params={"language": "ru"}, anonymize=False),
    Endpoint(path="/public/tags", method="GET", anonymize=False),
]