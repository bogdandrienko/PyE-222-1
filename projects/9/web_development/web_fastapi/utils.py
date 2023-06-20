from fastapi import Request
import datetime
import sqlite3
import main
# from main import DEBUG, LOGGING


def logging(request: Request):
    text = f"[{str(datetime.datetime.now())[0:-5:1]}] {request.url} ({request.method})\n"
    if main.DEBUG:
        print(f"\n{text}")
    if main.LOGGING:
        with open("static/log.txt", "a", encoding="utf-8") as file:
            file.write(text)


def db_query_sqlite(query: str, args=(), many=True) -> tuple | list[tuple] | None:
    with sqlite3.connect('database/database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        try:
            if many:
                return cursor.fetchall()
            return cursor.fetchone()
        except Exception as error:
            return None

def sqlite_create_posts_db():
    with sqlite3.connect('database/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
CREATE TABLE IF NOT EXISTS posts
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT,
description TEXT,
datetime TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

def sqlite_create_post_comments_db():
    with sqlite3.connect('database/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
CREATE TABLE IF NOT EXISTS post_comments
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
text TEXT,
datetime TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

if __name__ == "__main__":
    pass
