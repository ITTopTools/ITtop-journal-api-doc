# Расписание

Расписание занятий по дате, диапазону дат или месяцу. Все три эндпоинта возвращают одинаковую структуру ScheduleItem, описанную ниже.

<a id="scheduleitem-structure"></a>
## Структура ScheduleItem

Каждый эндпоинт этого раздела возвращает массив объектов со следующими полями:

| Поле | Тип | Описание |
|------|-----|----------|
| `date` | string | Дата занятия (`YYYY-MM-DD`) |
| `lesson` | integer | Номер занятия в течение дня |
| `started_at` | string | Время начала занятия |
| `finished_at` | string | Время окончания занятия |
| `teacher_name` | string | ФИО преподавателя |
| `subject_name` | string | Название предмета |
| `room_name` | string | Название аудитории |

## Эндпоинты

| Method | Path | Краткое описание | Ссылка |
|--------|------|------------------|--------|
| GET | `/schedule/operations/get-by-date` | Получить расписание на дату | [Подробнее](get-by-date.md) |
| GET | `/schedule/operations/get-by-date-range` | Получить расписание на диапазон дат | [Подробнее](get-by-date-range.md) |
| GET | `/schedule/operations/get-month` | Получить расписание на месяц | [Подробнее](get-by-month.md) |
