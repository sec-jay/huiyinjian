from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    text: str = Field(..., description="用户输入的自然语言描述")


class AnalyzeResponse(BaseModel):
    task_summary: str = Field(..., description="对当前输入的整体概括")
    tasks: list[str] = Field(default_factory=list, description="用户完成的动作列表")
    outputs: list[str] = Field(default_factory=list, description="形成的产出列表")
    skills: list[str] = Field(default_factory=list, description="体现的能力列表")
    evidence: list[str] = Field(default_factory=list, description="相关事实证据")
    resume_bullet: str = Field(..., description="可用于简历的一句话表达")
    reward_score: int = Field(..., ge=0, le=100, description="可见回报评分")
    reward_reason: str = Field(..., description="评分原因说明")
    next_actions: list[str] = Field(default_factory=list, description="下一步建议")
