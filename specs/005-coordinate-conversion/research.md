# Research: 座標変換（画像座標 → PDF座標）

## Decision: 誤差許容範囲 ±2pt
- Rationale: DPI換算・丸め誤差を考慮し、帳票実務上の許容範囲（約±0.7mm）と整合するため。
- Alternatives considered: ±1pt（精度は高いが現実的でない）、±5pt（実務上許容できない）

## Decision: 変換式
- X座標: `X_pdf = X_img * (Width_pdf / Width_img)`
- Y座標: `Y_pdf = Height_pdf - (Y_img * (Height_pdf / Height_img))`
- Rationale: PDF座標系は左下原点、画像座標系は左上原点のためY軸変換に符号反転が必要。
- Alternatives considered: Y座標をそのまま変換（誤差大きい）

## Best Practices: Pythonでの座標変換
- PILやPyPDF2で画像・PDFサイズ取得
- numpyで座標計算
- 単体テストはpytest

## Patterns: アスペクト比差異検証
- 画像とPDFのアスペクト比を比較し、差異が大きい場合は警告・誤差計測

## その他
- 入力値バリデーション（サイズ0や範囲外座標）
- 許容誤差をテストで検証

