# Quickstart: 下線検出（テキストフィールド）

## 概要
- 画像またはPDFから水平下線（テキストフィールド用）を自動検出
- パラメータ調整・バウンディングボックス・プレビュー画像出力対応

## 使い方

### 1. 必要パッケージのインストール
```
pip install opencv-python numpy pymupdf pillow
```


### 2. CLI実行例
```
python -m pfag.cli.underline_detect --file tests/sample/horizontal.png --output result.json --preview preview.png
```
--output: 検出結果（JSON）出力先
--preview: 下線付き画像出力先


### 3. APIサーバ起動例（FastAPI）
```
uvicorn pfag.api.underline:app --reload
```


### 4. APIリクエスト例
- /underline/detect: 画像/PDFをPOSTし、下線リスト（JSON）を取得
- /underline/preview: 画像/PDFをPOSTし、下線付きプレビュー画像（PNG）を取得

#### curl例
```
curl -F "file=@tests/sample/horizontal.png" http://localhost:8000/underline/detect
curl -F "file=@tests/sample/horizontal.png" http://localhost:8000/underline/preview --output preview.png
```

## テスト
```
pytest tests/unit/test_underline_detection.py
```

## 注意事項
- 入力画像は1000x1000px以内を推奨
- パラメータは仕様デフォルト値（min_line_width=30, line_gap_threshold=5, thickness=2, min_length=50）
- ノイズ・不要線抑制のため、最小幅・長さ・太さ閾値あり
