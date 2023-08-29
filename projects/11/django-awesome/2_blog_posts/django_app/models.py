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
