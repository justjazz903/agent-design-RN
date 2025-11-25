from pydantic import BaseModel


class HLDSection(BaseModel):
    id: str
    title: str
    description: str
    dependencies: list[str]
    context: str
    key_points: list[str]


class HLDPlan(BaseModel):
    sections: list[HLDSection]
    assumptions: list[str]
    writing_order: list[str]
