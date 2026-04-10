"""Recursive type-based anonymization of JSON-like payloads."""

import re
from typing import Any

from faker import Faker


class Anonymizer:
    """Replace all values with synthetic data based on their data types."""

    def __init__(self) -> None:
        self.fake = Faker()

    def anonymize(self, data: dict | list) -> dict | list:
        """Return a new anonymized copy of a dict/list payload."""
        
        return self._anonymize_node(data)

    def _anonymize_node(self, node: Any) -> Any:
        """Recursively process nested structures and apply type-based replacement."""

        if isinstance(node, dict):
            return {key: self._anonymize_node(value) for key, value in node.items()}

        if isinstance(node, list):
            return [self._anonymize_node(item) for item in node]

        if isinstance(node, str):
            if not node:
                return ""
            
            # Проверка на URL или пути
            if node.startswith(("http", "//")):
                return self.fake.url()
            if node.startswith("/"):
                return f"/{self.fake.uri_path()}"
            
            # Проверка на даты (ISO 8601 или YYYY-MM-DD)
            if re.match(r"^\d{4}-\d{2}-\d{2}", node):
                return self.fake.date_time_this_year().isoformat()
            
            # Проверка на UUID
            if re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", node, re.I):
                return self.fake.uuid4()
            
            # Проверка на email
            if "@" in node and "." in node.split("@")[-1]:
                return self.fake.email()

            # Дефолтная замена любой другой строки
            return self.fake.pystr(min_chars=5, max_chars=15)

        if isinstance(node, bool):
            # Булевы значения (true/false) безопасны
            return node

        if isinstance(node, int):
            return self.fake.random_int(min=1000, max=99999)

        if isinstance(node, float):
            return round(self.fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2)

        if node is None:
            return None

        # Fallback для непредвиденных типов
        return "ANONYMIZED"