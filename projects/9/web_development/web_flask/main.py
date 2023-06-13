from flask import Flask
from flask import render_template

# flask --app main run --host=0.0.0.0 --port=8000 --debug

app = Flask(__name__, template_folder="templates")


@app.route("/")  # URL (ссылка)
def hello_world():  # VIEW (функция-контроллер)
    names = ["Инна", "Ольа", "Юля"]  # MODEL (база данных)
    return render_template('index.html', names=names)  # TEMPLATE (html/шаблонизатор)
