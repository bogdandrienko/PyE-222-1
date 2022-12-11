import requests
import json

# text (str)
# html (str)
# json (dict)
# bytes (image, file)
# валюта - с сайтов банков
# цены - с сайтов маркетплейсов
# погода - с сайтов погоды
# реферат - с википедии

# get - read
# post - create
# put (patch) - update
# delete - delete

# CRUD

url1 = "https://ru.wikipedia.org/wiki/Python"
url2 = "https://jsonplaceholder.typicode.com/todos"
url3 = "https://picsum.photos/1920/1080/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def get1():
    response1 = requests.get(url=url1, headers=headers)
    print(response1, type(response1))  # <Response [200]> <class 'requests.models.Response'>

    content1 = response1.content  # bytes
    text1 = response1.text  # str
    # dict1 = response1.json()  # dict

    with open("new1.html", "w", encoding="utf8") as html_file:
        html_file.write(text1)

    with open("new2.html", "wb") as html_file:  # лучше
        html_file.write(content1)


def get2():
    response = requests.get(url=url2, headers=headers)
    content1 = response.content  # bytes
    text1 = response.text  # str
    dict1 = response.json()  # dict

    # print(content1)
    # print(text1)
    print(dict1)

    for index, value in enumerate(dict1, 1):
        with open(f"temp/new{index}.json", "w") as json_file:
            json.dump(value, json_file)
        # json.dumps()
        # json.load()
        # json.loads()


def get3():
    response = requests.get(url=url3, headers=headers)
    content1 = response.content  # bytes

    with open(f"images/new.jpg", "wb") as image_file:
        image_file.write(content1)

get3()
list0 = [
    "5",
    "6",
    8,
    2,
    5,
    12,
    24,
    54,
]

list1 = []
for i in list0:
    list1.append(int(i))
print(list1)


list2 = []
for i in list1:
    if i % 2 == 0:
        continue
    else:
        list2.append(i)

list2.sort(reverse=True)
print(list2)
print(sorted(list2, reverse=True))
