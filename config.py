# config.py
import os
import json

# 配置文件路径
config_dir = os.path.join(os.path.dirname(__file__), "config")
config_path = os.path.join(config_dir, "config.json")

# 配置文件模板
default_config = {
    "hanimeCookie": "",
    "aria2RpcUrl": "http://localhost:6800/jsonrpc",
    "aria2RpcSecret": "",
    "filePath":"/anime",
    "httpProxy": ""  # 新增代理配置项
}

# 检查并创建 config.json 文件
def ensure_config_exists():
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)  # 创建 config 目录
    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
        print(f"配置文件已创建：{config_path}。请更新配置文件中的信息后重启容器。")
ensure_config_exists()

# 读取 config.json 内容
with open(config_path, "r") as f:
    config = json.load(f)

header = {
    "cookie": config.get("hanimeCookie", "")
}

aria2_config = {
    "url": config.get("aria2RpcUrl", ""),
    "rpc_secret": config.get("aria2RpcSecret", "")
}
file_path=config.get("filePath", "")
# 设置数据库路径
db_path = os.path.join(os.path.dirname(__file__), "config/videos.db")
