"""Контроллеры."""
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models


def home(request: HttpRequest) -> HttpResponse:
    """Возврат домашней страницы."""

    return render(request, "django_app/home.html")


def register_view(request: HttpRequest) -> HttpResponse:
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


def login_view(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт пользователя."""

    if request.method == "GET":
        return render(request, "django_app/login.html")
    elif request.method == "POST":
        print("ПОПЫТКА ВОЙТИ В АККАУНТ")

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(
            request, username=email, password=password
        )  # пытается, взять из базы этого пользователя с этим паролем
        print(user)
        if user is None:
            return render(
                request,
                "django_app/login.html",
                {"error": "Некорректный email или пароль"},
            )
        login(request, user)  # сохраняет токен в кукесы(cookies)
        return redirect(reverse("home"))
    else:
        raise ValueError("Invalid method")


def logout_view(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


def list_view(request: HttpRequest) -> HttpResponse:
    """_view"""

    memes = models.Mem.objects.all()

    # фейковые данные
    # images = [
    #     {"id": x, "title": f"Наименование {x} Alema", "image": "img/error.jpg"}
    #     for x in range(1, 10+1)
    # ]
    return render(request, "django_app/list.html", {"images": memes})


def detail_view(request: HttpRequest, pk: str) -> HttpResponse:
    """_view"""
    return redirect(reverse("login"))


def create_view(request: HttpRequest, pk: str) -> HttpResponse:
    """_view"""
    return redirect(reverse("login"))


def list_memes(request):
    """Возврат списка мемов."""

    name = "Айгерим"
    # _ = """
    # SELECT * from memes
    # WHERE is_moderate=True
    # ORDER BY date_time DESC
    # """
    memes = models.Mem.objects.all().filter(is_moderate=True).order_by("-date_time")  # SQL
    return render(request, "django_app/list_memes.html", context={"name": name, "memes": memes})


def create_mem(request):
    """Создание нового мема."""

    if request.method == "GET":
        return render(request, "django_app/create_mem.html")
    elif request.method == "POST":
        title = request.POST.get("title", None)
        avatar = request.FILES.get("avatar", None)
        models.Mem.objects.create(author=request.user, title=title, description="", image=avatar)  # SQL
        return redirect(reverse("list_memes"))
    else:
        raise ValueError("Invalid method")



def update_mem(request, pk: str):
    """Обновление существующего мема."""

    if request.method == "GET":
        mem = models.Mem.objects.get(id=int(pk))  # SQL
        mem.title = mem.title[::-1]
        # mem.is_moderate = False
        mem.save()
        return redirect(reverse("list_memes"))
    else:
        raise ValueError("Invalid method")


def delete_mem(request, pk: str):
    """Удаление мема."""

    if request.method == "GET":
        mem = models.Mem.objects.get(id=int(pk))  # SQL
        mem.delete()
        return redirect(reverse("list_memes"))
    else:
        raise ValueError("Invalid method")