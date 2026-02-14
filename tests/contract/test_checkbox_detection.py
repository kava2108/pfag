def test_api_noise_exclusion(tmp_path):
    import cv2
    import numpy as np
    client = TestClient(app)
    noise_img = np.random.randint(0, 256, (100, 200), dtype=np.uint8)
    noise_path = tmp_path / "noise.png"
    cv2.imwrite(str(noise_path), noise_img)
    with open(noise_path, "rb") as f:
        response = client.post(
            "/checkbox/detect",
            files={"file": ("noise.png", f, "image/png")},
            data={"min_size": 15, "max_size": 50, "fill_threshold": 0.5}
        )
    assert response.status_code == 200
    data = response.json()
    assert "checkboxes" in data
    assert isinstance(data["checkboxes"], list)
    assert len(data["checkboxes"]) == 0  # ノイズは検出されない

import pytest
from fastapi.testclient import TestClient
from pfag.api.checkbox import app

@pytest.fixture
def sample_checkbox_image(tmp_path):
    import cv2
    import numpy as np
    img_path = tmp_path / "sample_checkbox.png"
    img = np.ones((100, 200, 3), dtype=np.uint8) * 255
    cv2.rectangle(img, (50, 30), (70, 50), (0, 0, 0), 2)
    cv2.imwrite(str(img_path), img)
    return str(img_path)

def test_api_detect_checkboxes(sample_checkbox_image):
    client = TestClient(app)
    with open(sample_checkbox_image, "rb") as f:
        response = client.post(
            "/checkbox/detect",
            files={"file": ("sample_checkbox.png", f, "image/png")},
            data={"min_size": 15, "max_size": 50, "fill_threshold": 0.5}
        )
    assert response.status_code == 200
    data = response.json()
    assert "checkboxes" in data
    assert isinstance(data["checkboxes"], list)
