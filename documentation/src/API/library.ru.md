# Библиотека

Учебные материалы и ресурсы библиотеки.

## Конечные точки

### GET /library/operations/list

Учебные материалы из библиотеки.

**Назначение:** Список материалов в разделе библиотеки приложения.

**Параметры:**

| Параметр | Тип | Описание |
|----------|-----|----------|
| `material_type` | int | Значение фильтра (по умолчанию: 2) |
| `filter_type` | int | Значение фильтра (по умолчанию: 0) |
| `recommended_type` | int | Значение фильтра (по умолчанию: 0) |

**Ответ:** Массив элементов материалов.

<!-- ?UNSURE: material_type/filter_type/recommended_type values are inferred from UI defaults, not documented; response schema unknown — collected data was empty -->
