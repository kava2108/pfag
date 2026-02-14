@router.get("/pdf/history")
def pdf_history():
	try:
		history = pdf_service.get_history()
		return history
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"履歴取得失敗: {str(e)}")
# PDF API endpoints (routing base)
from fastapi import APIRouter, FastAPI

router = APIRouter()


# 共通エラーハンドリング例
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

@router.get("/pdf/health")
def pdf_health():
	return {"status": "ok"}

@router.exception_handler(HTTPException)
async def pdf_http_exception_handler(request: Request, exc: HTTPException):
	return JSONResponse(
		status_code=exc.status_code,
		content={"detail": exc.detail, "pdf_api": True},
	)

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
from typing import Dict

pdf_service = PDFService()

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
