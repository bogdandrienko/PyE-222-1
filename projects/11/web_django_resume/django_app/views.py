import sqlite3
from django.db import connection
from django.shortcuts import render
from django_app import models


def register(request):
    try:
        if request.method == "POST":
            form = request.POST
            first_name = form.get('first_name', '')  # safe - default
            last_name = form['last_name']  # unsafe - Exception(KeyError)
            resume = models.Resume.objects.create(
                first_name=first_name
            )
        context = {"success": "Успешно создано!"}
        return render(request, "register.html", context=context)
    except Exception as error:
        context = {"error": str(error)}
        return render(request, "register.html", context=context)


def register_old(request):
    try:
        if request.method == "POST":
            print(request.GET)  # query params https://hh.ru/search/vacancy?text=Python&area=154
            print(request.POST)  # форма
            print(request.FILES)  # файлы
            # print(request.body)  # форма в байтах
            """
            <QueryDict: {'csrfmiddlewaretoken': ['2ctlNCfvyz0zJvk1vuPHTzqvQGpSRh7UAlVWgsrMfwXOjudJeXM5uNgeaKASwmJk'], 
            'first_name': ['Богдан'], 'last_name': ['Андриенко'], 'datetime': ['2023-09-13'], 'education': ['Высшее']}>
            """
            form = request.POST
            first_name = form.get('first_name', '')  # safe - default
            last_name = form['last_name']  # unsafe - Exception(KeyError)

            # ORM for django
            resume = models.Resume.objects.create(
                first_name=first_name
            )
            # raise Exception("Пользователь с таким ИИН уже есть!")
            # if resume.id % 2 == 0:
            #     resume.delete()

            # native for Django
        #         cursor = connection.cursor()
        #         query = f"""
        # INSERT INTO resume_model_table (first_name)
        # VALUES (%s)
        # """
        #         cursor.execute(query, (first_name,))
        #         connection.commit()

        # native - встроенный
        #         with sqlite3.Connection("db.sqlite3") as connection:
        #             cursor = connection.cursor()
        #             query = f"""
        # INSERT INTO resume_model_table (first_name)
        # VALUES (?)
        # """
        #             cursor.execute(query, (first_name,))
        #             connection.commit()
        context = {"success": "Успешно создано!"}
        return render(request, "register.html", context=context)
    except KeyError as error:
        context = {"error": f"Неизвестная ошибка. Не пытайся взломать поля: {error}"}
        return render(request, "register.html", context=context)
    except Exception as error:
        context = {"error": str(error)}
        return render(request, "register.html", context=context)


def example():
    # todo ООП: НАСЛЕДОВАНИЕ
    class Worker:
        def get_zarplata(self):
            print("Я хочу денег")

    class Buh(Worker):
        def get_zarplata(self):
            print("Я даю денег")

    class Sys(Worker):
        pass

    class Designer(Worker):
        pass

    d1 = Designer()
    d1.get_zarplata()


def test_database():
    with sqlite3.Connection("../db.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM resume_model_table")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
# test_database()
