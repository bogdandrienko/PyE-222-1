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
    # \n - переход на следующую строку
    # str3 = 'Python is awesome!\n \t'

    # str3 = "Python"[0]
    # str3 = "Python\n\n11111\n\n\n"[0:-2]
    # print(str3)
    # str4 = [12, 145, 16, 17][0:2:1]
    # arr = [12, 145, 16, 17, 12, 145, 16, 17]
    # str4 = arr[0:len(arr):1]

    data = opened_file.readlines()
    # data1 = opened_file.readlines()[0]
    print(data)  # ['Python is awesome!\n', '123\n', 'Python is awesome!']
    print(data[0])
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