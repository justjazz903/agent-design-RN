from pydantic import BaseModel


class Section(BaseModel):
    id: int
    title: str
    goal: str
    content: str


class WritingPlan(BaseModel):
    sections: list[Section]

COMMON_JSON_SCHEMA = """
{
  "sections": [
    {
      "section_index": integer,
      "title": "string",
      "goal": "string (brief description of what this section covers)",
      "content_requirements": "string (detailed instructions on what needs to be written in this section)"
    }
  ]
}
"""
