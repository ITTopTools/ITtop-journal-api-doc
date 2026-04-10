"""Tests for anonymization recursion and field rules."""

import src.anonymizer.anonymizer as anonymizer_module
from src.anonymizer.anonymizer import Anonymizer


def test_anonymize_replaces_fio(monkeypatch):
    """Known field should be replaced by configured rule."""

    monkeypatch.setattr(anonymizer_module, "RULES", {"fio": lambda: "MASKED_NAME"})

    original = {"fio": "Ivanov Ivan"}
    result = Anonymizer().anonymize(original)

    assert result["fio"] == "MASKED_NAME"
    assert result["fio"] != original["fio"]


def test_anonymize_replaces_nested_fields(monkeypatch):
    """Nested dictionaries should be processed recursively."""

    monkeypatch.setattr(
        anonymizer_module,
        "RULES",
        {
            "email": lambda: "masked@example.com",
            "fio": lambda: "MASKED_NAME",
        },
    )

    original = {
        "profile": {
            "fio": "Ivanov Ivan",
            "contacts": {"email": "real@example.com"},
        }
    }
    result = Anonymizer().anonymize(original)

    assert result["profile"]["fio"] == "MASKED_NAME"
    assert result["profile"]["contacts"]["email"] == "masked@example.com"


def test_anonymize_keeps_unknown_fields(monkeypatch):
    """Fields without rules should remain unchanged."""

    monkeypatch.setattr(anonymizer_module, "RULES", {"fio": lambda: "MASKED_NAME"})

    original = {"note": "leave me", "fio": "Ivanov Ivan"}
    result = Anonymizer().anonymize(original)

    assert result["note"] == "leave me"
