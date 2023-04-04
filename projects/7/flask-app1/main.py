import contextlib

from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import sqlite3


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

"""
Главная
Read (GET) [SELECT] Общий список книг (сокращённый формат)
Read (GET) [SELECT where id = 1] Детально о каждой книге
Create (POST) [INSERT] Страница формой для создания книг
Update (PUT | PATCH) [UPDATE] Редактирование
Delete (DELETE) [DELETE] Удаление
"""

"""
TODO TASKS:
категории(фильтры для книг, фантастика, детективы)
Развернуть на railway

Написать простейшее приложение для системы учёта товаров (id, title, description, price, count)
Вы владелец магазина, к Вам приехала машина с товаром, Вы должны этот товар "оприходовать", т.е. 
добавить в общий список (цена, наименование, количество). + поиск.
"""


# http://127.0.0.1:8000
# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

@app.route("/", methods=['GET'])
def home():
    kwargs = {
        "name": "Dias",
        "name2": "Dina",
        "is_fruit": True,
        "words": ["Python", "Go", "C", "C++"],
        "books": [
            {"id": 1, "title": "Amon Ra", "description": "Amon Ra Amon Ra", "author": "A.Pelevin"},
            {"id": 2, "title": "Amon Ra 1", "description": "Amon Ra 1 Amon Ra 1", "author": "V.Pelevin"},
            {"id": 3, "title": "Amon Ra 2", "description": "Amon Ra 2 Amon Ra 2", "author": "N.Pelevin"},
            {"id": 4, "title": "Amon Ra 3", "description": "Amon Ra 3 Amon Ra 3", "author": "K.Pelevin"},
        ],
        "ids": [5, 6, 8, 0, 12]
    }

    return render_template('pages/home.html', **kwargs)


@app.route('/create', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create():
    """
    Создание нового поста книг в базе данных
    """

    if request.method == "GET":
        return render_template('pages/book_create.html')
    elif request.method == "POST":
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        author = request.form['author'].strip()

        with psycopg2.connect(
                user="postgres",
                password="31284bogdan",
                host="127.0.0.1",
                port="5432",
                database="book_shop"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO public.book_posts (title, description, author) VALUES (%s, %s, %s);",
                    (title, description, author)
                )

        # with open("database.txt", mode="a", encoding="utf-8") as file:
        #     file.write(f"{title}_!_{description}_!_{author}\n")

        return redirect(url_for('book_list'))


@app.route('/list', methods=['GET', "POST"])  # TODO Read (GET) [SELECT] Общий список книг (сокращённый формат)
def book_list():
    """
    Вывод на экран всех постов с книгами в базе данных
    """
    title = request.form.get("title", "").strip()

    with psycopg2.connect(
            user="postgres",
            password="31284bogdan",
            host="127.0.0.1",
            port="5432",
            database="book_shop"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, description, author FROM public.book_posts  WHERE title LIKE %s ORDER BY id ASC;",
                (f"%{title}%",)
            )
            records = cursor.fetchall()
            # print(records)
            _books = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "title": record[1],
                    "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "author": record[3]
                }
                _books.append(new_dict)

    # with open("database.txt", mode="r", encoding="utf-8") as file:
    #     lines = file.readlines()
    #     new_lines = []
    #     for line in lines:
    #         if len(str(line)) > 3:
    #             new_lines.append(line)
    #     # lines = list(filter(lambda x: len(str(line)) > 3, lines))
    #
    #     new_dictionaries = []
    #     for idx, line in enumerate(new_lines, 1):
    #         data = line.split("_!_")
    #         new_dict = {
    #             "id": idx,
    #             "title": data[0].strip(),
    #             "description": data[1].strip(),
    #             "author": data[2].strip()
    #         }
    #         new_dictionaries.append(new_dict)
    #     # new_dictionaries = [
    #     #     {"id": idx, "title": line.split("_!_")[0].strip(), "description": line.split("_!_")[1].strip(), "author": line.split("_!_")[2].strip()}
    #     #     for idx, line in enumerate(new_lines, 1)
    #     # ]
    #     print(new_dictionaries)
    # return render_template('pages/book_list.html', books=new_dictionaries)

    categories = ["Детективы", "Фентези", "Исторические"]

    return render_template('pages/book_list.html', books=_books, search=title, categories=categories)


@app.route('/detail/<int:pk>', methods=['GET'])  # TODO Read (GET) [SELECT where id = 1] Детально о каждой книге
def detail(pk: int):
    """
    Вывод на экран одного поста книг из базе данных
    """

    with psycopg2.connect(
            user="postgres",
            password="31284bogdan",
            host="127.0.0.1",
            port="5432",
            database="book_shop"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, description, author FROM public.book_posts WHERE id = %s;", (pk,))
            record = cursor.fetchone()
            # print(records)
            _book = {
                "id": record[0],
                "title": record[1],
                "description": record[2],
                "author": record[3]
            }

    # with open("database.txt", mode="r", encoding="utf-8") as file:
    #     line = file.readlines()[pk - 1]
    #     data = line.split("_!_")
    #     new_dict = {
    #         "id": pk,
    #         "title": data[0].strip(),
    #         "description": data[1].strip(),
    #         "author": data[2].strip()
    #     }
    # return render_template('pages/book_detail.html', book=new_dict)

    return render_template('pages/book_detail.html', book=_book)


@app.route('/delete/<int:pk>', methods=['GET'])
def delete(pk: int):
    """
    Удаление поста из базы данных и возврат ко всем постам
    """

    with psycopg2.connect(
            user="postgres",
            password="31284bogdan",
            host="127.0.0.1",
            port="5432",
            database="book_shop"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM public.book_posts WHERE id = %s;", (pk,))
    return redirect(url_for('book_list'))


def database_create():
    """
    database - book_shop
    """

    """
CREATE DATABASE book_shop
WITH
OWNER = postgres
ENCODING = 'UTF8'
CONNECTION LIMIT = -1
IS_TEMPLATE = False;
    """

    """
    table - book_posts (id - serial, title - varchar200, description - varchar2000, author - varchar20)
    """

    """
CREATE TABLE public.book_posts
(
    id serial NOT NULL,
    title character varying(200) NOT NULL UNIQUE,
    description character varying(2000) DEFAULT '',
    author character varying(20) DEFAULT '',
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.book_posts
OWNER to postgres;
    """

    """
SELECT * FROM public.book_posts
ORDER BY id ASC 
    """

    """
INSERT INTO public.book_posts (title, description, author) VALUES ('Мёртвые души', 'Мёртвые души Мёртвые души Мёртвые души', 'Гоголь');
    """
    pass


def sql3_ex():
    with contextlib.closing(sqlite3.connect('database.db')) as connection:
        with connection as cursor:
            cursor.execute("CREATE TABLE movie(title, year, score)")


if __name__ == '__main__':
    # app.run(port=5000)
    # database_create()
    sql3_ex()
