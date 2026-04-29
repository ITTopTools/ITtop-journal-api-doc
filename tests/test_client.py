import pytest
from unittest.mock import AsyncMock
from src.collector.endpoints import Endpoint
from src.collector.client import JournalClient, DEFAULT_MAX_ITEMS


def test_default_max_items_is_3():
    assert DEFAULT_MAX_ITEMS == 3

@pytest.mark.asyncio
async def test_collect_all_uses_endpoint_max_items():
    ep_default = Endpoint(path="/default", method="GET")
    ep_custom = Endpoint(path="/custom", method="GET", max_items=7)

    client = JournalClient(login="test", password="test")
    client.authenticate = AsyncMock(return_value="token")
    client._fetch_with_retry = AsyncMock(side_effect=[
        [{"id": i} for i in range(10)],  # 10 items for /default
        [{"id": i} for i in range(10)],  # 10 items for /custom
    ])

    collected, raw_counts = await client.collect_all([ep_default, ep_custom])

    # /default trimmed to DEFAULT_MAX_ITEMS (3)
    assert len(collected["/default"]) == 3
    # /custom trimmed to max_items=7
    assert len(collected["/custom"]) == 7

@pytest.mark.asyncio
async def test_collect_all_returns_raw_counts_for_validate_count_endpoints():
    ep = Endpoint(
        path="/schedule/test",
        method="GET",
        validate_count=True,
        expected_max_items=5,
    )

    client = JournalClient(login="test", password="test")
    client.authenticate = AsyncMock(return_value="token")
    client._fetch_with_retry = AsyncMock(return_value=[{"id": i} for i in range(10)])

    collected, raw_counts = await client.collect_all([ep])

    assert "/schedule/test" in raw_counts
    assert raw_counts["/schedule/test"] == 10
    # Still trimmed to DEFAULT_MAX_ITEMS
    assert len(collected["/schedule/test"]) == 3

@pytest.mark.asyncio
async def test_collect_all_no_raw_count_for_non_validate_count():
    ep = Endpoint(path="/normal", method="GET")

    client = JournalClient(login="test", password="test")
    client.authenticate = AsyncMock(return_value="token")
    client._fetch_with_retry = AsyncMock(return_value=[{"id": i} for i in range(10)])

    collected, raw_counts = await client.collect_all([ep])

    assert "/normal" not in raw_counts

@pytest.mark.asyncio
async def test_collect_all_no_raw_count_for_dict_responses():
    ep = Endpoint(path="/dict-endpoint", method="GET", validate_count=True)

    client = JournalClient(login="test", password="test")
    client.authenticate = AsyncMock(return_value="token")
    client._fetch_with_retry = AsyncMock(return_value={"key": "value"})

    collected, raw_counts = await client.collect_all([ep])

    # dict response should not have raw_count even with validate_count=True
    assert "/dict-endpoint" not in raw_counts
