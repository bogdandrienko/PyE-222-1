from django.shortcuts import render

from forum import models


# Домашняя
def home(request):
    return render(request, "forum/home.html")


# Просмотр списка
def posts(request):
    _posts = models.Post.objects.all()
    return render(request, "forum/posts.html", {"posts": _posts})

# Register
# Login/Logout

# Создание постов
# Создание категорий
# Поиск
# Фильтрация
# Детальный просмотр
# Комментирование
# Рейтинги

# URL -> VIEW -> MODEL -> TEMPLATE
