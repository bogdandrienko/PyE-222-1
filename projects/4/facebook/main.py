import datetime
import psycopg2

import utils
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


# 127.0.0.1:8000
# flask --app main --debug run --host=0.0.0.0 --port=8000

@app.route('/index/')
def index():
    return 'Index Page'


@app.route('/default/')
def default():
    return {"data": False}


@app.route('/books/')
def books():
    with open("database/db.json", "r") as file:
        data_dict = json.load(file)

    datas = [3, 5, 6, 8]
    return render_template("books.html", books=data_dict, datas=datas)


@app.route('/books/<int:book_id>')
def books_id(book_id):
    with open("database/db.json", "r") as file:
        data_dict = json.load(file)
    return render_template("book.html", book=data_dict[book_id - 1])


@app.route('/books/create/', methods=['GET', 'POST'])
def books_create():
    if request.method == "GET":
        return render_template("book_create.html")
    elif request.method == "POST":
        title = str(request.form.get("title"))
        completed = request.form.get("completed")
        if completed is None:
            completed = False
        elif len(completed) < 1:
            completed = False
        else:
            completed = True
        with open("database/db.json", "r") as file:
            data_dict = list(json.load(file))
            _id = data_dict[-1]["id"] + 1
            dict1 = {"userId": 1, "id": _id, "title": title, "completed": completed}
            data_dict.append(dict1)
        with open("database/db.json", "w") as file:
            json.dump(data_dict, file)
        return redirect(url_for("books"))


@app.route('/books/<int:book_id>/delete/')
def books_delete(book_id):
    with open("database/db.json", "r") as file:
        data_dict = list(json.load(file))
        _ = data_dict.pop(book_id - 1)
    with open("database/db.json", "w") as file:
        json.dump(data_dict, file)
    return redirect(url_for("books"))


@app.route('/books/<int:book_id>/update/', methods=['GET', 'POST'])
def books_update(book_id):
    if request.method == "GET":
        with open("database/db.json", "r") as file:
            data_dict = list(json.load(file))
        return render_template("book_update.html", book=data_dict[book_id - 1])
    elif request.method == "POST":
        title = str(request.form.get("title"))
        completed = request.form.get("completed")
        if completed is None:
            completed = False
        elif len(completed) < 1:
            completed = False
        else:
            completed = True
        with open("database/db.json", "r") as file:
            data_dict = list(json.load(file))
            _id = data_dict[-1]["id"]
            dict1 = {"userId": 1, "id": _id, "title": title, "completed": completed}
            data_dict[book_id - 1] = dict1
        with open("database/db.json", "w") as file:
            json.dump(data_dict, file)
        return redirect(url_for("books"))


# CRUD


# замораживает (сохраняет) зависимости (библиотеки) с точной версией в файл
# pip freeze > requirements.txt
# установка в виртуальное окружение точной версии зависимостей
# pip install -r requirements.txt


# HOME добро пожаловать
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/posts/<int:pk>')  # primary key
def posts_id(pk):
    # TODO READ ONE
    # todo SQL read from PostgreSQL
    i = pk
    arr = {
        "id": i,
        "title": f"Заголовок {i}",
        "description": f"Описание {i} Описание {i} Описание {i}",
        "date_create": utils.Main.Datetime.get_current_time(),
        "status_moderate": i % 2 == 0
    }
    # TODO READ ONE
    return render_template("post.html", post=arr)


@app.route('/posts', methods=['GET'])
def posts():

    connect = psycopg2.connect(
        user="facebook_usr",
        password="12345Qwerty!",
        host="127.0.0.1",  # localhost - 192.168.1.100
        port="5432",
        dbname="facebook_db",
    )
    print(connect)
    cursor = connect.cursor()
    print(cursor)
    cursor.execute("SELECT * FROM public.posts")
    rows = cursor.fetchall()
    print(rows, type(rows))

    # TODO READ ALL
    # todo SQL read from PostgreSQL
    arr_posts = []
    for i in range(1, 20):
        arr_posts.append(
            {
                "id": i,
                "title": f"Заголовок {i}",
                "description": f"Описание {i} Описание {i} Описание {i} ...",
                "date_create": utils.Main.Datetime.get_current_time(),
                "status_moderate": i % 2 == 0
            }
        )
    # TODO READ ALL
    return render_template("posts.html", arr_posts=arr_posts)


@app.route('/posts/create', methods=['GET', 'POST'])
def post_create():
    if request.method == "GET":
        return render_template("post_create.html")
    elif request.method == "POST":

        print("ОТПРАВКА")

        title = str(request.form.get("title")).strip()  # left-right remove \t \n " "
        description = str(request.form.get("description")).strip()
        status = True if request.form.get("status") is not None else False
        date_create = datetime.datetime.now()  # timestamp
        print(title, description, status, date_create)

        if len(title) < 5:
            raise Exception("title is too small")
        # TODO INSERT ONE

        # TODO INSERT ONE
        return redirect(url_for("posts"))
    else:
        raise Exception("Method not allowed")


@app.route('/posts/<int:pk>/delete')  # primary key
def post_delete(pk):
    # TODO DELETE ONE
    # todo SQL read from PostgreSQL
    # TODO DELETE ONE
    return redirect(url_for("posts"))

# TODO CREATE TABLE
# CREATE TABLE public.posts
# (
#     id serial NOT NULL unique,
#     title varchar(255) NOT NULL unique,
#     description varchar(1024),
#     date_created timestamp NOT NULL DEFAULT now(),
#     status boolean NOT NULL DEFAULT 'false'
# );
#
# ALTER TABLE IF EXISTS public.posts
#     OWNER to postgres;

# выборка всего
# SELECT * FROM public.posts

# вставка первой строки
# insert into posts (title, description, status) values ('Купить кота', 'Купить купить куп', 'true');
# insert into posts (title, description, status) values ('Купить кота 2', 'Купить купить куп 2', 'true');

#
# CREATE USER facebook_usr WITH PASSWORD '12345Qwerty!';

# GRANT ALL PRIVILEGES ON DATABASE facebook_db TO facebook_usr;
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to facebook_usr;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to facebook_usr;
