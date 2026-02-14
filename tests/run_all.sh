#!/bin/bash
# サンプル画像・PDF生成＋全テスト自動実行スクリプト
set -e

# サンプル素材生成
python tests/sample/generate_checkbox_images.py

# 単体・コントラクトテスト実行
pytest tests/unit --maxfail=1 --disable-warnings -v
pytest tests/contract --maxfail=1 --disable-warnings -v

echo "全テスト・サンプル生成が完了しました。"
