# Панель управления

Раздел обзора панели управления — графики, таблицы лидеров, лента активности и предстоящие экзамены.

## Эндпоинты

| Method | Path | Краткое описание | Ссылка |
|--------|------|------------------|--------|
| GET | `/dashboard/chart/average-progress` | График среднемесячного прогресса | [Подробнее](average-progress.md) |
| GET | `/dashboard/chart/attendance` | График ежемесячной посещаемости | [Подробнее](attendance.md) |
| GET | `/dashboard/chart/progress` | Прогресс, сгруппированный по типу графика | [Подробнее](chart-progress.md) |
| GET | `/dashboard/progress/activity` | Лента активности | [Подробнее](activity.md) |
| GET | `/dashboard/progress/leader-group` | Таблица лидеров группы | [Подробнее](leader-group.md) |
| GET | `/dashboard/progress/leader-stream` | Таблица лидеров потока | [Подробнее](leader-stream.md) |
| GET | `/dashboard/progress/leader-group-points` | Позиция ученика в группе | [Подробнее](leader-group-points.md) |
| GET | `/dashboard/progress/leader-stream-points` | Позиция ученика в потоке | [Подробнее](leader-stream-points.md) |
| GET | `/dashboard/info/future-exams` | Список предстоящих экзаменов | [Подробнее](future-exams.md) |

## Графические эндпоинты

Графические эндпоинты (`average-progress`, `attendance`, `chart-progress`) имеют схожую структуру ответа на основе полей date, points и previous_points для отображения линий тренда.

## Зависимости

- [Аутентификация](../auth/index.md) — все эндпоинты требуют действительный JWT токен
