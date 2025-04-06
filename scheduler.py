# scheduler.py
import schedule
import time
import random
from datetime import datetime, timedelta
from scraper import traverse_and_get_links

def schedule_random_time_task():
    # 选择一个随机时间
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    run_time = datetime.now().replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"当前时间: {current_time}")
    print(f"将定时获取订阅列表，时间为每天的 {run_time.strftime('%H:%M')}")

    # 定义每天随机时间的任务
    schedule.every().day.at(run_time.strftime('%H:%M')).do(traverse_and_get_links)

    # 运行调度器
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次任务
