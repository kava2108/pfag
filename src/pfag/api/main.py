from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging


from pfag.api.pdf import router as pdf_router

app = FastAPI()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pfag.api")

# PDF APIルーターを組み込む
app.include_router(pdf_router)

@app.get("/health", response_class=JSONResponse)
def health():
    logger.info("/health accessed")
    return {"status": "ok"}

# エラー時のハンドリング例（起動時依存不足など）
@app.on_event("startup")
def startup_event():
    try:
        logger.info("API server startup")
        # 依存チェックや初期化処理（必要なら）
    except Exception as e:
        logger.error(f"Startup error: {e}")
        raise
