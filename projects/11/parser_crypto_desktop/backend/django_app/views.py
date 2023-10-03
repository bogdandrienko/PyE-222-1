from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import requests


@api_view(http_method_names=["GET", "POST"])
def weather(request: Request):
    """
Нужно вернуть данные в требуемом формате для умного зеркала
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers).text
    sep1 = '<div class="date">Сейчас</div>'
    text2 = response.split(sep=sep1)[1]
    sep2 = '</div></div><svg class'
    arr3 = text2.split(sep=sep2)
    text3 = arr3[0]
    sep3 = 'class="unit unit_temperature_c">'
    text4 = text3.split(sep=sep3)[-2::]
    sep4 = '</span>'
    arr = []
    for i in text4:
        arr.append(i.split(sep=sep4)[0].replace("&minus;", "-"))

    data = {
        "day": arr[1],
        "night": arr[0],
        "влажность": "",
        "давление": "",
        "ветер": "",
        "рекомендация": "возьмите зонт",
    }
    return Response(data=data, status=status.HTTP_200_OK)
