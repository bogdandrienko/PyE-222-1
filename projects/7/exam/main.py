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
