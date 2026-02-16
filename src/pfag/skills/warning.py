from pydantic import BaseModel, Field


class WarningMessage(BaseModel):
    # NOTE: 警告リストは本番ではDBや外部サービス管理推奨。現状はメモリ保持。
    """警告メッセージモデル"""
    code: str = Field(..., description="警告コード")
    message: str = Field(..., description="警告メッセージ")
    description: str = Field(..., description="説明")
    lang: str = Field('ja', description="言語（デフォルト: ja）")


_WARNINGS = [
    WarningMessage(
        code="W001",
        message="サンプル警告",
        description="これはサンプルの警告説明です。"
    )
]

def get_all_warnings():
    return [w.dict() for w in _WARNINGS]

def add_warning(warning: WarningMessage):
    _WARNINGS.append(warning)

def find_warning_by_code(code: str):
    for w in _WARNINGS:
        if w.code == code:
            return w.dict()
    return None
