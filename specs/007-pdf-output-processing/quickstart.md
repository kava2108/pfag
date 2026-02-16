# Quickstart: PDF出力処理

## 必要条件
- Python 3.8+
- pip install -r requirements.txt


## サンプルAPIリクエスト
### フィールド書き込み（バイナリ返却）
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"pdf_id": "sample.pdf", "fields": [{"name": "field_p1_t1", "type": "Tx", "page": 1, "rect": [100,700,200,720]}]}' \
  http://localhost:8000/pdf/write-fields --output result.pdf
```

### 一時ファイル削除API
```bash
curl -X POST http://localhost:8000/pdf/cleanup
```


## テスト実行
```bash
# 全テスト一括実行
pytest
# 主要テスト個別実行例
pytest tests/contract/test_pdf_field_writer.py
pytest tests/integration/test_pdf_field_writer.py
pytest tests/unit/test_acroform_field_writer.py
pytest tests/integration/test_pdf_service.py
pytest tests/contract/test_pdf_binary.py
pytest tests/integration/test_pdf_binary.py
```


## 注意
- 一時ファイルは自動削除されます（または /pdf/cleanup で明示削除可）
- フィールド情報はJSON形式で指定してください
- バイナリ返却APIはContent-Type: application/pdfで返却されます
