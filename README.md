# PFAG FastAPI APIサーバー Quickstart

## 必要条件
- Python 3.8以上
- pipで依存パッケージインストール可能

## セットアップ手順

1. 依存パッケージのインストール
   ```sh
   pip install -r requirements.txt
   ```
2. サーバー起動
   ```sh
   uvicorn src.pfag.api.main:app --reload
   ```
3. 疎通確認
   - ブラウザまたはcurlで http://localhost:8000/health にアクセス
   - `{ "status": "ok" }` が返れば成功

## トラブルシューティング
- ポート競合: `uvicorn`起動時にエラーが出た場合、`--port`オプションで空きポートを指定
- 依存不足: `ModuleNotFoundError`等が出た場合、`pip install -r requirements.txt`を再実行

## 開発Tips
- APIドキュメント: http://localhost:8000/docs
- テスト: `pytest`で自動化（tests/contract, tests/integration）
