from fastapi import FastAPI, Request, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from scraper import traverse_and_get_links, download_by_url
from fastapi import BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义标准响应模型
class StandardResponse(BaseModel):
    status: str
    message: str

@app.post("/trigger", 
          summary="触发订阅任务", 
          description="后台异步执行订阅任务",
          response_model=StandardResponse)
async def trigger_traverse(background_tasks: BackgroundTasks):
    # 使用后台任务异步执行
    background_tasks.add_task(traverse_and_get_links)
    return {"status": "success", "message": "成功触发订阅任务，正在后台执行"}

@app.post("/downloadUrl", 
          summary="下载视频", 
          description="通过URL添加视频下载任务",
          response_model=StandardResponse)
async def download_url(href: str = Body(..., description="视频资源的URL地址", embed=True)):
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download_by_url, href)
        return {"status": "success", "message": "成功添加下载任务"}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": "error", "message": str(e)})
