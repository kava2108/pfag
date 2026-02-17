# pfag/skills/__init__.py

"""
PFAG Agent Skills - Initial Skill Registration
Registers PFAG API endpoints as Copilot Agent Skills.
"""

from .schema import SkillSchema


def register_builtin_skills() -> None:
    """
    Register PFAG API endpoints as skills.
    """

    # -----------------------------
    # 1. formify
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="formify",
            description="Extract form fields from a PDF and return structured JSON.",
            input_schema={
                "type": "object",
                "properties": {
                    "pdf_url": {"type": "string", "description": "URL of the PDF to analyze"},
                    "include_positions": {"type": "boolean", "description": "Include field positions", "default": False}
                },
                "required": ["pdf_url"]
            },
            output_schema={
                "type": "object",
                "properties": {
                    "fields": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "value": {"type": "string"},
                                "position": {"type": "object"}
                            }
                        }
                    }
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 2. html_to_pdf
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="html_to_pdf",
            description="Convert HTML content into a PDF file.",
            input_schema={
                "type": "object",
                "properties": {
                    "html": {"type": "string", "description": "HTML content to convert"},
                    "css": {"type": "string", "description": "Optional CSS styles"},
                    "options": {"type": "object", "description": "PDF generation options"}
                },
                "required": ["html"]
            },
            output_schema={
                "type": "object",
                "properties": {
                    "pdf_url": {"type": "string", "description": "URL of the generated PDF"}
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 3. write_fields
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="write_fields",
            description="Write values into PDF form fields and return a new PDF.",
            input_schema={
                "type": "object",
                "properties": {
                    "pdf_url": {"type": "string", "description": "URL of the PDF"},
                    "fields": {
                        "type": "object",
                        "description": "Key-value pairs of field names and values"
                    }
                },
                "required": ["pdf_url", "fields"]
            },
            output_schema={
                "type": "object",
                "properties": {
                    "pdf_url": {"type": "string", "description": "URL of the updated PDF"}
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 4. preview
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="preview_pdf",
            description="Generate a preview image of a PDF file.",
            input_schema={
                "type": "object",
                "properties": {
                    "pdf_url": {"type": "string", "description": "URL of the PDF"},
                    "page": {"type": "integer", "description": "Page number to preview", "default": 1}
                },
                "required": ["pdf_url"]
            },
            output_schema={
                "type": "object",
                "properties": {
                    "image_url": {"type": "string", "description": "URL of the preview image"}
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 5. cleanup
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="cleanup",
            description="Clean up temporary PDF files on the server.",
            input_schema={"type": "object", "properties": {}},
            output_schema={
                "type": "object",
                "properties": {
                    "deleted": {"type": "integer", "description": "Number of files deleted"}
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 6. history
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="pdf_history",
            description="Return the history of generated PDFs.",
            input_schema={"type": "object", "properties": {}},
            output_schema={
                "type": "object",
                "properties": {
                    "items": {"type": "array"}
                }
            },
            version="1.0.0"
        )
    )

    # -----------------------------
    # 7. health
    # -----------------------------
    SkillSchema.save(
        SkillSchema(
            skill_name="health",
            description="Check PFAG server health.",
            input_schema={"type": "object", "properties": {}},
            output_schema={
                "type": "object",
                "properties": {
                    "status": {"type": "string"}
                }
            },
            version="1.0.0"
        )
    )


# Register all skills on module import
register_builtin_skills()