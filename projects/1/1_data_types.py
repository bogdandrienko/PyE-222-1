# TODO типы данных
from decimal import Decimal

# имя_переменной =(присваивание) значение_переменной

bool1 = True  # булевы значения в формате Правда/Ложь

int1 = 12  # целочисленные значения

float1 = 12.0  # значения с плавающей точкой

decimal1 = Decimal(12.0)  # значения с плавающей точкой, но для высокоточных расчётов

str1 = r"Python \n \t float1"  # строка - коллекция символьных элементов
str2 = 'Python'  # строка - коллекция символьных элементов
str3 = "I'm"  # строка - коллекция символьных элементов
str4 = """I'm 

man
"""  # строка - коллекция символьных элементов
# "Python".encode() => b"Python"
# b"Python".decode() => "Python"

str5 = "Python" + str(12.0)  # конкатенация (сложение строк)
str6 = f"Python {12.0}"  # интерполяция (вставка разных переменных в строку)
str7 = "Python \n \t float1"  # спец символы
str8 = r"Python \n \t float1"  # raw string

bytes1 = b"Python"  # байты - коллекция символьных элементов в виде байтов
bytes2 = b'\x01\x02\x03\x04\x05'
# b'\x016А\x02\x03\x04\x05' ASCII (256) vs UTF-8 (N миллионов)

list1 = [10, True, [], b"Python"]  # список - коллекция элементов

tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов

set1 = {12, False}  # множество - коллекция уникальных элементов

dict1 = {"Имя": "Python"}  # словарь - коллекция уникальных элементов в формате ключ-значение
dict2 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": 25,
        "arr": [10, True, []],
    },
}
dict3 = {"key_1": "va1", (12,): {"key1": "va1"}, 12: 12}  # ключом словаря может быть только неизменяемый тип данных
# (хэшируемый), т.е. он проходит через хэш функцию и генерирует уникальную комбинацию символов
# "контейнерные" типы данных могут быть ключом словаря, только при условии, что всё внутри хэшируемое


INT_CONSTANT = 12  # условно-неизменяемая
# print(INT_CONSTANT / 12)
# INT_CONSTANT = 13
is_commit = False  # можно изменить
IS_COMMIT = False  # можно изменить, но не желательно

bool1 = True
int1 = 12
float1 = 12.0
str1 = "Python"  # .encode() => b"Python"
bytes1 = b"Python"  # b'\x016А\x02\x03\x04\x05' ASCII (256) vs UTF-8 (N миллионов)
list1 = [10, True, []]
tuple1 = (12, False)
set1 = {12, False}
dict1 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": 25,
        "arr": [10, True, []],
    }
}

# val1 = 12
# print(val1)
# val1 = "Привет"
# print(val1)


########################################################################################################################
# TODO действия с переменными

# вывод значение переменной в консоль
print(bool1)

# вывод значение типа переменной в консоль
type_bool1 = type(bool1)
print(type_bool1)
print(type(bool1))  # type_bool1 = type(bool1)

# проверка принадлежности типа данных
print(isinstance(bool1, str))  # False
print(isinstance(bool1, bool))  # True
print(isinstance(12, int))  # True

# конвертация типов данных:
float_to_int1 = int(10.5)  # int()
int_to_float1 = float(10)  # float()
str_to_float1 = float("10.2")  # float()
float_to_str1 = str(10.4)  # str()
int_to_bool1 = bool(0)  # bool()
set_to_list1 = list((1, 2, 2, 5))  # list()
# list_to_set1 = set([1, 2, 2, 5])  # set()
list_to_set1 = set(set_to_list1)  # set()
# ...

# получение ввода от пользователя из консоли
str_from_user1 = input("Введите Ваше имя: ")
print(str_from_user1)

# получение элементов из коллекции
source_str1 = "Python is awesome"

source_str2 = source_str1[2]
print(source_str2)

print(source_str1[2])

source_str3 = source_str1[-2]
print(source_str3)

source_str4 = source_str1[2:6:1]
print(source_str4)

#               0  1  2  3
source_list1 = [1, 2, 3, 4, 5, 6, 7, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9]]

source_elem2 = source_list1[3]
print(source_elem2)

source_list2 = source_list1[2:5]
print(source_list2)

dict4 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
}
print(dict4["age"])
dict4["money"] = Decimal(12.0)
print(dict4)
del dict4["arr"]
print(dict4)


####################################################################################

import math
import time

# Программирование - оперирование типами данных

# float

# Контейнер (область в оперативной памяти, для переменной)
# имя переменной - ссылка на область в оперативной памяти

