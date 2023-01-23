import json
import pytest
from fastapi.testclient import TestClient
from sampleapi import app
from typing import Dict, Any

@pytest.mark.parametrize("name,expected_response", [
    ("Test Item", {"name": "Test Item", "id": 1}),
    ("Another Test Item", {"name": "Another Test Item", "id": 2}),
])
def test_create_item(name: str, expected_response: Dict[str, Any]):
    client = TestClient(app)
    response = client.post("/items/", json={"name": name})
    assert response.status_code == 200
    assert response.json()["name"] == expected_response["name"]
    assert isinstance(response.json()["id"], str)


