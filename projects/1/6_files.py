import os

#             путь           режим
# file = open("temp/new.txt", "r")  # файловый-объект
# file = open("new.txt", "r")  # файловый-объект
# file = open("new.txt", "rb")  # файловый-объект
# file = open("new.txt", "w")  # файловый-объект # overwrite
# file = open("new.txt", "wb")  # файловый-объект
# file = open("new.txt", "a")  # файловый-объект # add
# data = file.readlines()
# file.close()
with open("temp/new.txt", "r") as opened_file:  # менеджер контекста
    # закроект файл
    # \ - экранирование (изоляция следующего символа)
    # \n - переход на следующую строку
    # \t - табуляция
    # str3 = 'Python is awesome!\n \t'

    # str3 = "Python"[0]
    # str3 = "Python\n\n11111\n\n\n"[0:-2]
    # print(str3)
    # str4 = [12, 145, 16, 17][0:2:1]
    # arr = [12, 145, 16, 17, 12, 145, 16, 17]
    # str4 = arr[0:len(arr):1]

    data = opened_file.readlines()
    # data1 = opened_file.readlines()[0]
    # print(data)  # ['Python is awesome!\n', '123\n', 'Python is awesome!']
    # print(data[0])
    # внутри менеджера
    pass
# снаружи менеджера

with open("temp/new1.txt", "a") as opened_file:
    opened_file.write("\n\t \\ bananas")
    # opened_file.write("b\na\nn\n")
    # opened_file.writelines(["b\n", "a\n", "n\n"])

try:
    with open("temp1/new1.txt", "a") as opened_file:
        opened_file.write("\n\t \\ bananas")
        # opened_file.write("b\na\nn\n")
        # opened_file.writelines(["b\n", "a\n", "n\n"])
except FileNotFoundError:
    os.mkdir("temp1")
    with open("temp1/new1.txt", "a") as opened_file:
        opened_file.write("\n\t \\ bananas")
        # opened_file.write("b\na\nn\n")
        # opened_file.writelines(["b\n", "a\n", "n\n"])

import json

# Serialize obj as a JSON formatted
# сериализация obj (Python) => JSON
# десериализация JSON => obj (Python)

with open("temp/new.json", "r") as opened_file:
    # str1 = opened_file.read()
    # print(str1, type(str1))  # {"userId": 1,"id": 1,"title": "delectus aut autem","completed": false} <class 'str'>
    json_data = json.load(opened_file)  # функция пытается превратить файл
    print(json_data, type(json_data))

    # title = json_data['title']  # извлечение значения из словаря по ключу
    # print(title)

    str1 = opened_file.read()
    users_str_json = """[
        {"IIN": '14124152452', "age": 24, "Name": "Bogdan1", "married": false},
        {"IIN": '14124152453', "age": 24, "Name": "Bogdan2", "married": false},
        {"IIN": '14124152454', "age": 24, "Name": "Bogdan3", "married": true},
        {"IIN": '14124152455', "age": 24, "Name": "Bogdan4", "married": false},
        {"IIN": '14124152456', "age": 24, "Name": "Bogdan5", "married": false},
    ]"""
    json_data2 = json.loads(str1)  # функция пытается превратить любую строку
    users_dict = json.loads(users_str_json)


with open("temp/new_JSON.json", "w") as opened_file:
    dict1 = {
        'username': 'Alisher',
        'id': 1,
        'title': 'delectus aut autem',
        'completed': False
    }

    # todo сразу запись в файл
    json.dump(dict1, opened_file)

    # todo сначала сериализует словарь в json_строку
    # str1_json = json.dumps(dict1)
    # opened_file.write(str1_json)


# API application program interface


