from pydantic import BaseModel


class LLDSection(BaseModel):
    id: str
    title: str
    description: str
    dependencies: list[str]
    context: str
    key_points: list[str]


class LLDPlan(BaseModel):
    sections: list[LLDSection]
    assumptions: list[str]
    writing_order: list[str]
