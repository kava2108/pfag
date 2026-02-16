    @classmethod
    def validate_schema(cls, data: dict) -> None:
        """SkillSchemaのバリデーション。エラー時は詳細な説明付きで例外を投げる"""
        try:
            cls(**data)
        except Exception as e:
            # PydanticのValidationErrorなら詳細を返す
            from pydantic import ValidationError
            if isinstance(e, ValidationError):
                details = e.errors()
                msg = f"SkillSchema validation error: {details}"
                raise ValueError(msg)
            raise

    @classmethod
    def explain_error(cls, data: dict) -> str:
        """バリデーションエラーの説明文を返す（エラーがなければ空文字）"""
        try:
            cls(**data)
            return ""
        except Exception as e:
            from pydantic import ValidationError
            if isinstance(e, ValidationError):
                return str(e)
            return str(e)

from pydantic import BaseModel, Field
from typing import Any, Dict, Optional

_SKILL_SCHEMA_STORE: Dict[str, Dict[str, Any]] = {}


class SkillSchema(BaseModel):
    # NOTE: 型明示・バリデーションはpydanticで担保。パフォーマンス最適化はDB保存時に検討。
    """スキルのスキーマ定義モデル"""
    skill_name: str = Field(..., description="スキル名")
    input_schema: Dict[str, Any] = Field(..., description="入力スキーマ(JSON Schema)")
    output_schema: Dict[str, Any] = Field(..., description="出力スキーマ(JSON Schema)")
    description: str = Field(..., description="スキル説明")
    version: str = Field(..., description="スキルバージョン")

    @classmethod
    def save(cls, schema: "SkillSchema") -> None:
        """スキルスキーマを保存（メモリ内）"""
        if schema.skill_name in _SKILL_SCHEMA_STORE:
            raise ValueError(f"Skill '{schema.skill_name}' already exists.")
        _SKILL_SCHEMA_STORE[schema.skill_name] = schema.dict()

    @classmethod
    def get(cls, skill_name: str) -> Optional[Dict[str, Any]]:
        """スキルスキーマを取得"""
        return _SKILL_SCHEMA_STORE.get(skill_name)

    @classmethod
    def all(cls) -> Dict[str, Dict[str, Any]]:
        """全スキルスキーマを取得"""
        return _SKILL_SCHEMA_STORE.copy()
