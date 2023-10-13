from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.db import transaction
from django_app import models
import re

from django_app.models import Book

"""
Несколько операций, связанных между собой, должны выполнятся в рамках транзакции,
т.к. даже успешное выполнение первых, но отказ последующих должно вызывать откат изменений:
перевод средств другому человеку.
"""

"""
SELECT * FROM books

BEGIN TRANSACTION;
    BEGIN
        -- действие 1
        insert into books (title) values ('новый')
        -- действие 2
        insert into books (title) values ('новый4')

        -- SELECT COUNT(*) FROM books  -- можно делать ROLLBACK и при не соответствии логики

        COMMIT TRANSACTION;
    EXCEPTION WHEN OTHERS  
    THEN
        ROLLBACK TRANSACTION;
    END
END

SELECT * FROM books;
"""


@transaction.atomic  # атомарные запросы - каждый запрос индивидуален
# @transaction.non_atomic_requests  # не атомарные запросы
def home(request):
    """
    Атомарный режим: каждый запрос сам по себе, т.е. если второй запрос вызовет ошибку,
    первый всё равно запишет данные в базу.

    Не атомарный режим: если функция не отработает успешно до конца, то все запросы отменятся.
    """

    # 1
    # User.objects.create(username="User1", password=make_password("Qwerty!12345"))

    # 2
    # Book.objects.create(title="Название1")

    # print(1/0)

    return HttpResponse("OK")


def create(request):
    try:
        # todo START TRANSACTION
        transaction.set_autocommit(False)  # todo ! django default = autocommit = TRUE !
        print("ДО добавления книги")
        Book.objects.create(title="Название1")
        print("ПОСЛЕ добавления книги")

        # todo danger action
        # print(1 / 0)
        # todo danger action

        transaction.commit()  # применение изменений в базе
        return HttpResponse("<h1>Книга успешно создана!</h1>")
    except Exception as error:
        print(f"[ERROR] ({datetime.datetime.now()}): ", error)
        transaction.rollback()  # откатить все изменения в базе после начала транзакции
        return HttpResponse(f"<h1>Ошибка создания {error}</h1>")


