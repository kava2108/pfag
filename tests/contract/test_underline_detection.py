import os
import pytest
from fastapi.testclient import TestClient
from pfag.api.underline import app

# サンプル画像生成（水平線のみ）
def create_sample_image(path, width=200, height=100, line_y=50):
    import cv2
    import numpy as np
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.line(img, (10, line_y), (width-10, line_y), (0,0,0), 2)
    cv2.imwrite(path, img)

@pytest.fixture
def sample_image(tmp_path):
    img_path = tmp_path / "sample.png"
    create_sample_image(str(img_path))
    return str(img_path)

def test_api_detect_underlines(sample_image):
    client = TestClient(app)
    with open(sample_image, "rb") as f:
        response = client.post(
            "/underline/detect",
            files={"file": ("sample.png", f, "image/png")},
            data={"min_line_width": 30, "line_gap_threshold": 5, "thickness": 2, "min_length": 50}
        )
    assert response.status_code == 200
    data = response.json()
    assert "underlines" in data
    assert isinstance(data["underlines"], list)
    assert len(data["underlines"]) >= 1

def test_api_preview_underlines(sample_image):
    client = TestClient(app)
    with open(sample_image, "rb") as f:
        response = client.post(
            "/underline/preview",
            files={"file": ("sample.png", f, "image/png")},
            data={"min_line_width": 30, "line_gap_threshold": 5, "thickness": 2, "min_length": 50}
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/png")
    assert len(response.content) > 100
