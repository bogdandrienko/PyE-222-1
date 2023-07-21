"""Контроллеры(VIEW) - ЛОГИКА"""

import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app import models
from django_app import utils


def home(request: HttpRequest) -> HttpResponse:
    """Возврат домашней страницы."""

    return render(request, "django_app/home.html")


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


def logout_(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


def list(request: HttpRequest) -> HttpResponse:
    """Возврат списка публикаций с книгами."""

    list_books = utils.CustomCache.caching(key="list books", timeout=2,
                                           lambda_func=lambda: models.Mem.objects.all())
    # фейковые данные
    # memes = [
    #     {
    #         "id": x,
    #         "title": f"Наименование {x} Alema",
    #         "description": {"data1": {"price": random.randint(1, 1000000) + random.random()}},
    #         "image": "media/images/posts/error.jpg",
    #         "datetime": datetime.datetime.now(),
    #     }
    #     for x in range(1, 20 + 1)
    # ]
    current_page = utils.CustomPaginator.paginate(list_books, request, 15)
    return render(request, "django_app/list.html", {"current_page": current_page})


# news
def news_list(request):
    """Возврат списка новостей."""

    search = request.POST.get("search", "")
    news = utils.CustomCache.caching(key="news_list", timeout=2,
                                     lambda_func=lambda: models.News.objects.all().filter(is_ban=False).filter(
                                         title__icontains=search))
    current_page = utils.CustomPaginator.paginate(object_list=news, limit=3, request=request)
    return render(request, "django_app/news_list.html", context={"current_page": current_page, "search": search})


def news_detail(request, pk):
    """Возврат новости."""

    new = utils.CustomCache.caching(key="news_detail_" + str(pk), timeout=5,
                                    lambda_func=lambda: models.News.objects.get(id=int(pk)))
    comments = utils.CustomCache.caching(key="comments_news_detail_" + str(pk), timeout=1,
                                         lambda_func=lambda: models.NewsComments.objects.filter(news=new))
    current_page = utils.CustomPaginator.paginate(object_list=comments, limit=3, request=request)

    post_rating_objs = models.NewsRatings.objects.all().filter(post=new)
    rating = post_rating_objs.filter(status=True).count() - post_rating_objs.filter(status=False).count()
    count_r = post_rating_objs.count()

    return render(request, "django_app/news_detail.html", context=
    {"new": new, "current_page": current_page, "rating": {"rating": rating, "count_r": count_r}
     })


def news_comments_create(request, pk):
    """Создание комментария."""

    if request.method != "POST":
        raise Exception("Invalid method")

    news = models.News.objects.get(id=int(pk))
    user = request.user
    text = request.POST.get("text", "")
    models.NewsComments.objects.create(news=news, author=user, text=text)

    return redirect(reverse('news_detail', args=(pk,)))


def rating_change(request, pk, status):
    """Создаёт рейтинг к новости"""

    if request.method == "GET":
        post_obj = models.News.objects.get(id=int(pk))
        author_obj = request.user
        status = True if int(status) == 1 else False
        post_rating_objs = models.NewsRatings.objects.filter(post=post_obj, author=author_obj)
        if len(post_rating_objs) <= 0:
            models.NewsRatings.objects.create(post=post_obj, author=author_obj, status=status)
        else:
            post_rating_obj = post_rating_objs[0]
            if (status is True and post_rating_obj.status is True) or \
                    (status is False and post_rating_obj.status is False):
                post_rating_obj.delete()
            else:
                post_rating_obj.status = status
                post_rating_obj.save()
        return redirect(reverse('news_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")


#
#
#
#
#
#
#
#
#
#
#
#
#
#


def detail_view(request: HttpRequest, pk: str) -> HttpResponse:
    """_view"""
    return redirect(reverse("login"))


def create_view(request: HttpRequest) -> HttpResponse:
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
