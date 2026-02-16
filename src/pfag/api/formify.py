from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse
from typing import Optional
import json
from pfag.core.pdf_service import PDFService
import logging

router = APIRouter()
pdf_service = PDFService()

@router.post("/v1/formify", response_class=Response)
async def formify(
    file: UploadFile = File(...),
    options: Optional[str] = Form(None),
    request: Request = None
):
    """
    PDFフォーム化API: multipart/form-dataでPDFファイルとオプションJSONを受け取る
    """
    try:
        # ファイル受信
        pdf_bytes = await file.read()
        if not pdf_bytes:
            raise HTTPException(status_code=422, detail="ファイルが空です")
        # optionsパース
        opts = {}
        if options:
            try:
                opts = json.loads(options)
            except Exception:
                raise HTTPException(status_code=422, detail="options JSONのパースに失敗")
        detection_mode = opts.get("detection_mode", "default")
        sensitivity = opts.get("sensitivity", 0.5)
        output_prefix = opts.get("output_prefix", "formified_")
        # --- 検出処理（ダミー: 0件検出時の例） ---
        detected = []  # TODO: 実装
        if not detected:
            headers = {"X-PFAG-Warning": "No fields detected"}
            return Response(content=pdf_bytes, media_type="application/pdf", headers=headers)
        # --- 通常レスポンス ---
        return Response(content=pdf_bytes, media_type="application/pdf")
    except HTTPException as he:
        raise he
    except Exception as e:
        logging.error(f"formify error: {e}")
        raise HTTPException(status_code=500, detail="サーバ内部エラー")
