# PDFレンダリングAPI ドキュメント

## 概要
- HTML→PDF変換、プレビュー、履歴取得APIを提供
- FastAPI + WeasyPrint/PyPDF2

## エンドポイント一覧

### 1. POST /pdf
- HTMLデータをPDFに変換し返却
- リクエスト: { "html": "<h1>見出し</h1>" }
- レスポンス: application/pdf

### 2. GET /pdf/preview?id=ファイル名
- 指定IDのPDFを直接返却
- レスポンス: application/pdf
- 404: ファイルが存在しない場合

### 3. GET /pdf/history
- 生成済みPDFの履歴一覧をJSONで返却
- レスポンス例:
```
[
  {"id": "pdf_xxx.pdf", "created_at": "2026-02-14T12:34:56", "filename": "pdf_xxx.pdf"},
  ...
]
```

## 使い方例
- HTMLをPOST → PDFダウンロード
- 生成IDでプレビュー
- 履歴一覧取得

## 注意事項
- PDF一時保存先: システムの一時ディレクトリ配下
- 履歴はサーバー再起動で消える場合あり
- 大量生成時はストレージ容量に注意
