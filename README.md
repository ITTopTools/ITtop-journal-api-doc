# ITtop Journal API Docs

> Автоматическая OpenAPI-документация для [IT Top Academy Journal](https://journal.top-academy.ru).
> Данные собираются, анонимизируются и публикуются через GitHub Pages.

## О проекте

IT Top Journal не имеет публичной документации. Этот проект заполняет пробел:

- **Собирает** реальные ответы API через авторизованные запросы
- **Валидирует** структуру через Pydantic — если API изменился, пайплайн падает и открывается Issue
- **Анонимизирует** данные через Faker — реальные имена, ID и даты не попадают в публичный репозиторий
- **Генерирует** `openapi.json` и публикует Swagger UI на GitHub Pages

Пайплайн запускается автоматически каждый день в 03:00 UTC через GitHub Actions. Также доступен ручной запуск (workflow_dispatch).

## Как это работает

```
Авторизация → Сбор ответов → Pydantic-валидация → Faker-анонимизация → OpenAPI-генерация → GitHub Pages
                                        ↓ (ошибка)
                                  GitHub Issue
```

1. `collector/` — логинится по `/auth/login`, обходит все эндпоинты, сохраняет сырые ответы
2. `validator/` — прогоняет ответы через Pydantic-модели; несовпадения → Issue с деталями
3. `anonymizer/` — подменяет PII (имена, ID, даты) на Faker-генерированные значения
4. `publisher/` — строит `openapi.json` + `index.html` (Swagger UI) из анонимизированных данных

## Структура проекта

```
src/
  collector/             Авторизация и сбор данных с эндпоинтов
    client.py            HTTP-клиент (httpx)
    endpoints.py         Реестр всех эндпоинтов (путь, метод, параметры)
    array_trimmer.py     Обрезка длинных массивов для примеров
  validator/             Pydantic-модели и валидация ответов
    models.py            Схемы ответов для каждого эндпоинта
    validator.py         Прогон ответов через модели, формирование Issue
  anonymizer/            Faker-замена реальных значений
    anonymizer.py        Основная логика анонимизации
    rules.py             Правила замены по полям
  publisher/             Генерация openapi.json и Swagger UI
    builder.py           Сборка OpenAPI-спеки из примеров
data/
  raw/                   Сырые ответы API (в .gitignore, не коммитится)
  examples/              Анонимизированные примеры (коммитятся)
documentation/           Артефакты для GitHub Pages (openapi.json + index.html)
devel/
  design/                Архитектурные решения
  plans/                 Планы реализации
  changelog/             История изменений
tests/                   Pytest-тесты
scripts/                 Вспомогательные скрипты (сборка mock-worker и т.д.)
mock/                    Cloudflare Worker для mock-API
```

## Установка и запуск

### Зависимости

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (рекомендуется) или pip

### Установка

```bash
uv sync
```

### Локальный запуск

```bash
JOURNAL_LOGIN=ваш_логин JOURNAL_PASSWORD=ваш_пароль uv run main.py
```

После запуска появятся:

| Файл | Описание |
|------|----------|
| `data/raw/latest.json` | Сырые ответы API (в .gitignore) |
| `data/examples/latest.json` | Анонимизированные примеры |
| `documentation/openapi.json` | Готовая OpenAPI-спека |
| `documentation/index.html` | Swagger UI |

### Просмотр документации локально

```bash
cd documentation && python -m http.server 8000
```

Открыть http://localhost:8000 — там будет Swagger UI с интерактивной документацией.

## Покрытые эндпоинты

**34 эндпоинта**, включая авторизацию, профиль, дашборд, расписание, успеваемость, домашние задания и публичные данные.

### Авторизация

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/auth/login` | POST | Авторизация, получение Bearer-токена |

### Профиль

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/settings/user-info` | GET | Профиль студента, группа, поток |
| `/profile/operations/settings` | GET | Настройки профиля, контакты, фото |
| `/profile/statistic/student-achievements` | GET | Достижения студента |

### Дашборд — графики

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/dashboard/chart/average-progress` | GET | Средний прогресс по месяцам |
| `/dashboard/chart/attendance` | GET | Посещаемость по месяцам |
| `/dashboard/chart/progress` | GET | Графики прогресса по типам (chart_type + chart_models) |

### Дашборд — рейтинг

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/dashboard/progress/leader-group` | GET | Топ студентов по группе |
| `/dashboard/progress/leader-stream` | GET | Топ студентов по потоку |
| `/dashboard/progress/leader-group-points` | GET | Позиция и баллы студента в группе |
| `/dashboard/progress/leader-stream-points` | GET | Позиция и баллы студента в потоке |
| `/dashboard/progress/activity` | GET | Лента активности (баллы, достижения) |

### Дашборд — экзамены

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/dashboard/info/future-exams` | GET | Предстоящие экзамены |

### Расписание

| Эндпоинт | Метод | Описание | Параметры |
|----------|-------|----------|-----------|
| `/schedule/operations/get-by-date` | GET | Расписание на дату | `?date_filter=YYYY-MM-DD` |
| `/schedule/operations/get-by-date-range` | GET | Расписание за период | `?date_start&date_end=YYYY-MM-DD` |
| `/schedule/operations/get-month` | GET | Расписание на месяц | `?date_filter=YYYY-MM-DD` |

### Успеваемость

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/progress/operations/student-visits` | GET | Журнал посещений и оценок |
| `/progress/operations/student-exams` | GET | Оценки за экзамены |
| `/count/homework` | GET | Счётчики домашних заданий по типам |

### Библиотека

| Эндпоинт | Метод | Описание | Параметры |
|----------|-------|----------|-----------|
| `/library/operations/list` | GET | Список материалов | `?material_type&filter_type&recommended_type` |

### Домашние задания

| Эндпоинт | Метод | Описание | Параметры |
|----------|-------|----------|-----------|
| `/homework/settings/group-history` | GET | Группы студента с предметами (переключатель в ДЗ) | |
| `/settings/group-specs` | GET | Предметы текущей группы | |
| `/homework/evaluation/operations/get-tags` | GET | Теги для самооценки ДЗ | |
| `/homework/operations/list` | GET | Список домашних заданий | `?page&status&type&group_id` |

### Отзывы и обратная связь

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/reviews/index/list` | GET | Отзывы преподавателей |
| `/reviews/index/instruction` | GET | Инструкция по отзывам |
| `/feedback/students/evaluate-lesson-list` | GET | Список уроков для оценки |
| `/feedback/social-review/get-review-list` | GET | Социальные отзывы (ссылки, скриншоты) |

### Сигналы

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/signal/operations/signals-list` | GET | Список сигналов (обращения, проблемы) |
| `/signal/operations/problems-list` | GET | Список типов проблем |

### Новости

| Эндпоинт | Метод | Описание |
|----------|-------|----------|
| `/news/operations/latest-news` | GET | Последние новости |

### Публичные эндпоинты

| Эндпоинт | Метод | Описание | Параметры |
|----------|-------|----------|-----------|
| `/public/languages` | GET | Доступные языки | |
| `/public/translations` | GET | Локализационные строки | `?language=ru` |
| `/public/tags` | GET | Публичные теги | |

## Аутентификация

Все эндпоинты кроме `/auth/login` требуют заголовки:

```
Authorization: Bearer <access_token>
Origin: https://journal.top-academy.ru
Referer: https://journal.top-academy.ru/
```

Токен получается через POST `/auth/login`:

```json
{
  "application_key": "<key>",
  "id_city": null,
  "username": "<login>",
  "password": "<password>"
}
```

## Публикация на GitHub Pages

Документация публикуется автоматически через GitHub Actions. Но можно и вручную.

### Автоматическая публикация (через CI)

Пайплайн `.github/workflows/collect.yml` запускается:
- **По расписанию** — каждый день в 03:00 UTC
- **Вручную** — кнопка «Run workflow» на вкладке Actions

Для работы CI нужно настроить в Settings → Secrets and variables → Actions:

| Секрет | Описание |
|--------|----------|
| `JOURNAL_LOGIN` | Логин от журнала |
| `JOURNAL_PASSWORD` | Пароль от журнала |
| `GITHUB_TOKEN` | Автоматически предоставляется GitHub (не нужно добавлять) |
| `CLOUDFLARE_API_TOKEN` | Для деплоя mock-worker (опционально) |

### Ручная публикация

Если нужно обновить документацию вручную, без CI:

**Вариант 1 — через gh-pages ветку (рекомендуется):**

```bash
# Запускаем пайплайн локально
JOURNAL_LOGIN=ваш_логин JOURNAL_PASSWORD=ваш_пароль uv run main.py

# Пушим содержимое documentation/ на ветку gh-pages
npx gh-pages -d documentation
```

**Вариант 2 — через git subtree:**

```bash
uv run main.py

git add documentation/
git commit -m "docs: update openapi spec"
git subtree push --prefix documentation origin gh-pages
```

### Настройка GitHub Pages в репозитории

1. Открыть **Settings → Pages**
2. В поле **Source** выбрать `Deploy from a branch`
3. В поле **Branch** выбрать `gh-pages` и папку `/ (root)`
4. Нажать **Save**

После этого документация будет доступна по адресу:
`https://<username>.github.io/<repo-name>/`

## Мониторинг изменений API

Если структура ответа API изменилась и перестала проходить Pydantic-валидацию:

1. Пайплайн падает
2. Создаётся GitHub Issue с лейблом `api-change` и описанием конкретных полей
3. Issue нужно обработать — обновить модель в `src/validator/models.py`

## Тесты и линтинг

```bash
# Запуск тестов
uv run pytest

# Линтинг
uv run ruff check .

# Фикс автоисправимых проблем
uv run ruff check --fix .
```

## Для AI-агентов

Все AI-агенты в этом репозитории следуют общим правилам из [`AGENTS.md`](AGENTS.md). Файлы агентов дополняют, а не дублируют:

| Файл | Инструмент | Назначение |
|------|------------|------------|
| [`AGENTS.md`](AGENTS.md) | Все | Общие правила — единый источник правды |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code | TDD, верификация |
| [`GEMINI.md`](GEMINI.md) | Gemini CLI | Фазы разработки, протокол решений |
| [`.codex/AGENTS.md`](.codex/AGENTS.md) | Codex | Стиль, настройки |

## Планы

### Выполнено

- [x] Добавить `BearerAuth` security scheme в OpenAPI-спеку
- [x] Задокументировать обязательные заголовки (`Origin`, `Referer`) как параметры
- [x] Исправить схему ответов (`array` vs `object`) на основе реальных данных
- [x] Покрыть основные эндпоинты (34 из известных)

### В планах

- [ ] Текстовая документация по каждому эндпоинту — типы полей, возможные значения, семантика
- [ ] Документирование enum-значений (`status_was`, `counter_type`, `gender`, `group_status`) — частично: `counter_type` задокументирован в `endpoints.py`
- [ ] Автоматический changelog из истории Issue об изменениях API
