import datetime
import random
import re

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models
from django.core.cache import caches, CacheHandler

RamCache = caches["default"]
DatabaseCache = caches["extra"]


# base
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "django_app/home.html", context={})


def register(request: HttpRequest) -> HttpResponse:
    """Регистрация пользователя."""

    if request.method == "GET":
        return render(request, "django_app/register.html")
    elif request.method == "POST":
        email = str(request.POST.get("email", None)).strip()  # Admin1@gmail.com
        password = str(request.POST.get("password", None)).strip()  # Admin1@gmail.com
        valid_email = re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email)
        valid_password = re.match(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!.]).*$", password)

        # print(f"valid_email: ", valid_email)
        # print(f"valid_password: ", valid_password)

        if valid_email is None or valid_password is None:
            return render(
                request,
                "django_app/register.html",
                {"error": "Некорректный формат email или пароль"},
            )
        try:
            user = User.objects.create(
                username=email,
                password=make_password(password),  # HASHING PASSWORD
                email=email,
            )
            # user_profile = models.UserProfile.objects.create(
            #     user=user,
            # )
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


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        user = request.user
        user_profile = user.profile  # models.Post.objects.get(user=user)
        context = {"profile": user_profile}

        return render(request, "django_app/profile.html", context)


# posts
@login_required
def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.filter(is_active=True)
    selected_page = request.GET.get(key="page", default=1)
    limit_post_by_page = 3
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)
    return render(request, "django_app/post_list.html", context={"current_page": current_page, "is_detail_view": True})


@login_required
def post_list_simple(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.filter(is_active=True)
    selected_page = request.GET.get(key="page", default=1)
    limit_post_by_page = 3
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)
    return render(request, "django_app/post_list.html", context={"current_page": current_page, "is_detail_view": False})


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


@login_required
def post_detail(request: HttpRequest, pk: str) -> HttpResponse:
    # 1. Проверяем, нет ли объект-а в кэш-е
    # 1.1 Если есть, возвращаем кэш
    # 2. Получаем объект из базы данных
    # 2.1 Кэшируем объект
    # 2.2 Возращаем объект

    post = RamCache.get(f"post_detail_{pk}")
    if post is None:
        post = models.Post.objects.get(id=pk)  # тяжёлое обращение к базе данных -- 100x - 1000x
        RamCache.set(f"post_detail_{pk}", post, timeout=30)

    # Если мы поставили лайк - то закрашиваем кнопку
    # post + user

    comments = models.PostComments.objects.filter(post=post)
    ratings = models.PostRatings.objects.filter(post=post)
    ratings = {
        "like": ratings.filter(status=True).count(),
        "dislike": ratings.filter(status=False).count(),
        "total": ratings.filter(status=True).count() - ratings.filter(status=False).count(),
    }

    return render(request, "django_app/post_detail.html", context={"post": post, "comments": comments, "ratings": ratings, "is_detail_view": True})


@login_required
def post_hide(request: HttpRequest, pk: str) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    post.is_active = False
    post.save()
    return redirect(reverse("post_list"))


@login_required
def post_comment_create(request: HttpRequest, pk: str) -> HttpResponse:
    """Создание комментария."""

    post = models.Post.objects.get(id=int(pk))
    text = request.POST.get("text", "")
    models.PostComments.objects.create(post=post, author=request.user, text=text)

    return redirect(reverse("post_detail", args=(pk,)))


@login_required
def post_rating(request: HttpRequest, pk: str, is_like: str) -> HttpResponse:
    post = models.Post.objects.get(id=int(pk))
    is_like = True if str(is_like).lower().strip() == "лайк" else False  # тернарный оператор

    print(post)
    print(is_like)

    # 1. Поставил ли я лайк ранее?
    # 2. "Отжатие лайка"

    ratings = models.PostRatings.objects.filter(post=post, author=request.user)
    if len(ratings) < 1:
        models.PostRatings.objects.create(post=post, author=request.user, status=is_like)
    else:
        rating = ratings[0]
        if is_like == True and rating.status == True:
            rating.delete()
        elif is_like == False and rating.status == False:
            rating.delete()
        else:
            rating.status = is_like
            rating.save()

    return redirect(reverse("post_detail", args=(pk,)))


def user_password_recover_send(request):
    # Почта: восстановление пароля от аккаунта на почту

    """
    1. Человек потерял свой пароль, но знает почту/номер телефона(username)

    2. Кнопку, которая ведёт на страницу для сброса пароля.
    2.1 Просто посылаем ему сразу одноразовый пароль для восстановления.
    Не даём ничего делать, пока он на заменит пароль на постоянный.

    !danger! 3.1 В момент регистрации, записывать в профиль реальный пароль человека.

    """

    if request.method == "GET":
        context = {}
        return render(request, "django_app/user_password_recover_send.html", context)
    elif request.method == "POST":
        email = str(request.POST["email"]).strip()
        users = User.objects.filter(username=email)
        if len(users) < 1:
            context = {"error": "Неправильное имя пользователя/почта", "email": email}
            return render(request, "django_app/user_password_recover_send.html", context)

        """
        ОТПРАВКА ПИСЬМА это платно*, поэтому нужно будет потом придумать как ограничить
        
        
        1. SendPulse - 
        + гибко, есть html шаблоны, не блочится другими почтами...
        - платно, сложное api
        
        2. Яндекс smtp
        2.1 Создать яндекс аккаунт
        2.2 Зайти в настройки (https://id.yandex.kz/security/app-passwords) - пароль от SMTP сохранить
        2.3 Создать и настроить ENV-файл(переменные окружения)
        2.4 В Django задать переменные (EMAIL_HOST...)
        2.5 Отправить письмо через send_mail(...)
        + бесплатно, не блочится другими почтами
        - есть ограничения
        
        """
        try:
            m_from = settings.EMAIL_HOST_USER
            m_to = [email]
            m_subject = "Восстановление доступа к аккаунту"
            m_message = f"Ваш старый пароль: {users[0].password} {datetime.datetime.now()}"  # TODO
            # TODO HTML
            send_mail(m_subject, m_message, m_from, m_to)

            context = {"success": "На указанную почту отправлен код восстанвления! Следуйте инструкциям в письме."}
            return render(request, "django_app/user_password_recover_send.html", context)
        except Exception as error:
            return render(
                request,
                "django_app/user_password_recover_send.html",
                {"error": str(error)},
            )
