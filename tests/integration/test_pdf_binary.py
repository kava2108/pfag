"""
Integration Test: バイナリ返却API
T023: バイナリ返却の統合テスト
"""
import pytest
from fastapi.testclient import TestClient
from src.pfag.api.main import app
import shutil
import os

client = TestClient(app)

def setup_module(module):
    # サンプルPDFを一時ディレクトリにコピー
    tmp_dir = "/tmp/pfag_pdf"
    os.makedirs(tmp_dir, exist_ok=True)
    shutil.copyfile("tests/sample/sample.pdf", os.path.join(tmp_dir, "sample.pdf"))

def test_pdf_binary_integration():
    payload = {
        "pdf_id": "sample.pdf",
        "fields": [
            {
                "name": "field_p1_t1",
                "type": "Tx",
                "page": 1,
                "rect": [100, 700, 200, 720],
                "options": {"value": "integration-binary"}
            }
        ]
    }
    response = client.post("/pdf/write-fields", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content[:4] == b"%PDF"
    # バイナリ長・ダウンロード可能性
    assert len(response.content) > 100
    # 実際にファイルとして保存し、PyPDF2で開けるか
    from PyPDF2 import PdfReader
    import io
    reader = PdfReader(io.BytesIO(response.content))
    assert len(reader.pages) == 1
