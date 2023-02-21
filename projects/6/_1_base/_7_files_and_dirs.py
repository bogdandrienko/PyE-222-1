########################################################################################################################
# TODO работа с текстовыми файлами

import json
import os
import shutil

# open('имя_и_расширение_файла', 'режим_открытия')
# режимы: w r a wb rb w+ r+

# ручное закрытие файла
file1 = open('z_new.txt', mode='w')  # файловый-объект, если файл в папке 'data' - open('data/z_new.txt', 'w')
file1.write("Python is awesome!123\n\thi")
# file1.seek()
# print(1/0)
file1.close()

file1 = open('z_new.txt', mode='w')  # файловый-объект, если файл в папке 'data' - open('data/z_new.txt', 'w')
try:
    file1.write("Python is awesome!123\n\thi")
except Exception as error:
    print(error)
else:
    pass
finally:
    file1.close()

# контекстный менеджер
with open('z_new.txt', 'r') as file2:
    line1 = file2.read()
    print(line1)

    lines1 = file2.readlines()
    print(lines1)
    # внутри контекстного менеджера
# снаружи контекстного менеджера

########################################################################################################################

########################################################################################################################
# TODO работа с JSON - файлами

# Serialize obj as a JSON formatted (де-факто стандарт для веба)
# сериализация obj (Python) => JSON
# десериализация JSON => obj (Python)

dict1 = {"name": "Bogdan"}
# запись
with open('data/new.json', 'w') as file1:
    # todo сразу запись словаря в файл
    json.dump(dict1, file1)

    # todo сначала сериализуем словарь в json_строку
    # str1_json = json.dumps(dict1)
    # opened_file.write(str1_json)

dict_str1 = json.dumps(dict1)  # сначала сериализуем словарь в json_строку
print(dict_str1, type(dict_str1))  # "{"name": "Bogdan"}"

# JSON в виде строки (часто приходит из "интернет" запросов)
dict_str2 = """
[{"IIN": "14124152452", "age": 24, "Name": "Bogdan1", "married": false},
{"IIN": "14124152453", "age": 24, "Name": "Bogdan2", "married": false},
{"IIN": "14124152454", "age": 24, "Name": "Bogdan3", "married": true},
{"IIN": "14124152455", "age": 24, "Name": "Bogdan4", "married": false}]
"""
print(type(dict_str2))
dict2 = json.loads(dict_str2)  # десериализация JSON => obj (Python)
print(dict2, type(dict2))
print(dict2[0], type(dict2[0]))

# чтение
with open('data/new.json', 'r') as file2:
    # todo сразу чтение словаря из файла
    dict3 = json.load(file2)
    print(dict3)

    # todo сначала сериализуем json_строку в словарь
    # dict4 = json.loads(file2.read())
    # print(dict4, type(dict4))


########################################################################################################################

########################################################################################################################
# TODO работа с папками
