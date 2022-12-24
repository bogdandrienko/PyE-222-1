# 1) Получить данные и превращаем объекты в словарь (массив словарей)

import requests


def first(is_logging=False) -> list[dict]:
    link = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url=link)
    # json_data = response.content  # bytes (image, file...)
    # json_data = response.text  # str (str, html...)
    json_data = response.json()  # dict (dict, [dict, dict, dict]...)
    if is_logging:
        print(json_data, type(json_data))
    return json_data
