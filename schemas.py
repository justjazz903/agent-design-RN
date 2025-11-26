from pydantic import BaseModel


class Section(BaseModel):
    id: int
    title: str
    goal: str
    content: str


class WritingPlan(BaseModel):
    sections: list[Section]

