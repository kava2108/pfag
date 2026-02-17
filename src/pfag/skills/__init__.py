# pfag/skills/__init__.py

"""
PFAG Agent Skills - Initial Skill Registration
This module registers built‑in skills at application startup.
"""

from .schema import SkillSchema


def register_builtin_skills() -> None:
    """
    Register initial built‑in skills so that PFAG exposes at least one skill
    to Copilot via /skills.
    """

    # Example Skill: echo
    SkillSchema.save(
        skill_name="echo",
        description="Echo back the input text.",
        input_schema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to echo back"}
            },
            "required": ["text"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Echoed text"}
            }
        },
        version="1.0.0"
    )


# Register skills immediately when this module is imported
register_builtin_skills()