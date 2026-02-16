from typing import Any, Dict, Optional
from .schema import SkillSchema
from .sensitivity import SensitivityParam
from .warning import WarningMessage

class SkillWrapper:
    # NOTE: 実運用時はAPI呼び出し部分でタイムアウト・リトライ・認証等のセキュリティ対策を追加すること。
    """スキル呼び出しラッパークラス"""
    def __init__(self, schema: SkillSchema, endpoint_url: str, method: str = 'POST', headers: Optional[Dict[str, str]] = None, timeout: float = 10.0, retry_policy: Optional[Dict[str, Any]] = None) -> None:
        self.schema: SkillSchema = schema
        self.endpoint_url: str = endpoint_url
        self.method: str = method
        self.headers: Dict[str, str] = headers or {}
        self.timeout: float = timeout
        self.retry_policy: Dict[str, Any] = retry_policy or {}

    def call(self, input_data: Dict[str, Any], sensitivity: Optional[SensitivityParam] = None) -> Dict[str, Any]:
        """スキル呼び出し（バリデーション・エコー実装）"""
        try:
            SkillSchema.validate_schema(self.schema.dict())
        except Exception as e:
            raise ValueError(f"Skill schema invalid: {e}")

        if not isinstance(input_data, dict):
            raise ValueError("input_data must be dict")
        if self.schema.skill_name == "echo":
            text = input_data.get("text", "")
            return {"result": text, "warnings": []}
        raise NotImplementedError(f"Skill '{self.schema.skill_name}' is not implemented.")
