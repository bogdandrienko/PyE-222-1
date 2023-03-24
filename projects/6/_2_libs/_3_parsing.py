import concurrent.futures
import time
import threading
import requests
import bs4
from bs4 import BeautifulSoup


def get_wheather(city_name: str, url: str) -> None:
    # todo Получение "сырых" данных от api #################################################################################
    # url = "https://www.gismeteo.kz/weather-astana-5164/"
    # url = "https://www.gismeteo.kz/weather-alger-6498/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    data = requests.get(url=url, headers=headers).text
    # print(data)

    # todo Получение "сырых" данных от api #################################################################################

    #

    # todo Начинаем отрезать ненужные нам части ШАГ 1 ######################################################################

    sep1 = 'class="tab-content"><div class="date">Сейчас</div><div class="day" data-pattern="G:i">'
    data1 = data.split(sep=sep1)[1]
    # print(data1)

    # todo Начинаем отрезать ненужные нам части ШАГ 1 ######################################################################

    # todo Начинаем отрезать ненужные нам части ШАГ 2 ######################################################################
    sep2 = '<span class="unit unit_temperature_c">'
    data2 = data1.split(sep=sep2)[1]
    # print(data2)
    # todo Начинаем отрезать ненужные нам части ШАГ 2 ######################################################################

    # todo Начинаем отрезать ненужные нам части ШАГ 3 ######################################################################
    sep3 = '</span> <span'
    data3 = data2.split(sep=sep3)[0]
    # print(data3)
    # todo Начинаем отрезать ненужные нам части ШАГ 3 ######################################################################

    # todo Если погода отрицательная, то отрезаем ненужные нам части ШАГ 4 #################################################
    if data3.find("&minus;") == -1:
        # print("выше нуля")
        final = int(data3.split(sep="</span>")[1])
    else:
        # print("ниже нуля")
        final = int(data3.split(sep="</span>")[1]) * -1
    # todo Если погода отрицательная, то отрезаем ненужные нам части ШАГ 4 #################################################

    print(f"Погода в {city_name} сейчас: {final}")


def time_measure(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Time res: ", round(end - start, 3))
        return result

    return wrapper


@time_measure
def sync_f(arr):
    """
    Последовательное(синхронное) получение данных со всех городов
    """
    for name, url in arr:
        get_wheather(name, url)


@time_measure
def threading_f(arr):
    """
    Параллельное(одновременно) получение данных со всех городов
    """
    # thread_list = []
    # for name, url in arr:
    #     new_thread = threading.Thread(target=get_wheather, args=(name, url))
    #     thread_list.append(new_thread)
    # for i in thread_list:
    #     i.start()
    # for i in thread_list:
    #     i.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for name, url in arr:
            executor.submit(parsing_with_bs4, name, url)


def parsing_with_bs4(city_name, url):
    # todo Получение "сырых" данных от api #############################################################################
    # url = "https://www.gismeteo.kz/weather-astana-5164/"
    # url = "https://www.gismeteo.kz/weather-alger-6498/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    data = requests.get(url=url, headers=headers).content
    # print(data)

    # todo Получение "сырых" данных от api #############################################################################

    #

    # todo Извлечение данных библиотекой bs4 ###########################################################################
    soup = bs4.BeautifulSoup(data, 'html.parser')
    final = soup.find_all('span', {"class": "unit_temperature_c"})[0].text
    # todo Извлечение данных библиотекой bs4 ###########################################################################

    print(f"(обновлено)Погода в {city_name} сейчас: {final}")


if __name__ == '__main__':
    cities = [
        ["Астана", "https://www.gismeteo.kz/weather-astana-5164/"],
        ["Алматы", "https://www.gismeteo.kz/weather-almaty-5205/"],
        ["Алжир", "https://www.gismeteo.kz/weather-alger-6498/"],
        ["Шымкент", "https://www.gismeteo.kz/weather-shymkent-5324/"],
        ["Уральск", "https://www.gismeteo.kz/weather-oral-5156/"],
        ["Астана", "https://www.gismeteo.kz/weather-astana-5164/"],
        ["Алматы", "https://www.gismeteo.kz/weather-almaty-5205/"],
        ["Алжир", "https://www.gismeteo.kz/weather-alger-6498/"],
        ["Шымкент", "https://www.gismeteo.kz/weather-shymkent-5324/"],
        ["Уральск", "https://www.gismeteo.kz/weather-oral-5156/"],
        ["Астана", "https://www.gismeteo.kz/weather-astana-5164/"],
        ["Алматы", "https://www.gismeteo.kz/weather-almaty-5205/"],
        ["Алжир", "https://www.gismeteo.kz/weather-alger-6498/"],
        ["Шымкент", "https://www.gismeteo.kz/weather-shymkent-5324/"],
        ["Уральск", "https://www.gismeteo.kz/weather-oral-5156/"],
    ]

    # sync_f(arr=cities)  # Time res:  1.352 (5x) (500x = 135.2)
    # threading_f(arr=cities)  # Time res:  0.464 (15x) (1500x = 0.464) ! todo many memory and cpu
    threading_f(arr=cities)  # Time res:  0.446 (15x) (50x = 0.446 * 3 = 1.5)
