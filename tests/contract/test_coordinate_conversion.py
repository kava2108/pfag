import pytest
from fastapi.testclient import TestClient
from pfag.api.coordinate import app

def test_coordinate_convert_contract():
    client = TestClient(app)
    payload = {
        "x_img": 100,
        "y_img": 200,
        "img_width": 1200,
        "img_height": 900,
        "pdf_width": 595.0,
        "pdf_height": 842.0
    }
    response = client.post("/coordinate-convert", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "x_pdf" in data
    assert "y_pdf" in data
    assert abs(data["x_pdf"] - (100 * (595.0 / 1200))) <= 2.0
    assert abs(data["y_pdf"] - (842.0 - (200 * (842.0 / 900)))) <= 2.0
