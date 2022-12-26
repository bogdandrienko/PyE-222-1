dict1 = {"name": "Богдан"}
print(dict1)
val3 = dict1["name"]  # GET
print(f"Имя: {val3}")

dict1["name"] = "Тамерлан"  # UPDATE
dict1["Возраст"] = 20  # SET
print(dict1)

dict2 = dict(name="Богдан2", возраст=24)
print(dict2)

# print(int(2.5))
# print(int("2"), type(int("2")))

import json

with open("temp/2.json", "w", encoding="utf8") as file:
    # json.dump(dict1, file, ensure_ascii=False)

    str_json = json.dumps(dict1, ensure_ascii=False)
    file.write(str_json)

import requests

url = "https://picsum.photos/1920/1080/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
data = requests.get(url, headers=headers)
print(data, type(data))

content = data.content
# text = data.text  # data.content.decode()
# json_obj = data.json()  # json.loads(data.content.decode())
# print(content)
# with open("temp/3.jpg", "wb") as file:  # write in bytes
#     file.write(content)

url2 = "https://jsonplaceholder.typicode.com/posts/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
data = requests.get(url2, headers=headers)
json_data = data.json()
print(json_data)

index = 0
for i in json_data:
    index += 1
    with open(f"temp/new{index}.json", "w", encoding="utf8") as file:
        json.dump(i, file, ensure_ascii=False)
