import sqlite3
from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse  # native django
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request  # DRF
from rest_framework.response import Response  # DRF
import re
from django_app import models, serializers


@api_view(http_method_names=["GET", "POST"])
def register(request: Request) -> Response:
    try:
        if request.method == "GET":
            return Response(data={"message": "Сюда можно отправить форму."}, status=status.HTTP_200_OK)
        elif request.method == "POST":
            first_name: str = request.data.get('first_name', '')
            if re.match(r'^(?=.*?[а-я])(?=.*?[А-Я])(?=.*?[0-9]).{4,}$', first_name):
                models.Resume.objects.create(first_name=first_name)
                return Response(data={"message": "Успешно!"}, status=status.HTTP_201_CREATED)
            return Response(data={"message": "Validation Error!"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(data={"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "POST"])
def register_old(request: Request) -> Response:
    try:
        if request.method == "GET":
            return Response(data={"message": "Отправьте сюда форму."}, status=status.HTTP_200_OK)
        elif request.method == "POST":
            # {"first_name":"Богдан 888", "last_name":"888"}
            print(request.GET)  # query params https://hh.ru/search/vacancy?text=Python&area=154
            print(request.POST)  # форма (multipart-form-data)
            print(request.FILES)  # файлы
            # print(request.body)  # форма в байтах
            print(request.data)  # форма в JSON
            form = request.data
            # {"first_name": "1Zzбб"}  # False
            # {"first_name": "Яябб"}  # False
            # {"first_name": "1Яя"}  # False
            # {"first_name": "1Яябб"}  # True
            # я хочу, чтобы first_name был в формате 1 цифра, 1 буква в двух регистрах, только кириллица
            # first_name.lower()
            # first_name.upper()
            # first_name.isascii()
            # first_name.isalpha()
            first_name = form.get('first_name', '')  # safe - default
            # валидация
            last_name = form['last_name']  # unsafe - Exception(KeyError)
            if re.match(r'^(?=.*?[а-я])(?=.*?[А-Я])(?=.*?[0-9]).{4,}$', first_name):
                models.Resume.objects.create(first_name=first_name)
                resume = models.Resume.objects.create(
                    first_name=first_name
                )
                # return JsonResponse(data={"message": "Успешно!"}, safe=True)  # Expected type 'Response', got 'JsonResponse' instead
                return Response(data={"message": "Успешно!"}, status=status.HTTP_201_CREATED)
            return Response(data={"message": "Validation Error!"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(data={"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
def resume_list(request: Request) -> Response:
    try:
        # http://127.0.0.1:8000/resume/list/?search=Бо
        search = str(request.GET.get("search", "")).strip()
        resumes_objs = models.Resume.objects.filter(first_name__icontains=search)
        resumes_json = serializers.ResumeSerializer(resumes_objs, many=True).data
        return Response(data={"resumes": resumes_json}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(data={"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["GET"])
def resume_list_old(request: Request) -> Response:
    try:
        print(request.GET)
        resumes_objs = models.Resume.objects.all()  # <class 'django.db.models.query.QuerySet'>

        # todo native serialization ####################################################################
        # медленнее, менее гибко, много повторяющегося кода
        # resumes = []
        # for resumes_obj in resumes_objs:
        #     new_dict = {"id": resumes_obj.id, "first_name": resumes_obj.first_name}
        #     resumes.append(new_dict)
        # todo native serialization ####################################################################
        resumes_json = serializers.ResumeSerializer(resumes_objs, many=True).data
        return Response(data={"resumes": resumes_json}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(data={"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

def resume_list_mvt(request: HttpRequest) -> HttpResponse:
    try:
        # filter - фильтрация, т.е. выбор нужных данных
        # search - поиск, т.е. выбор нужных данных
        # order - сортировка, т.е. порядок отображения
        # cache - использование старых данных, для ускорения
        # пагинация - разделение данных на порции(страницы)
        # print(request.GET)
        resumes = models.Resume.objects.all()  # filter(), order_by()...
        return render(request, "resume_list.html", context={"resumes": resumes})
    except Exception as error:
        return render(request, "resume_list.html", context={"error": str(error)})

def register_mvt(request: HttpRequest) -> HttpResponse:
    try:
        context = {}
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


def register_mvt_old(request):
    try:
        context = {}
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
            context = {"success": "Успешно создано!"}
            # native for Django
        #         cursor = connection.cursor()
        #         query = """
        # INSERT INTO resume_model_table (first_name)
        # VALUES (%s)
        # """
        #         cursor.execute(query, (first_name,))
        #         connection.commit()

        # native - встроенный
        #         with sqlite3.Connection("db.sqlite3") as connection:
        #             cursor = connection.cursor()
        #             query = """
        # INSERT INTO resume_model_table (first_name)
        # VALUES (?)
        # """
        #             cursor.execute(query, (first_name,))
        #             connection.commit()

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

