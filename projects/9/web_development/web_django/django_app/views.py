from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import random
from django_app import models


# base
def home(request: HttpRequest) -> HttpResponse:
    """Домашняя страница"""

    return render(request, "index.html", {})


def login_f(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт"""

    if request.method == "GET":
        return render(request, "login.html", {})
    elif request.method == "POST":
        email = request.POST.get('email')  # user@gmail.com
        password = request.POST.get('password')  # Qwerty!123

        # В первый раз, ты "предъявляешь" логин и пароль, система генерирует тебе токен на 15 минут, и следующие 15 минут "предъявляя" этот токен,
        # ты доказываешь что ты это ты. Система "автоматически" обновляет токен по истечению времени.

        # 1. конфиденциальность - пароль отправляется единожды.
        # 2. брутфорс сильно ослажняется.

        user = authenticate(request, username=email, password=password)  # пытается, взять из базы этого пользователя с этим паролем

        # 1       -> (хэш-функция) -> й3ащшаasdgfsdf124р12141431
        # Qwerty1!-> (хэш-функция) -> й3ащшар32щ1р43124р12141431
        # Qwerty! -> (хэш-функция) -> й3ащшар32щ1р43124р12542153
        if user is None:
            raise Exception("ДАННЫЕ ДЛЯ ВХОДА НЕПРАВИЛЬНЫЕ!")
        else:
            login(request, user)  # сохраняет токен в кукесы(cookies)
            return redirect(reverse('home'))
    else:
        raise Exception("Method not allowed!")


def logout_f(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""
    logout(request)
    return redirect(reverse('login'))


def register_f(request: HttpRequest) -> HttpResponse:
    """Создание нового аккаунта"""
    if request.method == "GET":
        return render(request, "register.html", {})
    elif request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        avatar = request.FILES.get('avatar')

        # TODO REGEX

        email = request.POST.get('email')

        # TODO REGEX

        password = request.POST.get('password')
        # User.objects.create(
        #     username=email,
        #     password=password,  # TODO DANGER!!!
        # )
        # User.objects.create_user(
        #     username=email,
        #     password=password,
        # )
        User.objects.create(
            username=email,
            password=make_password(password),
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect(reverse('login'))
    else:
        raise Exception("Method not allowed!")


# posts
def post_list(request: HttpRequest) -> HttpResponse:
    """Отображает все публикации"""
    search = request.POST.get('search')
    if search is None:
        posts_objs = models.Posts.objects.all().filter(is_moderate=True)
    else:
        posts_objs = models.Posts.objects.all().filter(is_moderate=True).filter(title__icontains=search)  # .filter(title="Гоголь")  # фильтрация
    return render(request, "list.html", {"list": posts_objs, "search": "" if search is None else search})


def post_create(request: HttpRequest) -> HttpResponseRedirect:
    """Создание новой публикации"""
    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        title = str(request.POST.get('title')).strip()
        print(title)
        if len(title) < 1:
            raise Exception("Слишком короткое название!")

        description = str(request.POST.get('description')).strip()
        models.Posts.objects.create(author=request.user.username, title=title, description=description)
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


def post_detail(request: HttpRequest, pk: str) -> HttpResponse:
    """Отображает публикацию подробно"""
    post_obj = models.Posts.objects.get(id=int(pk))
    post_comments_objs = models.PostComments.objects.all()

    # Получение рейтингов только для этого поста
    post_rating_objs = models.PostRatings.objects.all().filter(post=post_obj)
    # Получение только положительных рейтингов для этого поста
    likes = post_rating_objs.filter(status=True).count()
    # Получение только отрицательных рейтингов для этого поста
    dislikes = post_rating_objs.filter(status=False).count()
    # Итоговая разница
    rating = likes - dislikes
    count_r = post_rating_objs.count()

    return render(request, "detail.html", {"post": post_obj, "comments": post_comments_objs, "rating": rating, "count_r": count_r})


def post_change(request: HttpRequest, pk: str) -> HttpResponse:
    """Отображает публикацию подробно"""
    if request.method == "GET":
        post_obj = models.Posts.objects.get(id=int(pk))
        return render(request, "change.html", {"post": post_obj})
    elif request.method == "POST":
        post_obj = models.Posts.objects.get(id=int(pk))
        post_obj.title = request.POST.get('title')
        post_obj.description = request.POST.get('description')
        post_obj.is_moderate = False
        post_obj.save()
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


def post_delete(request: HttpRequest, pk: str) -> HttpResponseRedirect:
    """Удаляет существующую публикацию"""
    if request.method == "GET":
        post = models.Posts.objects.get(id=int(pk))
        post.delete()
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


# post comments
def post_comment_create(request: HttpRequest, pk: str) -> HttpResponseRedirect:
    """Создаёт комментарий к публикации"""
    # Проверка метода, т.к. форма приходит POST-методом
    if request.method == "POST":
        # Получение объекта поста
        post_obj = models.Posts.objects.get(id=int(pk))
        # TODO Выбор автора
        author = request.user.username
        # Получение текста комментария из форма
        text = request.POST.get('text')
        # Создание комментария в базе данных
        models.PostComments.objects.create(post_id=post_obj.id, author=author, text=text)
        # Перенаправление в случае успеха
        return redirect(reverse('post_detail', args=[pk]))
    else:
        # Возбуждение исключения в случае неправильного метода
        raise Exception("Method not allowed!")


# post ratings
def rating_change(request: HttpRequest, pk: str, status: str) -> HttpResponseRedirect:
    """Создаёт рейтинг к публикации"""
    if request.method == "GET":
        # Получение объекта-поста
        post_obj = models.Posts.objects.get(id=int(pk))
        # Получение объекта-автора
        author_obj = request.user
        # Получение статуса, который пользователь нажал
        status = True if int(status) == 1 else False
        # Получение всех рейтингов только для этого поста и этого автора
        post_rating_objs = models.PostRatings.objects.filter(post=post_obj, author=author_obj)
        # Если человек ещё не ставил рейтинг, то его надо создать. Иначе - изменить
        if len(post_rating_objs) <= 0:
            models.PostRatings.objects.create(post=post_obj, author=author_obj, status=status)
        else:
            post_rating_obj = post_rating_objs[0]
            if (status is True and post_rating_obj.status is True) or \
                    (status is False and post_rating_obj.status is False):
                post_rating_obj.delete()
            else:
                post_rating_obj.status = status
                post_rating_obj.save()
        return redirect(reverse('post_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")
