# main.py
import os
import json
import threading
from scheduler import schedule_random_time_task
from api import app


def start_scheduler():
    schedule_random_time_task()

def start_api():
    app.run(host='0.0.0.0', port=5051)

if __name__ == "__main__":

    scheduler_thread = threading.Thread(target=start_scheduler)
    api_thread = threading.Thread(target=start_api)

    scheduler_thread.start()
    api_thread.start()

    scheduler_thread.join()
    api_thread.join()
