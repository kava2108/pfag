# PDFレンダリングAPI クイックスタート

## セットアップ

1. 依存パッケージをインストール
   ```sh
   pip install -r requirements.txt
   ```
2. サーバ起動例（main.py等でFastAPI appにrouterをinclude）
   ```python
   from fastapi import FastAPI
   from pfag.api.pdf import router as pdf_router
   app = FastAPI()
   app.include_router(pdf_router)
   ```
   ```sh
   uvicorn main:app --reload
   ```

## API利用例

### 1. HTML→PDF変換
```sh
curl -X POST http://localhost:8000/pdf -H "Content-Type: application/json" -d '{"html": "<h1>Hello</h1>"}' --output out.pdf
```

### 2. PDFプレビュー
```sh
curl -X GET "http://localhost:8000/pdf/preview?id=pdf_xxx.pdf" --output preview.pdf
```

### 3. PDF履歴取得
```sh
curl -X GET http://localhost:8000/pdf/history
```

## 注意
- PDF一時保存先はシステムの一時ディレクトリ
- 履歴はサーバー再起動で消える場合あり
