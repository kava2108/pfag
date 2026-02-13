import pytest
from fastapi.testclient import TestClient
from src.pfag.api.main import app

client = TestClient(app)

def test_health_contract():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
