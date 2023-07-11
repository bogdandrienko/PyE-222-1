from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    todos = get_todos(headers)
    weather = get_weather(headers)
    coin = get_coin(headers)

    # print("\n\n\ntodos: ", todos)
    # print("\n\n\nweather: ", weather)
    # print("\n\n\ncoin: ", coin)

    return render(request, 'home.html', context={"todos": todos, "weather": weather, "coin": coin})


def get_todos(headers):
    """API - программный интерфейс"""

    # за деньги да!

    return requests.get('https://jsonplaceholder.typicode.com/todos', headers=headers).json()


def get_weather(headers):
    """Ручной парсинг данных"""

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

    return {"day": arr[1], "night": arr[0]}


def get_coin(headers):
    """Полу-автоматический парсинг данных"""

    response = requests.get("https://finance.rambler.ru/calculators/converter/1-KZT-USD/", headers=headers)
    soup_obj = BeautifulSoup(response.text, 'html.parser').find_all(
        'div', class_="converter-display__value"
    )[-1].get_text()
    current = round(float(soup_obj), 1)
    return current


def get_selenium():
    """Продвинутый способ парсинг данных"""

    # 1. Есть скрытый режим
    # 2. Абсолютно похож на пользователя
    # 3. Можно подключать авторизацию, кукесы, localstorage и ...

    return None
