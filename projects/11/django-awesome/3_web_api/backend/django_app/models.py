from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Worker(models.Model):
    """Таблица с полями и их настройками в базе данных"""

    iin = models.CharField(verbose_name="ИИН", unique=True, max_length=13)
    first_name = models.CharField(verbose_name="Имя", max_length=200)
    last_name = models.CharField(verbose_name="Фамилия", max_length=200)

    class Meta:
        app_label = "django_app"
        ordering = ("iin",)
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return f"<Worker {self.iin} {self.first_name} {self.last_name}>"


class Rating(models.Model):
    # {"user_id": 1354314, "value": 7, "post_id": 1354}
    post_id = models.BigIntegerField(verbose_name="Пост", unique=True)
    user_id = models.BigIntegerField(verbose_name="Пользователь")
    value = models.SmallIntegerField(verbose_name="Значение рейтинга", validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        app_label = "django_app"
        ordering = ("post_id", "user_id")
        verbose_name = "Отметка рейтинга"
        verbose_name_plural = "Отметки рейтинга"

    def __str__(self):
        return f"<Rating {self.post_id} {self.user_id} {self.value}>"

