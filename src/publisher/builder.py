"""OpenAPI specification builder for collected Journal endpoint data."""

import json
from datetime import date
from pathlib import Path
from typing import Any

from src.collector.endpoints import ENDPOINTS, LOGIN_PATH
from src.validator.validator import MODELS as VALIDATOR_MODELS

API_DOWN_WARNING = "⚠️ API unavailable at collection time. Examples may be outdated."

# Обязательные заголовки для всех аутентифицированных запросов к Journal API.
# Origin и Referer проверяются сервером как часть CORS-политики —
# без них запрос вернёт 403 даже с валидным Bearer токеном.
REQUIRED_HEADERS = [
    {
        "name": "Origin",
        "in": "header",
        "required": True,
        "schema": {"type": "string"},
        "example": "https://journal.top-academy.ru",
        "description": "Required by the API CORS policy.",
    },
    {
        "name": "Referer",
        "in": "header",
        "required": True,
        "schema": {"type": "string"},
        "example": "https://journal.top-academy.ru/",
        "description": "Required by the API. Must end with trailing slash.",
    },
    {
        "name": "User-Agent",
        "in": "header",
        "required": False,
        "schema": {"type": "string"},
        "example": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        ),
        "description": "Recommended to match a real browser UA to avoid blocks.",
    },
]

# Worker — единственная точка входа для Swagger UI.
# Прямой доступ к msapi.top-academy.ru из браузера невозможен из-за CORS:
# сервер не возвращает Access-Control-Allow-Origin, браузер блокирует ответ.
#
# Worker решает это прозрачно:
#   с Bearer токеном → проксирует на реальный API (живые данные)
#   без токена       → отдаёт mock (анонимизированные данные)
SERVERS = [
    {
        "url": "https://ittop-mock.blazer19092008.workers.dev/api/v2",
        "description": "Mock + proxy: без токена — mock-данные, с Bearer токеном — реальный API",
    },
]

# Глобальный массив тегов — порядок определяет порядок секций в Swagger UI.
TAGS = [
    {"name": "auth", "description": "Authentication — login to obtain JWT access token"},
    {"name": "profile", "description": "Student profile and personal settings"},
    {"name": "dashboard", "description": "Dashboard overview: progress charts, attendance, leaderboards, upcoming exams"},
    {"name": "schedule", "description": "Class schedule by date and date range"},
    {"name": "progress", "description": "Academic progress: visit records and exam results"},
    {"name": "homework", "description": "Homework and assignments: lists, counters, self-evaluation tags"},
    {"name": "library", "description": "Learning materials and library"},
    {"name": "reviews", "description": "Reviews and lesson feedback"},
    {"name": "signals", "description": "Academic alert signals and problem indicators"},
    {"name": "news", "description": "Academy news and announcements"},
    {"name": "public", "description": "Public reference data — no authentication required"},
]


def _pydantic_to_openapi_schema(model_cls: type, is_list: bool) -> dict[str, Any]:
    """Convert a Pydantic model to an OpenAPI 3.0.3 response schema.

    Uses model_json_schema() and resolves $defs/$ref into components/schemas
    references. Returns the schema and a dict of component schemas to merge.
    """
    json_schema = model_cls.model_json_schema()
    defs = json_schema.pop("$defs", {})

    # Собираем схемы для components/schemas
    component_schemas: dict[str, Any] = {}
    for def_name, def_schema in defs.items():
        component_schemas[def_name] = _clean_json_schema(def_schema)

    # Основная схема модели
    main_schema = _clean_json_schema(json_schema)

    # Если есть $ref — заменяем на компонентную ссылку
    main_schema = _resolve_refs(main_schema)

    if is_list:
        items_schema = main_schema
        # Если основная схема — просто объект без имени, пробуем вытащить из $ref
        if "$ref" in items_schema:
            pass  # уже правильная ссылка
        result = {"type": "array", "items": items_schema}
    else:
        result = main_schema

    return result, component_schemas


