import pytest
from fastapi.testclient import TestClient
from src.pfag.api.skills import app

client = TestClient(app)

def test_get_warnings():
    res = client.get("/warnings")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
