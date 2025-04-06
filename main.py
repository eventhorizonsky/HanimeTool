import asyncio
import threading
from scheduler import schedule_random_time_task
import uvicorn
from api import app
from config import config 

def check_config():
    print("\n====== 配置检查 ======")
    print(f"HTTP代理:{config.get('httpProxy') if config.get('httpProxy') else '未配置'}")
    print(f"存储路径: {config.get('filePath', '未配置')}")
    print(f"aria2 RPC地址: {config.get('aria2RpcUrl', '未配置')}")
    print(f"aria2 RpcSecret: {'已配置' if config.get('aria2RpcSecret') else '未配置'}")
    print(f"Cookie配置: {'已配置' if config.get('hanimeCookie') else '未配置'}")
    print("====================\n")
def start_scheduler():
    schedule_random_time_task()

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=5051)

if __name__ == "__main__":
    check_config()  # 新增配置检查
    
    scheduler_thread = threading.Thread(target=start_scheduler)
    api_thread = threading.Thread(target=start_api)

    scheduler_thread.start()
    api_thread.start()

    scheduler_thread.join()
    api_thread.join()
