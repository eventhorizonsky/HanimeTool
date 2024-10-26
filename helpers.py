# helpers.py

import re

def get_video_id(url):
    pattern = r"v=(\d+)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def remove_dir_invalid_symbol(title):
    return re.sub(r'[^\w\s-]', '', title)
