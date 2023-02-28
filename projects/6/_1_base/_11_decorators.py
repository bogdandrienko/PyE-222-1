########################################################################################################################
# TODO декораторы

import time
import datetime


# нужно изменить функцию (значения на входе/выходе, или действия внутри)
# 1 мы не разработчики - нет доступа
# 2 этого функционала ещё нет
# 3 мы не понимаем, как правильно изменить функцию
# 4 таких функций много (DRY - don`t repeat yourself)
# SOLID (одиночная ответственность) / KISS (как можно проще)

# декоратор для округления результата до 3 знака после запятой
def decorator_rounding(func):  # определение декоратора -> ссылку на функцию
    def wrapper(*args, **kwargs):  # args аргументы - позиционные (tuple) | key-word args - именные {dict}
        # todo BEFORE

        # подмена
        # new_first_value = int(dict1["first_value"])  # todo взятие из словаря значения
        # dict1["first_value"] = new_first_value  # todo обновления значения в словаре по ключу

        print(args)
        print(kwargs)

        # подмена
        new_value2 = abs(kwargs["value2"])  # todo взятие из словаря значения
        kwargs["value2"] = new_value2  # todo обновление значения в словаре по ключу

        # подмена

        new_value1 = args[0] * 2  # todo взятие из кортежа значения по индексу
        list1 = []  # todo создание массива
        list1.append(new_value1)  # todo обновление значения в кортеже по индексу
        args = tuple(list1)

        # # anti-ddos
        # if requests > 100:
        #     raise Exception
        #
        # # authentificataion
        # if data["password"] != password:
        #     raise Exception

        print(args)
        print(kwargs)
        # todo BEFORE
        result = func(*args, **kwargs)
        # todo AFTER
        result = round(result, 2)  # todo CORE
        # todo AFTER
        return result

    return wrapper


@decorator_rounding
def summing(value1, value2, value3):
    print("summing")
    res = value1 + value2 + value3
    return res  # возврат результата функции


@decorator_rounding
def divider(value1, value2):
    res = value1 / value2
    return res  # возврат результата функции


# def round_new(val):
#     return round(val, 2)
#
#
# res1 = summing(-12, 17.0006, 1)
# print(round_new(res1))  # вызов функции и вывод результата
# print(round_new(divider(12, -17)))  # вызов функции и вывод результата

# print(summing(value1=-12, value2=17.0006, value3=1))  # вызов функции и вывод результата
# print(divider(12, -17))  # вызов функции и вывод результата # todo позиционные
# print(divider(12, value2=-17))  # вызов функции и вывод результата # todo именнованные

# # исходник
# dict1 = {"first_value": 12.7, "second_value": 2}
#
# # подмена
# new_first_value = int(dict1["first_value"])
# dict1["first_value"] = new_first_value
#
# # результат
# result = dict1["first_value"] / dict1["second_value"]
# print(result)

# замер производительности
def decorator_time_measuring(function):  # объявление имени декоратора и получение функции как аргумент
    def decorator(*args, **kwargs):  # объявление "внутренней функции" и получение аргумен. для вызова функции-аргумента
        start = time.perf_counter()  # первая отсечка времени
        result = function(*args, **kwargs)  # вызов функции-аргумента
        stop = time.perf_counter()  # вторая отсечка времени
        print("elaped time: ", stop - start)  # рассчёт занятого времени
        return result  # возврат "внутренней функции"

    return decorator  # возврат "внутренней функции"


def decorator_rounding2(function):
    def decorator(*args, **kwargs):
        result = int(function(*args, **kwargs))
        return result

    return decorator


@decorator_rounding2
@decorator_time_measuring
def count_sum(stop):
    counter = 1.5123523524524652346
    for i in range(1, stop + 1):
        counter += i
    return counter


@decorator_time_measuring
def count_mul(stop):
    counter = 1
    for i in range(1, stop + 1):
        counter *= i
    return counter


# print(count_sum(10000000))
# print(count_sum(20000000))


# print(count_mul(500))

# наслоение декораторов
def twice(function):
    def wrapper(*args, **kwargs):
        print("twice")
        result = function(*args, **kwargs)
        return result * 2

    return wrapper


def rounding(function):
    def wrapper(*args, **kwargs):
        print("rounding")
        result = function(*args, **kwargs)
        return round(result, 3)

    return wrapper


@twice
@twice
@rounding
@twice
def func1(val1, val2):
    result = val1 + val2
    return result


# result2 = func1(val1=12, val2=15.95324325)
# print(result2)


########################################################################################################################

########################################################################################################################
# TODO *args & **kwargs

# args - позиционные аргументы (tuple - кортеж)
# kwargs - именные аргументы (dict - словарь)

def twice_of_divider2(function):
    def wrapper(*args, **kwargs):
        print(args, type(args))  # func2(2, 2) => (2, 2) <class 'tuple'>
        print(args, type(args))  # func2(val1=2, divider=2) => () <class 'tuple'>

        print(kwargs, type(kwargs))  # func2(2, 2) => {} <class 'dict'>
        print(kwargs, type(kwargs))  # func2(val1=2, divider=2) => {'val1': 2, 'divider': 2} <class 'dict'>

        # kwargs["divider"] = kwargs["divider"] * 2
        kwargs["divider"] *= 2

        result = function(*args, **kwargs)

        return result

    return wrapper


@twice_of_divider2
def func2(val1, divider):
    result = val1 / divider
    return result


# result2 = func2(2, divider=2)
# print(result2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (1, 2, 3)
dict1 = {"name": "Python", "age": 20}

list3 = []
# print(list3)
# list3.extend(list1)
# list3.extend(list2)
# print(list3)

# print(list3)
# for i in list1:
#     list3.append(i)
# for i in list2:
#     list3.append(i)
# print(list3)

# print(list3)
# list3 = [*list1, *list2]
# print(list3)

print(list1)
print(*list1)  # unpacking

print(list3)  # [1, 2, 3]
print(*list3)  # 1 2 3
print(tuple1)  # (1, 2, 3)
print(*tuple1)  # 1 2 3 unpacking
print(1, 2, 3)  # 1 2 3 unpacking

print(dict1)  # {'name': 'Python', 'age': 20}
print(*dict1)  # name age
# print(**dict1)  # dict(name="Python", age=20)
print(dict1.keys(), dict1.values(), dict1.items())
for k, v in dict1.items():
    print(f"{k}(key)", f"{v}(значение)")

########################################################################################################################
