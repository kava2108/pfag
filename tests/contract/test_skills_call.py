import pytest
from fastapi.testclient import TestClient
from src.pfag.api.skills import app

client = TestClient(app)

def test_call_skill_success():
    # 事前にスキルスキーマを登録
    skill_name = "echo"
    schema = {
        "skill_name": skill_name,
        "input_schema": {"type": "object", "properties": {"text": {"type": "string"}}},
        "output_schema": {"type": "object", "properties": {"result": {"type": "string"}}},
        "description": "Echo skill",
        "version": "1.0"
    }
    client.post("/skills", json=schema)
    # スキル呼び出し
    payload = {"text": "hello"}
    res = client.post(f"/skills/{skill_name}/call", json=payload)
    assert res.status_code == 200
    assert "result" in res.json()

def test_call_skill_not_found():
    res = client.post("/skills/not_exist/call", json={"text": "test"})
    assert res.status_code == 404
    assert res.json()["detail"] == "Skill not found"
