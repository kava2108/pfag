# quickstart.md: formify API integration test

## 概要
formify APIの統合テストは、pytest+FastAPI TestClientで自動化されています。

## 前提
- Python 3.12
- FastAPI, pytest, python-multipart インストール済み
- src/pfag/api/formify.py 実装済み

## 実行手順
1. 仮想環境を有効化
   ```sh
   source .venv/bin/activate
   ```
2. テスト実行
   ```sh
   pytest tests/integration/test_formify.py
   ```

## 期待される結果
- すべてのテストがパスすること
- 主要な異常系（422, 500）も網羅
- X-PFAG-Warningヘッダの有無も検証

## 参考
- [OpenAPI仕様](./contracts/openapi.yaml)
- [データモデル](./data-model.md)
- [仕様書](./spec.md)
