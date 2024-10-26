# scraper.py

from bs4 import BeautifulSoup
from curl_cffi import requests
from config import header
from helpers import get_video_id, remove_dir_invalid_symbol
from database import insert_video, check_if_downloaded
from downloader import download_with_aria2


def get_dl(vid, user_name):
    url = f"https://hanime1.me/download?v={vid}"
    page = requests.get(url, headers=header, impersonate="chrome110")
    soup = BeautifulSoup(page.content, "html.parser")

    tables = soup.find_all("table", class_="download-table")
    if not tables:
        return

    a_tags = tables[0].find_all("a")
    for a in a_tags:
        link = a.get("href")
        title = remove_dir_invalid_symbol(a.get("download"))
        download_with_aria2(vid, link, title, user_name)
        break

def download_by_url(href):
    vid = get_video_id(href)
    if vid and not check_if_downloaded(vid):
        page = requests.get(href, headers=header, impersonate="chrome110")
        soup = BeautifulSoup(page.content, "html.parser")
        user_name = soup.select_one("a#video-artist-name").text.strip()
        insert_video(vid, user_name)
        get_dl(vid, user_name)

def traverse_and_get_links():
    page = requests.get("https://hanime1.me/subscriptions", headers=header, impersonate="chrome110")
    soup = BeautifulSoup(page.content, "html.parser")
    total_pages = int(soup.select("#home-rows-wrapper > div:nth-child(2) > ul > li")[-2].find("a").text)

    vid_set = set()
    for page_num in range(1, total_pages + 1):
        print(f"Fetching page {page_num}")
        page = requests.get(f"https://hanime1.me/subscriptions?page={page_num}", headers=header, impersonate="chrome110")
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
