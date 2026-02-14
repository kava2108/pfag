def test_noise_and_non_rect_exclusion(tmp_path):
    import cv2
    import numpy as np
    service = CheckboxDetectionService()
    # ノイズ画像（ランダム）
    noise_img = np.random.randint(0, 256, (100, 200), dtype=np.uint8)
    noise_path = tmp_path / "noise.png"
    cv2.imwrite(str(noise_path), noise_img)
    result = service.detect_checkboxes(str(noise_path))
    assert len(result) == 0  # ノイズは検出されない

    # 非矩形（長方形: 極端な比率）
    img = np.ones((100, 200, 3), dtype=np.uint8) * 255
    cv2.rectangle(img, (10, 10), (180, 30), (0, 0, 0), 2)  # 横長
    rect_path = tmp_path / "long_rect.png"
    cv2.imwrite(str(rect_path), img)
    result = service.detect_checkboxes(str(rect_path))
    assert len(result) == 0  # 極端な比率は除外

    # 非矩形（台形: 角度が直角でない）
    img2 = np.ones((100, 200, 3), dtype=np.uint8) * 255
    pts = np.array([[50,30],[70,30],[75,50],[45,50]], np.int32).reshape((-1,1,2))
    cv2.polylines(img2, [pts], isClosed=True, color=(0,0,0), thickness=2)
    trap_path = tmp_path / "trapezoid.png"
    cv2.imwrite(str(trap_path), img2)
    result = service.detect_checkboxes(str(trap_path))
    assert len(result) == 0  # 直角でない台形も除外
import pytest
from pfag.core.checkbox_detection import CheckboxDetectionService


import pytest
from pfag.core.checkbox_detection import CheckboxDetectionService

@pytest.fixture
def sample_checkbox_image(tmp_path):
    import cv2
    import numpy as np
    img_path = tmp_path / "sample_checkbox.png"
    img = np.ones((100, 200, 3), dtype=np.uint8) * 255
    cv2.rectangle(img, (50, 30), (70, 50), (0, 0, 0), 2)
    cv2.imwrite(str(img_path), img)
    return str(img_path)

def test_detect_checkbox_basic(sample_checkbox_image):
    service = CheckboxDetectionService()
    # 仮: 実装前は空リスト返す
    result = service.detect_checkboxes(sample_checkbox_image)
    assert isinstance(result, list)
    # 実装後: チェックボックスが1つ以上検出されること
    # assert len(result) >= 1

def test_fill_detection(sample_checkbox_image):
    def test_to_json_output(sample_checkbox_image):
        service = CheckboxDetectionService()
        result = service.detect_checkboxes(sample_checkbox_image)
        json_str = service.to_json(result)
        import json
        data = json.loads(json_str)
        assert "checkboxes" in data
        for box in data["checkboxes"]:
            assert set(box.keys()) == {"x", "y", "width", "height", "is_checked"}
            assert isinstance(box["x"], int)
            assert isinstance(box["y"], int)
            assert isinstance(box["width"], int)
            assert isinstance(box["height"], int)
            assert isinstance(box["is_checked"], bool)
    service = CheckboxDetectionService()
    # 仮: 実装前は空リスト返す
    result = service.detect_checkboxes(sample_checkbox_image)
    for box in result:
        assert "is_checked" in box
        assert isinstance(box["is_checked"], bool)
