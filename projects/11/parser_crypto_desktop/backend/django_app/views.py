from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def news(request: HttpRequest):
    data1 = requests.get("https://fakenews.squirro.com/news/sport", headers=headers).json()
    _news = data1["news"]
    data2 = []
    for new in _news:
        data2.append({"id": new["id"], "title": new["headline"]})
    return JsonResponse(data={"news": data2}, safe=True)


@api_view(http_method_names=["GET", "POST"])
def weather(request: Request):
    """Получение погоды по API"""

    # определить геолокацию
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
    }
    return Response(data={"weather": data}, status=status.HTTP_200_OK)
