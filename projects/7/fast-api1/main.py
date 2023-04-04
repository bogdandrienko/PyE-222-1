from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
import contextlib

from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    with contextlib.closing(sqlite3.connect('database/database.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
                SELECT id, title, description, status FROM todos
                ORDER BY id DESC
                """)
            records: list[tuple] = rows.fetchall()
            todos = [
                {"id": row[0], "title": row[1], "description": row[2], "status": row[3]}
                for row in records
            ]

    return templates.TemplateResponse("pages/home.html", {"request": request, "todos": todos})


@app.post("/create")
async def create(request: Request):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    status = True if form.get("status") == "on" else False

    with contextlib.closing(sqlite3.connect('database/database.db')) as connection:
        with connection as cursor:
            cursor.execute("""
                INSERT INTO todos (title, description, status) VALUES (?, ?, ?);
                """, (title, description, status))

    return RedirectResponse(url='/', status_code=301)


if __name__ == '__main__':
    with contextlib.closing(sqlite3.connect('database/database.db')) as connection:
        with connection as cursor:
            cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos
    (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        description TEXT DEFAULT '',
        status BOOLEAN DEFAULT 0
    );
                """)

            cursor.execute("""

    INSERT INTO todos (title, description, status) VALUES ('Помыть верблюда 1', 'Помыть верблюда 1 Помыть верблюда 1', 'false');

                """)

            rows = cursor.execute("""
    SELECT * FROM todos
    ORDER BY id ASC 
    """)

            data = rows.fetchall()
            print(data)
