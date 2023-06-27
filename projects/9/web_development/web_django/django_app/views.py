from django.shortcuts import render, redirect
from django.urls import reverse
import random
from django_app import models


def home(request):
    """Домашняя страница"""

    # utils.logging(request)

    return render(request, "index.html", {})


def post_list(request):
    """Отображает все публикации"""

    # utils.logging(request)

    posts_objs = models.Posts.objects.all()
    return render(request, "list.html", {"list": posts_objs})


def post_create(request):
    """Создание новой публикации"""

    # utils.logging(request)

    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = random.choice(["Илья", "Абулхаир", "Арман"])
        models.Posts.objects.create(author=author, title=title, description=description)
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


def post_delete(request, pk):
    """Удаляет существующую публикацию"""

    # utils.logging(request)

    if request.method == "GET":
        post = models.Posts.objects.get(id=int(pk))
        post.delete()
        return redirect(reverse('posts'))
    else:
        raise Exception("Method not allowed!")


def post_detail(request, pk):
    """Отображает публикацию подробно"""

    # utils.logging(request)

    post_obj = models.Posts.objects.get(id=int(pk))
    post_comments_objs = models.PostComments.objects.all()
    post_rating_obj = models.PostRatings.objects.filter(post_id=post_obj.id)
    if len(post_rating_obj) <= 0:
        rating = 0
    else:
        rating = post_rating_obj[0]

    return render(request, "detail.html", {"post": post_obj, "comments": post_comments_objs, "rating": rating})


def post_change(request, pk):
    """Отображает публикацию подробно"""

    # utils.logging(request)

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


def post_comment_create(request, pk):
    """Создаёт комментарий к публикации"""

    # utils.logging(request)

    if request.method == "POST":
        post_obj = models.Posts.objects.get(id=int(pk))
        author = random.choice(["Дина", "Алема", "Айгерим"])
        text = request.POST.get('text')
        models.PostComments.objects.create(post_id=post_obj.id, author=author, text=text)
        return redirect(reverse('post_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")


def rating_like(request, pk):
    """Создаёт рейтинг к публикации"""

    # utils.logging(request)

    if request.method == "GET":
        post_obj = models.Posts.objects.get(id=int(pk))
        post_rating_objs = models.PostRatings.objects.filter(post_id=post_obj.id)
        if len(post_rating_objs) <= 0:
            models.PostRatings.objects.create(post_id=post_obj.id, rating=1)
        else:
            post_rating_objs[0].rating += 1
            post_rating_objs[0].save()

        return redirect(reverse('post_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")


def rating_dislike(request, pk):
    """Создаёт рейтинг к публикации"""

    # utils.logging(request)

    if request.method == "GET":
        post_obj = models.Posts.objects.get(id=int(pk))
        post_rating_objs = models.PostRatings.objects.filter(post_id=post_obj.id)
        if len(post_rating_objs) <= 0:
            models.PostRatings.objects.create(post_id=post_obj.id, rating=-1)
        else:
            post_rating_objs[0].rating -= 1
            post_rating_objs[0].save()

        return redirect(reverse('post_detail', args=[pk]))
    else:
        raise Exception("Method not allowed!")
