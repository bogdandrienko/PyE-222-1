from django.db import models
from django.utils import timezone

# todo ВСЕ ФАЙЛЫ 'models.py' - ЭТО БАЗА ДАННЫХ

table_for_clients = """
create table Clients
(
id int AUTOINCREMENT
username string (VARChar500)
password string (VARChar500)
email string (VARChar500)
number int (VARChar500)
name string (VARChar500)
...
)
"""

table_for_workers = """
create table Workers
(
id int AUTOINCREMENT
username string (VARChar500)
password string (VARChar500)
email string (VARChar500)
number int (VARChar500)
name string (VARChar500)
...
)
"""


class Requests(models.Model):  # todo ТАБЛИЦА
    # id = models.BigAutoField() - default
    #

    client = models.CharField(
        # db_column="requests_client_db_column",  # имя колонки в SQL
        # db_index=True,  # создавать или нет индекс для колонки
        # db_tablespace="created_db_tablespace",
        # error_messages=False,
        primary_key=False,  # является ли это поле первичный ключом
        unique=False,  # ограничение на количество в этой таблице
        editable=True,  # можно ли поле менять после вставки
        blank=True,  # доступно ли для ввода
        null=True,  # может ли поле быть нулевым
        default="Аноним",  # стандартное значение для колонки
        verbose_name="Клиент",  # имя столбца в админ-панели
        help_text='<small class="text-muted">строка</small><hr><br>',  # вспомогательный текст в админ-панели

        #

        max_length=200,  # максимальная длина для Char
    )  # todo ЗАГЛУШКА - models.ForeignKey

    #
    title = models.CharField("Название", max_length=500)
    description = models.TextField("Описание")
    # worker = models.CharField(max_length=200)  # todo ЗАГЛУШКА - models.ForeignKey
    is_success = models.BooleanField(default=False, null=False)
    # additions_image = models.ImageField(upload_to="requests/images")  # %d
    # additions_files = models.FileField(upload_to="requests/additions")  # %d
    date = models.DateField("дата", auto_now=True)
    # time = models.TimeField()
    price = models.DecimalField(
        verbose_name="Цена обращения",  # имя столбца в админ-панели
        help_text='<small class="text-muted">сумма</small><hr><br>',  # вспомогательный текст в админ-панели

        #

        max_digits=12,
        decimal_places=2
    )
    datetime = models.DateTimeField(
        verbose_name="Дата и время создания",  # имя столбца в админ-панели
        help_text='<small class="text-muted">сумма</small><hr><br>',  # вспомогательный текст в админ-панели
        default=timezone.now,

        #

        # auto_now=False,  # каждый раз, когда модель сохраняется (updated)
        # auto_now_add=False,  # один раз, когда модель добавляется (created)
        # auto_created=False,
    )
    # updated = models.DateTimeField(
    #     auto_now=True
    # )
    # created = models.DateTimeField(
    #     auto_now_add=True
    # )

    class Meta:
        app_label = "django_app"
        ordering = ("-is_success", "-datetime", "title")  # '-' - DESC | ORDER BY is_success DESC, datetime DESC, title ASC
        verbose_name = "Запрос к юристам"
        verbose_name_plural = "Запросы к юристам"

    def __str__(self):
        return f"ОБЪЕКТ {self.title} {self.datetime} {self.is_success} {self.price}"

    # CRUD -


table_for_requests = """
create table Requests 
(
id int AUTOINCREMENT
client PrimaryKey (OneToMany | Foreign key | Вторичный/внешний ключ) -> Client(id)
title string (VARChar500)
description string (VARChar)
worker PrimaryKey (OneToMany | Foreign key | Вторичный/внешний ключ) -> Workers(id)
datetime datetime
)
"""

# ORM - вместо SQL можно использовать python
