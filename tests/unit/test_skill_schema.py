from src.pfag.skills.schema import SkillSchema

def test_skill_schema_fields():
    schema = SkillSchema(
        skill_name="test",
        input_schema={"type": "object"},
        output_schema={"type": "object"},
        description="desc",
        version="1.0"
    )
    assert schema.skill_name == "test"
    assert schema.input_schema["type"] == "object"
    assert schema.version == "1.0"
