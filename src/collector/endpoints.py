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
    tag: str = ""
    summary: str = ""
    description: str = ""
    response_description: str = ""
    uncertain: str = ""

ENDPOINTS: list[Endpoint] = [
    # ── Auth ──
    Endpoint(
        path=LOGIN_PATH,
        method="POST",
        params={
            "application_key": "6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6",
            "id_city": None,
            "username": "<login>",
            "password": "<password>",
        },
        tag="auth",
        summary="Submit login credentials",
        description=(
            "Login with username and password to obtain a JWT access token. "
            "The `access_token` from the response is used as a Bearer token "
            "for all other endpoints."
        ),
        response_description="JWT tokens and user session info",
    ),

    # ── Profile / Settings ──
    Endpoint(
        path="/settings/user-info",
        method="GET",
        tag="profile",
        summary="Get current student info",
        description=(
            "Returns the authenticated student's profile: name, group, stream, "
            "current group ID, and other personal details. "
            "`current_group_id` is used as `group_id` parameter in homework endpoints."
        ),
        response_description="Student profile with group, stream, and personal info",
    ),
    Endpoint(
        path="/profile/operations/settings",
        method="GET",
        tag="profile",
        summary="Get profile settings",
        description=(
            "Editable student profile fields: name, address, email, phone verification status, "
            "photo, and profile completion percentage. "
            "Note: the API returns `ful_name` (typo) instead of `full_name`."
        ),
        response_description="Editable profile fields and verification status",
    ),
    Endpoint(
        path="/profile/statistic/student-achievements",
        method="GET",
        tag="profile",
        summary="List student achievements",
        description=(
            "Achievements earned by the student (badges, milestones). "
            "Each achievement has a `translate_key` for the UI label and an `achieve_points` list."
        ),
        response_description="Array of achievements with points",
    ),

    # ── Dashboard ──
    Endpoint(
        path="/dashboard/chart/average-progress",
        method="GET",
        tag="dashboard",
        summary="Get average progress chart",
        description=(
            "Monthly average progress values for the student. "
            "Used to render the progress line chart on the main dashboard. "
            "Each item has `points` (current month) and `previous_points` (previous month)."
        ),
        response_description="Array of monthly progress data points",
    ),
    Endpoint(
        path="/dashboard/chart/attendance",
        method="GET",
        tag="dashboard",
        summary="Get attendance chart data",
        description=(
            "Monthly attendance percentages for the student's group. "
            "Used to render the attendance chart on the main dashboard. "
            "`points` is the attendance percentage for the given month."
        ),
        response_description="Array of monthly attendance percentages",
    ),
    Endpoint(
        path="/dashboard/chart/progress",
        method="GET",
        tag="dashboard",
        summary="Get progress charts by type",
        description=(
            "Progress chart data grouped by `chart_type`. "
            "Each group contains `chart_models` with the same structure as "
            "average-progress items. Used for the multi-chart dashboard view.",
        ),
        response_description="Array of chart groups, each with typed progress data",
        uncertain="Meaning of each chart_type value is not documented by the API",
    ),
    Endpoint(
        path="/dashboard/progress/activity",
        method="GET",
        tag="dashboard",
        summary="Get activity feed",
        description=(
            "Activity feed with points, achievements, and badges. "
            "Shows recent actions (earned points, unlocked achievements) "
            "on the dashboard activity section."
        ),
        response_description="Array of activity events with points and achievements",
    ),
    Endpoint(
        path="/dashboard/progress/leader-group",
        method="GET",
        tag="dashboard",
        summary="Get group leaderboard",
        description=(
            "Top students in the student's group ranked by points. "
            "Each entry has `position`, `full_name`, and `amount` (total points)."
        ),
        response_description="Array of group members ranked by points",
    ),
    Endpoint(
        path="/dashboard/progress/leader-stream",
        method="GET",
        tag="dashboard",
        summary="Get stream leaderboard",
        description=(
            "Top students across the entire stream ranked by points. "
            "Same structure as group leaderboard but covering the whole stream."
        ),
        response_description="Array of stream members ranked by points",
    ),
    Endpoint(
        path="/dashboard/progress/leader-group-points",
        method="GET",
        tag="dashboard",
        summary="Get student position in group",
        description=(
            "Current student's position and point stats within the group: "
            "`studentPosition`, `totalCount` (group size), `weekDiff`, `monthDiff` "
            "(point change relative to previous week/month)."
        ),
        response_description="Student's group position and point dynamics",
    ),
    Endpoint(
        path="/dashboard/progress/leader-stream-points",
        method="GET",
        tag="dashboard",
        summary="Get student position in stream",
        description=(
            "Current student's position and point stats within the stream. "
            "Same structure as leader-group-points but for the whole stream. "
            "`totalCount` can be null."
        ),
        response_description="Student's stream position and point dynamics",
    ),
    Endpoint(
        path="/dashboard/info/future-exams",
        method="GET",
        tag="dashboard",
        summary="Get upcoming exams",
        description="List of upcoming exams with subject name (`spec`) and date.",
        response_description="Array of upcoming exam entries",
    ),

    # ── Schedule ──
    Endpoint(
        path="/schedule/operations/get-by-date",
        method="GET",
        params={"date_filter": date.today().isoformat()},
        tag="schedule",
        summary="Get schedule for a date",
        description=(
            "Class schedule for a specific date. Returns lessons with time, "
            "teacher, subject, and room info. "
            "Number of items varies by how many classes are scheduled that day."
        ),
        response_description="Array of scheduled lessons for the date",
    ),
    Endpoint(
        path="/schedule/operations/get-by-date-range",
        method="GET",
        params={
            "date_start": date.today().isoformat(),
            "date_end": date.today().isoformat(),
        },
        tag="schedule",
        summary="Get schedule for a date range",
        description=(
            "Class schedule for a date range (start and end inclusive). "
            "Returns an empty array if no classes fall within the range — this is normal."
        ),
        response_description="Array of scheduled lessons in the date range",
    ),
    Endpoint(
        path="/schedule/operations/get-month",
        method="GET",
        params={"date_filter": date.today().isoformat()},
        tag="schedule",
        summary="Get schedule for a month",
        description=(
            "Class schedule for the month containing the given date. "
            "Same item structure as get-by-date."
        ),
        response_description="Array of scheduled lessons for the month",
    ),

    # ── Progress ──
    Endpoint(
        path="/progress/operations/student-visits",
        method="GET",
        tag="progress",
        summary="Get visit journal with grades",
        description=(
            "Visit records with grades per lesson. Each entry includes "
            "visit status (`status_was`), subject, teacher, lesson theme, "
            "and separate grade fields: `control_work_mark`, `home_work_mark`, "
            "`lab_work_mark`, `class_work_mark`, `practical_work_mark`, `final_work_mark`."
        ),
        response_description="Array of visit records with lesson grades",
    ),
    Endpoint(
        path="/progress/operations/student-exams",
        method="GET",
        tag="progress",
        summary="Get exam grades",
        description=(
            "Exam results with teacher, mark, date, subject, and optional "
            "file attachments (`file_path`, `id_file`). "
            "`mark_type` distinguishes exam types."
        ),
        response_description="Array of exam results with grades and files",
        uncertain="mark_type values not documented — observed 0 and 1 in data",
    ),

    # ── Library ──
    Endpoint(
        path="/library/operations/list",
        method="GET",
        params={
            "material_type": 2,
            "filter_type": 0,
            "recommended_type": 0,
        },
        tag="library",
        summary="List learning materials",
        description=(
            "Learning materials from the library. "
            "`material_type`, `filter_type`, `recommended_type` are filter parameters "
            "observed in the UI with default values 2, 0, 0 respectively."
        ),
        response_description="Array of learning material items",
        uncertain="material_type/filter_type/recommended_type values are inferred from UI, not documented; response schema unknown — collected data was empty",
    ),

    # ── Homework ──
    Endpoint(
        path="/count/homework",
        method="GET",
        tag="homework",
        summary="Get homework counters by status",
        description=(
            "Count of homework items per status type. `counter_type` meanings:\n"
            "- 0 — overdue (deadline passed, auto-fail grade assigned)\n"
            "- 1 — reviewed by teacher (has a grade)\n"
            "- 2 — submitted, awaiting teacher review\n"
            "- 3 — current (not yet submitted by student)\n"
            "- 4 — total across all types\n"
            "- 5 — deleted by teacher (was submitted but rejected)"
        ),
        response_description="Array of counter_type/counter pairs",
    ),
    Endpoint(
        path="/homework/settings/group-history",
        method="GET",
        tag="homework",
        summary="List student groups with subjects",
        description=(
            "Student's groups with their subjects (specs). "
            "Shown in the group switcher in the homework (DZ) tab. "
            "Not used to resolve `group_id` — that comes from "
            "`current_group_id` in `/settings/user-info`."
        ),
        response_description="Array of groups with nested subject lists",
    ),
    Endpoint(
        path="/settings/group-specs",
        method="GET",
        tag="homework",
        summary="Get subjects of current group",
        description="Subjects (specs) linked to the student's current group.",
        response_description="Array of subject items with id, name, short_name",
    ),
    Endpoint(
        path="/homework/evaluation/operations/get-tags",
        method="GET",
        tag="homework",
        summary="Get homework evaluation tags",
        description=(
            "Tags for the homework evaluation form. "
            "Shown to the student after submitting homework to describe their confidence and effort level."
        ),
        response_description="Array of evaluation tag items",
    ),
    Endpoint(
        path="/homework/operations/list",
        method="GET",
        params={
            "page": 1,
            "status": 1,
            "type": 0,
            "group_id": 4,
        },
        tag="homework",
        summary="List homework assignments",
        description=(
            "Paginated list of homework assignments.\n"
            "- `page`: page number for pagination\n"
            "- `status`: filter by status — 0=overdue, 1=reviewed, 2=submitted, 3=current, 5=deleted\n"
            "- `type`: 0=regular homework, 1=lab work (identical response structure)\n"
            "- `group_id`: from `current_group_id` in `/settings/user-info`"
        ),
        response_description="Paginated array of homework items with submission details",
    ),

    # ── Reviews / Feedback ──
    Endpoint(
        path="/reviews/index/list",
        method="GET",
        tag="reviews",
        summary="List lesson reviews",
        description=(
            "Reviews written about lessons. Each entry includes date, "
            "message text, subject, and teacher name."
        ),
        response_description="Array of review entries",
    ),
    Endpoint(
        path="/reviews/index/instruction",
        method="GET",
        tag="reviews",
        summary="Get review instructions",
        description=(
            "Instructions for submitting reviews. "
            "Returns `null` when no instruction is available."
        ),
        response_description="Review instruction text or null",
    ),
    Endpoint(
        path="/feedback/students/evaluate-lesson-list",
        method="GET",
        tag="reviews",
        summary="List lessons available for evaluation",
        description=(
            "Lessons the student can evaluate (leave feedback for). "
            "Each entry has lesson date, teacher name, and subject."
        ),
        response_description="Array of lessons eligible for student evaluation",
    ),
    Endpoint(
        path="/feedback/social-review/get-review-list",
        method="GET",
        tag="reviews",
        summary="List social review submissions",
        description=(
            "Student's submitted social reviews (e.g., course reviews on external platforms). "
            "Each entry has a link, screenshot, teacher comment, and visibility status."
        ),
        response_description="Array of social review submissions",
    ),

    # ── Signals ──
    Endpoint(
        path="/signal/operations/signals-list",
        method="GET",
        tag="signals",
        summary="List academic signals",
        description=(
            "Academic signals/alerts assigned to the student (requests, problems). "
            "Each signal has priority, status, message, initiator, and linked problem."
        ),
        response_description="Array of signal entries with priority and status",
    ),
    Endpoint(
        path="/signal/operations/problems-list",
        method="GET",
        tag="signals",
        summary="List problem types",
        description="Reference list of problem types used in signals. Each has `id` and `title`.",
        response_description="Array of problem type entries",
    ),

    # ── News ──
    Endpoint(
        path="/news/operations/latest-news",
        method="GET",
        tag="news",
        summary="Get latest news",
        description=(
            "Academy news and announcements. Each entry has a theme, "
            "timestamp, and viewed status."
        ),
        response_description="Array of news items",
    ),

    # ── Public ──
    Endpoint(
        path="/public/languages",
        method="GET",
        anonymize=False,
        tag="public",
        summary="List available languages",
        description="Available UI languages. Each has a `name_mystat` and `short_name` (locale code).",
        response_description="Array of language entries",
    ),
    Endpoint(
        path="/public/translations",
        method="GET",
        params={"language": "ru"},
        anonymize=False,
        tag="public",
        summary="Get localization strings",
        description=(
            "Localization key-value pairs for the given language. "
            "Returns a flat dictionary of translation keys to translated strings. "
            "Only `language=ru` (Russian) was collected; other locales share the same schema."
        ),
        response_description="Dictionary of translation keys to localized strings",
    ),
    Endpoint(
        path="/public/tags",
        method="GET",
        anonymize=False,
        tag="public",
        summary="List public tags",
        description="Reference list of public tags. Schema unknown — collected data was empty.",
        response_description="Array of tag items",
        uncertain="response schema unknown — collected data returned an empty array",
    ),
]