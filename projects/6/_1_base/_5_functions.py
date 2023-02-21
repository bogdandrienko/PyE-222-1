########################################################################################################################
# TODO функции

import math
import time
from typing import Union


# print("Hi")
# print("Hi 1")
# print("Hi")


# код "до" функции
def function1():  # определение функции
    print("Hi")
    # код "внутри" функции (отступы: 2-4 пробела)


# код "после" функции


link1 = function1  # ссылка на функцию (alias)
link1()  # вызов функции
function1()


# грязная функция
def twice_value1(val1, val2):  # функция с параметрами (аргументами)
    result = val1 ** val2
    print(result)


twice_value1(5, 2)


# чистая функция
def twice_value2(val2, val1):
    result = val1 ** val2
    return result  # возврат значения


res = twice_value2(5, 2)
print(res)

result1 = twice_value2(6, 2)  # позиционные аргументы
print(result1)

result2 = twice_value2(val2=2, val1=6)  # именные (именованные) аргументы
print(result2)


def twice_value3(val1, val2=2):  # функция со стандартным параметром (аргументом)
    result = val1 ** val2
    return result


result3 = twice_value3(val1=6)
print(result3)

########################################################################################################################

########################################################################################################################
# TODO типизация

# Типизация - строгое задание типов для переменных и параметров (аргументов)
# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++ - статическая типизация (- скорость разработки + скорость работы - к багам)

val1: int = 2
print(val1)
val1 = "2"
print(val1)


# | - or        & - and
def twice_value4(val1: Union[int, float], val2: int = 2) -> int | float:  # функция с типизацией
    result = val1 ** val2
    return result


print(twice_value4(4.0, 2))


def twice_value5(val1: float, val2=2) -> int | float:  # функция с типизацией
    result = val1 ** val2
    return result


result4 = twice_value5(val1=6) / 10
print(result4)

########################################################################################################################

########################################################################################################################
# TODO стандартные функции

print(sum([1, 2, 3]))
print(round(2.555, 1))
print(int(2.0))
print(type(True))
# print(input("Введите: "))
print(abs(-100))
print(len("Привет"))
print(len([1, 2, 3, 4, 5]))

print(any([False, False, False, False]))
print(any([False, True, False, False]))
print(any([True, False, False, False]))

print(all([True, True, True, True]))
print(all([False, True, True, True]))
print(all([False, False, False]))


# ...
# https://pythonru.com/osnovy/vstroennye-funkcii-python
# https://letpy.com/handbook/builtins/


########################################################################################################################

########################################################################################################################
# TODO анонимные функции (lambda)

def multiply1(a, b, c):
    return a ** b + c


multiply2 = lambda a, b, c: a ** b + c

res4 = multiply1(6, 2, 1)
res5 = multiply2(6, 2, 1)
print(res4)
print(res5)

peoples1: list[dict[str, any]] = [
    {"name": "Bogdan1", "age": 24},  # dict 24
    {"name": "Bogdan3", "age": 20},  # dict 20
    {"name": "Bogdan1", "age": 22},  # dict 22
]


def sort1(x):
    return x["age"]


print(peoples1)
peoples2 = sorted(peoples1, key=sort1, reverse=True)
print(peoples2)
print(sorted(peoples1, key=lambda x: x["age"], reverse=True))

peoples3 = [
    [1, 1, 99, 4],  # tuple
    ("Python", 2, 6),  # list
    [99, 1, 3],  # list
]


def sort2(x):
    return x[-1]


print(peoples3)
print(sorted(peoples3, key=sort2, reverse=True))
print(sorted(peoples3, key=lambda x: x[-1], reverse=True))


########################################################################################################################

########################################################################################################################
# TODO рекурсивные функции (рекурсия)

# процедурный (код - портянка сверху вниз, справа налево)
# ООП - объектно-ориентированный (сущности-объекты и взаимодействие между ними - Ячейка, Строки, Лист, Рабочая книга)
# Функциональный - (очень математический - нет циклом(рекурсия), нет грязных функций ), Haskell)

