########################################################################################################################
# TODO типы данных
from decimal import Decimal
from collections import OrderedDict


bool1 = True
bool2 = False

int1 = 12
float1 = 12.0135235
decimal1 = Decimal(12.01352352452345242346246245245)

str1 = "Python"  # dynamic typing
str2: str = "Python"  # static typing
str3 = 'Python'
str4 = "I'm"
str5 = '"Синоним"'
str6 = """

    ***Python

"""

bytes1 = b"Python"
bytes2 = b'\x01\x02\x03\x04\x05'

bytes3 = str5.encode()
str7 = bytes1.decode()

dict1 = {"name": "Python"}  # not ordered
dict1['age'] = 22

dict2 = dict(name="Python")  # not ordered

dict3 = OrderedDict()  # ordered
dict3['name'] = 'Python'

tuple1 = ("admin", "Qwerty!")  # not change
tuple2 = ("admin",)
tuple3 = (12, "job")

list1 = ["admin", "Qwerty!"]  # not change
list2 = ["admin"]
list3 = [12, "job"]

list1[0] = 12
list1.append(666)

set1 = {1, 2, 3}  # only unique elements
set2 = {1, 2, 2, 3}
print(set2)

# set1.difference()
# set1.intersection()

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
print(isinstance(12.0, int))  # False

# конвертация типов данных:
float_to_int1 = int(10.5)  # int()
int_to_float1 = float(10)  # float()
str_to_float1 = float("10.2")  # float()
int_to_str1 = str(10.4)  # str()
int_to_bool1 = bool(0)  # bool()  0 '' [] () - false | != 0 - true "f" [1]
set_to_list1 = list((1, 2, 2, 5))  # list()
# list_to_set1 = set([1, 2, 2, 5])  # set()
list_to_set1 = set(set_to_list1)  # set()
# ...

# получение ввода от пользователя
# str_from_user1 = input("Введите Ваше имя: ")  # !STR
# print("Hello " + str_from_user1)

# получение элементов из коллекции
#              012345678    -2-1
source_str1 = "Python is awesome"  # ['P', 'y', 't'...]

source_str2 = source_str1[8]  # index elem
print(source_str2)  # s

source_str3 = source_str1[-2]
print(source_str3)  # m

#                       start:stop:step
# source_str4 = source_str1[7:len(source_str1):1]
source_str4 = source_str1[:6:]
print(source_str4)  # Python
source_str4 = source_str1[7::]
print(source_str4)  # is awesome

#               0  1  2  3
source_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]]

dict4 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
}
print(dict4)
print(dict4["age"])
dict4["money"] = Decimal(12.05)
print(dict4)
del dict4["arr"]
print(dict4)
