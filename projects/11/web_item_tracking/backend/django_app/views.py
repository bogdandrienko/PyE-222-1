import re
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models, utils


# TODO PUBLIC #################################################################################################


def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={"message": "OK"}, safe=False)


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "django_app/home.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "django_app/about.html", context=context)


def pricing(request: HttpRequest) -> HttpResponse:
    def example():
        search = str(request.POST.get("search", ""))
        price_list = models.Product.objects.filter(is_active=True, title__icontains=search)  # ORM

        # models.Product.objects.filter(is_active=True, title__icontains=search)

        print("Часть названия для поиска: ", search)

        query = f"""
    SELECT * FROM django_app_product WHERE {search};
    """  # SELECT name FROM sqlite_master WHERE type='table';
        print("query: ", query)

        # TODO RAW
        # price_list = models.Product.objects.filter(is_active=True, title__icontains=search)  # ORM
        query = f"""
    SELECT id, title, description, price, is_active, image 
    FROM django_app_product
    WHERE is_active = True AND title LIKE %s
    """
        with connection.cursor() as cursor:
            cursor.execute(query, (f"%{search}%",))
            results = cursor.fetchall()
            """
    [
    (1, 'Доставка очень мелких грузов', 'до 5 кг, цена указана за 1 кг с округлением вверх', 
    600, True, None), 

    (2, 'Доставка мелких животных', 'до 500 кг, цена указана за 1 кг с округлением вверх', 
    60000, True, 'images/products/vizok-vantazhniy-s-bortami-1-e1608142879333.jpg')
    ]

            """
            price_list_new = []
            for i in results:
                new_dict = {
                    "id": i[0],
                    "title": i[1],
                    "description": i[2],
                    "price": i[3],
                    "is_active": i[4],
                    "image": i[5],
                }
                price_list_new.append(new_dict)
            print(results)
            print(price_list_new)

    search = str(request.POST.get("search", ""))
    price_list_new = models.Product.objects.filter(is_active=True, title__icontains=search)  # ORM

    return render(request, "django_app/pricing.html", {"price_list": price_list_new, "search": search})


def register(request: HttpRequest) -> HttpResponse:
    """Регистрация пользователя."""

    if request.method == "GET":
        return render(request, "django_app/register.html")
    elif request.method == "POST":
        email = request.POST.get("email", None)  # Admin1@gmail.com
        password = request.POST.get("password", None)  # Admin1@gmail.com
        if (
            re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email) is None
            or re.match(
                r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!.]).*$",
                password,
            )
            is None
        ):
            return render(
                request,
                "django_app/register.html",
                {"error": "Некорректный формат email или пароль"},
            )
        try:
            User.objects.create(
                username=email,
                password=make_password(password),  # HASHING PASSWORD
                email=email,
            )
        except Exception as error:
            return render(
                request,
                "django_app/register.html",
                {"error": str(error)},
            )
        return redirect(reverse("login"))
    else:
        raise ValueError("Invalid method")


