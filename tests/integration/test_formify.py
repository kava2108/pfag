
import io
import json
import pytest
from fastapi.testclient import TestClient
from pfag.api.main import app

client = TestClient(app)

def test_formify_success():
    # ダミーPDFバイト列
    pdf_bytes = b"%PDF-1.4 dummy pdf file"
    options = {"detection_mode": "test", "sensitivity": 0.9, "output_prefix": "test_"}
    response = client.post(
        "/v1/formify",
        files={"file": ("dummy.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
        data={"options": json.dumps(options)}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content == pdf_bytes

def test_formify_no_file():
    response = client.post("/v1/formify", files={})
    assert response.status_code == 422

def test_formify_invalid_options():
    pdf_bytes = b"%PDF-1.4 dummy pdf file"
    response = client.post(
        "/v1/formify",
        files={"file": ("dummy.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
        data={"options": "not-a-json"}
    )
    assert response.status_code == 422
    assert "options JSONのパースに失敗" in response.text

def test_formify_no_fields_detected():
    pdf_bytes = b"%PDF-1.4 dummy pdf file"
    response = client.post(
        "/v1/formify",
        files={"file": ("dummy.pdf", io.BytesIO(pdf_bytes), "application/pdf")}
    )
    assert response.status_code == 200
    assert response.headers.get("X-PFAG-Warning") == "No fields detected"
