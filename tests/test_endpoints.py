from src.collector.endpoints import Endpoint, ENDPOINTS


def test_endpoint_has_anonymize_field():
    ep = Endpoint(path="/test", method="GET")
    assert ep.anonymize is True

def test_endpoint_anonymize_can_be_false():
    ep = Endpoint(path="/test", method="GET", anonymize=False)
    assert ep.anonymize is False

def test_endpoint_has_max_items_field():
    ep = Endpoint(path="/test", method="GET")
    assert ep.max_items is None

def test_endpoint_max_items_can_be_set():
    ep = Endpoint(path="/test", method="GET", max_items=7)
    assert ep.max_items == 7

def test_endpoint_has_validate_count_field():
    ep = Endpoint(path="/test", method="GET")
    assert ep.validate_count is False

def test_endpoint_validate_count_can_be_true():
    ep = Endpoint(path="/test", method="GET", validate_count=True)
    assert ep.validate_count is True

def test_endpoint_has_expected_max_items_field():
    ep = Endpoint(path="/test", method="GET")
    assert ep.expected_max_items is None

def test_endpoint_expected_max_items_can_be_set():
    ep = Endpoint(path="/test", method="GET", validate_count=True, expected_max_items=1)
    assert ep.expected_max_items == 1

def test_public_endpoints_have_anonymize_false():
    public_paths = [e.path for e in ENDPOINTS if e.path.startswith("/public/")]
    for e in ENDPOINTS:
        if e.path in public_paths:
            assert e.anonymize is False, f"{e.path} should have anonymize=False"

def test_schedule_endpoints_do_not_validate_count():
    schedule_paths = [
        "/schedule/operations/get-by-date",
        "/schedule/operations/get-by-date-range",
        "/schedule/operations/get-month",
    ]
    for e in ENDPOINTS:
        if e.path in schedule_paths:
            assert e.validate_count is False, f"{e.path} should have validate_count=False"
            assert e.expected_max_items is None, f"{e.path} should have no expected_max_items"
