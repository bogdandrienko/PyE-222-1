from django.http import HttpRequest


def get_posts_count(request: HttpRequest) -> dict[str, any]:
    """Возвращает количество постов.

    Контекстный процессор (работает на ВСЕХ HTML-шаблонах) - лишняя нагрузка
    """

    # posts = models.Mem.objects.filter(is_moderate=True)
    # count = posts.count()
    # return {"book_count": count}

    return {"posts_count": 666}
