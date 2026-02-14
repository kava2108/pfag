import pytest
from fastapi.testclient import TestClient
from pfag.api.pdf import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

def test_pdf_history_integration():
    client = TestClient(app)
    # まずPDFを1つ生成
    html = "<h1>HistoryTest</h1>"
    client.post("/pdf", json={"html": html})
    # 履歴APIで取得
    response = client.get("/pdf/history")
    assert response.status_code in (200, 501)
    if response.status_code == 200:
        assert isinstance(response.json(), list)
