from flask import Flask, request, render_template, redirect, url_for
import datetime
import random
import sqlite3

app = Flask(__name__, template_folder="templates")


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


@app.route("/")
def home():
    """Домашняя страница"""

    return render_template('index.html')


@app.route("/list", methods=["GET", "POST"])
def view_list():
    """Отображает все публикации"""

    if request.method == "GET":
        raw_rows = db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts""")
        rows = [{"id": i[0], "author": i[1], "title": i[2], "description": i[3], "datetime": i[4]} for i in raw_rows]
        return render_template('list.html', list=rows)
    elif request.method == "POST":
        search = request.form.get("search")
        raw_rows = db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts
        WHERE title LIKE ?
        """, ('%' + search + '%',))
        rows = [{"id": i[0], "author": i[1], "title": i[2], "description": i[3], "datetime": i[4]} for i in raw_rows]
        return render_template('list.html', list=rows, search=search)


@app.route("/create", methods=["GET", "POST"])
def view_create():
    """Создаёт новую публикацию"""

    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        author = random.choice(["Илья", "Абулхаир", "Арман"])
        date = str(datetime.datetime.now())[:-7]
        db_query_sqlite(
            f"""INSERT INTO posts (author, title, description, datetime) VALUES (?, ?, ?, ?)""",
            (author, title, description, date)
        )
        return redirect(url_for('view_list'), 301)


@app.route("/change", methods=["GET", "POST"])
def view_change():
    """Обновляет уже существующую публикацию"""

    if request.method == "GET":
        pk = request.args.get('pk', default=0, type=int)
        raw_row = db_query_sqlite(
            """SELECT id, author, title, description, datetime FROM posts WHERE id = ?""",
            args=(int(pk),), many=False
        )
        new_dict = {"id": raw_row[0], "author": raw_row[1], "title": raw_row[2], "description": raw_row[3], "datetime": raw_row[4]}
        return render_template('change.html', post=new_dict)
    elif request.method == "POST":
        pk = request.form.get("pk")
        title = request.form.get("title")
        description = request.form.get("description")
        date = str(datetime.datetime.now())[:-7]
        db_query_sqlite(
            f"""UPDATE POSTS SET title = ?, description = ?, datetime = ? WHERE id = ?""",
            (title, description, date, pk)
        )
        return redirect(url_for('view_list'), 301)


@app.route("/delete", methods=["GET"])
def view_delete():
    """Удаляет существующую публикацию"""

    pk = request.args.get('pk', default=0, type=int)
    db_query_sqlite(f"""DELETE FROM posts where id = ?""", (pk,))
    return redirect(url_for('view_list'), 301)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
    # flask --app main run --host=0.0.0.0 --port=8000 --debug

    # 1. Поднять фласк,
    # 2. запросить с jsonplaceholder массив постов и
    # 3. вывести их на html в
    # 4. вывести их в списке ul
