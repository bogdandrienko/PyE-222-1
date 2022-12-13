# TODO работа с датой и временем

import time
import datetime

# from datetime import datetime
# from datetime import time
# from datetime import timezone
# from datetime import timedelta

# timestamp - числовое отображение количества секунд от 1970-01-01 00:00:01

# текущее время
val1 = datetime.datetime.now()  # 2022-12-13 19:25:02.985214 <class 'datetime.datetime'>
print(val1, type(val1))

# изменение времени
print(datetime.datetime.now() + datetime.timedelta(minutes=10, hours=-2, days=1))  # 2022-12-14 17:37:04.658784

# форматирование даты и времени

now1 = datetime.datetime.now()  # объект типа "дата и время"
now2 = now1.strftime("%A %B %m-%d-%y, %H:%M:%S.%f")  # Tuesday December 12-13-22, 19:27:59.358846 <class 'str'>

# https://www.programiz.com/python-programming/datetime/strftime
# https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/

print(now2, type(now2))
print(now1.strftime("%d %B"))
print(now1.strftime("%H:%M"))
print(datetime.datetime.now().strftime("%m-%d-%y, %H:%M:%S"))

# получение timestamp
val3 = datetime.datetime.now()
val4 = datetime.datetime.timestamp(val3)  # 1670938181.000156
print(val4)

val5 = datetime.datetime.fromtimestamp(1620333104.005, tz=None)  # 2021-05-07 02:31:44.005000
print(val5)

# "задержки кода"
print("stopped")
time.sleep(0.5)  # "код" будет ждать заданное количество секунд
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

time_elapsed = round(time.perf_counter() - point1, 3)
print(time_elapsed)  # 0.389
