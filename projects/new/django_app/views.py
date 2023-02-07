from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    # https://jinja.palletsprojects.com/en/3.1.x/

    fruits = ["banana", "lemon", "apple", "apelsin"]
    for fruit in fruits:
        print(fruit)

    age = 17
    if age < 18:
        print("Запрещено")
    else:
        print("Разрешено")

    # return HttpResponse("<h1>Maksim</h1>")
    # return JsonResponse(data={"name": "Maksim", "age": 666}, safe=False)

    context = {"name": "Maksim", "fruits": fruits, "user_is_auth": False, "user": {"age": 30}}
    return render(request, "home.html", context)  # https://getbootstrap.com/docs/5.0/examples/


def login(request):
    context = {}
    return render(request, "login.html", context)
