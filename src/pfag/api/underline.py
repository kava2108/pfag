# 下線検出APIエンドポイント設計（スケルトン）


from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List
import tempfile
import shutil
import logging
from pfag.core.underline_detection import UnderlineDetectionService


app = FastAPI()
service = UnderlineDetectionService()
logging.basicConfig(level=logging.INFO)

@app.post("/underline/detect")
def detect_underlines(
    file: UploadFile = File(...),
    min_line_width: int = Form(30),
    line_gap_threshold: int = Form(5),
    thickness: int = Form(2),
    min_length: int = Form(50)
):
    """
    画像またはPDFから下線を検出するAPI
    """
    # 一時ファイルに保存
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        # サービス呼び出し
        underlines = service.detect_underlines(
            tmp_path,
            min_line_width=min_line_width,
            line_gap_threshold=line_gap_threshold,
            min_thickness=thickness,
            min_length=min_length
        )
        return {"underlines": underlines}
    except Exception as e:
        logging.error(f"/underline/detect error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/underline/preview")
def preview_underlines(
    file: UploadFile = File(...),
    min_line_width: int = Form(30),
    line_gap_threshold: int = Form(5),
    thickness: int = Form(2),
    min_length: int = Form(50)
):
    """
    下線検出結果付きプレビュー画像を返すAPI
    """
    import fastapi
    import os
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        underlines = service.detect_underlines(
            tmp_path,
            min_line_width=min_line_width,
            line_gap_threshold=line_gap_threshold,
            min_thickness=thickness,
            min_length=min_length
        )
        out_path = service.draw_underlines_on_image(tmp_path, underlines)
        from fastapi.responses import FileResponse
        response = FileResponse(out_path, media_type="image/png")
        return response
    except Exception as e:
        logging.error(f"/underline/preview error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
