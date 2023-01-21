from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
import utils
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# cd twitter_fastapi
# python -m venv env
# call env/Scripts/activate.bat
# pip install -r requirements.txt
# pip freeze > requirements.txt
# uvicorn main:app --reload --host=0.0.0.0 --port=8000

@app.get("/index")
async def index():
    return 'Index Page $3'


@app.get("/default")
async def default():
    return {"data": False}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/posts")
async def posts(request: Request):
    with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                          host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
        with connection.cursor() as cursor:  # syntax sugar
            cursor.execute("SELECT * FROM public.posts;")
            rows = cursor.fetchall()
            if rows is None:
                raise Exception("not have objs")
    arr_dicts = [
        {
            "id": row[0], "title": row[1], "description": row[2],
            "date_create": utils.Main.Datetime.get_format_time(dt=row[3]), "status_moderate": row[4]
        } for row in rows
    ]
    return templates.TemplateResponse("posts.html", {"request": request, "arr_posts": arr_dicts})


@app.get("/pay")
async def pay(request: Request):
    result = requests.post("http://127.0.0.1:8000/api/pay", data={'key': 9.0})
    return {"result": result.json()}

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("home.html", {"request": request, "id": id})
# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