def _clean_json_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """Remove JSON Schema fields not valid in OpenAPI 3.0.3."""
    remove_keys = {"title", "default"}
    cleaned = {}
    for key, value in schema.items():
        if key in remove_keys:
            continue
        if isinstance(value, dict):
            cleaned[key] = _clean_json_schema(value)
        elif isinstance(value, list):
            cleaned[key] = [
                _clean_json_schema(item) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            cleaned[key] = value
    return cleaned


def _resolve_refs(schema: dict[str, Any]) -> dict[str, Any]:
    """Convert JSON Schema $defs/... references to OpenAPI #/components/schemas/... format."""
    result = {}
    for key, value in schema.items():
        if key == "$ref" and isinstance(value, str) and value.startswith("#/$defs/"):
            name = value.split("/")[-1]
            result[key] = f"#/components/schemas/{name}"
        elif isinstance(value, dict):
            result[key] = _resolve_refs(value)
        elif isinstance(value, list):
            result[key] = [
                _resolve_refs(item) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            result[key] = value
    return result


class OpenAPIBuilder:
    """Build and persist OpenAPI schema generated from known endpoints."""

    def build(self, examples: dict[str, Any], is_api_down: bool = False) -> dict:
        """Build OpenAPI 3.0.3 document with examples from collected payloads.

        Args:
            examples: Анонимизированные ответы эндпоинтов из anonymizer-а.
                      Ключ — путь эндпоинта (/dashboard/chart/attendance),
                      значение — уже очищенный JSON (dict или list).
            is_api_down: Если True — добавляет предупреждение в description,
                         что сбор данных не удался и примеры могут быть устаревшими.

        Returns:
            Готовый OpenAPI 3.0.3 документ в виде dict, готовый к json.dumps().
        """

        description = "Auto-generated documentation from daily Journal API collection."
        if is_api_down:
            description = f"{description}\n\n{API_DOWN_WARNING}"

        component_schemas: dict[str, Any] = {}

        spec: dict[str, Any] = {
            "openapi": "3.0.3",
            "info": {
                "title": "IT Top Journal API",
                "version": date.today().isoformat(),
                "description": description,
            },
            "tags": TAGS,
            "servers": SERVERS,
            "components": {
                "securitySchemes": {
                    "BearerAuth": {
                        "type": "http",
                        "scheme": "bearer",
                        "bearerFormat": "JWT",
                        "description": (
                            "JWT access token obtained from POST /auth/login response field "
                            "`access_token`. Pass as: Authorization: Bearer <token>"
                        ),
                    }
                },
                "schemas": component_schemas,
            },
            "paths": {},
        }

        for endpoint in ENDPOINTS:
            method = endpoint.method.lower()

            # Генерируем схему ответа из Pydantic-модели
            if endpoint.path in VALIDATOR_MODELS:
                model_cls, is_list = VALIDATOR_MODELS[endpoint.path]
                try:
                    response_schema, new_schemas = _pydantic_to_openapi_schema(
                        model_cls, is_list
                    )
                    component_schemas.update(new_schemas)
                except Exception:
                    # Fallback если генерация схемы упала
                    if is_list:
                        response_schema = {
                            "type": "array",
                            "items": {"type": "object", "additionalProperties": True},
                        }
                    else:
                        response_schema = {"type": "object", "additionalProperties": True}
            else:
                response_schema = {"type": "object", "additionalProperties": True}

            resp_desc = endpoint.response_description or "Successful response"

            operation: dict[str, Any] = {
                "summary": endpoint.summary or f"{endpoint.method} {endpoint.path}",
                "description": endpoint.description
                    or f"Auto-generated operation for `{endpoint.path}`.",
                "tags": [endpoint.tag] if endpoint.tag else [],
                "responses": {
                    "200": {
                        "description": resp_desc,
                        "content": {
                            "application/json": {
                                "schema": response_schema
                            }
                        },
                    }
                },
            }

            # x-uncertain маркер
            if endpoint.uncertain:
                operation["x-uncertain"] = endpoint.uncertain

            # Query-параметры для GET-эндпоинтов (например date_filter, language).
            if endpoint.method.upper() == "GET" and endpoint.params:
                operation["parameters"] = [
                    {
                        "name": key,
                        "in": "query",
                        "required": False,
                        "schema": {"type": "string"},
                        "example": value,
                    }
                    for key, value in endpoint.params.items()
                ]

            # requestBody для POST-эндпоинтов (только /auth/login).
            if endpoint.method.upper() == "POST" and endpoint.params:
                operation["requestBody"] = {
                    "description": "Content-Type: application/json must be set explicitly.",
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"type": "object", "additionalProperties": True},
                            "example": endpoint.params,
                        }
                    },
                }

            # Все эндпоинты кроме /auth/login требуют Bearer токен.
            # Worker пробрасывает его на реальный API автоматически.
            # Origin/Referer/User-Agent Worker тоже подставляет сам —
            # но документируем их чтобы юзер понимал что реальный API требует.
            if endpoint.path != LOGIN_PATH:
                operation["security"] = [{"BearerAuth": []}]
                existing_params = operation.get("parameters", [])
                operation["parameters"] = REQUIRED_HEADERS + existing_params

            # Подставляем анонимизированный пример ответа если он есть.
            if endpoint.path in examples:
                operation["responses"]["200"]["content"]["application/json"]["example"] = examples[
                    endpoint.path
                ]

            spec["paths"].setdefault(endpoint.path, {})[method] = operation

        return spec

    def save(self, spec: dict, path: str = "documentation/src/openapi.json") -> None:
        """Persist generated OpenAPI document as formatted JSON.

        Args:
            spec: Документ из метода build().
            path: Куда сохранять. По умолчанию — documentation/src/,
                  откуда MkDocs подхватывает файл для swagger-ui-tag.
        """

        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
