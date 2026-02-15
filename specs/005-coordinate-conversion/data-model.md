# Data Model: 座標変換（画像座標 → PDF座標）

## Entities

### 画像サイズ
- width_px: int
- height_px: int

### PDFサイズ
- width_pt: float
- height_pt: float

### 座標
- X_img: int
- Y_img: int
- X_pdf: float
- Y_pdf: float

### 変換誤差
- error_x: float
- error_y: float

## Relationships
- 画像サイズ・PDFサイズは座標変換時に参照される
- 座標変換結果と期待値との差が変換誤差として記録される

## Validation Rules
- width_px, height_px, width_pt, height_pt > 0
- X_img, Y_img は画像範囲内
- 誤差許容範囲: error_x, error_y ≤ 2pt

## State Transitions
- 入力 → 変換 → 結果 → 誤差検証

