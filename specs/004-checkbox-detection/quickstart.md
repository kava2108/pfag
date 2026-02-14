# Quickstart: チェックボックス検出

## 1. サンプル画像生成
```
python -m tests.sample.generate_checkbox_images
```

## 2. CLI実行例
```
python -m pfag.cli.checkbox_detect --file sample.png --output result.json --min_size 15 --max_size 50 --fill_threshold 0.5
```

## 3. APIサーバ起動例
```
uvicorn pfag.api.checkbox:app --reload
```

## 4. APIリクエスト例
```
curl -F "file=@sample.png" http://localhost:8000/checkbox/detect
```

## 注意事項
- 入力画像は1200x1200px以内を推奨
- パラメータ（min_size, max_size, fill_threshold）は用途に応じて調整
- ノイズ・非矩形は自動除外
