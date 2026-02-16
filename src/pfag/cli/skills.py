# skills CLIルーティング構造（typer用）
import typer
from src.pfag.skills.wrapper import SkillWrapper
from src.pfag.skills.warning import WarningMessage
import json
from src.pfag.skills.schema import SkillSchema
_WARNINGS = [
	WarningMessage(
		code="W001",
		message="サンプル警告",
		description="これはサンプルの警告説明です。"
	).dict()
]

@app.command()
def warnings():
	"""警告説明リストを表示"""
	import json
	typer.echo(json.dumps(_WARNINGS, ensure_ascii=False, indent=2))
app = typer.Typer()

_SKILL_SCHEMAS = {}


@app.command()
def register(
	skill_name: str,
	input_schema: str,
	output_schema: str,
	description: str,
	version: str
):
	"""スキルスキーマをCLIから登録"""
	try:
		input_schema_dict = json.loads(input_schema)
		output_schema_dict = json.loads(output_schema)
		schema = SkillSchema(
			skill_name=skill_name,
			input_schema=input_schema_dict,
			output_schema=output_schema_dict,
			description=description,
			version=version
		)
		if skill_name in _SKILL_SCHEMAS:
			typer.echo(f"Skill '{skill_name}' already exists.")
			raise typer.Exit(code=1)
		_SKILL_SCHEMAS[skill_name] = schema.dict()
		typer.echo(f"Skill schema '{skill_name}' registered.")
	except Exception as e:
		typer.echo(f"Error: {e}")
		raise typer.Exit(code=1)


@app.command()
def call(skill_name: str, input_data: str):
	"""スキル呼び出し（CLIラッパ）"""
	try:
		if skill_name not in _SKILL_SCHEMAS:
			typer.echo(f"Skill '{skill_name}' not found.")
			raise typer.Exit(code=1)
		schema_dict = _SKILL_SCHEMAS[skill_name]
		schema = SkillSchema(**schema_dict)
		wrapper = SkillWrapper(schema, endpoint_url="dummy")
		input_dict = json.loads(input_data)
		result = wrapper.call(input_dict)
		typer.echo(json.dumps(result, ensure_ascii=False))
	except Exception as e:
		typer.echo(f"Error: {e}")
		raise typer.Exit(code=1)
