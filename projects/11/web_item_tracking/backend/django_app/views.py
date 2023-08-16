from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={"message": "OK"}, safe=False)


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {"name": "Dina"})


def pricing(request: HttpRequest) -> HttpResponse:
    price_list: list[dict] = [
        {
            "title": "Доставка мелких грузов",
            "description": "до 5 кг, цена указана за 1 кг с округлением вверх",
            "price": 600.00,
            "valute": "KZ",
        },
        {
            "title": "Доставка крупных грузов",
            "description": "до 500 кг, цена указана за 1 кг с округлением вверх",
            "price": 60000.00,
            "valute": "KZ",
        },
    ]
    return render(request, "pricing.html", {"price_list": price_list})


class Person:
    access = "public"
    points = 12


class Manager(Person):
    # points = 20
    pass


m1 = Manager()
print(m1.points)
