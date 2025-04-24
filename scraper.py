# scraper.py

from bs4 import BeautifulSoup
from curl_cffi import requests
from config import header, config  # 新增导入config
from helpers import get_video_id, remove_dir_invalid_symbol
from database import insert_video, check_if_downloaded
from downloader import download_with_aria2


def make_request(url):
    proxies = {}
    if config.get("httpProxy"):
        proxies = {
            "http": config["httpProxy"],
            "https": config["httpProxy"]
        }
    return requests.get(
        url,
        headers=header,
        impersonate="chrome110",
        proxies=proxies
    )

def get_dl(vid, user_name):
    url = f"https://hanime1.me/download?v={vid}"
    page = make_request(url)  # 修改为使用新的请求方法
    soup = BeautifulSoup(page.content, "html.parser")

    tables = soup.find_all("table", class_="download-table")
    if not tables:
        return

    a_tags = tables[0].find_all("a")
    for a in a_tags:
        link = a.get("data-url")
        title = remove_dir_invalid_symbol(a.get("download"))
        download_with_aria2(vid, link, title, user_name)
        break

def download_by_url(href):
    vid = get_video_id(href)
    if vid and not check_if_downloaded(vid):
        page = make_request(href)  # 修改为使用新的请求方法
        soup = BeautifulSoup(page.content, "html.parser")
        user_name = soup.select_one("a#video-artist-name").text.strip()
        insert_video(vid, user_name)
        get_dl(vid, user_name)

def traverse_and_get_links():
    try:
        page = make_request("https://hanime1.me/subscriptions")
        soup = BeautifulSoup(page.content, "html.parser")
        # 更安全的获取总页数方式
        pagination = soup.select("#home-rows-wrapper > div:nth-child(2) > ul > li")
        if not pagination or len(pagination) < 2:
            print("无法获取分页信息，可能页面结构已变更")
            return
            
        total_pages = 1  # 默认1页
        try:
            total_pages = int(pagination[-2].find("a").text)
        except (AttributeError, ValueError):
            print("解析总页数失败，使用默认值1")
        
        vid_set = set()
        for page_num in range(1, total_pages + 1):
            print(f"加载页数： {page_num}")
            page = make_request(f"https://hanime1.me/subscriptions?page={page_num}")  # 修改为使用新的请求方法
            soup = BeautifulSoup(page.content, "html.parser")
    
            divs = soup.select("#home-rows-wrapper > div:nth-child(1) > div > div")
            for div in divs:
                a_tag = div.find("a")
                if a_tag:
                    href = a_tag.get("href")
                    user_name_tag = div.select_one("a.card-mobile-user")
                    user_name = user_name_tag.text if user_name_tag else "Unknown Author"
    
                    vid = get_video_id(href)
                    if vid and (vid, user_name) not in vid_set:
                        vid_set.add((vid, user_name))
    
                        if not check_if_downloaded(vid):
                            insert_video(vid, user_name)
                            get_dl(vid, user_name)
    
    except Exception as e:
        print(f"遍历订阅列表出错: {str(e)}")
        raise  # 抛出异常让上层处理
