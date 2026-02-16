from src.pfag.skills.wrapper import SkillWrapper
from src.pfag.skills.schema import SkillSchema

def test_skill_wrapper_echo():
    schema = SkillSchema(
        skill_name="echo",
        input_schema={"type": "object", "properties": {"text": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"result": {"type": "string"}}},
        description="Echo",
        version="1.0"
    )
    wrapper = SkillWrapper(schema, endpoint_url="dummy")
    result = wrapper.call({"text": "hello"})
    assert result["result"] == "hello"
