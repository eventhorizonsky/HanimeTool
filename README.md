# HanimeTool

HanimeTool 是一个自动下载 Hanime 视频的工具，支持定时任务和手动触发下载。

<!-- PROJECT SHIELDS -->

[![贡献者][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />

## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

下面是针对您的项目的上手指南，包含了如何使用 Docker 来构建和运行程序的详细步骤。

### 上手指南

本节将指导您如何使用 Docker 来构建和运行 HanimeDownloader。

###### 开发前的配置要求

1. 确保您已安装 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。
2. 检查 Docker 是否安装成功：

```sh
docker --version
docker-compose --version
```

###### **安装步骤**

1. **拉取 Docker 镜像**

   您可以从 Docker Hub 拉取预构建的镜像：

   ```sh
   docker pull ezsky333/hanimetool
   ```

2. **修改 Docker Compose 文件**

   修改`docker-compose.yml` 文件的config映射地址

   ```yaml
   version: '3.8'

   services:
     hanime:
       image: ezsky333/hanimetool
       container_name: hanime_tool
       volumes:
         - ./config:/app/config
       restart: unless-stopped
   ```

3. **启动容器**

   使用以下命令启动 Docker 容器：

   ```sh
   docker-compose up -d
   ```

   这将以后台模式启动容器。
   
4. **创建配置文件**

   修改config目录的 `config.json` 文件，内容如下：

   ```json
   {
       "aria2RpcUrl": "你的_RPC_URL",
       "aria2RpcSecret": "你的_RPC_密钥",
       "hanimeCookie": "你的_Hanime_网站_Cookie"
   }
   ```

   请根据您的实际情况替换其中的值，并重启容器。
5. **访问 API**

   一旦容器启动成功，您可以通过以下接口来手动触发视频下载：

   - **触发下载**：`http://localhost:5051/trigger`
   - **通过 href 添加视频**：`http://localhost:5051//downloadUrl`

   您可以使用工具如 Postman 或直接在浏览器中访问这些接口。

6. **查看日志**

   您可以通过以下命令查看容器的日志，以确保一切正常运行：

   ```sh
   docker-compose logs -f
   ```

7 注意事项

- 请确保配置文件中的 RPC URL 和 Cookie 是有效的。
- 如果您需要查看或修改代码，可以通过以下命令进入容器的命令行：

```sh
docker exec -it hanime_tool /bin/bash
```

通过上述步骤，您应该能够顺利使用 Docker 来构建和运行 HanimeDownloader 项目。如果遇到问题，请查看 Docker 日志以获取更多信息，或者在项目的 GitHub 页面提出问题。

###### 开发前的配置要求

1. Python 3.6 或更高版本
2. 安装所需依赖项

###### **安装步骤**

1. 克隆仓库：

```sh
git clone https://github.com/eventhorizonsky/HanimeTool.git
```

2. 进入项目目录并安装依赖：

```sh
cd HanimeDownloader
pip install requests bs4 schedule curl_cffi flask Flask[async]
```

### 文件目录说明

```
filetree 
├── Dockerfile
├── docker-compose.yml
├── README.md
├── config/
│   ├── config.json
├── scraper.py
├── scheduler.py
├── api.py
└── main.py
```

### 开发的架构 

请阅读 [ARCHITECTURE.md](https://github.com/eventhorizonsky/HanimeTool/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

1. 使用 Docker 部署：

```sh
docker-compose up -d
```

### 使用到的框架

- [Flask](https://flask.palletsprojects.com)
- [schedule](https://schedule.readthedocs.io)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是 **非常感谢** 的。

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 版本控制

该项目使用 Git 进行版本管理。您可以在 repository 参看当前可用版本。

### 版权说明

该项目签署了 MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/eventhorizonsky/HanimeTool/blob/master/LICENSE.txt)。

<!-- links -->
[your-project-path]: eventhorizonsky/HanimeTool
[contributors-shield]: https://img.shields.io/github/contributors/eventhorizonsky/HanimeTool.svg?style=flat-square
[contributors-url]: https://github.com/eventhorizonsky/HanimeTool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/eventhorizonsky/HanimeTool.svg?style=flat-square
[forks-url]: https://github.com/eventhorizonsky/HanimeTool/network/members
[stars-shield]: https://img.shields.io/github/stars/eventhorizonsky/HanimeTool.svg?style=flat-square
[stars-url]: https://github.com/eventhorizonsky/HanimeTool/stargazers
[issues-shield]: https://img.shields.io/github/issues/eventhorizonsky/HanimeTool.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/eventhorizonsky/HanimeTool.svg
[license-shield]: https://img.shields.io/github/license/eventhorizonsky/HanimeTool.svg?style=flat-square
[license-url]: https://github.com/eventhorizonsky/HanimeTool/blob/master/LICENSE.txt
