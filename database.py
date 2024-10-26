# database.py

import sqlite3

def connect_db():
    conn = sqlite3.connect('config\\videos.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS videos
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        vid TEXT,
        user_name TEXT,
        isDownloaded INTEGER)
    ''')
    conn.commit()
    return conn, c

def update_download_status(vid):
    conn, c = connect_db()
    c.execute('UPDATE videos SET isDownloaded=1 WHERE vid=?', (vid,))
    conn.commit()
    conn.close()

def check_if_downloaded(vid):
    conn, c = connect_db()
    c.execute('SELECT * FROM videos WHERE vid=? AND isDownloaded=1', (vid,))
    downloaded = bool(c.fetchone())
    conn.close()
    return downloaded

def insert_video(vid, user_name):
    conn, c = connect_db()
    c.execute('INSERT INTO videos (vid, user_name, isDownloaded) VALUES (?, ?, 0)', (vid, user_name))
    conn.commit()
    conn.close()
