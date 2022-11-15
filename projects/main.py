import math
import time

# Программирование - оперирование типами данных

# float

# Контейнер (область в оперативной памяти, для переменной)
# имя переменной - ссылка на область в оперативной памяти

float1 = 12.15  # 0.0 -10.0 float - число с плавающей точкой
int1 = 12  # 0 -10 integer - целочисленное значение
# с++ - float / decimal / integer - smallinteger - biginteger /

str1 = "B o g dan"  # string - строка
str2 = "B"  # string - строка
str3 = ""  # string - строка
str4 = 'Python'  # string - строка
str5 = 'I"m ready'  # string - строка
str6 = "I'm ready"  # string - строка
str7 = """I''"''m ready"""  # string - строка
# с++ - char / string

bool1 = True  # False bool - (Правда или ложь) 1 и 0

list1 = []  # list список
#        0   1      2        3      4
list2 = [12, 15, 15, "Python", False]  # list список

set1 = {50.0, 12}  # set множество (только уникальные элементы)
set2 = {}

tuple1 = (15, 15, "Python")  # tuple Кортеж (неизменяемый - меньше оперативной памяти)
tuple2 = (15,)
tuple3 = ("",)

none1 = None  # ничто

list4 = [12, 15, 15, "Python", False]
# print(объект) - вывод на экран
# print(list4)
# list4.append("Awesome")
# print(list4)

dict1 = {"key": "value"}  # dict словарь (коллекция - массив, с парами ключ-значение)
dict2 = {
    # 1 пара
    "key": {"key": "value"},
    # 2 пара
    "Студенты": ["Амина", "Алишер"]
}

dict3 = {"key": "value"}
# print(dict3)  # {'key': 'value'}
# print(dict3["key"])  # value

dict3["Мой номер"] = "+7 176"  # присвоение
dict3["IIN"] = 180  # присвоение
# print(dict3)  # {'key': 'value', 'Мой номер': '+7 176'}
# print(dict3["Мой номер"])  #

# type(объект) узнать тип

result = type(False)  # <class 'bool'>
# print(result)

res1 = False


# print(type(res1))  # <class 'bool'>


# def - define - определить
# def имя_фунции(аргумент1, аргумент2...): - ОПРЕДЕЛЕНИЕ ФУНКЦИИ (! ЕЁ НУЖНО ВЫЗВАТЬ !)
#   расчёт...
def sum_two_values(value1, value2):  # snake case
    result5 = value1 + value2  # расчёты....
    # print(result5)
    return result5  # возврат результата


res4 = sum_two_values(13, 12)
# print(res4)
# print(12)

result9 = 10 - 10
result10 = 10 + 10
result11 = 10 * 10
result12 = 10 / 10  # 1.0
result13 = 15 // 10  # 1 - округляет до целого вниз
result14 = 2 ** 4  # 16 - возведение в степень
result15 = 16 ** 0.5  # 4.0 - извлечение из под корня
result16 = int(math.sqrt(16))  # float()  # 4 - извлечение из под корня
result17 = 15 % 4  # 3 - остаток от деления
result21 = 15 < 4  # False -
result22 = 15 > 4  # True -
result23 = 15 <= 4  # 3 -
result24 = 15 >= 4  # 3 -
result25 = 15 == 4  # False - равен ли
result26 = 15 != 4  # True - не равен ли
# print(result17)

# 1 - 1000
# итерация - повторение
# переменная цикла  старт  стоп ШАГ
final = 0
for value in range(1, 1000 + 1, 1):
    # 1 ... 2 ... 3
    # print(value)
    final = final + value
    # print(final)

for i in ["Амина", "Алишер", "Амина", "Алишер", "Амина", "Алишер"]:
    # print(i)
    pass

for i in "Амина":
    # print(i)
    pass


def something():
    pass


# seconds = 0
# minuts = 0
# while seconds < 60:  # пока(пока ещё)
# print(seconds)
# seconds = seconds + 1
# seconds += 1  # increment увеличение
# seconds -= 10  # increment увеличение
# seconds *= 10  # increment увеличение


# val1 = 15
# val2 = 20
#
# if val1 < val2:  # если
#     print("Больше")  # ПРАВДА
# else:  # ЛОЖЬ
#     print("не больше")

seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(0.001)
    if seconds < 60:
        seconds += 1
    else:
        if minutes < 60:
            minutes += 1
            seconds = 0
        else:
            if hours < 24:
                minutes = 0
                hours += 1
            else:
                seconds = 0
                minutes = 0
                hours = 0

    # print("секунды: ", seconds)
    # print("минуты: ", minutes)
    # print("часы: ", hours)

    # print("секунды: " + str(seconds) + "минуты: ")
    print(f"{hours}:{minutes}:{seconds}")  # f-строка - вложение переменной любого типа внутрь строки
    # конкатенация строк (сложение)
