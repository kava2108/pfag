# quickstart.md

## 前提
- Python 3.8以上
- pipで依存パッケージインストール可能

## セットアップ手順

1. 依存パッケージのインストール
   ```sh
   pip install fastapi uvicorn
   ```
2. サーバー起動
   ```sh
   uvicorn src.pfag.api.main:app --reload
   ```
3. 疎通確認
   - ブラウザまたはcurlで http://localhost:8000/health にアクセス
   - `{ "status": "ok" }` が返れば成功

## 開発Tips
- APIドキュメント: http://localhost:8000/docs
- ポート変更: `--port 8080` などuvicorn引数で指定可
- テスト: pytestで自動化予定（Phase 1以降）
