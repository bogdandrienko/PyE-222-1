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


def saves(request):
    try:
        # todo START TRANSACTION
        transaction.savepoint('create user')  # создание контрольной точки (КТ)
        User.objects.create(username="Admin")
        print(1 / 0)  # error
    except Exception as error:
        print(error)

        transaction.savepoint('again create user')
        User.objects.create(username="Admin")
        transaction.savepoint_commit('again create user')

        transaction.savepoint_rollback('create user')  # отмена КТ
    else:
        transaction.savepoint_commit('create user')  # сохрание КТ
    finally:
        pass

    return HttpResponse("<h1>Книга успешно создана!</h1>")


def create(request):
    # Book(title)

    # single create
    """
INSERT INTO django_book
(title)
VALUES
('Война и мир')
    """  # TODO SQL injection!
    models.Book.objects.create(title='Война и мир')
    # single create

    # mass create
    """
INSERT INTO django_book
(title)
VALUES
('Война и мир'), 
('Война и мир 2'), 
('Война и мир 3')
    """  # TODO SQL injection!

    """
    INSERT INTO django_book
    (title)
    VALUES
    ('Война и мир')
        """  # * 10 loop

    for i in range(1, 100):
        models.Book.objects.create(title=f'Война и мир {i}')  # todo TOO many requests!

    list_objects_for_create: list[Book] = []
    for i in range(1, 100):
        book1 = models.Book(title=f'Война и мир {i}')  # нет запроса к БД, создание идёт в RAM
        list_objects_for_create.append(book1)
    # 10000 - за раз слишком много
    # по 1 - за раз слишком долго и много запросов
    # нужно, исходя из "условного" размера сущности выбрать размер "пачки"(batch_size) = 30
    # 10000 / 30 = 300 отправок
    models.Book.objects.bulk_create(list_objects_for_create, batch_size=30)
    # mass create

    return HttpResponse("<h1>Книга успешно создана!</h1>")


def read(request):
    # выборка всех объектов из таблицы
    """
select * from public.django_app_book;
"""
    books = models.Book.objects.all()

    # выборка всех объектов из таблицы по условию(фильтрация)
    """
select * from public.django_app_book where title='Война и мир';
"""
    books = models.Book.objects.filter(title='Война и мир')

    # выборка всех данных, и сортировка по двум критериям
    """
select * from public.django_app_book ORDER BY title ASC, id DESC;
"""
    books = models.Book.objects.order_by('title', '-id')

    # выборка первых двух объектов из таблицы
    """
select * from public.django_app_book WHERE R <= 2;
"""
    books = models.Book.objects.all()[:2]

    # берёт один объект по id (фильтрация)
    """
select * from public.django_app_book WHERE id = 2;
"""
    books = models.Book.objects.get(id=2)

    # выбор всех объектов, которые по title начинаются с Война...
    """
SELECT * from public.django_app_book WHERE title LIKE 'Война%';
"""
    books = models.Book.objects.filter(title__startswith='Lennon')  # Война%
    books = models.Book.objects.filter(title__endswith='Lennon')  # %Война
    books = models.Book.objects.filter(title__icontains='Lennon')  # %Война% - регистронезависимый
    books = models.Book.objects.filter(title__contains='Lennon')  # %Война%

    # выборка объектов по id между 2 и 10 (фильтрация)
    """
select * from public.django_app_book WHERE id BETWEEN 2 AND 10;
"""
    books = models.Book.objects.filter(id__gte=2, id__le=10)  # gte - greater than | le - lower than | eq = equal

    # выборка объектов исключая дату старше 2005-1-3 и
    """
SELECT * from public.django_app_book
WHERE NOT (pub_date > '2005-1-3' AND title = 'Война')
"""
    books = models.Book.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), title='Война')

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/
    # books = models.Book.objects.all().filter(title__startswith='Lennon').exclude(pub_date__gt=datetime.date(2005, 1, 3)).filter(title='Война и мир').order_by('title', '-id')[:2]

    return HttpResponse("<h1>Книга успешно создана!</h1>")


def update(request):
    # simple single update
    """
UPDATE public.django_app_book
SET t1.title = t1.title || t1.id || '_обновление'
WHERE id = 24
(SELECT id, title from public.django_app_book
WHERE id = 24
) t1
"""
    # получить объект из базы
    book = Book.objects.get(id=24)
    # изменить нужные поля
    book.title = book.title + book.id + '_обновление'
    # ...
    # применить изменения в базу
    book.save()

    # mass update
    """
UPDATE public.django_app_book 
SET title = title || '_новое поступление' 
where title='Война и мир';
    """

    # todo СЛИШКОМ МНОГО ЗАПРОСОВ
    for i in models.Book.objects.filter(title='Война и мир'):
        i.title = i.title + "_новое поступление"
        i.save()

    list_ignore = [1, 2, 3, 4, 7]

    update_list = []
    for i in models.Book.objects.filter(title='Война и мир'):
        if i.id in list_ignore:
            continue
        i.title = i.title + "_новое поступление"
        update_list.append(i)
    models.Book.objects.bulk_update(update_list, batch_size=50)
    # mass update

    return HttpResponse("<h1>Книга успешно создана!</h1>")


def delete(request):
    # single delete
    """
DELETE FROM public.django_app_book
where id=1
"""
    models.Book.objects.get(id=1).delete()

    # mass delete
    """
DELETE FROM public.django_app_book
where title='Война и мир'
"""
    models.Book.objects.filter(title='Война и мир').delete()

    return HttpResponse("<h1>Книга успешно создана!</h1>")
