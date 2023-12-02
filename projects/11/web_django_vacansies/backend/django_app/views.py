import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def api(request):
    return JsonResponse(data={"message": "OK"}, safe=True)


def index(request):
    return render(request, "index2.html", context={})


def vacasies(request):
    search = request.GET.get('search', "")
    data = [{"id": i, "name": f"Bogdan {i} {search}", "experience": i * 2} for i in range(1, 100)]
    return JsonResponse(data={"list": data}, safe=True)


# @csrf_exempt
@api_view(http_method_names=["GET", "POST"])
def blank(request):
    """Эта функция, нужна для отправки резюме"""

    print(request.GET)  # query params https://hh.ru/search/vacancy?text=Python&area=154
    print(request.POST)
    print(request.FILES)
    print(request.data)
    # print(request.body)

    # data = json.loads(b'{"name":"111111111111"}'.decode("utf-8"))
    # print(type(data), data)

    # return JsonResponse(data={"message": "OK"}, safe=True)
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET"])
def best_seller(request):
    """
    Написать API, которая будет парсить токены криптовалюты, и
    выводить только несколько полей. При этом, не показывать валюты ниже 1$

    1. Безопасность.
    2. Нужный формат данных.

    https://api.coingecko.com/api/v3/coins/list
    """
    try:

        top = int(request.GET.get('top', 10))
        tg = float(request.GET.get('tg', 450))
        # print("top: ", top)
        response = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"
        ).json()
        # print(response)
        data = []
        index = 1
        for i in response:
            data.append({"id": index, "name": i["name"], "price": i["current_price"] * tg})
            index += 1

        # d = [16, 17, 18, 19, 20, 21, 22, 23, 17]
        # print("d: ", d)
        #                 как проверяем  | что проверяем
        # e = list(filter(lambda i: i <= 18, d))
        # print("e: ", e)

        data = list(filter(lambda i: i["price"] >= 1, data))
        data = sorted(data, key=lambda x: (x["price"], i["name"]), reverse=True)

        return Response(data={"data": data[:top], "list": [
            {"id": 1, "name": "BTC", "price": 26000},
            {"id": 2, "name": "Etherium", "price": 26000},
            {"id": 3, "name": "Dogcoin", "price": 26000},
        ]})
    except Exception as error:
        print(error)
        return Response(data={"data": [], "list": [
            {"id": 1, "name": "BTC", "price": 26000},
            {"id": 2, "name": "Etherium", "price": 26000},
            {"id": 3, "name": "Dogcoin", "price": 26000},
        ]})


