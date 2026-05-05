# Mock-сервер

Cloudflare Worker находится между браузером и реальным API.

**Адрес воркера:** `https://ittop-mock.blazer19092008.workers.dev/api/v2`

**Реальный API:** `https://msapi.top-academy.ru/api/v2`

## Логика маршрутизации

Воркер обрабатывает каждый запрос по следующей логике:

1. **OPTIONS** (CORS preflight) → немедленный ответ `204 No Content` с CORS-заголовками
2. **POST /auth/login** → проксирование к реальному API; при ошибке 4xx или сбое сети — возврат mock-данных
3. **Есть заголовок `Authorization: Bearer ...`** → проксирование к реальному API с добавлением `Origin`/`Referer`
4. **Нет токена** → возврат анонимизированных mock-данных

## Зачем это нужно

Swagger UI на `github.io` не может вызывать реальный API напрямую:

1. **CORS** — API не разрешает кросс-доменные запросы с произвольных доменов
2. **Origin/Referer** — API требует эти заголовки равными `journal.top-academy.ru`, что браузер на github.io сделать не может

Воркер решает обе проблемы: добавляет CORS-заголовки к каждому ответу и подставляет `Origin`/`Referer` при проксировании.

## Сборка и деплой

- `mock/build_worker.py` — генерирует `worker.js` из шаблона + анонимизированных примеров данных
- `mock/wrangler.toml` — конфигурация Cloudflare Wrangler
- Деплой: `wrangler deploy` (автоматически через CI, шаг `worker`)
