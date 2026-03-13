from pydantic import BaseModel
from typing import List


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    original_input: str
    summary: str
    tasks: List[str]
    outputs: List[str]
    skills: List[str]
    resume_bullets: List[str]
    reward_score: int
    reward_comment: str
