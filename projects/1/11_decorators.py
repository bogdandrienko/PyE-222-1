# TODO декораторы

import time
import datetime


# нужно изменить функцию (значения на входе/выходе, или действия внутри)
# 1 мы не разработчики - нет доступа
# 2 этого функционала ещё нет
# 3 мы не понимаем, как правильно изменить функцию
# 4 таких функций много

# декоратор для округления результата до 3 знака после запятой
def decorator_rounding(func):  # определение декоратора -> ссылку на функцию
    def wrapper(*args, **kwargs):  # передача аргументов к вызову функции

        # BEFORE - корректировка аргументов (параметров) на входе

        res = func(*args, **kwargs)  # вызов функции

        # AFTER - корректировка результата после отработки функции
        res = round(res, 3)

        return res  # возврат результата функции

    return wrapper


@decorator_rounding
def summing(value1, value2, value3):
    res = value1 + value2 + value3
    return res


@decorator_rounding
def divider(value1, value2):
    res = value1 / value2
    return res


print(summing(-12, 17.0006, 1))
print(divider(12, -17))


def decorator_time_measuring(function):
    def decorator(*args, **kwargs):
        time_start = datetime.datetime.now()

        result = function(*args, **kwargs)

        time_difference = datetime.datetime.now() - time_start
        print(round(time_difference.total_seconds(), 5), "sec")

        return result

    return decorator


@decorator_time_measuring
def function_something_write(value: int):
    time.sleep(0.15)  # Ядро функции 1
    return value


@decorator_time_measuring
def function_something_read():
    time.sleep(0.07)  # Ядро функции 2
    return ['12', 124325]


val1 = function_something_write(666)
print(val1)
print(function_something_read())


# наслоение декораторов
def twice(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result * 2

    return wrapper


def rounding(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return round(result, 3)

    return wrapper


@rounding
@twice
def func1(val1, val2):
    result = val1 + val2
    return result


result2 = func1(val1=12, val2=15.95324325)  # 55.906
print(result2)


###################################################################################
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


result2 = func2(2, divider=2)
print(result2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (1, 2, 3)
dict1 = {"name": "Python", "age": 20}

list3 = [*list2, *list1]
print(list3)  # [1, 2, 3]
print(*list3)  # 1 2 3
print(tuple1)  # (1, 2, 3)
print(*tuple1)  # 1 2 3 unpacking
print(1, 2, 3)  # 1 2 3 unpacking

print(dict1)  # {'name': 'Python', 'age': 20}
print(*dict1)  # name age
print(dict1.items(), type(dict1.items()))  # dict_items([('name', 'Python'), ('age', 20)]) <class 'dict_items'>
for key, value in dict1.items():  # auto unpacking
    print(f"{key}: {value} !!!")
