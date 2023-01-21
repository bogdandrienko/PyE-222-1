import datetime
import psycopg2
import utils
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


# cd facebook_flask
# python -m venv env
# call env/Scripts/activate.bat
# pip install -r requirements.txt
# pip freeze > requirements.txt
# flask --app main --debug run --host=0.0.0.0 --port=8000

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

# CREATE USER facebook_usr WITH PASSWORD '12345Qwerty!';

# GRANT ALL PRIVILEGES ON DATABASE facebook_db TO facebook_usr;
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to facebook_usr;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to facebook_usr;

@app.route('/index')
def index():
    return 'Index Page $3'


@app.route('/default')
def default():
    return {"data": False}


@app.route('/')
def home():
    return render_template("home.html")


# CRUD

@app.route('/posts', methods=['GET'])
def posts():
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
    return render_template("posts.html", arr_posts=arr_dicts)


@app.route('/posts/<int:pk>', methods=['GET'])  # primary key
def posts_id(pk):
    with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                          host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
        with connection.cursor() as cursor:  # syntax sugar
            cursor.execute(f"SELECT * FROM public.posts where id='{pk}';")
            row = cursor.fetchone()
            if row is None:
                raise Exception("not have obj")
            new_dict = {
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "date_create": utils.Main.Datetime.get_format_time(dt=row[3]),
                "status_moderate": row[4]
            }
            return render_template("post.html", post=new_dict)


@app.route('/posts/create', methods=['GET', 'POST'])
def post_create():
    if request.method == "GET":
        return render_template("post_create.html")
    elif request.method == "POST":
        title = str(request.form.get("title")).strip()  # left-right remove \t \n " "
        description = str(request.form.get("description")).strip()
        date_create = datetime.datetime.now()  # timestamp
        status = "true" if request.form.get("status") is not None else "false"

        if len(title) < 5:
            raise Exception("title is too small")
        # keep-alive: 60 * 10 (RAM)
        with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                              host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
            connection.autocommit = False
            with connection.cursor() as cursor:  # syntax sugar
                try:
                    cursor.execute(f"insert into posts "
                                   f"(title, description, date_created, status) values "
                                   f"('{title}', '{description}', '{date_create}','{status}');")
                except Exception as error:
                    print("error: ", error)
                    cursor.rollback()
                else:
                    cursor.commit()
                finally:
                    return redirect(url_for("posts"))
    else:
        raise Exception("Method not allowed")


@app.route('/posts/<int:pk>/delete', methods=['GET', 'POST', 'DELETE'])  # primary key
def post_delete(pk):  # primary key
    with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                          host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
        connection.autocommit = False
        with connection.cursor() as cursor:  # syntax sugar
            try:
                cursor.execute(f"delete from posts where id='{pk}';")
            except Exception as error:
                print("error: ", error)
                cursor.rollback()
            else:
                cursor.commit()
            finally:
                return redirect(url_for("posts"))


@app.route('/posts/<int:pk>/update', methods=['GET', 'POST', 'DELETE', ''])  # primary key
def post_update(pk):
    if request.method == "GET":
        with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                              host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
            with connection.cursor() as cursor:  # syntax sugar
                cursor.execute(f"SELECT * FROM public.posts where id='{pk}';")
                row = cursor.fetchone()
                new_dict = {
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "date_create": utils.Main.Datetime.get_format_time(dt=row[3]),
                    "status_moderate": row[4]
                }
                return render_template("post_update.html", post=new_dict)
    if request.method == "POST":
        title = str(request.form.get("title")).strip()  # left-right remove \t \n " "
        description = str(request.form.get("description")).strip()
        status = "true" if request.form.get("status") is not None else "false"

        if len(title) < 5:
            raise Exception("title is too small")
        with psycopg2.connect(user="facebook_usr", password="12345Qwerty!",
                              host="127.0.0.1", port="5432", dbname="facebook_db") as connection:  # syntax sugar
            connection.autocommit = False
            with connection.cursor() as cursor:  # syntax sugar
                try:
                    cursor.execute(f"update posts "
                                   f"SET title='{title}', description='{description}', "
                                   f"status='{status}' where id='{pk}';")
                except Exception as error:
                    print("error: ", error)
                    cursor.rollback()
                else:
                    cursor.commit()
                finally:
                    return redirect(url_for("posts_id", pk=pk))


@app.route('/api/pay', methods=['POST'])
def pay():
    value = float(request.form.get("key"))
    return {"result": value**2}
