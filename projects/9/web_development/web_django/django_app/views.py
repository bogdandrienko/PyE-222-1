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
        user = authenticate(request, username=email, password=password)  # пытается, взять из базы этого пользователя с этим паролем
        if user is not None:
            login(request, user)  # сохраняет токен в кукесы(cookies)
            return redirect(reverse('home'))
        else:
            raise Exception("ДАННЫЕ ДЛЯ ВХОДА НЕПРАВИЛЬНЫЕ!")
    else:
        raise Exception("Method not allowed!")


def logout_f(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт"""
    logout(request)
    return redirect(reverse('login'))


# posts
def post_list(request: HttpRequest) -> HttpResponse:
    """Отображает все публикации"""
    search = request.POST.get('search')
    if search is None:
        posts_objs = models.Posts.objects.all()
    else:
        posts_objs = models.Posts.objects.all().filter(title__icontains=search)  # .filter(title="Гоголь")  # фильтрация
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
        author = random.choice(["Илья", "Абулхаир", "Арман"])
        models.Posts.objects.create(author=author, title=title, description=description)
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


def post_detail(request: HttpRequest, pk: str) -> HttpResponse:
    """Отображает публикацию подробно"""
    post_obj = models.Posts.objects.get(id=int(pk))
    post_comments_objs = models.PostComments.objects.all()
    post_rating_obj = models.PostRatings.objects.filter(post_id=post_obj.id)
    if len(post_rating_obj) <= 0:
        rating = 0
    else:
        rating = post_rating_obj[0].rating
    return render(request, "detail.html", {"post": post_obj, "comments": post_comments_objs, "rating": rating})


def post_change(request: HttpRequest, pk: str) -> HttpResponse:
    """Отображает публикацию подробно"""
    if request.method == "GET":
        post_obj = models.Posts.objects.get(id=int(pk))
        return render(request, "change.html", {"post": post_obj})
    elif request.method == "POST":
        post_obj = models.Posts.objects.get(id=int(pk))
        post_obj.title = request.POST.get('title')
        post_obj.description = request.POST.get('description')
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
        author = random.choice(["Дина", "Алема", "Айгерим"])
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
        post_obj = models.Posts.objects.get(id=int(pk))
        post_rating_objs = models.PostRatings.objects.filter(post_id=post_obj.id)
        if len(post_rating_objs) <= 0:
            models.PostRatings.objects.create(post_id=post_obj.id, rating=int(status))
        else:
            post_rating_objs[0].rating += int(status)
            post_rating_objs[0].save()
        return redirect(reverse('post_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")
