from fastapi import FastAPI


app = FastAPI(
    title="回音笺 HuiYinJian Backend",
    description="回音笺后端最小服务骨架。",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "回音笺后端服务已启动"}
