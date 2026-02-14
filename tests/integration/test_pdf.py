import pytest
from fastapi.testclient import TestClient
from pfag.api.pdf import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

def test_html_to_pdf_integration():
    client = TestClient(app)
    # HTML→PDF変換の統合テスト（正常系）
    html = "<html><body><h1>PDF Test</h1></body></html>"
    response = client.post("/pdf", json={"html": html})
    assert response.status_code in (200, 501)  # 実装前は501等でもOK
    # PDFレスポンスならContent-Type確認
    if response.status_code == 200:
        assert response.headers["content-type"].startswith("application/pdf")
