from fastapi import FastAPI
from backend.app.schemas import AnalyzeRequest, AnalyzeResponse

app = FastAPI(title="HuiYinJian API")


@app.get("/")
def root():
    return {"message": "HuiYinJian API is running"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest):
    return AnalyzeResponse(
        original_input=payload.text,
        summary="你最近做的事情具有明确的执行价值，并开始形成可见成果。",
        tasks=["整理项目需求", "搭建项目仓库", "完成首次代码提交"],
        outputs=["GitHub 仓库", "项目说明文档", "基础目录结构"],
        skills=["项目启动能力", "Git 协作基础", "技术落地执行力"],
        resume_bullets=[
            "独立完成 AI 产品 MVP 的仓库初始化与项目结构搭建",
            "使用 Git 与 GitHub 建立版本管理流程并完成首次发布"
        ],
        reward_score=72,
        reward_comment="你已经完成了从想法到可见资产的关键一步，建议继续把接口跑通，快速形成可演示成果。"
    )
