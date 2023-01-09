########################################################################################################################
# TODO ООП
import concurrent
import time
from concurrent.futures import ThreadPoolExecutor


# Объектно-ориентированное программирование: способ представления взаимодействий сущностей как в реальной жизни

# Процедурное программирование - Паскаль
# Функциональное программирование F#
# Объектно-ориентированное программирование  C#, Делфи, Python, C++

# int -> object
# str -> object
# bool -> object
# int1 = 12
# print(type(int1))

#     object
# class Samsung(object):
#     pass
class Samsung:
    display = "17'"  # переменные класса
    new = True  # переменные класса
    price = 8000000  # переменные класса

    def print_is_old(self):  # method - метод (функция внутри класса)
        if self.new:
            print("I'm a new")
        else:
            print("I'm not a new")


sams1 = Samsung()  # создание объекта -> инициализация, создание инстанса(экземпляр)
# print(sams1)  # <__main__.Samsung object at 0x000001F44E997040>
# print(type(sams1))  # <class '__main__.Samsung'>
# print(sams1.display, sams1.price, sams1.new)  # 17' 8000000 True
# print(sams1.print_is_old())
#
# sams2 = Samsung()  # создание объекта -> инициализация, создание инстанса(экземпляр)
# print(sams2.price)  # 8000000


#                  Electric
#      Smartphone                 PC
#  Samsung      Iphone  Lg     mobile       desktop
#  A70   A50                           mac   windows
# 5000 6000 mah

class Figure:
    def __init__(self, side1: int | float, side2: int | float):
        self.side1 = side1  # переменные экземпляра класса
        self.side2 = side2  # переменные экземпляра класса

    def perimeter(self) -> int | float:
        result = (self.side1 + self.side2) * 2
        return result

    def area(self) -> int | float:
        return self.side1 * self.side2


class Pramoug(Figure):
    pass


class Square(Figure):
    def __init__(self, side: int | float):
        super().__init__(side, side)


# pr1 = Pramoug()
# print(pr1.perimeter())
# print(pr1.area())
# pr2 = Pramoug(7, 7)
# print(pr2.perimeter())
# print(pr2.area())

# sq1 = Square(10)
# print(sq1.perimeter())
# print(sq1.area())


#                     объект - видимость, рендеринг, коллизии (физики)
#                     техника - скорость, масса, может с ними взаимодействовать
#         сухопутные водоплавающие - точки, где можно перемещаться
#  Велосипед Машина Мотоцикл гидро скутер Лодка - текстуры, цвет

class Grandmother1:
    eyes_color = "red"

    def give_many(self):
        return 12000


class Mother1(Grandmother1):
    eyes_color = "brown"

    def say_hi(self):
        print("HEEEEEELOOO")

    def build_house(self):
        print("!!!!!!!!!")


class Father1:
    eyes_color = "blue"

    def build_house(self):
        print("completed")

    def say_hi(self):
        print("hi")


class Child1(Mother1, Father1):  # множественное наследование
    eyes_color = "yellow"  # override
    pass


# child1 = Child1()
# print(child1.eyes_color)
# print(child1.say_hi())
# print(child1.build_house())

class Calculator:
    def __init__(self, val1: int | float, val2: int | float):
        self.val1 = val1
        self.val2 = val2

    def summing(self):
        return self.val1 + self.val2

    def substract(self):
        return self.val1 - self.val2

    def muliply(self):
        return self.val1 * self.val2

    @staticmethod  # статический метод не имеет привязки к экземпляру
    def multiply(val1, val2):
        return val1 * val2


calc1 = Calculator(10, 5)
calc2 = Calculator(7, 3)

print(calc1.summing())
print(calc2.summing())

print(calc1.muliply())
print(calc2.muliply())

print(Calculator.multiply(10, 20))

import utils

# from .utils import Datetime, Excel

print(utils.Datetime.get_current_time())
print(utils.Datetime.get_asia_time())

excel1 = utils.Excel(filename="new1.xlsx")
excel2 = utils.Excel(filename="new2.xlsx")

print(excel1.read_all())
print(excel2.read_all())
print(excel2.read_selected_row(4))
print(excel2.read_selected_row(5))
print(excel2.read_selected_row(6))
matrix = \
    [
        [1111, 2222, 3333],
        [1111, 2222, 3333],
        [1111, 2222, 3333],
        [1111, 2222, 3333],
        [1111, 2222, 3333],
        [1111, 2222, 3333],
    ]
print(excel2.read_selected_row(6))

# excel2.write_from_coordinates(matrix=matrix, start_row=1, start_column=1)

print(utils.Datetime.get_time_in_selected_timezone(grinvich=0))

data = [
    '11111111111111',
    "222222222222222",
    "3333333333333",
    '11111111111111',
    "222222222222222",
    "3333333333333",
    '11111111111111',
    "222222222222222",
    "3333333333333",
    '11111111111111',
    "222222222222222",
    "3333333333333",
    '11111111111111',
    "222222222222222",
    "3333333333333",
    '11111111111111',
    "222222222222222",
    "3333333333333",
]

time_start = time.perf_counter()


def write_to_file(filename: str, text: str):
    print("STAAAAAAAAAAAAAAART")
    with open(f"temp/{filename}", "wb") as file:
        file.write(text.encode())
    time.sleep(0.5)
    print(utils.Main.Datetime.get_current_time())


index = 0
for i in data:  # 9.17958120000003
    index += 1
    # write_to_file(filename=f"{index}.txt", text=i)

count = len(data)
print(count)  # 18

#            0.5427359999994223
# utils.MyMultithreading.start_in_side_threads(write_to_file, objects=data, max_workers=18)

time_stop = time.perf_counter()

print(time_stop - time_start)

# with ThreadPoolExecutor(max_workers=1) as executor:
#     executor.submit(write_to_file, f"1.txt", "111111111111111")

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = []
#     for url in data:
#         futures.append(executor.submit(write_to_file, 1, 1))
#     for future in concurrent.futures.as_completed(futures):
#         print(future.result())

# CRUD
print(utils.Main.Databases.read(db="new_db", query="Select * from books order by id desc", autocommit=True))
