########################################################################################################################
# TODO get json data and write

import requests
import json

# HTTP (TCP/IP) - протоколы запросов
# request - запрос / response - ответ

# post - create
# get - read
# put (patch) - update
# delete - delete

# текст
# html
# картинки
# валюта - с сайтов банков
# цены - с сайтов маркетплейсов
# погода - с сайтов погоды
# реферат - с википедии

##########################################################
# Получить данные и записать в дж файл!
import requests
import json


# response = requests.get("https://jsonplaceholder.typicode.com/todos")
#
# if response.status_code == 200:
#     with open("json_file.json", "w") as file:
#         json.dump(response, file)
# else:
#     raise Exception(response.status_code)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get("https://ru.wikipedia.org/wiki/Python", headers=headers).content
with open("python.html", "wb") as file:
    file.write(response)


