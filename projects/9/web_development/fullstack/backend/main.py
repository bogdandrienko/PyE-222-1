from fastapi import Request, FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Index Page"}


@app.post("/insert")
async def post_list_post(request: Request):
    try:
        form = await request.form()
        title = str(form.get('title'))
        place = str(form.get('place'))
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO ideas (title, place) VALUES (?, ?)''', (title, place))
        return {"message": "success"}
    except Exception as error:
        return {"message": f"error: {error}"}


@app.get("/list")
async def get_list_post():
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * from ideas''')
        return cursor.fetchall()
    except Exception as error:
        return {"message": f"error: {error}"}


class Database:
    @staticmethod
    def sqlite_create_posts_db():
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
CREATE TABLE IF NOT EXISTS ideas
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
place TEXT
)
''')

    @staticmethod
    def check_data():
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM ideas''')
            data = cursor.fetchall()
            print(data)


if __name__ == "__main__":
    # uvicorn main:app --reload --host=0.0.0.0 --port=8000

    # 1. Поднять сервер с возвратом данных
    # 2. Получить данные из формы и вывести json в консоль
    # 3. Создать бд и функцию, кот записывает рац предложение

    # todo создание таблицы в первый раз
    # Database.sqlite_create_posts_db()

    # todo создание таблицы в первый раз
    Database.check_data()

    pass
