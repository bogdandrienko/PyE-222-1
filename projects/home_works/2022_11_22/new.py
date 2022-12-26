########################################################################################################################
# TODO 1

import requests
import json

# url = input("Введи ссылку откуда качать картинку: ")
# name = input("Введи имя картинки: ")
# count = int(input("Введи количество картинок: "))

# url = "https://picsum.photos/320/240/"
# name = "img"
# count = 10

# for i in range(1, count+1):
#     response = requests.get(url=url)
#     result = response.content  # bytes
#     with open(f"{name}{i}.jpg", mode="wb") as file_object:
#         file_object.write(result)

########################################################################################################################
# TODO 2

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url=url)
# result = response.json()  # JSON -> dict(Python)
# with open(f"data/new.json", mode="w") as file_object:
#     json.dump(result, file_object)

########################################################################################################################
# TODO 3

# url = "https://jsonplaceholder.typicode.com/todos"
# response = requests.get(url=url)
# result = response.json()  # JSON -> dict(Python)
# index = 0
# for i in result:
#     index = index + 1
#     with open(f"data/new{index}.json", mode="w") as file_object:
#         json.dump(i, file_object)

########################################################################################################################
