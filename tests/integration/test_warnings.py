import pytest
from fastapi.testclient import TestClient
from src.pfag.api.skills import app

client = TestClient(app)

def test_get_warnings_integration():
    res = client.get("/warnings")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    # 追加の検証は警告ロジック実装後に拡張
