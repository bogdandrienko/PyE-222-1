"""
2.	Как выполняется интерполяция строк?
"""

# age = 18
# a1 = "Dias" + " " + str(age)  # Конкатенация
# b1 = f"Dias {age}"  # Интерполяция
# c1 = "Dias {0}".format(age)  # Устаревшая интерполяция
# print(a1, b1, c1)

"""
4.	Как работает умножение строк?
5.	Как работает умножение списка?
"""

# a2 = "Banana "
# b2 = [1, 2, 3]
# print(a2 * 2)
# print(b2 * 3)

"""
6.	Как объединить списки в Python?
"""
# 1
# b1 = [1, 2, 3]
# b2 = [3, 4, 5]
# b1.extend(b2)
# c1 = b1
# print(c1)

# 2
# b1 = [1, 2, 3]
# b2 = [3, 4, 5]
# for i in b2:
#     b1.append(i)
# c1 = b1
# print(c1)

# 3
# b1 = [1, 2, 3]
# b2 = [3, 4, 5]
# c1 = [*b1, *b2]
# print(c1)

"""
8.	Как проверить, существует ли значение в списке?
"""

# el = 2
# b1 = [1, 2, 3]
# print(el in b1)


"""
12.	Получите список ключей из словаря
"""

dict1 = {"key1": "a", "key2": "b"}
print(dict1.keys())

"""
14.	Что такое переменная
"""

"Контейнер, который 'хранит'(ссылается) какие-то данные"
a = 12

"""
16.	Как запросить у пользователя ввод
"""

# str1 = input("Вопрос 1 - ")
# int1 = int(input("Вопрос 2 - "))
# print(str1)

"""
39.	Объясните функцию range 
"""

"Диапазон, <class 'range'>, 1 аргумент по умолчанию 0 - старт, 2 аргумент - стоп, 3 аргумент по умолчанию 1 - шаг " \
"чаще всего для итерации в цикле for"

# a = range(10)
# print(a)
# for i in range(1, 100+1, 2):
#     print(i)

"""
40.	Cрезы или слайсы в python 
"""

"""
'Python'[0:len('Python'):1]
"""

str1 = "Python"
list1 = [1, 2, 3, 4]
print(str1[0:len(str1):1])
print(list1[-2::1])

"""
42.	Чем файл .pyc отличается от .py
"""

'pyc - бинарный файл для ускорения(предкомпиляция), py - python-код'

"""
45.	Что означает self в классе?
"""

"self - для 'обращения' к себе(к своим параметрам, свойствам и методам)"

# class Human:
#     def __init__(self):
#         age = 20
#         print(age)
#         self.age = 20
#
#     def say_my_age(self):
#         print(self.age)


"""
44.	В чем разница между func и func()? Где func это функция. 
"""


def func():
    print("hi")


a = func
a()
b = func()

"""
47.	Какая разница между словарями и JSON?
"""

"""словарь - python-like, json - javascript-like
Сериализация и десериализация - json
"""

"""
50.	В чем разница между pass, continue и break? 
"""

'pass - заглушка, для пропуска кода, continue - пропуск итерации цикла, break - тормоз всего цикла'


def func1():
    pass


"""
66.	В чем разница между глубокой и мелкой(поверхностной) копиями?
"""

# поверхностная
dict1 = {"key": 12}
dict2 = dict1
dict1["key"] = 13
print(dict1, dict2)

# глубокая
dict3 = {"key": 12}
dict4 = dict3.copy()
dict3["key"] = 13
print(dict3, dict4)

# глубокая
list1 = [1, 2, 3]
list2 = list1.copy()

"""
70.	Модификаторы доступа, какие бывают? 
"""


class Human1:
    age = 20  # public публичная
    _age = 21  # protected защищённая
    __age = 22  # private приватная
    pass


h1 = Human1()
print(h1.age)
print(h1._age)
# print(h1.__age)
print(h1._Human1__age)


class Child(Human1):  # Наследование
    pass


"""
74.	Множественное наследование
"""


class Parent1:
    pass


class Parent2:
    pass


class LoginRequiredMixin:
    pass


class Child1(Parent2, Parent1, LoginRequiredMixin):
    pass


######################################################################################################################################################


import math

# 1.  В чем разница между списком и кортежем?
# Элементы кортежа неизменяемы


# 2.Как развернуть список?
# 1) reverse
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)
# 2) slice
arr1 = [1, 2, 3, 4, 5]
print(arr1[::-1])