float1 = 12.15  # 0.0 -10.0 float - число с плавающей точкой
int1 = 12  # 0 -10 integer - целочисленное значение
# с++ - float / decimal / integer - smallinteger - biginteger /

str1 = "B o g dan"  # string - строка
str2 = "B"  # string - строка
str3 = ""  # string - строка
str4 = 'Python'  # string - строка
str5 = 'I"m ready'  # string - строка
str6 = "I'm ready"  # string - строка
str7 = """I''"''m ready"""  # string - строка
# с++ - char / string

bool1 = True  # False bool - (Правда или ложь) 1 и 0

list1 = []  # list список
#        0   1      2        3      4
list2 = [12, 15, 15, "Python", False]  # list список

set1 = {50.0, 12}  # set множество (только уникальные элементы)
set2 = {}

tuple1 = (15, 15, "Python")  # tuple Кортеж (неизменяемый - меньше оперативной памяти)
tuple2 = (15,)
tuple3 = ("",)

none1 = None  # ничто

list4 = [12, 15, 15, "Python", False]
# print(объект) - вывод на экран
# print(list4)
# list4.append("Awesome")
# print(list4)

dict1 = {"key": "value"}  # dict словарь (коллекция - массив, с парами ключ-значение)
dict2 = {
    # 1 пара
    "key": {"key": "value"},
    # 2 пара
    "Студенты": ["Амина", "Алишер"]
}

dict3 = {"key": "value"}
# print(dict3)  # {'key': 'value'}
# print(dict3["key"])  # value

dict3["Мой номер"] = "+7 176"  # присвоение
dict3["IIN"] = 180  # присвоение
# print(dict3)  # {'key': 'value', 'Мой номер': '+7 176'}
# print(dict3["Мой номер"])  #

# type(объект) узнать тип

result = type(False)  # <class 'bool'>
# print(result)

res1 = False


# print(type(res1))  # <class 'bool'>


# def - define - определить
# def имя_фунции(аргумент1, аргумент2...): - ОПРЕДЕЛЕНИЕ ФУНКЦИИ (! ЕЁ НУЖНО ВЫЗВАТЬ !)
#   расчёт...
def sum_two_values(value1, value2):  # snake case
    result5 = value1 + value2  # расчёты....
    # print(result5)
    return result5  # возврат результата


res4 = sum_two_values(13, 12)
# print(res4)
# print(12)

result9 = 10 - 10
result10 = 10 + 10
result11 = 10 * 10
result12 = 10 / 10  # 1.0
result13 = 15 // 10  # 1 - округляет до целого вниз
result14 = 2 ** 4  # 16 - возведение в степень
result15 = 16 ** 0.5  # 4.0 - извлечение из под корня
result16 = int(math.sqrt(16))  # float()  # 4 - извлечение из под корня
result17 = 15 % 4  # 3 - остаток от деления
result21 = 15 < 4  # False -
result22 = 15 > 4  # True -
result23 = 15 <= 4  # 3 -
result24 = 15 >= 4  # 3 -
result25 = 15 == 4  # False - равен ли
result26 = 15 != 4  # True - не равен ли
# print(result17)

# 1 - 1000
# итерация - повторение
# переменная цикла  старт  стоп ШАГ
final = 0
for value in range(1, 1000 + 1, 1):
    # 1 ... 2 ... 3
    # print(value)
    final = final + value
    # print(final)

for i in ["Амина", "Алишер", "Амина", "Алишер", "Амина", "Алишер"]:
    # print(i)
    pass

for i in "Амина":
    # print(i)
    pass


def something():
    pass


# seconds = 0
# minuts = 0
# while seconds < 60:  # пока(пока ещё)
# print(seconds)
# seconds = seconds + 1
# seconds += 1  # increment увеличение
# seconds -= 10  # increment увеличение
# seconds *= 10  # increment увеличение


# val1 = 15
# val2 = 20
#
# if val1 < val2:  # если
#     print("Больше")  # ПРАВДА
# else:  # ЛОЖЬ
#     print("не больше")

seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(0.001)
    if seconds < 60:
        seconds += 1
    else:
        if minutes < 60:
            minutes += 1
            seconds = 0
        else:
            if hours < 24:
                minutes = 0
                hours += 1
            else:
                seconds = 0
                minutes = 0
                hours = 0

    # print("секунды: ", seconds)
    # print("минуты: ", minutes)
    # print("часы: ", hours)

    # print("секунды: " + str(seconds) + "минуты: ")
    print(f"{hours}:{minutes}:{seconds}")  # f-строка - вложение переменной любого типа внутрь строки
    # конкатенация строк (сложение)


