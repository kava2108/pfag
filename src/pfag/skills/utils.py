# skills/utils.py: エラーハンドリング・ロギング用ユーティリティ
import logging
from loguru import logger

# 共通ロガー
log = logger

# 共通エラーハンドラ例
class SkillError(Exception):
    pass

# 例: エラーをログ出力し例外化
def handle_error(msg: str):
    log.error(msg)
    raise SkillError(msg)
