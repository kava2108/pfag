import sys
sys.path.insert(0, './src')
import pytest
from src.pfag.core.coordinate_conversion import convert_coordinates, calculate_error_margin

def test_coordinate_conversion_basic():
    # 画像サイズ: 1200x900px, PDFサイズ: 595x842pt (A4)
    x_img, y_img = 100, 200
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 595.0, 842.0
    x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    # 許容誤差±2pt
    assert abs(x_pdf - (100 * (595.0 / 1200))) <= 2.0
    assert abs(y_pdf - (842.0 - (200 * (842.0 / 900)))) <= 2.0

def test_coordinate_conversion_aspect_ratio():
    # アスペクト比差異ケース
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 600.0, 800.0
    x_img, y_img = 600, 450
    x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    assert abs(x_pdf - (600 * (600.0 / 1200))) <= 2.0
    assert abs(y_pdf - (800.0 - (450 * (800.0 / 900)))) <= 2.0

def test_aspect_ratio_warning():
    # アスペクト比差異が大きい場合の警告（ロジック追加予定）
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 1200.0, 600.0  # アスペクト比大きく異なる
    x_img, y_img = 100, 100
    x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    # アスペクト比差異が大きい場合、警告が出ること（実装後にassert追加）

def test_coordinate_conversion_zero_size():
    # サイズ0の場合は例外
    with pytest.raises(ValueError):
        convert_coordinates(10, 10, 0, 900, 595.0, 842.0)
    with pytest.raises(ValueError):
        convert_coordinates(10, 10, 1200, 0, 595.0, 842.0)
    with pytest.raises(ValueError):
        convert_coordinates(10, 10, 1200, 900, 0, 842.0)
    with pytest.raises(ValueError):
        convert_coordinates(10, 10, 1200, 900, 595.0, 0)

def test_calculate_error_margin():
    # 誤差計算の基本ケース
    x_img, y_img = 100, 200
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 595.0, 842.0
    error_x, error_y = calculate_error_margin(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    assert error_x <= 2.0
    assert error_y <= 2.0
    # アスペクト比差異ケース
    x_img, y_img = 600, 450
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 600.0, 800.0
    error_x, error_y = calculate_error_margin(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    assert error_x <= 2.0
    assert error_y <= 2.0
    # アスペクト比差異ケース
    x_img, y_img = 600, 450
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 600.0, 800.0
    error_x, error_y = calculate_error_margin(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    assert error_x <= 2.0
    assert error_y <= 2.0
    # y_imgが範囲外
    with pytest.raises(ValueError):
        convert_coordinates(100, 901, img_w, img_h, pdf_w, pdf_h)

def test_conversion_error_margin():
    # 許容誤差±2pt内で変換されること
    img_w, img_h = 1200, 900
    pdf_w, pdf_h = 595.0, 842.0
    x_img, y_img = 100, 200
    x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    expected_x = x_img * (pdf_w / img_w)
    expected_y = pdf_h - (y_img * (pdf_h / img_h))
    error_x = abs(x_pdf - expected_x)
    error_y = abs(y_pdf - expected_y)
    assert error_x <= 2.0
    assert error_y <= 2.0
