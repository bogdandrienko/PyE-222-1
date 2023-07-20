"""Контекстный процессор (работает на ВСЕХ HTML-шаблонах)
todo ! БОЛЬШАЯ НАГРУЗКА
"""
import datetime

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

