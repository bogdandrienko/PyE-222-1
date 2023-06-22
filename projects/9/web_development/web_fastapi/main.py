from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
import datetime
import random
import utils

#

DEBUG = True
LOGGING = True

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Домашняя страница"""
    utils.logging(request)

    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/list", response_class=HTMLResponse)
async def post_list_get(request: Request):
    """Отображает все публикации"""
    utils.logging(request)

    raw_rows = utils.db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts""")
    rows = [
        {"id": i[0], "author": i[1], "title": i[2], "description": str(i[3])[:20] + "..." if len(str(i[3])) > 20 else i[3], "datetime": i[4]}
        for i in raw_rows
    ]
    return templates.TemplateResponse("list.html", {"request": request, "list": rows})


@app.post("/list", response_class=HTMLResponse)
async def post_list_post(request: Request):
    """Поиск"""
    utils.logging(request)

    form = await request.form()
    search = form.get('search')
    # if search is None:  # TODO[исправлено] исправить перенаправление с функции с метода POST
    #     search = ""
    raw_rows = utils.db_query_sqlite(
        """SELECT id, author, title, description, datetime FROM posts WHERE title LIKE ?""",
        ('%' + search + '%',)
    )
    rows = [
        {"id": i[0], "author": i[1], "title": i[2], "description": str(i[3])[:20] + "..." if len(str(i[3])) > 20 else i[3], "datetime": i[4]}
        for i in raw_rows
    ]
    return templates.TemplateResponse("list.html", {"request": request, "list": rows, "search": search})


@app.get("/create", response_class=HTMLResponse)
async def post_create_get(request: Request):
    """Возврат страницы с формой для отправки постов"""
    utils.logging(request)

    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/create", response_class=RedirectResponse)
async def post_create_post(request: Request):
    """Создаёт новую публикацию"""
    utils.logging(request)

    form = await request.form()
    title = form.get('title')
    description = form.get('description')
    author = random.choice(["Илья", "Абулхаир", "Арман"])
    date = str(datetime.datetime.now())[:-7]
    utils.db_query_sqlite(
        f"""INSERT INTO posts (author, title, description, datetime) VALUES (?, ?, ?, ?)""",
        (author, title, description, date)
    )
    return RedirectResponse(url=app.url_path_for("post_list_get"), status_code=303)


@app.get("/change", response_class=HTMLResponse)
async def post_change_get(request: Request):
    """Отображает форму для изменения поста"""
    utils.logging(request)

    pk = int(request.query_params.get("pk"))
    raw_row = utils.db_query_sqlite(
        """SELECT id, author, title, description, datetime FROM posts WHERE id = ?""",
        args=(int(pk),), many=False
    )
    new_dict = {"id": raw_row[0], "author": raw_row[1], "title": raw_row[2], "description": raw_row[3], "datetime": raw_row[4]}
    return templates.TemplateResponse("change.html", {"request": request, "post": new_dict})


@app.post("/change", response_class=RedirectResponse)
async def post_change_post(request: Request):
    """Изменяет существующую публикацию"""
    utils.logging(request)

    form = await request.form()
    pk = form.get('pk')
    title = form.get('title')
    description = form.get('description')
    date = str(datetime.datetime.now())[:-7]
    utils.db_query_sqlite(
        f"""UPDATE POSTS SET title = ?, description = ?, datetime = ? WHERE id = ?""",
        (title, description, date, pk)
    )
    return RedirectResponse(url=app.url_path_for("post_list_get"), status_code=303)


@app.get("/delete", response_class=RedirectResponse)
async def post_delete(request: Request):
    """Удаляет существующую публикацию"""
    utils.logging(request)

    pk = int(request.query_params.get("pk"))
    utils.db_query_sqlite(f"""DELETE FROM posts where id = ?""", (pk,))
    return RedirectResponse(url=app.url_path_for("post_list_get"), status_code=303)


@app.get("/detail", response_class=HTMLResponse)
async def post_detail_get(request: Request):
    """Отображает публикацию подробно"""
    utils.logging(request)

    pk = int(request.query_params.get("pk"))
    raw_row = utils.db_query_sqlite(
        """SELECT id, author, title, description, datetime FROM posts WHERE id = ?""",
        args=(int(pk),), many=False
    )
    new_dict = {"id": raw_row[0], "author": raw_row[1], "title": raw_row[2], "description": raw_row[3], "datetime": raw_row[4]}
    return templates.TemplateResponse("detail.html", {"request": request, "post": new_dict})


@app.post("/comment/create", response_class=RedirectResponse)
async def post_comment_create(request: Request):
    """Удаляет существующую публикацию"""
    utils.logging(request)

    form = await request.form()
    pk = form.get('pk')
    author = random.choice(["Дина", "Алема", "Айгерим"])
    text = form.get('text')

    utils.db_query_sqlite(
        f"""INSERT INTO post_comments (title_id, author, text) VALUES (?, ?, ?)""",
        (pk, author, text)
    )
    return RedirectResponse(url=app.url_path_for("post_detail_get") + f"?pk={pk}", status_code=303)


if __name__ == '__main__':
    """
    Сайт, для публикации постов, с комментариями и лайками
    """

    # todo
    # детальный просмотр поста
    # комментарии
    # лайки
    # TODO исправить удаление и изменение на delete и put методы

    # todo ИДЕЯ
    # Люди, со своих компьютеров должны уметь посылать рационализаторские предложения

    # todo ДИЗАЙН
    # В настольном приложении, есть форма с полями:
    # Наименование - label, Место - combobox, Экономический эффект - float

    # todo СТЭК
    # fastapi   - backend
    # database  - sqlite
    # pyqt6     - frontend (aiohttp) / android / ios



    pass
