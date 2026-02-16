# Data Model: Agent Skills連携機能

## SkillSchema
- skill_name: str
- input_schema: dict (JSON Schema)
- output_schema: dict (JSON Schema)
- description: str
- version: str

## SkillWrapper
- schema: SkillSchema
- endpoint_url: str
- method: str (GET/POST/PUT...)
- headers: dict
- timeout: float
- retry_policy: dict

## SensitivityParam
- param_name: str
- value: float/int
- min_value: float/int
- max_value: float/int
- default: float/int
- description: str

## WarningMessage
- code: str
- message: str
- detail: str
- lang: str (default: 'ja')

---

- SkillSchemaはPydanticモデルで実装、input/outputはJSON Schema互換
- SkillWrapperはAPI呼び出しのラッパ、バリデーション・例外処理・リトライ含む
- SensitivityParamはスキルごとに可変、バリデーション必須
- WarningMessageは多言語対応可能な構造
