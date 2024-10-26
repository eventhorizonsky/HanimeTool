# Dockerfile
FROM python:3.9-slim

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 安装依赖，包括 Flask
RUN pip install requests bs4 schedule curl_cffi flask Flask[async]

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 运行主程序
CMD ["python", "main.py"]
