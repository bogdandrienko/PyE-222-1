from django.db import models
from django.utils.timezone import now


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "title")
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Complaint(models.Model):
    username = models.CharField(max_length=300, verbose_name="Имя пользователя")
    text = models.TextField(max_length=3000, verbose_name="Описание")
    type = models.CharField(max_length=300, verbose_name="Тип жалобы")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    date_time = models.DateTimeField(default=now, verbose_name="Дата и время подачи")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "date_time", "type")
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    def __str__(self):
        return self.text[:30]


class Cities(models.Model):
    LIST_DB_VIEW_CHOICES = [("0", "Пункт отправки"), ("1", "Пункт сортировки"), ("2", "Пункт приёма")]

    name = models.CharField(max_length=300, verbose_name="Наименование")
    index = models.CharField(max_length=300, verbose_name="Индекс города", unique=True)
    type = models.CharField(max_length=300, verbose_name="Тип отделения(сортировка/приём)", choices=LIST_DB_VIEW_CHOICES, default="0")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "type", "name")
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"

    def __str__(self):
        return self.name
