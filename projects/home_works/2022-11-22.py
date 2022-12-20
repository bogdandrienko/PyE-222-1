import requests

"""
Пользователь вводит с клавиатуры ссылку, начало имени картинки для сохранения, и количество загружаемых картинок.
Необходимо после этого в папку «img» сохранить выбранное количество картинок с выбранной ссылки,
но чтобы имя начиналось с «начало имени».
"""

# 1) Получить от пользователя ссылку, начало имени картинки и количество загружаемых картинок
# 2) Получаем картинку из интернета в оперативную память, затем сохраняем эту картинку в папку
# 3)

# link = input("Введите ссылку: ")
link = "https://picsum.photos/320/240/"
# name = input("Введите начало имени: ")
name = "image"
# count = int(input("Введите количество загружаемых картинок: "))
count = 5

# response = requests.get(url=link)
# print(response.content, type(response.content))

# str1 = "Hello"
# with open("new.txt", mode="w") as file:
#     file.write(str1)

# for i in range(1, 5 + 1):
#     response = requests.get(url=link)
#     with open(f"img/{name}{i}.jpg", mode="wb") as file:
#         file.write(response.content)

list1 = [
    "https://rg.ru/uploads/images/226/04/06/hrom.jpeg",
    "https://www.ixbt.com/img/n1/news/2021/2/2/Google_large.png",
    "https://cdn.lifehacker.ru/wp-content/uploads/2021/06/8-besplatnyh-analogov-Google-Foto_1622554356-1280x640.jpg",
]


# for index, link in enumerate(list1, 10):
#     response = requests.get(url=link)
#     with open(f"img/{name}{index}.jpg", mode="wb") as file:
#         file.write(response.content)

import json

# link = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url=link)
# with open("new.json", mode="wb") as file:
#     file.write(response.content)
# with open("json_temp/new.json", mode="w") as file:
#     json.dump(response.json(), file)

link = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url=link)
list_data = response.json()

index = 0
for cup in list_data:
    index = index + 1
    with open(f"json_temp/new{index}.json", mode="w") as file:
        json.dump(cup, file)
