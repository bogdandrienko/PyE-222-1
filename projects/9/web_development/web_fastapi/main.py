from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse, Response
import datetime
import random
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DEBUG = True  # True если приложение ещё отлаживается
LOGGING = True  # True если нужно сохранять логи


def logging(request: Request):
    text = f"[{str(datetime.datetime.now())[0:-5:1]}] {request.url} ({request.method})\n"
    if DEBUG:
        print(f"\n{text}")
    if LOGGING:
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


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Домашняя страница"""
    logging(request)

    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/list", response_class=HTMLResponse)
async def view_list_get(request: Request):
    """Отображает все публикации"""
    logging(request)

    raw_rows = db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts""")
    rows = [
        {"id": i[0], "author": i[1], "title": i[2],
         "description": str(i[3])[:20] + "..." if len(str(i[3])) > 20 else i[3], "datetime": i[4]}
        for i in raw_rows]
    return templates.TemplateResponse("list.html", {"request": request, "list": rows})


@app.post("/list", response_class=HTMLResponse)
async def view_list_post(request: Request):
    """Поиск"""
    logging(request)

    form = await request.form()
    search = form.get('search')
    if search is None:  # TODO исправить перенаправление с функции с метода POST
        search = ""
    raw_rows = db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts
    WHERE title LIKE ?
    """, ('%' + search + '%',))
    rows = [
        {"id": i[0], "author": i[1], "title": i[2],
         "description": str(i[3])[:20] + "..." if len(str(i[3])) > 20 else i[3], "datetime": i[4]}
        for i in raw_rows
    ]
    return templates.TemplateResponse("list.html", {"request": request, "list": rows, "search": search})


@app.get("/create", response_class=HTMLResponse)
async def view_create_get(request: Request):
    """Возврат страницы с формой для отправки постов"""
    logging(request)

    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/create", response_class=RedirectResponse)
async def view_create_post(request: Request):
    """Создаёт новую публикацию"""
    logging(request)

    form = await request.form()
    title = form.get('title')
    description = form.get('description')
    author = random.choice(["Илья", "Абулхаир", "Арман"])
    date = str(datetime.datetime.now())[:-7]

    db_query_sqlite(
        f"""INSERT INTO posts (author, title, description, datetime) VALUES (?, ?, ?, ?)""",
        (author, title, description, date)
    )

    return RedirectResponse(url=app.url_path_for("view_list_get"))


@app.get("/change", response_class=HTMLResponse)
async def view_change_get(request: Request):
    """Отображает форму для изменения поста"""
    logging(request)

    pk = int(request.query_params.get("pk"))
    raw_row = db_query_sqlite(
        """SELECT id, author, title, description, datetime FROM posts WHERE id = ?""",
        args=(int(pk),), many=False
    )
    new_dict = {"id": raw_row[0], "author": raw_row[1], "title": raw_row[2], "description": raw_row[3], "datetime": raw_row[4]}
    return templates.TemplateResponse("change.html", {"request": request, "post": new_dict})


@app.post("/change", response_class=RedirectResponse)
async def view_change_post(request: Request):
    """Изменяет существующую публикацию"""
    logging(request)

    form = await request.form()
    pk = form.get('pk')
    title = form.get('title')
    description = form.get('description')
    date = str(datetime.datetime.now())[:-7]

    db_query_sqlite(
        f"""UPDATE POSTS SET title = ?, description = ?, datetime = ? WHERE id = ?""",
        (title, description, date, pk)
    )

    return RedirectResponse(url=app.url_path_for("view_list_get"))


@app.get("/delete", response_class=RedirectResponse)
async def view_delete(request: Request):
    """Удаляет существующую публикацию"""
    logging(request)

    pk = int(request.query_params.get("pk"))
    db_query_sqlite(f"""DELETE FROM posts where id = ?""", (pk,))

    return RedirectResponse(url=app.url_path_for("view_list_get"))


if __name__ == '__main__':
    # todo
    # детальный просмотр поста
    # комментарии
    # лайки
    # TODO исправить удаление и изменение на delete и put методы
    pass