def login_(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт пользователя."""

    if request.method == "GET":
        return render(request, "django_app/login.html")
    elif request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=email, password=password)
        if user is None:
            return render(request, "django_app/login.html", {"error": "Некорректный email или пароль"})
        login(request, user)
        return redirect(reverse("home"))
    else:
        raise ValueError("Invalid method")


def complaint(request: HttpRequest) -> HttpResponse:
    """Жалобы и предложения."""

    if request.method == "GET":
        return render(request, "django_app/complaint.html")
    elif request.method == "POST":
        try:
            username = request.POST.get("username", None)
            text = request.POST.get("text", None)
            type_ = request.POST.get("type", None)

            models.Complaint.objects.create(
                username=str(username),
                text=str(text),
                type=str(type_),
            )
        except Exception as error:
            return render(
                request,
                "django_app/complaint.html",
                {"error": str(error)},
            )
        return redirect(reverse("home"))
    else:
        raise ValueError("Invalid method")


# TODO PUBLIC #################################################################################################

# TODO PRIVATE ################################################################################################


@utils.custom_login_required
def currency(request: HttpRequest) -> HttpResponse:
    """Выводить на страницу курс валют: доллар, юань, рубль"""

    def get_valute(soup_obj: BeautifulSoup, prefix):
        """Вытаскивает значение валюты по префиксу"""

        valute_link = soup_obj.find_all("a", href=prefix)[0]
        data_arr = valute_link.text.split(" ")
        valute_str = list(filter(lambda x: len(x) > 1, data_arr))[1]
        valute = float(valute_str.strip().replace(",", "."))

        # step_1 = soup_obj.find_all("a", href=prefix)  # <a href="prefix">
        # print(f"\n\n\n\nstep 1: ", step_1)
        #
        # step_2 = step_1[0]
        # print(f"\n\n\n\nstep 2: ", step_2)
        #
        # step_3 = step_2.text
        # print(f"\n\n\n\nstep 3: ", step_3)
        #
        # step_4 = step_3.split(" ")
        # print(f"\n\n\n\nstep 4: ", step_4)
        #
        # step_5 = filter(lambda x: len(x) > 1, step_4)
        # print(f"\n\n\n\nstep 5: ", step_5)
        #
        # step_6 = list(step_5)
        # print(f"\n\n\n\nstep 6: ", step_6)
        #
        # step_7 = step_6[1]
        # print(f"\n\n\n\nstep 7: ", step_7)
        #
        # step_8 = step_7.strip()
        # print(f"\n\n\n\nstep 8: ", step_8)
        #
        # step_9 = step_8.replace(",", ".")
        # print(f"\n\n\n\nstep 9: ", step_9)
        #
        # step_10 = float(step_9)
        # print(f"\n\n\n\nstep 10: ", step_10)

        # return step_10

        return valute

    value = int(request.POST.get("value", 0))

    text = requests.get("https://kase.kz/ru/currency/").text
    soup = BeautifulSoup(text, "html.parser")

    usd = get_valute(soup, "#USDKZT")
    cny = get_valute(soup, "#CNYKZT")
    rub = get_valute(soup, "#RUBKZT")

    return render(
        request,
        "django_app/currency.html",
        {
            "data": {
                "value": value,
                "usd": usd,
                "my_usd": round(value / usd, 2),
                "cny": cny,
                "my_cny": round(value / cny, 2),
                "rub": rub,
                "my_rub": round(value / rub, 2),
            }
        },
    )


@utils.custom_login_required
def coins(request: HttpRequest) -> HttpResponse:
    """Выводить на страницу курс крипто-валют"""

    data = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=" "market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"
    ).json()

    return render(
        request,
        "django_app/сoins.html",
        {
            "data": {
                "bit": data[0].get("current_price"),
                "ether": data[1].get("current_price"),
            }
        },
    )


@utils.custom_login_required
def news(request: HttpRequest) -> HttpResponse:
    """Выводить на страницу список новостей с чужого сайта"""

    # поиск
    # детальный просмотр
    # пагинация
    # кэш

    text = requests.get("https://tengrinews.kz/tengri-sport/").text
    news_list = []
    for i in text.split('a class="media__text-link"'):
        try:
            text = i.split("</a")[0].split(">")[1]
            if len(text) <= 10:
                continue
            if text.find("<html") > 0:
                continue
            news_list.append(text.replace("&quot;", "'"))
        except:
            pass

    return render(
        request,
        "django_app/news.html",
        {"news_list": news_list},
    )


@utils.custom_login_required
def logout_(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


@utils.custom_login_required
def sms(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    if request.method == "POST":
        text: str = request.POST["text"]
        print("Текст смс: ", text)
        with open("sms_s.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    return render(request, "django_app/sendsms.html", {"data": []})


@utils.custom_login_required
def track_start(request: HttpRequest) -> HttpResponse:
    """Запуск посылки."""

    if request.method == "GET":
        cities = models.Cities.objects.all().filter(is_active=True)
        context = {"cities": cities}
        return render(request, "django_app/track_start.html", context=context)
    elif request.method == "POST":
        try:
            point = request.POST["point"]
            print(type(point), point)

            # создать трек-код

            # username = request.POST.get("username", None)
            # text = request.POST.get("text", None)
            # type_ = request.POST.get("type", None)
            #
            # models.Complaint.objects.create(
            #     username=str(username),
            #     text=str(text),
            #     type=str(type_),
            # )
            pass
        except Exception as error:
            return render(
                request,
                "django_app/track_start.html",
                {"error": str(error)},
            )
        return redirect(reverse("track_start"))
    else:
        raise ValueError("Invalid method")


# TODO PRIVATE ################################################################################################
