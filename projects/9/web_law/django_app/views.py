import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models


def home(request):
    data = [{"id": x, "name": f"Алема {x}"} for x in range(1, 100 + 1)]
    return render(request, "django_app/home.html", context={"peoples": data})


# todo REQUESTS ###############################################
def get_requests(request):  # todo READ (many) - GET
    # вернуть все запросы

    # todo выборка
    select1_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    """
    # select1_orm = models.Requests.objects.all()
    # select1_orm[0].id
    # select1_orm[0].price
    # select1_orm[0].title
    # select1_orm[0].is_success
    # todo выборка

    # todo фильтрация
    select2_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    WHERE is_success='false'
    """
    # select2_orm = models.Requests.objects.filter(is_success=False)
    # todo фильтрация

    # todo сортировка
    select3_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    ORDER BY datetime DESC
    """
    # select3_orm = models.Requests.objects.order_by("-datetime")
    # todo сортировка

    select_orm = models.Requests.objects.all()
    # select_orm - [<class 'django_app.models.Requests'>, ...]
    # select_orm[0] - <class 'django_app.models.Requests'>
    for i in select_orm:
        print(type(i), i)
        # i.delete()
        # i.save()
        # i.title = "Dias" + i.title
        print(i.title, i.price, i.is_success, i.description)
    # print(select_orm)
    # print(type(select_orm))

    return render(request, "django_app/requests.html", context={"select_orm": select_orm})


def get_request(request, pk):  # todo READ (one) - GET
    # id(1) - зарезервирована
    # todo выборка
    select1_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    WHERE id = 1
    """
    select1_orm = models.Requests.objects.get(id=int(pk))
    print(type(select1_orm))
    print(select1_orm)
    # select1_orm.title
    # select1_orm.price
    # select1_orm.is_success
    # todo выборка

    return render(request, "django_app/request.html", context={"req": select1_orm})


def post_request(request):  # todo CREATE - POST
    if request.method == "GET":
        return render(request, "django_app/send_request.html")
    elif request.method == "POST":
        title = str(request.POST.get("title"))
        description = str(request.POST.get("description"))
        price = float(request.POST.get("price"))

        print(title, description, price)

        # todo вставка
        insert1_raw = """
        INSERT INTO Requests (id, title, description, price, is_success, datetime) 
        VALUES (1, 'ЭЦП', 'Помогите выписать ЭЦП для юр. лица', '15000.0', 'false', '2023-06-09 20:00')
        """
        insert1_orm = models.Requests.objects.create(
            title=title, description=description, price=price,
            client="Аноним"
        )
        return redirect(reverse("home"))
    else:
        return HttpResponse("error")


def delete_requests(request):
    return HttpResponse("delete_requests")


def update_request(request):
    return HttpResponse("update_request")


# todo REQUESTS ###############################################


def register(request):
    return HttpResponse("register")


def recover(request):
    return HttpResponse("recover")


def recover_new(request):
    pass
