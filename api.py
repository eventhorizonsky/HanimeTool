from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from scraper import traverse_and_get_links, download_by_url
from fastapi import BackgroundTasks

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/trigger")
async def trigger_traverse(background_tasks: BackgroundTasks):
    # 使用后台任务异步执行
    background_tasks.add_task(traverse_and_get_links)
    return {"status": "success", "message": "成功触发订阅任务，正在后台执行"}

@app.post("/downloadUrl")
async def download_url(request: Request):
    data = await request.json()
    href = data.get("href")
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download_by_url, href)
        return {"status": "success", "message": "成功添加下载任务"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
