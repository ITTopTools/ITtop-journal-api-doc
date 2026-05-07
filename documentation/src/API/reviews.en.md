# Reviews

Lesson reviews and student feedback.

## Endpoints

### GET /reviews/index/list

Reviews written about lessons.

**Purpose:** Displays teacher reviews on the student's profile. Each entry includes the review date, message text, subject, and teacher name.

**Response:** Array of objects with `date`, `message`, `spec` (short subject name), `full_spec` (full subject name), `teacher`.

### GET /reviews/index/instruction

Instructions for submitting reviews.

**Purpose:** Review submission guidelines displayed to the student.

**Response:** Review instruction text, or `null` when no instruction is available.

### GET /feedback/students/evaluate-lesson-list

Lessons the student can evaluate (leave feedback for).

**Purpose:** Feedback form — shows past lessons where the student can rate the teacher. Each entry has lesson date, teacher name, and subject.

**Response:** Array of objects with `key`, `date_visit`, `fio_teach`, `spec_name`, `teach_photo`.

### GET /feedback/social-review/get-review-list

Student's submitted social reviews (e.g., course reviews on external platforms).

**Purpose:** Social review tracking — shows which reviews the student has submitted, their approval status, and teacher comments.

**Response:** Array of objects with `status`, `social_id`, `link_id`, `link`, `screen_shot`, `review_id`, `comment`, `teach_name`, `updated_at`, `is_visibility`.
