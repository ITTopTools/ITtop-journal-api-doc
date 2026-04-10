"""Tests for validation flow behavior."""

import pytest
from pydantic import BaseModel, ConfigDict

import src.validator.validator as validator_module
from src.validator.validator import Validator


class RequiredFieldModel(BaseModel):
    """Model with one required field for validation tests."""

    model_config = ConfigDict(extra="allow")
    required_field: int


@pytest.mark.parametrize(
    ("raw", "expected_success", "expected_error_count"),
    [
        ({"/known": {"required_field": 1}}, True, 0),
        ({"/known": {}}, False, 1),
    ],
)
def test_validate_all_for_known_path(monkeypatch, raw, expected_success, expected_error_count):
    """Validator should validate known endpoints against mapped models."""

    monkeypatch.setattr(validator_module, "MODELS", {"/known": RequiredFieldModel})

    results = Validator().validate_all(raw)

    assert len(results) == 1
    assert results[0].success is expected_success
    assert len(results[0].errors) >= expected_error_count


def test_validate_all_unknown_path_is_success(monkeypatch):
    """Validator should skip unknown endpoints without failing."""

    monkeypatch.setattr(validator_module, "MODELS", {})

    results = Validator().validate_all({"/unknown": {"any": "value"}})

    assert len(results) == 1
    assert results[0].endpoint == "/unknown"
    assert results[0].success is True
    assert results[0].errors == []
