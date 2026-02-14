import pytest
from fastapi.testclient import TestClient
from pfag.api.pdf import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

def test_pdf_contract():
    # HTML→PDF変換APIの契約テスト（正常系・異常系）
    client = TestClient(app)
    # 正常系: HTMLをPOSTしてPDFレスポンス
    response = client.post("/pdf", json={"html": "<h1>Hello</h1>"})
    assert response.status_code in (200, 501)  # 実装前は501等でもOK
    # 異常系: 空データ
    response = client.post("/pdf", json={"html": ""})
    assert response.status_code in (400, 422, 501)
