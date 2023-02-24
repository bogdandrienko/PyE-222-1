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
