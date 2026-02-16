# Data Model: PDF出力処理

## Entity: PDFファイル
- 属性: ファイルパス, バイナリデータ, 一時ファイルフラグ

## Entity: AcroFormフィールド情報
- 属性: name, type (Tx/Btn), page, rect, options (JSON)
- 例: { "name": "field_p1_t1", "type": "Tx", "page": 1, "rect": [x1, y1, x2, y2], "options": { ... } }

## 関連
- 1つのPDFファイルに複数のAcroFormフィールド情報が紐づく

## バリデーション
- フィールド名は一意
- rectはPDF座標系で正規化済み
- typeはTxまたはBtnのみ許容

## 状態遷移
- 入力: PDF + フィールド情報(JSON)
- 変換: PDFへフィールド埋め込み
- 出力: バイナリPDF返却
