# Agent Skills連携との関係

PDFレンダリング機能は、Agent Skills連携の一部スキル（例：PDF解析・変換）として拡張可能。
スキルAPI経由でPDF操作・解析・出力処理を統合できる設計。
# 4. POST /coordinate-convert
- 画像座標→PDF座標変換API
- リクエスト: { "x_img": int, "y_img": int, "img_width": int, "img_height": int, "pdf_width": float, "pdf_height": float }
- レスポンス: { "x_pdf": float, "y_pdf": float, "error_x": float, "error_y": float, "warning": str }

## 使い方例（座標変換）
- CLI: pfag-cli coordinate-convert --x 100 --y 200 --img-width 1200 --img-height 900 --pdf-width 595 --pdf-height 842
- API: POST /coordinate-convert
  {
    "x_img": 100,
    "y_img": 200,
    "img_width": 1200,
    "img_height": 900,
    "pdf_width": 595.0,
    "pdf_height": 842.0
  }
  → { "x_pdf": 49.58, "y_pdf": 654.22, "error_x": 0.00, "error_y": 0.00, "warning": "" }

## 注意事項（座標変換）
- アスペクト比差異が大きい場合は警告（warning）を返す
- 座標変換誤差は±2pt以内
- 入力値バリデーションあり（サイズ0や範囲外座標はエラー）
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
