"""
Contract Test: バイナリ返却API
T022: バイナリ返却のcontractテスト
"""
import pytest
from fastapi.testclient import TestClient
from src.pfag.api.main import app

client = TestClient(app)

def test_pdf_binary_contract():
    # サンプルPDFを事前配置
    payload = {
        "pdf_id": "sample.pdf",
        "fields": [
            {
                "name": "field_p1_t1",
                "type": "Tx",
                "page": 1,
                "rect": [100, 700, 200, 720],
                "options": {"value": "binary"}
            }
        ]
    }
    response = client.post("/pdf/write-fields", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content[:4] == b"%PDF"
    # バイナリ長・ダウンロード可能性
    assert len(response.content) > 100
