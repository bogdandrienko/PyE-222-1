"""Модели(MODELS) - ТАБЛИЦЫ В БАЗЕ ДАННЫХ С ДАННЫМИ"""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Mem(models.Model):
    """Таблица с мемами"""

    author = models.ForeignKey(to=User, max_length=200, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=200, unique=True)
    description = models.TextField("Описание", default="")
    image = models.ImageField("Изображение", upload_to="images/posts")
    date_time = models.DateTimeField("Дата и время создания", default=timezone.now)
    is_moderate = models.BooleanField("Прошёл ли модерацию", default=False)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-date_time", "title")
        verbose_name = "Мем"
        verbose_name_plural = "Мемы"

    def __str__(self):
        if self.is_moderate:
            status = "ОК"
        else:
            status = "НА ПРОВЕРКЕ"
        return f"{status} {self.title} {self.date_time} {self.title}"


class News(models.Model):
    """Таблица с новостями"""

    author = models.ForeignKey(to=User, max_length=200, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=200, unique=True)
    description = models.TextField("Описание", default="")
    image = models.ImageField("Изображение", upload_to="images/posts")
    date_time = models.DateTimeField("Дата и время создания", default=timezone.now)
    is_ban = models.BooleanField("Отключено ли отображение", default=False)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-date_time", "title")
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.title} {self.date_time} {self.description[:20]}"


class NewsComments(models.Model):
    """Комментарии к новостям"""

    news = models.ForeignKey(to=News, verbose_name="К какой новости", max_length=200, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Автор",max_length=200, on_delete=models.CASCADE)
    text = models.TextField("Текст комментария", default="")
    date_time = models.DateTimeField("Дата и время создания", default=timezone.now)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "news")
        verbose_name = "Комментарий к новости"
        verbose_name_plural = "Комментарии к новостям"

    def __str__(self):
        return f"{self.date_time} {self.author.username} {self.news.title} {self.text[:20]}"

#
# class PostRatings(models.Model):
#     """
#     """
#
#     author = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE  # удаление
#         # on_delete=models.DO_NOTHING  # ничего не делать
#         # on_delete=models.SET_DEFAULT  # установить в стандартное
#         # on_delete=models.SET_NULL  # установить в None
#     )
#     post = models.ForeignKey(
#         to=Posts,
#         on_delete=models.CASCADE
#     )
#     status = models.BooleanField(default=False)  # Лайк или дизлайк
#
#     class Meta:
#         app_label = "django_app"
#         ordering = ("-post", "author")
#         verbose_name = "Рейтинг к публикации"
#         verbose_name_plural = "Рейтинги к публикациям"
#
#     def __str__(self):
#         if self.status:
#             like = "ЛАЙК"
#         else:
#             like = "ДИЗЛАЙК"
#         return f"{self.post.title} {self.author.username} {like}"
