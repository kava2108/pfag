import pytest
from fastapi.testclient import TestClient
from src.pfag.api.skills import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router, prefix="/skills")

@pytest.fixture
def client():
    return TestClient(app)

def test_post_skills_contract(client):
    # スキーマ定義APIの契約テスト（失敗することを期待）
    payload = {
        "skill_name": "ocr_text_extraction",
        "input_schema": {"type": "object", "properties": {"image": {"type": "string"}}},
        "output_schema": {"type": "object", "properties": {"text": {"type": "string"}}},
        "description": "OCRテキスト抽出スキル",
        "version": "1.0.0"
    }
    response = client.post("/skills", json=payload)
    assert response.status_code == 201  # まずは失敗することを期待
