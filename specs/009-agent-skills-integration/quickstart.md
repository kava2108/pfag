# Quickstart: Agent Skills連携機能

## 1. スキルスキーマの定義

```python
from pfag.skills.schema import SkillSchema

schema = SkillSchema(
    skill_name="ocr_text_extraction",
    input_schema={...},
    output_schema={...},
    description="OCRテキスト抽出スキル",
    version="1.0.0"
)
```

## 2. スキルAPIラッパの利用

```python
from pfag.skills.wrapper import SkillWrapper

wrapper = SkillWrapper(schema=schema, endpoint_url="https://api.example.com/ocr", method="POST")
result = wrapper.call(input_data={...})
```

## 3. 感度調整パラメータの設定

```python
from pfag.skills.sensitivity import SensitivityParam

param = SensitivityParam(param_name="threshold", value=0.8, min_value=0.0, max_value=1.0, default=0.5)
```

## 4. 警告メッセージの利用

```python
from pfag.skills.warning import WarningMessage

warn = WarningMessage(code="INVALID_INPUT", message="入力データが不正です", detail="JSONスキーマに違反", lang="ja")
```
