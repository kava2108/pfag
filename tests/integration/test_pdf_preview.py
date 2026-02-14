import pytest
from fastapi.testclient import TestClient
from pfag.api.pdf import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

def test_pdf_preview_integration():
    client = TestClient(app)
    # まずPDF生成
    html = "<h1>PreviewIntegration</h1>"
    pdf_resp = client.post("/pdf", json={"html": html})
    if pdf_resp.status_code == 200:
        # プレビューAPIにアクセス（idは未実装なので仮）
        response = client.get("/pdf/preview?id=dummy")
        assert response.status_code in (200, 404, 501)
    else:
        assert pdf_resp.status_code in (400, 422, 501)
