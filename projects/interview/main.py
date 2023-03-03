# https://www.edureka.co/blog/interview-questions/python-interview-questions/
# https://intellipaat.com/blog/interview-question/python-interview-questions/
# https://mindmajix.com/python-interview-questions

########################################################################################################################

# What is the difference between list and tuples in Python?
# неизменяемый(кортеж), синтаксис, методы(действия над объектом), меньшее потребление

list1 = [""]
tuple1 = ("",)

########################################################################################################################

# What are the key features of Python?
# лёгкий синтаксис, скорость разработки, наибольшее количество библиотек (numpy, opencv, pandas, keras, tensorflow...)

########################################################################################################################

# What type of language is python?
# динамическая типизация, интепретируемый(читает код на лету - .py), со сборщиком мусора (GC - garbage collector)

# (компилятор - собирает код в байт код 0101010)

a: int = 12  # подобие статической типизацию
print(a)
a = "12"  # Warning
print(a)

########################################################################################################################

# How is Python an interpreted language?
# yep,

########################################################################################################################

# What is pep 8?
# рекомендации (соглашение) для программистов как писать код (отступы)

########################################################################################################################

# How is memory managed in Python?
# автоматически, сборщиком мусора (GC - garbage collector), когда переменные(ссылки) выходят из области видимости,
# сборщик их чистит
# a = 12
# b = a
# del a

########################################################################################################################

# What is name space in Python?
# пространство имён

# name = "Dina"  # global
#
#
# def check_name():
#     name = "Amina"  # local for "check_name"
#
#     global name
#     name = "Amina"  # global
#
#     def check_name1():
#         name = "Amina"  # local for "check_name1"
#
#         def check_name2():
#             name = "Amina"  # local for "check_name2"
#
#
# print(name)
# check_name()
# print(name)

########################################################################################################################

# What is the Difference Between a Shallow Copy and Deep Copy?
#

a = 12


def summing(a, b=2):
    print(a + b)
    return a + b


a = summing(a)

dict1 = {"username": "Dias", "password": "Qwerty!"}


# {'username': 'Dias', 'password': 'Qwerty!'}
def change(dictionary: dict):
    dictionary.clear()
    return dictionary


print(dict1)
# change(dict1)  # поверхностная копия - отправляет только ссылка на тот же объект
change(dict1.copy())  # глубокая копия - для отправляемого аргумента создаёт полная копия
print(dict1)

# https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/01/Python-Shallow-Copy-Deep-Copy.jpg

########################################################################################################################

# What are the two major loop statements?
# while(do while) / for

########################################################################################################################

# What is the difference between .py and .pyc files?
# .py - python like lang files
# .pyc - python bytes - precompile

########################################################################################################################

# deploy - ci/cd
# Развёртывание программного обеспечения — это все действия, которые делают программную систему готовой к использованию
# https://habr.com/ru/company/otus/blog/515078/

#####################################################################

# What is slicing in Python?
# отрезок (получение подколлекции) - коллекции данных (list, array, tuple, str)
str5 = "Python"
str7 = str5[:3:]
print(str7)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple2 = tuple(range(1, 10 + 1))
print(list1)
print(tuple2)

print(list1[1::2])

################################

# Is python case sensitive?
# yes

def Func1():
    print("Func1")

def func1():
    print("Func1")

Func1()

##############################

# What is type conversion in Python?
# все конвертации происходят с помощью одноимённых функций int - int()

num1 = int("12")  # str -> int
num2 = float("12.0")  # str -> int
num3 = str(12.0)  # str -> int
tuple3 = tuple(["12", 2])

#######################################

# What are Literals in Python and explain about different Literals
# примитивные типы данных, которые не изменяются и передаются по ссылке как объект

aaa = {"12": 12, 12: 12, ('', ): 12}

###################################################
