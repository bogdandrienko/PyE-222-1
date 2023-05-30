import re

from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import hashlib


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        # print(request.POST)
        # TODO НУЖНО ВСЕГДА ПРОВЕРЯТЬ ДАННЫЕ

        email = request.POST.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise Exception(f"Ошибка ввода почты {email}")

        password = request.POST.get('password')
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$", email):
            raise Exception(f"Ошибка ввода почты {email}")

        username = request.POST.get('username')
        save = request.POST.get('save')
        sex = request.POST.get('sex')
        datetime = request.POST.get('datetime')  # .strftime("%Y-%m-%d %H:%M:%S")

        # todo WRITE TO TXT FILE
        # with open("static/users.txt", mode="a", encoding="utf-8") as file:
        #     file.write(f"{email} | {password} | {username} | {save} | {sex} | {datetime} |\n")

        with sqlite3.connect('database/db.db') as connection:
            cursor = connection.cursor()

            query = """
INSERT INTO users (username, email, password, sex) VALUES (?, ?, ?, ?)
            """
            # todo ОТКРЫТЫЕ ПАРОЛИ В БАЗЕ ХРАНИТЬ НЕЛЬЗЯ!
            hash_password = hashlib.sha256(password.encode()).hexdigest()
            args = (username, email, hash_password, sex)

            cursor.execute(query, args)
            connection.commit()
        return HttpResponse("Метод в процессе реализации")
    else:
        return HttpResponse("Метод не реализован")
