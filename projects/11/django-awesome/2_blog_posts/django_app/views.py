import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models


# base
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "django_app/home.html", context={})


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


@login_required
def logout_(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


# posts
@login_required
def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.filter(is_active=True)
    selected_page = request.GET.get(key="page", default=1)
    limit_post_by_page = 3
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)
    return render(request, "django_app/post_list.html", context={"current_page": current_page})


@login_required
def post_search(request: HttpRequest) -> HttpResponse:
    search = str(request.POST.get("search", ""))
    posts = models.Post.objects.filter(is_active=True, title__icontains=search)
    return render(request, "django_app/post_search.html", {"posts": posts, "search": search})


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "django_app/post_create.html", context={})
    elif request.method == "POST":
        try:
            title = str(request.POST["title"])
            description = str(request.POST["description"])
            image = request.FILES["image"]

            models.Post.objects.create(
                author=request.user,
                title=title,
                description=description,
                image=image,
            )
        except Exception as error:
            return render(
                request,
                "django_app/post_create.html",
                {"error": str(error)},
            )
        return redirect(reverse("post_list"))
