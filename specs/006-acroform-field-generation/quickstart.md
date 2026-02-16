# Quickstart: AcroFormフィールド生成

1. 必要パッケージをインストール
   ```sh
   pip install fastapi uvicorn PyPDF2 WeasyPrint Pillow numpy
   ```

2. APIサーバ起動
   ```sh
   uvicorn src.pfag.api.main:app --reload
   ```

3. フィールド追加APIの呼び出し例
   ```sh
   curl -X POST \
     -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{
       "pdf": "<base64-pdf>",
       "fields": [
         {"name": "field_p1_Tx1", "type": "Tx", "page": 1, "rect": [100, 200, 120, 20]},
         {"name": "field_p1_Btn1", "type": "Btn", "page": 1, "rect": [300, 400, 15, 15]}
       ]
     }' \
     http://localhost:8000/v1/acroform/fields -o out.pdf
   ```

4. 生成PDFをAcrobat/Chrome/Edgeで開き、フォーム入力・保存を確認

5. CLIやコアロジックの利用はsrc/pfag/cli, src/pfag/core参照
