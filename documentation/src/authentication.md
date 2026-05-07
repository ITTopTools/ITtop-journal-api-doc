# Аутентификация

## Логин

Все эндпоинты, кроме `/auth/login`, требуют Bearer-токен.

### POST /auth/login

```json
{
  "application_key": "<key>",
  "id_city": null,
  "username": "<login>",
  "password": "<password>"
}
```

Возвращает `access_token`, который используется как `Bearer <token>`.

Этот эндпоинт можно вызвать прямо из Swagger UI — воркер проксирует запрос к реальному API. Нажмите «Try it out», заполните поля и выполните.

## Заголовки для прямых запросов

При прямых запросах к API (мимо воркера) каждый авторизованный запрос должен содержать:

| Заголовок | Значение |
|-----------|----------|
| `Authorization` | `Bearer <access_token>` |
| `Origin` | `https://journal.top-academy.ru` |
| `Referer` | `https://journal.top-academy.ru/` |

Без `Origin` и `Referer` API вернёт **403 Forbidden**.

## Работа в Swagger UI

В Swagger UI заголовки `Origin` и `Referer` выставлять не нужно — воркер добавляет их автоматически при проксировании.

### Кнопка Authorize

1. Нажмите **Authorize** (замок вверху страницы)
2. Вставьте `access_token` в поле значения (без `Bearer` — Swagger добавит его сам)
3. Нажмите **Authorize**, затем **Close**
4. Все последующие запросы будут включать заголовок `Authorization`

### Без токена

Без токена Swagger UI тоже работает — mock-сервер вернёт анонимизированные примеры данных для каждого эндпоинта.
