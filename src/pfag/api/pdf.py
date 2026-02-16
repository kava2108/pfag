from fastapi import APIRouter, FastAPI, Response
router = APIRouter()

@router.get("/pdf/history")
def pdf_history():
	try:
		history = pdf_service.get_history()
		return history
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"履歴取得失敗: {str(e)}")


# 共通エラーハンドリング例
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

@router.get("/pdf/health")
def pdf_health():
	return {"status": "ok"}

from fastapi import Query

@router.get("/pdf/preview", response_class=Response)
def pdf_preview(id: str = Query(..., description="PDFファイルID/ファイル名")):
    try:
        pdf_path = pdf_service.get_pdf_file(id)
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        return Response(content=pdf_bytes, media_type="application/pdf")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="PDFが見つかりません")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDFプレビュー失敗: {str(e)}")

from fastapi import Body, Response, status, HTTPException
from pfag.core.pdf_service import PDFService
from pfag.core.acroform_field_writer import AcroformFieldWriter
from typing import Dict, List

pdf_service = PDFService()

# --- 新規追加: PDFフィールド書き込みAPI ---
@router.post("/pdf/write-fields", response_class=Response, status_code=200)
def write_fields_endpoint(payload: Dict = Body(...)):
	"""
	既存PDFにAcroFormフィールドを書き込む（スケルトン）
	"""
	pdf_id = payload.get("pdf_id")
	fields = payload.get("fields")
	# 入力バリデーション（簡易）
	if not pdf_id or not isinstance(fields, list):
		raise HTTPException(status_code=400, detail="pdf_idまたはfieldsが不正です")
	try:
		# PDFファイル取得
		pdf_path = pdf_service.get_pdf_file(pdf_id)
		with open(pdf_path, "rb") as f:
			pdf_bytes = f.read()
		# AcroFormフィールド埋め込み（現状は未実装）
		result_bytes = AcroformFieldWriter.write_fields(pdf_bytes, fields)
		return Response(content=result_bytes, media_type="application/pdf")
	except FileNotFoundError:
		raise HTTPException(status_code=404, detail="PDFが見つかりません")
	except Exception as e:
		import traceback, logging
		logging.error(f"PDFフィールド書き込み失敗: {e}\n{traceback.format_exc()}")
		raise HTTPException(status_code=500, detail=f"PDFフィールド書き込み失敗: {str(e)}\n{traceback.format_exc()}")

@router.post("/pdf", response_class=Response, status_code=200)
def html_to_pdf_endpoint(payload: Dict = Body(...)):
	html = payload.get("html")
	if not isinstance(html, str) or not html.strip():
		raise HTTPException(status_code=400, detail="HTMLデータが空です")
	try:
		pdf_path = pdf_service.html_to_pdf(html)
		with open(pdf_path, "rb") as f:
			pdf_bytes = f.read()
		return Response(content=pdf_bytes, media_type="application/pdf")
	except ValueError as ve:
		raise HTTPException(status_code=400, detail=str(ve))
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"PDF生成失敗: {str(e)}")

from fastapi.responses import JSONResponse

@router.post("/pdf/cleanup", response_class=JSONResponse, status_code=200)
def cleanup_tmp_files_endpoint():
	try:
		removed = pdf_service.cleanup_tmp_files(days=1)
		return JSONResponse({"removed": removed})
	except Exception as e:
		import traceback, logging
		logging.error(f"一時ファイル削除失敗: {e}\n{traceback.format_exc()}")
		raise HTTPException(status_code=500, detail=f"一時ファイル削除失敗: {str(e)}\n{traceback.format_exc()}")
