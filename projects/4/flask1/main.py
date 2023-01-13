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


@app.route('/')
def home():
    name = "Python"
    return render_template("home.html", name=13, name_2="Marina")


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
