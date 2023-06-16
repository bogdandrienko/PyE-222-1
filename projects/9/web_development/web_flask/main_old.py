import datetime

from flask import Flask, request, render_template, redirect, url_for
import utils
import random

app = Flask(__name__, template_folder="templates")


@app.route("/")  # URL (ссылка)
def home():  # VIEW (функция-контроллер)
    names = ["Инна", "Ольга", "Юля"]  # MODEL (база данных)
    return render_template('index.html', names=names)  # TEMPLATE (html/шаблонизатор)


@app.route("/list")  # URL (ссылка)
def view_list():  # VIEW (функция-контроллер)
    # todo ПОЛУЧАЕМ СЫРЫЕ ДАННЫЕ ИЗ БАЗЫ
    raw_rows = utils.db_query_sqlite("""SELECT id, author, title, description, datetime FROM posts""")  # MODEL (база данных)

    # todo ПРЕВРАЩАЕМ ЭТИ ДАННЫЕ В СЛОВАРЬ НУЖНОГО ФОРМАТА
    rows = []
    for i in raw_rows:
        new_dict = {"id": i[0], "author": i[1], "title": i[2], "description": i[3], "datetime": i[4]}
        rows.append(new_dict)

    return render_template('list.html', list=rows)  # TEMPLATE (html/шаблонизатор)


@app.route("/create", methods=["GET", "POST"])  # URL (ссылка)
def view_create():  # VIEW (функция-контроллер)
    if request.method == "GET":
        # todo ВОЗВРАЩАЕМ СТРАНИЦУ С ФОРМОЙ
        return render_template('create.html')  # TEMPLATE (html/шаблонизатор)
    elif request.method == "POST":
        # todo ПОЛУЧАЕМ ПЕРЕМЕННЫЕ ИЗ ФОРМЫ
        title = request.form.get("title")
        description = request.form.get("description")
        author = random.choice(["Илья", "Абулхаир", "Арман"])
        date = str(datetime.datetime.now())[:-7]

        # print(title, description)
        # TODO SQL INJECTION - НЕЛЬЗЯ "НАПРЯМУЮ" ВСТАВЛЯТЬ ПЕРЕМЕННЫЕ В ЗАПРОС
        # raw_rows = db_query(f"""INSERT INTO posts (title, description) VALUES ('{title}', '{description}')""")  # MODEL (база данных)

        # todo ВСТАВКА ДАННЫХ В БАЗУ
        utils.db_query_sqlite(f"""INSERT INTO posts (author, title, description, datetime) VALUES (?, ?, ?, ?)""",
                              (author, title, description, date))  # MODEL (база данных)

        return redirect(url_for('view_list'), 301)  # TEMPLATE (html/шаблонизатор)


@app.route("/change", methods=["GET", "POST"])  # URL (ссылка)
def view_change():  # VIEW (функция-контроллер)
    if request.method == "GET":
        pk = request.args.get('pk', default=0, type=int)
        raw_row = utils.db_query_sqlite(
            """SELECT id, author, title, description, datetime FROM posts WHERE id = ?""",
            args=(int(pk),),
            many=False
        )
        i = raw_row
        new_dict = {"id": i[0], "author": i[1], "title": i[2], "description": i[3], "datetime": i[4]}
        return render_template('change.html', post=new_dict)
    elif request.method == "POST":
        pk = request.form.get("pk")
        title = request.form.get("title")
        description = request.form.get("description")
        date = str(datetime.datetime.now())[:-7]

        utils.db_query_sqlite(
            f"""UPDATE POSTS SET title = ?, description = ?, datetime = ? WHERE id = ?""",
            (title, description, date, pk))

        return redirect(url_for('view_list'), 301)


@app.route("/delete", methods=["GET"])  # URL (ссылка)
def view_delete():  # VIEW (функция-контроллер)
    pk = request.args.get('pk', default=0, type=int)
    # todo ВСТАВКА ДАННЫХ В БАЗУ
    utils.db_query_sqlite(f"""DELETE FROM posts where id = ?""", (int(pk),))  # MODEL (база данных)
    return redirect(url_for('view_list'), 301)  # TEMPLATE (html/шаблонизатор)


if __name__ == '__main__':
    # todo ЗАПУСК ОТЛАДОЧНОГО СЕРВЕРА
    app.run(host="127.0.0.1", port=8000, debug=True)
    # flask --app main run --host=0.0.0.0 --port=8000 --debug

    # utils.sqlite_create_posts_db()

    # DRY
    # PEP8 (linter, black)
    # KISS
    # SOLID
