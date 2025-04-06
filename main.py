import asyncio
import threading
from scheduler import schedule_random_time_task
import uvicorn
from api import app

async def run_scheduler():
    # 将调度器运行在事件循环中
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, schedule_random_time_task)

async def run_api():
    config = uvicorn.Config(app, host="0.0.0.0", port=5051)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    # 同时运行API服务和调度器
    await asyncio.gather(
        run_api(),
        run_scheduler()
    )

if __name__ == "__main__":
    asyncio.run(main())
