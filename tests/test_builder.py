"""Tests for OpenAPI builder output structure."""

from src.collector.endpoints import ENDPOINTS
from src.publisher.builder import OpenAPIBuilder


def test_build_returns_required_keys():
    """Builder should produce base OpenAPI sections."""

    spec = OpenAPIBuilder().build(examples={})

    assert isinstance(spec, dict)
    assert "openapi" in spec
    assert "info" in spec
    assert "paths" in spec


def test_build_adds_api_down_warning():
    """Builder should append warning text when API was unavailable."""

    spec = OpenAPIBuilder().build(examples={}, is_api_down=True)

    assert "API unavailable at collection time" in spec["info"]["description"]


def test_build_contains_known_endpoints():
    """Builder should include all known endpoint paths and methods."""

    spec = OpenAPIBuilder().build(examples={})

    for endpoint in ENDPOINTS:
        assert endpoint.path in spec["paths"]
        assert endpoint.method.lower() in spec["paths"][endpoint.path]
