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

    def safe_traverse():
        try:
            traverse_and_get_links()
        except Exception as e:
            print(f"执行订阅任务出错: {str(e)}")
            # 记录错误日志或发送通知
            # 可以在这里添加重试逻辑

    # 修改任务函数
    schedule.every().day.at(run_time.strftime('%H:%M')).do(safe_traverse)

    # 运行调度器
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次任务
