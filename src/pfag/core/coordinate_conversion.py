from typing import Tuple
import logging
import numpy as np

class CoordinateConversionError(ValueError):
    pass

logger = logging.getLogger("pfag.coordinate_conversion")

def convert_coordinates(x_img: int, y_img: int, img_w: int, img_h: int, pdf_w: float, pdf_h: float) -> Tuple[float, float]:
    logger.debug(f"入力値: x_img={x_img}, y_img={y_img}, img_w={img_w}, img_h={img_h}, pdf_w={pdf_w}, pdf_h={pdf_h}")
    # 入力値バリデーション
    if img_w <= 0 or img_h <= 0 or pdf_w <= 0 or pdf_h <= 0:
        logger.error("画像・PDFサイズは0より大きい値で指定してください")
        raise CoordinateConversionError("画像・PDFサイズは0より大きい値で指定してください")
    if not (0 <= x_img < img_w) or not (0 <= y_img < img_h):
        logger.error("画像座標は画像範囲内で指定してください")
        raise CoordinateConversionError("画像座標は画像範囲内で指定してください")
    # アスペクト比差異チェック
    aspect_img = img_w / img_h
    aspect_pdf = pdf_w / pdf_h
    aspect_diff = abs(aspect_img - aspect_pdf)
    if aspect_diff > 0.2:  # 差異が大きい場合は警告
        logger.warning(f"アスペクト比差異が大きい: 画像={aspect_img:.2f}, PDF={aspect_pdf:.2f}")
    # X座標変換
    x_pdf = x_img * (pdf_w / img_w)
    # Y座標変換（PDFは左下原点、画像は左上原点）
    y_pdf = pdf_h - (y_img * (pdf_h / img_h))
    logger.info(f"変換結果: x_pdf={x_pdf}, y_pdf={y_pdf}")
    return x_pdf, y_pdf

def calculate_error_margin(x_img: int, y_img: int, img_w: int, img_h: int, pdf_w: float, pdf_h: float) -> Tuple[float, float]:
    x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
    expected_x = x_img * (pdf_w / img_w)
    expected_y = pdf_h - (y_img * (pdf_h / img_h))
    error_x = np.abs(x_pdf - expected_x)
    error_y = np.abs(y_pdf - expected_y)
    return error_x, error_y
