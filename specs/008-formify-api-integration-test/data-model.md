# data-model.md: formify API integration test

## Entity: formifyリクエスト
- file: PDFバイナリ (multipart/form-data, required)
- options: JSON文字列 (Form field, optional)
  - detection_mode: str (default: "default")
  - sensitivity: float (default: 0.5)
  - output_prefix: str (default: "formified_")

## Entity: formifyレスポンス
- content: PDFバイナリ (application/pdf)
- headers:
  - X-PFAG-Warning: str (optional, 検出0件時のみ)
- status_code: int (200, 422, 500)
- error: str (422/500時のみ)

## Validation Rules
- fileは必須、空不可
- optionsはJSONとしてパース可能であること
- detection_mode, sensitivity, output_prefixは省略可
- 不正なfile/optionsは422エラー
- サーバ内部例外は500エラー

## State Transitions
- リクエスト受信 → バリデーションOK → PDFバイナリ返却（200）
- リクエスト受信 → バリデーションNG → 422エラー
- リクエスト受信 → サーバ例外 → 500エラー
- 検出0件時のみX-PFAG-Warningヘッダ付与
