# TODO функции
import math
from typing import Union
import operator


# код "до" функции
def function1():  # определение функции
    print("Hi")
    # код "внутри" функции (отступы: 2-4 пробела)

# код "после" функции

link1 = function1  # ссылка на функцию
link1()  # вызов функции
function1()  # вызов функции


# грязная функция
def twice_value1(val1, val2):  # функция с параметрами (аргументами)
    result = val1 ** val2
    print(result)


twice_value1(5, 2)


# чистая функция
def twice_value2(val1, val2):
    result = val1 ** val2
    return result  # возврат значения


result1 = twice_value2(5, 2)  # позиционные аргументы
print(result1)
result2 = twice_value2(val2=2, val1=6)  # именные аргументы
print(result2)


def twice_value3(val1, val2=1):  # функция со стандартным параметром (аргументом)
    result = val1 ** val2
    return result


result3 = twice_value3(val1=6)
print(result3)
result4 = twice_value3(val1=6, val2=2)
print(result4)


# TODO типизация

# Типизация - строгое задание типов для переменных и параметров (аргументов)
# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++(C) - статическая типизация (- скорость разработки + скорость работы - к багам)


def twice_value4(val1: float, val2=2) -> Union[int, float]:  # функция с типизацией
    result = val1 ** val2
    return result


def twice_value5(val1: float, val2=2) -> int | float:  # функция с типизацией
    result = val1 ** val2
    return result


result4 = twice_value5(val1=6) / 10
print(result4)

# TODO стандартные функции

print(sum([1, 2, 3]))
print(round(2.555, 1))
print(int(2.0))
print(type(True))
print(input("Введите: "))
print(abs(-100))
print(len("Привет"))
print(len([1, 2, 3, 4, 5]))

print(any([False, False, False, False]))
print(any([False, True, False, False]))
print(any([True, False, False, False]))

print(all([True, True, True, True]))
print(all([False, True, True, False]))
print(all([False, False, False]))


# ...
# https://pythonru.com/osnovy/vstroennye-funkcii-python
# https://letpy.com/handbook/builtins/

# TODO анонимные функции (lambda)

def multiply1(a, b):
    return a ** b


multiply2 = lambda a, b: a ** b

res4 = multiply1(6, 2)
res5 = multiply2(6, 2)
print(res4)
print(res5)

peoples1 = [
    {"name": "Bogdan1", "age": 24},  # dict 24
    {"name": "Bogdan1", "age": 22},  # dict 22
    {"name": "Bogdan3", "age": 20},  # dict 20
]


def sort1(x):
    return x["age"]


sorted_peoples1 = sorted(peoples1, key=lambda x: x["age"], reverse=True)
print(sorted_peoples1)

sorted_peoples1.sort(key=lambda x: x["age"], reverse=True)  # меняет исходный объект
print(sorted_peoples1)

peoples2 = [
    [1, 1, 99, 4],  # tuple
    ("Python", 2, 6),  # list
    [99, 1, 3],  # list
]


def sort2(x):
    return x[-1]


print(sorted(peoples2, key=sort2, reverse=True))
print(sorted(peoples2, key=lambda x: x[-1], reverse=True))


# TODO рекурсивные функции (рекурсия)

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
        # counter = counter * stop_value
        counter *= stop_value
        # stop_value = stop_value - 1
        stop_value -= 1
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


print(for_sum1(10))


def recursion_sum1(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        res = stop_value + recursion_factorial(stop_value - 1)
        return res


print(recursion_sum1(10))

str5 = "мадам"
str6 = str5[::-1]
cond5 = str5 == str5[::-1]


def is_palindrome1(text1: str):
    return text1 == text1[::-1]

    # text2 = text1[::-1]
    # if text1 == text2:
    #     return True
    # else:
    #     return False


def is_palindrome2(text: str):
    if len(text) < 1:
        return True
    if text[0] == text[-1]:  # "p" == "p"
        return is_palindrome2(text[1:-1])
    else:
        return False


print(is_palindrome1("Мадам"))
print(is_palindrome2("Мадам"))

# TODO области видимости
global_var = 12  # глобальная область видимости
print(global_var)


def func1(var1):
    global global_var  # использование переменной из глобальной области видимости
    print(global_var)

    global_var = 10  # локальная область видимости func1
    print(global_var)

    def func2(var2):
        global global_var  # использование переменной из глобальной области видимости
        print(global_var)

        global_var = 10  # локальная область видимости func2
        print(global_var)

        print(global_var)

        def func3(var2):
            global global_var  # использование переменной из глобальной области видимости
            print(global_var)

            global_var = 10  # локальная область видимости func3
            print(global_var)

            print(global_var)

    func2(var1)

    pass


print(global_var)
func1(global_var)
print(global_var)

res2 = "Привет"


def sym3():
    global res2
    res2 = "Пока"


print(res2)
sym3()
print(res2)

# TODO __name__ == '__main__'

import for_import


def print_hi(name):
    print(f'Hi, {name}')
    for_import.summing(12, 13)


if __name__ == '__main__':
    print_hi('Bogdan')


# TODO калькулятор на числах

def calc_3(number1, number2, operation="-"):
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
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 % number2


result1 = calc_3(operation="/", number1=10, number2=2)
print(result1)

############################################################################################







####################################################
# todo объявление функции
def print_hello():
    print("Hello world11111!")


# todo объявление функции

# todo вызов функции
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# todo вызов функции

# DRY - don't repeat yourself
# action > 2 (>=2)

input_from_user = 12  # замодокументируемый код


def multiply_two_values(val1, val2):  # замодокументируемый код
    # эта функция умножает два значения
    result = val1 / val2
    print(result)


# multiply_two_values(10, 20)  # позиционные аргументы
# multiply_two_values(val2=20, val1=10)  # именные аргументы


def multiply_two_values_clear(val1, val2):
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 / val2
    return result  # clear function


res = multiply_two_values_clear(val2=20, val1=10)


# print(res)

def multiply_two_values_default(val1=10, val2=10):
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 / val2
    return result  # default function


res2 = multiply_two_values_default()
print(res2)


# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++ - статическая типизация (- скорость разработки + скорость работы - к багам)

def multiply_two_values_typing(val1: float, val2=12) -> float:
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 * val2
    # return "result"  # typing function
    return result  # typing function


res2 = multiply_two_values_typing(val1=12, val2=15) / 10
print(res2)
print("Продолжение")


def multiply(a: float, b: float) -> float:
    return a * b


def calculate(a: float, b: float, action="+") -> float:
    match action:
        case "+":
            return a + b
        case "-":
            return a - b
        case _:
            print("Вы ввели некорректное действие")
            return None
    return None


val1 = float(input("Введи первое число: "))  # int == float | float != int
val2 = float(input("Введи второе число: "))
action = input("Введи действие (+ - * / ** ^): ")
res3 = calculate(val1, val2, action)
print(res3)
