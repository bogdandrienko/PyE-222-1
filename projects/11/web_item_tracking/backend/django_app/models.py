import random

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from django_app import utils


# Create your models here.


class Product(models.Model):
    """"""

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
    """Жалобы пользователей"""

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
    """Список отделений"""

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


class Item(models.Model):
    """Основной товар для отслеживания"""

    #                        db       admin
    LIST_DB_VIEW_CHOICES = [("0", "На проверке"), ("1", "В пути"), ("2", "Сортировка"), ("3", "Ожидает получения"), ("4", "Доставлено")]

    track = models.CharField(max_length=500, verbose_name="Трек код", unique=True)

    status = models.CharField(max_length=300, verbose_name="Статус", choices=LIST_DB_VIEW_CHOICES, default="0")
    target = models.CharField(max_length=300, verbose_name="Пункт назначения")

    weight = models.DecimalField(verbose_name="Вес", max_digits=10, decimal_places=2)
    width = models.DecimalField(verbose_name="Ширина", max_digits=10, decimal_places=2)
    height = models.DecimalField(verbose_name="Высота", max_digits=10, decimal_places=2)
    depth = models.DecimalField(verbose_name="Глубина", max_digits=10, decimal_places=2)

    contact = models.CharField(max_length=300, verbose_name="Наименование")
    address = models.TextField(max_length=3000, verbose_name="Адрес")

    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)

    is_active = models.BooleanField(verbose_name="Активность", default=True)
    date_time_start = models.DateTimeField(default=now, verbose_name="Дата отправки")
    # date_time_planing = models.DateTimeField(verbose_name="Ожидаемая дата пребытия товара")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-status", "-date_time_start")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.address

    @staticmethod
    def track_generator() -> str:
        f1 = "NL"
        f2 = utils.generate_track(4, "1234567890")
        f3 = utils.generate_track(4, "1234567890")
        f4 = utils.generate_track(3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # f1  f2   f3   f4
        # NL-1354-1342-KJG

        # NL-5868-8592-OMC
        # NL-0085-6320-QTK
        # NL-1395-6601-RZP
        return f"{f1}-{f2}-{f3}-{f4}"

    @staticmethod
    def price_formul(**kwargs) -> float:
        """Формула на основании место назначения и веса, объёма..."""

        return random.randint(1000, 100000)

    def get_choice(self):
        status = self.status
        #                           k        v
        # LIST_DB_VIEW_CHOICES = [("0", "На проверке"), ("1", "В пути"),
        # ("2", "Сортировка"), ("3", "Ожидает получения"), ("4", "Доставлено")]
        for k, v in self.LIST_DB_VIEW_CHOICES:
            if k == status:
                return v


class Find(models.Model):
    """Закреплённые товары для отслеживания"""

    # ForeignKey(unique=True) === OneToOneField
    user = models.ForeignKey(verbose_name="Трек код", to=User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(verbose_name="Трек код", to=Item, null=True, blank=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("user",)
        verbose_name = "Отслеживание"
        verbose_name_plural = "Отслеживания"

    def __str__(self):
        return self.user.username


class IceCreamType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    ice_type = models.ForeignKey(verbose_name="Тип", to=IceCreamType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    category = models.ManyToManyField(verbose_name="Тип", to=BookCategory, blank=True)

    def __str__(self):
        return self.name
