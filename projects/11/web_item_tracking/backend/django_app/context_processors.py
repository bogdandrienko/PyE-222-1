"""Контекстный процессор (работает на ВСЕХ HTML-шаблонах)
todo ! БОЛЬШАЯ НАГРУЗКА
"""
import datetime
from django.core.cache import caches
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils import timezone
from django_app import models


def get_book_count(request: HttpRequest) -> dict[str, any]:
    """Возвращает количество одобренных книг на веб-платформе."""

    return {"book_count": models.Mem.objects.filter(is_moderate=True).count()}


def get_news_count(request: HttpRequest) -> dict[str, any]:
    all_news_count = models.News.objects.all().filter(is_ban=False)
    now = timezone.now() - datetime.timedelta(minutes=30)
    fresh_count = [x for x in all_news_count if x.date_time > now]
    return {"all_news_count": all_news_count.count(), "fresh_count": len(fresh_count)}


def get_complete_item(request: HttpRequest) -> dict[str, any]:
    # complete_item = 0
    # in_progress_item = 0
    # if request.user.is_authenticated:
    #     user: User = request.user
    #     find = models.Find.objects.filter(user=user)
    #     if len(find) > 0:
    #         find = find[0]
    #         complete_item = find.tracks.all().filter(status="3").count()
    #         in_progress_item = find.tracks.all().filter(status="1").count()
    # return {"complete_item": complete_item, "in_progress_item": in_progress_item}

    # news = utils.CustomCache.caching(
    #     key="news_list", timeout=2, lambda_func=lambda: models.News.objects.all().filter(is_ban=False).filter(title__icontains=search)
    # )

    cache = caches["default"]
    data = cache.get(f"get_complete_item {request.user.username}")
    if data is None:
        complete_item = 0
        in_progress_item = 0
        if request.user.is_authenticated:
            user: User = request.user
            find = models.Find.objects.filter(user=user)
            if len(find) > 0:
                find = find[0]
                complete_item = find.tracks.all().filter(status="3").count()
                in_progress_item = find.tracks.all().filter(status="1").count()
        data = {"complete_item": complete_item, "in_progress_item": in_progress_item}
        cache.set(f"get_complete_item {request.user.username}", data, timeout=30)
    return data
