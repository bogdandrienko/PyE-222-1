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

print(os.getcwd())

first = os.path.abspath(os.path.dirname(__file__))  # содержит абсолютный путь к текущему скрипту
print(first)
first = ''  # содержит относительный путь к текущему скрипту
second = "temp\\tempjunk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
# r"" - сырая строка
third = r"temp\junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
fourth = "temp/junk2.txt"  # \ - изоляция символа   \n - перенос строки, \t - табуляция...
print(second)

path = os.path.join(second, third)  # склеивает несколько путей, корректным образом для каждой системы
print(f"path: {path}")

# os.remove("../")
# os.remove("junk.txt")  # remove file
# os.rmdir("junk")  # этим способом можно удалить только пустую папку
# shutil.rmtree("junk")  # этим способом можно удалить папку

if os.path.exists("temp"):
    shutil.rmtree("./temp")
else:
    os.mkdir("temp")
    with open('temp/new.txt', 'w') as file:
        file.write("Hello world!")

for filename in os.listdir('../_1_base'):
    print(filename)


# os.rename()  # переименовать
# shutil.copy()
# shutil.move()

def get_all_files_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    files_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in files:
            if name.find(".txt") > 0:
                files_list.append(f"{os.path.join(root, name)}")
    return files_list


print(get_all_files_in_path())


def get_all_dirs_in_path(p=os.path.dirname(os.path.abspath('__file__'))):
    directories_list = []
    for root, dirs, files in os.walk(p, topdown=True):
        for name in dirs:
            directories_list.append(f"{os.path.join(root, name)}")
    return directories_list


print(get_all_dirs_in_path())


def create_folder_in_this_dir(folder_name='new_folder', current_path=os.path.dirname(os.path.abspath('__file__'))):
    full_path = current_path + f'/{folder_name}'
    try:
        os.makedirs(full_path)
    except Exception as err:
        print(f'directory already yet | {err}')
    finally:
        return full_path


create_folder_in_this_dir("temp3")

########################################################################################################################

########################################################################################################################
# TODO импорт функций и библиотек

# импорт всей библиотеки
# import tkinter
# tkinter.Variable

# импорт всей библиотеки с присовением псевдонима
# import tkinter as tk
# import json as js

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !
# from tkinter import *
# from new import *
# Variable
# print()

# импорт отдельной функции из модуля(из нашего файла)
# from new import buddle_sort
# print(buddle_sort([1, 2]))

########################################################################################################################
