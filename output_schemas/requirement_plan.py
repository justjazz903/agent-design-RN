from pydantic import BaseModel


class RequirementSection(BaseModel):
    id: str
    title: str
    description: str
    dependencies: list[str]
    context: str
    key_points: list[str]


class RequirementPlan(BaseModel):
    sections: list[RequirementSection]
    assumptions: list[str]
    writing_order: list[str]
