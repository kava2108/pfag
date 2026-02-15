# Quickstart: 座標変換（画像座標 → PDF座標）

## 概要
画像座標（px）をPDF座標（pt）へ変換するライブラリ・CLIツールの導入・利用方法。

## インストール
```bash
pip install pillow pypdf2 numpy pytest
```

## サンプルコード
```python
from pfag.core.coordinate_conversion import convert_coordinates

# 画像・PDFサイズ
img_w, img_h = 1200, 900
pdf_w, pdf_h = 595.0, 842.0  # A4サイズ（pt）

# 画像座標
x_img, y_img = 100, 200

# 座標変換
x_pdf, y_pdf = convert_coordinates(x_img, y_img, img_w, img_h, pdf_w, pdf_h)
print(f"PDF座標: ({x_pdf}, {y_pdf})")
```

## テスト実行
```bash
pytest tests/unit/test_coordinate_conversion.py
```

## CLI例
```bash
pfag-cli coordinate-convert --x 100 --y 200 --img-width 1200 --img-height 900 --pdf-width 595 --pdf-height 842
```