# 3.Как округлить число до трех десятичных знаков?
# 1)
a = 2378.4687665
print(round(a, 3))

# 2)
num = 3.14159265359
formatted_num = "{:.3f}".format(num)
print(formatted_num)
# 3)
print(math.floor(3.999))

# 4)
print(math.ceil(3.999))
# 5)
print(math.trunc(7.11))

print(int(math.floor(2.6)))

# 4.  Как получить абсолютное значение целого числа?
# 1)
x = -5
abs_x = abs(x)
print(abs_x)

# 2)
b = -6
int_b = int(b)
if int_b < 0:
    int_b = int_b * -1
else:
    pass
print(int_b)

# 5.  Как перевести строку в верхний/нижний регистр?
# 1)ВЕРХНИЙ РЕГИСТР
string = "строка"
upper_string = string.upper()
print(upper_string)
# 2)НИЖНИЙ РЕГИСТР
string1 = "СТРОКА"
lower_string = string.lower()
print(lower_string)

# 6.  Какие циклы есть в python и чем отличаются
# 1) FOR
for i in range(1, 10):
    print(i)
# 2) WHILE
i = 0
while i < 10:
    print(i)
    i += 1

# 3) DO WHILE
c = 0
while True:
    print(c)
    c += 1
    if c == 10:
        break

# 7.  Строка — это последовательность или нет?
# Да, строка является последовательностью символов, имеющих собственный индекс


# 8.Что такое PEP?
# PEP - это сокращение от "Python Enhancement Proposal" (предложение по улучшению Python).
# PEP - это документ, который описывает и объясняет новую функциональность или улучшение языка Python.

# 9.В чем разница между remove, del и pop?
# remove
my_list = [1, 2, 3, 2, 4, 5]
my_list2 = [1, 2, 3, 2, 4, 5]

print(my_list.remove(3))
print(my_list)

# del
my_list2 = [1, 2, 3, 2, 4, 5]
del my_list2[2]
print(my_list2)

# pop
my_list3 = [1, 2, 3, 2, 4, 5]
print(my_list3.pop(4))
print(my_list3)

# 10.Что такое лямбда-функция?
# лямба-функция-это анонимная функция
# ЛЯМБДА-ФУНКЦИЯ
ab = lambda x: x ** 2
abb = ab(5)
print(abb)


# ОБЫЧНАЯ ФУНКЦИЯ
def square(a):
    return a ** 2


print(square(3))


# 11.Магические методы и пару примеров
class Class():
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(str(self.value))


######################################################################################################################################################


# """11.  Проверьте, что в строке только числа"""
#
# # str1 = '12334324'
# # str2 = 'fh2dg1jhj'
#
# def check(strr):
#     for item in strr:
#         if not item.isdigit():
#             return False
#     return
#
# # print(check(str1))
# # print(check(str2))
# #
# # print(str1.isnumeric())
# # print(str2.isnumeric())
#
# """21.  Что делает метод split() и join()"""
#
#
# str1 = '123 343 24'
#
# #print(str1.split(" "))
# # print(str2.join(""))
#
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
#
# #print(x)
#
#
#
# """Как избежать конфликтов при импорте файлов"""
#
# from tkinter import ttk
#
# from json import *
#
# import pandas as pd
#
# import pandas, time
#
# from json import loads
#
#
#
#
#
# """48.  Как удалить из списка дубликаты?"""
#
# mylist = ["a", "b", "a", "c", "c"]
# mylist2 = list(set(mylist))
# # print(mylist2)
#
#
# """49.  Как отсортировать словарь по ключам, в алфавитном порядке?"""
#
# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
#
# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[0])
#
# new_dict = dict((x, y) for x, y in sorted_footballers_by_goals)
#
# nw_dict = {}
#
# for x, y in sorted_footballers_by_goals:
#     nw_dict[x] = y
#
# print(footballers_goals)
# print(new_dict)
# print(nw_dict)
#


# """"53.  Что такое Git и как создать гит репозиторий локально""" - git init

# """67.  Где быстрее поиск: в словарях или списках? И почему."""
# # dict > list
# dict = O(1) const
# list = O(n) lineiaer
#
"""76.  Напишите лучший код для перестановки двух чисел местами."""
a = 9
b = 7

a, b = b, a




####################################################################################

20.	Можно ли число сделать строкой и как



