# ITtop Journal API Docs

> Автоматическая OpenAPI-документация для [IT Top Academy Journal](https://journal.top-academy.ru).
> Данные собираются, анонимизируются и публикуются через GitHub Pages.

## О проекте

IT Top Journal не имеет публичной документации. Этот проект заполняет пробел:

- **Собирает** реальные ответы API через авторизованные запросы
- **Валидирует** структуру через Pydantic — если API изменился, открывается Issue
- **Анонимизирует** данные через Faker — реальные имена, ID и даты не попадают в публичный репозиторий
- **Генерирует** `openapi.json` и публикует Swagger UI на GitHub Pages
- **Разворачивает** mock-сервер на Cloudflare Worker — решает CORS и Origin/Referer для Swagger UI

Пайплайн запускается каждый день в 03:00 UTC через GitHub Actions. Также доступен ручной запуск (workflow_dispatch).

## Как это работает

```
tests → collect → validate → anonymize → publish → worker → mkdocs
                      ↓ (ошибка)
                GitHub Issue (api-change)
```

7 последовательных джобов, каждый — reusable workflow:

1. **collect** — логинится по `/auth/login`, обходит все 34 эндпоинта, сохраняет сырые ответы в `data/raw/latest.json`
2. **validate** — Pydantic-валидация; soft-fail (exit 0), пишет флаг `validation_failed`, создаёт Issue с лейблом `api-change`
3. **anonymize** — подменяет PII (имена, ID, даты) на Faker-генерированные значения; сохраняет в `data/examples/latest.json`
4. **publish** — строит `openapi.json` из примеров; сохраняет в `documentation/src/openapi.json`
5. **worker** — генерирует Cloudflare Worker из шаблона `mock/build_worker.py` + примеры; деплоит через wrangler
6. **mkdocs** — собирает MkDocs Material-сайт, деплоит на gh-pages через peaceiris/actions-gh-pages

## Структура проекта

```
src/
  collector/             Авторизация и сбор данных
  validator/             Pydantic-модели и валидация
  anonymizer/            Faker-замена PII
  publisher/             Генерация OpenAPI
data/
  raw/                   Сырые ответы API (gitignore)
  examples/              Анонимизированные примеры (коммитятся)
documentation/
  src/                   Markdown + openapi.json
  site/                  Собранный сайт (gitignore, gh-pages)
mock/
  worker.js              Сгенерированный Cloudflare Worker
  build_worker.py        Шаблон, генерирующий worker.js
  wrangler.toml          Конфиг Worker
devel/
  design/                Архитектурные решения (01-idea → 08-branch-strategy)
  plans/                 Планы реализации
  changelog/             История изменений
  skills/                Справочники для AI-агентов
tests/                   Pytest-тесты (37 тестов, включая test_worker.py)
.github/workflows/       CI/CD (pipeline.yml + 8 reusable workflows)
```

## Mock-сервер (Cloudflare Worker)

URL: `https://ittop-mock.blazer19092008.workers.dev/api/v2`

Режимы работы:

- **Без Bearer-токена** — возвращает анонимизированные mock-данные
- **С Bearer-токеном** — проксирует запрос на реальный API `https://msapi.top-academy.ru/api/v2`, подставляя Origin/Referer/User-Agent
- **`/auth/login`** — всегда проксирует на реальный API; при 4xx/ошибке fallback на mock (логин без токена)

Зачем нужен: Swagger UI на `github.io` не может обращаться к реальному API напрямую из-за CORS и требования Origin/Referer = `journal.top-academy.ru`. Worker решает обе проблемы — добавляет CORS-заголовки ко всем ответам и инжектит нужные заголовки при проксировании.

Worker собирается из шаблона `mock/build_worker.py` — встраивает MOCK-данные прямо в `worker.js`.

## Swagger UI

MkDocs Material-сайт с плагином `swagger-ui-tag`. Страница `swagger.md` содержит тег `<swagger-ui src="openapi.json"/>`, который рендерит интерактивную документацию.

- Try it out включён для всех методов: GET, PUT, POST, DELETE, PATCH
- Без авторизации — запросы идут на mock-сервер (анонимизированные данные)
- С авторизацией — запросы проксируются на реальный API

Доступен на GitHub Pages.

## Документация

MkDocs Material (русский язык, переключатель тёмной/светлой темы).

Плагины: awesome-pages, swagger-ui-tag.

Страницы: index, authentication, swagger, mock-server, API/* (8 страниц по группам эндпоинтов).

Исходники: `documentation/src/`, сборка: `documentation/site/` (gitignore, деплой на gh-pages).

## Установка и запуск

### Зависимости

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (рекомендуется) или pip

### Установка

```bash
uv sync --group docs
```

### Локальный запуск

```bash
# Полный пайплайн
JOURNAL_LOGIN=ваш_логин JOURNAL_PASSWORD=ваш_пароль uv run main.py

# Отдельные шаги
uv run main.py --step collect     # Сбор данных (требует JOURNAL_LOGIN/PASSWORD)
uv run main.py --step validate    # Валидация (всегда exit 0, soft fail)
uv run main.py --step anonymize   # Анонимизация
uv run main.py --step publish     # Генерация openapi.json
```

Результаты:

| Файл | Описание |
|------|----------|
| `data/raw/latest.json` | Сырые ответы API (gitignore) |
| `data/examples/latest.json` | Анонимизированные примеры |
| `documentation/src/openapi.json` | Готовая OpenAPI-спека |

### Просмотр документации локально

```bash
.venv/bin/mkdocs serve
```

Открыть http://localhost:8000 — Swagger UI с интерактивной документацией.

## Покрытые эндпоинты

**34 эндпоинта**, включая авторизацию, профиль, дашборд, расписание, успеваемость, библиотеку, домашние задания, отзывы, сигналы, новости и публичные данные.

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
| `/homework/evaluation/operations/get-tags` | GET | Теги оценки ДЗ | |
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

Документация публикуется автоматически через GitHub Actions.

### Автоматическая публикация (CI)

Пайплайн `.github/workflows/pipeline.yml` запускается:

- **По расписанию** — каждый день в 03:00 UTC
- **Вручную** — кнопка «Run workflow» на вкладке Actions

Необходимые секреты (Settings → Secrets and variables → Actions):

| Секрет | Описание |
|--------|----------|
| `JOURNAL_LOGIN` | Логин от журнала |
| `JOURNAL_PASSWORD` | Пароль от журнала |
| `GITHUB_TOKEN` | Автоматически предоставляется GitHub |
| `CLOUDFLARE_API_TOKEN` | Для деплоя Worker (опционально) |

### Ручная публикация

```bash
# Запускаем пайплайн локально
JOURNAL_LOGIN=ваш_логин JOURNAL_PASSWORD=ваш_пароль uv run main.py

# Собираем и деплоим MkDocs-сайт
.venv/bin/mkdocs build
npx gh-pages -d documentation/site
```

### Настройка GitHub Pages в репозитории

1. Открыть **Settings → Pages**
2. В поле **Source** выбрать `Deploy from a branch`
3. В поле **Branch** выбрать `gh-pages` и папку `/ (root)`
4. Нажать **Save**

Документация доступна по адресу: `https://<username>.github.io/<repo-name>/`

## Мониторинг изменений API

Если структура ответа API изменилась и перестала проходить Pydantic-валидацию:

1. Шаг validate пишет `validation_failed=true` в GITHUB_OUTPUT (soft fail — exit 0)
2. Создаётся GitHub Issue с лейблом `api-change` и описанием конкретных полей
3. Пайплайн продолжает работу — использует последние закоммиченные примеры
4. Issue нужно обработать — обновить модель в `src/validator/models.py`

## Тесты и линтинг

```bash
uv run pytest                # Запуск тестов (37 тестов)
uv run ruff check .          # Линтинг
uv run ruff check --fix .    # Фикс автоисправимых проблем
```

## Для AI-агентов

Все AI-агенты в этом репозитории следуют общим правилам из [`AGENTS.md`](AGENTS.md). Файлы агентов дополняют, а не дублируют:

| Файл | Инструмент | Назначение |
|------|------------|------------|
| [`AGENTS.md`](AGENTS.md) | Все | Общие правила — единый источник правды |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code | TDD, верификация |
| [`GEMINI.md`](GEMINI.md) | Gemini CLI | Фазы разработки, протокол решений |
| [`.codex/AGENTS.md`](.codex/AGENTS.md) | Codex | Стиль, настройки |
