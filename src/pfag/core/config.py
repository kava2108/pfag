# config.py
# 環境設定用（今後拡張可）

import os

class Config:
    PORT = int(os.getenv("PFAG_PORT", 8000))
    DEBUG = bool(os.getenv("PFAG_DEBUG", True))

config = Config()
