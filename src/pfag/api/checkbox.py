# チェックボックス検出APIエンドポイント（スケルトン）



from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import tempfile
import logging
from pfag.core.checkbox_detection import CheckboxDetectionService

app = FastAPI()

@app.post("/checkbox/detect")
async def detect_checkbox(file: UploadFile = File(...)):
	if not file.filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
		logging.warning(f"未対応ファイル形式: {file.filename}")
		raise HTTPException(status_code=400, detail="画像ファイルのみ対応")
	try:
		with tempfile.NamedTemporaryFile(delete=True, suffix=".png") as tmp:
			content = await file.read()
			tmp.write(content)
			tmp.flush()
			service = CheckboxDetectionService()
			checkboxes = service.detect_checkboxes(tmp.name)
			json_str = service.to_json(checkboxes)
		return JSONResponse(content=json_str, media_type="application/json")
	except FileNotFoundError as e:
		logging.error(f"ファイル未検出: {e}")
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		logging.exception(f"API検出処理でエラー: {e}")
		raise HTTPException(status_code=500, detail=str(e))
