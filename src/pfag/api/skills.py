# skills APIルーティング構造（FastAPI用）
from fastapi import APIRouter

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from src.pfag.skills.schema import SkillSchema
from src.pfag.skills.wrapper import SkillWrapper
from src.pfag.skills.warning import WarningMessage
_WARNINGS = [
	WarningMessage(
		code="W001",
		message="サンプル警告",
		description="これはサンプルの警告説明です。"
	).dict()
]

@router.get("/warnings")
def get_warnings():
	# 警告説明リストを返す
	return _WARNINGS
router = APIRouter()

# メモリ内ストレージ（本番ではDB等に置換）
_SKILL_SCHEMAS = {}


@router.post("/skills", status_code=status.HTTP_201_CREATED)
def register_skill_schema(schema: SkillSchema):
	# スキル名重複チェック
	if schema.skill_name in _SKILL_SCHEMAS:
		return JSONResponse(status_code=400, content={"detail": "Skill already exists"})
	_SKILL_SCHEMAS[schema.skill_name] = schema.dict()
	return {"message": "Skill schema registered", "skill_name": schema.skill_name}


@router.post("/skills/{skill_name}/call")
def call_skill(skill_name: str, input_data: dict):
	# スキル存在チェック
	schema_dict = _SKILL_SCHEMAS.get(skill_name)
	if not schema_dict:
		return JSONResponse(status_code=404, content={"detail": "Skill not found"})
	schema = SkillSchema(**schema_dict)
	wrapper = SkillWrapper(schema, endpoint_url="dummy")
	try:
		result = wrapper.call(input_data)
		return result
	except Exception as e:
		return JSONResponse(status_code=400, content={"detail": str(e)})
