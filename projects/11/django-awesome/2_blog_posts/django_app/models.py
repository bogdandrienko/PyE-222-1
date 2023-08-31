from time import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    """Наша модель поста"""

    author = models.ForeignKey(verbose_name="Автор", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активность поста", default=True)
    date_time = models.DateTimeField(default=now, verbose_name="Дата и время подачи")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "title")
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"<Post {self.title} {self.author.username}>"


class PostComments(models.Model):
    """Комментарии к постам"""

    post = models.ForeignKey(to=Post, verbose_name="К какому посту", max_length=200, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Автор", max_length=200, on_delete=models.CASCADE)  # +-
    text = models.TextField("Текст комментария", default="")
    date_time = models.DateTimeField("Дата и время создания", default=now)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "post")
        verbose_name = "Комментарий к посту"
        verbose_name_plural = "Комментарии к постам"

    def __str__(self):
        return f"{self.date_time} {self.author.username} {self.post.title} {self.text[:20]}"


class PostRatings(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # OneToMany +-
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        app_label = "django_app"
        ordering = ("-post", "author")
        verbose_name = "Рейтинг к новости"
        verbose_name_plural = "Рейтинги к новостям"

    def __str__(self):
        if self.status:
            like = "ЛАЙК"
        else:
            like = "ДИЗЛАЙК"
        return f"{self.post.title} {self.author.username} {like}"
