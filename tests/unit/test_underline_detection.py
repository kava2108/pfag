import os
import pytest
from pfag.core.underline_detection import UnderlineDetectionService

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

def test_detect_underlines_basic(sample_image):
    service = UnderlineDetectionService()
    underlines = service.detect_underlines(sample_image)
    assert len(underlines) >= 1
    u = underlines[0]
    assert abs(u["start_y"] - u["end_y"]) <= 2
    assert u["width"] >= 30

def test_generate_bounding_boxes(sample_image):
    service = UnderlineDetectionService()
    underlines = service.detect_underlines(sample_image)
    boxes = service.generate_bounding_boxes(underlines)
    assert len(boxes) == len(underlines)
    for b in boxes:
        assert b["width"] > 0
        assert b["height"] == 20

def test_apply_field_layout(sample_image):
    service = UnderlineDetectionService()
    underlines = service.detect_underlines(sample_image)
    boxes = service.generate_bounding_boxes(underlines)
    layout = {"height": 25, "offset": 10, "inset": 5}
    result = service.apply_field_layout(boxes, layout)
    for b in result:
        assert b["height"] == 25
        assert b["width"] >= 0
