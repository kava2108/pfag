"""
Contract Test: PDFフィールド書き込みAPI (OpenAPI準拠)
T013: POST /pdf/write-fields
"""
import pytest
from fastapi.testclient import TestClient
from src.pfag.api.main import app

client = TestClient(app)

def test_write_fields_contract():
    # サンプルPDFとフィールド情報（JSON）
    payload = {
        "pdf_id": "sample.pdf",
        "fields": [
            {
                "name": "field_p1_t1",
                "type": "Tx",
                "page": 1,
                "rect": [100, 700, 200, 720],
                "options": {"value": "テスト"}
            }
        ]
    }
    response = client.post("/pdf/write-fields", json=payload)
    # 仕様通り: 200でPDFバイナリ返却
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content[:4] == b"%PDF"  # PDFヘッダ
