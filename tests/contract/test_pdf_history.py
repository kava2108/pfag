import pytest
from fastapi.testclient import TestClient
from pfag.api.pdf import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

def test_pdf_history_contract():
    client = TestClient(app)
    response = client.get("/pdf/history")
    assert response.status_code in (200, 501)
    if response.status_code == 200:
        assert response.headers["content-type"].startswith("application/json")
