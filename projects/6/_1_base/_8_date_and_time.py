########################################################################################################################
# TODO работа с датой и временем
import sys
import time
import datetime
# from datetime import datetime
# from datetime import time
# from datetime import timezone  # часовые пояса
# from datetime import timedelta  # разницы, вычитание, сложение

# timestamp - числовое отображение количества секунд от 1970-01-01 00:00:01

var1 = 1677248234
var2 = "1677248234"

print(sys.getsizeof(var1))
print(sys.getsizeof(var2))

val1 = datetime.datetime.now()  # 2023-02-24 20:21:00.934978 <class 'datetime.datetime'>
print(val1, type(val1))

# изменение времени
print(datetime.datetime.now() + datetime.timedelta(minutes=10, hours=2))

# форматирование даты и времени
now1 = datetime.datetime.now()  # объект типа "дата и время"
now2 = now1.strftime("%A %B %m-%d-%y, %H:%M:%S")  # Friday February 02-24-23, 20:36:54 <class 'str'>
print(now2, type(now2))


# https://www.programiz.com/python-programming/datetime/strftime
# https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/

print(now1.strftime("%d %B"))
print(now1.strftime("%H:%M"))
print(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))

# получение timestamp
val3 = datetime.datetime.now()
val4 = datetime.datetime.timestamp(val3)  # 1 677 249 511.573126
print(val4)

val5 = datetime.datetime.fromtimestamp(1577249511.573126, tz=None)  # 2019-12-25 10:51:51.573126
print(val5)

########################################################################################################################

########################################################################################################################
# TODO time

# "задержки кода"
print("stopped")
time.sleep(1.5)  # "код" будет ждать заданное количество секунд
print("running")


# замер производительности
def sum1(start_value: int, stop_value: int) -> int:
    sum_value = 0
    for i in range(start_value, stop_value + 1, 1):
        sum_value += i
    return sum_value


point1 = time.perf_counter()  # 6161.9708401 <class 'float'>
print(point1, type(point1))

# ДО ФУНКЦИИ
res = sum1(1, 10000000)
print(res)
# ПОСЛЕ ФУНКЦИИ

point2 = time.perf_counter()
time_elapsed = round(point2 - point1, 3)
print(time_elapsed)  # 0.364

########################################################################################################################
