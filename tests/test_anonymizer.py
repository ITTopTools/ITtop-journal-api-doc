import pytest
from src.anonymizer.anonymizer import Anonymizer

def test_anonymize_replaces_strings():
    anon = Anonymizer()
    data = {"name": "Ivan Ivanov", "bio": "Some long description"}
    result = anon.anonymize(data)
    
    assert result["name"] != "Ivan Ivanov"
    assert isinstance(result["name"], str)
    assert result["bio"] != "Some long description"

def test_anonymize_replaces_integers():
    anon = Anonymizer()
    data = {"id": 12345}
    result = anon.anonymize(data)
    
    assert result["id"] != 12345
    assert isinstance(result["id"], int)

def test_anonymize_nested_structure():
    anon = Anonymizer()
    data = {
        "user": {"name": "Admin", "settings": {"theme": "dark"}},
        "items": [1, 2, 3]
    }
    result = anon.anonymize(data)
    
    assert result["user"]["name"] != "Admin"
    assert result["user"]["settings"]["theme"] != "dark"
    assert all(i != original for i, original in zip(result["items"], [1, 2, 3]))

def test_anonymize_preserves_special_formats():
    anon = Anonymizer()
    data = {
        "url": "https://google.com",
        "email": "test@test.com",
        "date": "2024-01-01"
    }
    result = anon.anonymize(data)
    
    assert result["url"].startswith("http")
    assert "@" in result["email"]
    # Проверка формата даты через регулярку (базовая)
    assert "-" in result["date"]