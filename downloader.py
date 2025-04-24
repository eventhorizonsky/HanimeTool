# downloader.py

import json
import requests
from config import aria2_config,file_path
from database import update_download_status


def download_with_aria2(vid, link, title, user):
    download_dir = f"{file_path}/{user}"
    file_name = f"{title}-[{vid}].mp4"

    params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "aria2.addUri",
        "params": [
            f"token:{aria2_config['rpc_secret']}",
            [link],
            {
                "dir": download_dir,
                "out": file_name
            }
        ]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(aria2_config["url"], data=json.dumps(params), headers=headers)

    if response.status_code == 200:
        print(f"下载任务成功发送至 aria2 : {file_name}")
        update_download_status(vid)
    else:
        print("下载任务发送至aria2失败:", response.text)