# вывод всех чисел от нужного до 1
def while_counter(value_from):
    while value_from > 0:
        print(value_from)
        value_from = value_from - 1


while_counter(10)


def recursion_counter(value_from):
    print(value_from)
    if value_from <= 1:
        return 1
    else:
        recursion_counter(value_from - 1)


recursion_counter(10)


# факториал - произведение всех чисел от 1 до нужного
def while_factorial(stop_value: int):
    counter = 1
    while stop_value > 0:
        counter = counter * stop_value
        stop_value = stop_value - 1
    return counter


print(while_factorial(5))


def recursion_factorial(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        res = stop_value * recursion_factorial(stop_value - 1)
        return res


print(recursion_factorial(5))


# сумма всех чисел от 1 до нужного
def for_sum1(stop_value: int) -> int:
    sum_value = 0
    for i in range(1, stop_value + 1, 1):
        sum_value += i
    return sum_value


print(for_sum1(5))


def recursion_sum1(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        return stop_value + recursion_sum1(stop_value - 1)


print(recursion_sum1(5))

# проверка палиндрома
str5 = "Мадам"
str5_1 = "tea"  # анаграмма
str5_2 = "eat"  # анаграмма

str5_eq = str5[::-1]
print(str5)
print(str5_eq)
print(str5.lower() == str5_eq.lower())


def is_palindrome1(text1: str) -> bool:
    return text1.lower() == text1[::-1].lower()


print(is_palindrome1("Мадам"))


def is_palindrome2(text: str) -> bool:
    if len(text) <= 1:
        return True
    if text[0].lower() == text[-1].lower():  # "м" == "м"
        return is_palindrome2(text[1:-1:])
    else:
        return False


# "Мадам"
# str7 = "Мадам"
# print(str7)

print(is_palindrome1("Мадам"))
print(is_palindrome2("Мадам"))

print(is_palindrome1("Надам"))
print(is_palindrome2("Надам"))

print("\n\n\n\n\n**********\n\n\n\n")

########################################################################################################################

########################################################################################################################
# TODO области видимости

res2 = "Привет"  # глобальная область видимости


def sym1():
    res2 = "Пока"  # локальная(блочная) область видимости func1
    print(res2)

    # name = "Alema"


# print(name)


def sym2():
    global res2  # использование переменной из глобальной области видимости
    res2 = "Пока"  # переменная из глобальной области видимости


def sym3():
    return "Пока"


# res2 = sym3()

print(res2)
sym1()
print(res2)

time.sleep(0.1)

print(res2)
sym2()
print(res2)

# пример сложнее
local_var = 12  # глобальная область видимости
print(local_var)


def func1(var1):
    global local_var  # использование переменной из глобальной области видимости
    print(local_var)

    local_var = 10  # локальная область видимости func1
    print(local_var)

    name = "Alema1"

    def func2(var2):
        global local_var  # использование переменной из глобальной области видимости
        print(local_var)

        local_var = 10  # локальная область видимости func2
        print(local_var)

        print(var2)
        name = "Alema2"

    print(name)
    func2(var1)


func1(local_var)

print("\n\n\n\n\n**********\n\n\n\n")

########################################################################################################################

########################################################################################################################
# TODO "кэширование/мемоизация аргументов"

from functools import partial


def multiply(x, y):
    return x * y


double = partial(multiply, 2)
result1 = double(6)
print(result1)  # 12

########################################################################################################################

########################################################################################################################
# TODO __name__ == '__main__'

import _for_import


def print_hi(name):
    print(f'Hi, {name}')
    _for_import.summing(12, 13)


if __name__ == '__main__':
    print_hi('Python')


########################################################################################################################

########################################################################################################################
# TODO калькулятор на числах

def calc_3(number1, number2, operation="+"):
    print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 == 0:
            print("Второе число не может быть 0")
            return None
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
            return None
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
            return None
        else:
            return number1 % number2


result1 = calc_3(operation="/", number1=10, number2=2)
print(result1)

########################################################################################################################
