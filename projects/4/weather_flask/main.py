import datetime
from collections import OrderedDict
from decimal import Decimal
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


@app.route('/get_string')
def get_string():
    value = 12
    return f'get_string {value}'  # interpolation


@app.route('/get_html_string')
def get_html_string():
    return '<h1>get_html_string</h1>' + '<li>123</li>'  # concatenation


@app.route('/get_json')
def get_json():

    list2 = [
        "wrgwrgwrg\n",
        "wrgwrgwrg\n",
        "wfgwgwrgerwg\n",
        "wrgrwgwrg\n",
        "wrgrwgrwg\n"
    ]

    elem1 = 8
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # O(n)
    for i in list1:
        if i == elem1:
            print("find!")
    return {"data": False, "d": {"data": False, "value": 12}, "value": 12}  # O(1)


@app.route('/get_html_file')
def get_html_file():
    return render_template("html_file.html")


@app.route('/get_html_with_data')
def get_html_with_data():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    pers1 = Person(name="Anya", age=12)
    print(pers1.name)
    print(pers1.age)

    data1 = "PyE222/1"
    data2 = {"user": "Alica", "age": 22}
    data3 = {"result": 80, "success": False}
    data4 = [{"result": 80, "name": "Anya"}, {"result": 40, "name": "Ivan"}, {"result": 120, "name": "Luci"}]
    return render_template(
        "html_file2.html",
        name_for_jinja1=data1,
        name_for_jinja2=data2,
        name_for_jinja3=data3,
        name_for_jinja4=data4
    )


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


@app.route('/get_html_from_web')
def get_html_from_web():
    # sep2 = "is"
    # words = "Python is awesome"
    # arr = words.split(sep=sep2)
    # print(arr, type(arr))
    response = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers)
    # response = requests.get("https://www.gismeteo.kz/weather-lagos-6834/", headers=headers)
    text1 = response.text  # bytes1 = response.content.decode()

    sep1 = '<div class="date">Сейчас</div>'
    text2 = text1.split(sep=sep1)[1]

    sep2 = '</div></div><svg class'
    arr3 = text2.split(sep=sep2)
    text3 = arr3[0]

    sep3 = 'class="unit unit_temperature_c">'
    text4 = text3.split(sep=sep3)[-2::]

    sep4 = '</span>'
    arr = []
    for i in text4:
        arr.append(i.split(sep=sep4)[0].replace("&minus;", "-"))

    arr[0], arr[1] = "День: " + arr[1], "Ночь: " + arr[0]

    return render_template("html_file3.html", text=arr)


@app.route('/get_html_from_money/<int:ml>')
def get_html_from_money(ml=1):
    response = requests.get("https://finance.rambler.ru/calculators/converter/1-KZT-USD/", headers=headers)
    soup_instance = BeautifulSoup(response.text, 'html.parser')
    soup_obj = soup_instance.find_all('div', class_="converter-display__value")[-1]
    valute_text = soup_obj.get_text()
    current = round(float(valute_text), 1)
    result = ml * current
    return render_template("html_file4.html", current=current, result=result)


@app.route('/get_html_form', methods=['GET', 'POST'])
def get_html_form():
    name = ""
    surname = ""
    if request.method == "POST":
        name = request.form.get("name_form", "")
        surname = request.form.get("surname_form", "")

        with open("data.txt", "a", encoding='utf-8') as file:
            file.write(f"{name} {surname} {datetime.datetime.now()} \n")

    return render_template("html_file5.html", surname=surname, name=name)
