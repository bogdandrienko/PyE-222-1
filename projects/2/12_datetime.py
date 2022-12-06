# timestamp - числое отображение количества секунд от 1970 года
# 1970-01-01 00:00:01

import datetime
# from datetime import datetime
# from datetime import datetime.now
# from datetime import time

import time

# from time import time


val1 = datetime.datetime.now()  # 2022-12-06 19:21:46.411941 <class 'datetime.datetime'>
print(val1, type(val1))

val2 = datetime.datetime.timestamp(val1)  # 1670333104.69883
print(val2)
val3 = datetime.datetime.fromtimestamp(1620333104.005, tz=None)  # 2021-05-07 02:31:44.005000
print(val3)

now1 = datetime.datetime.now()  # объект типа "дата и время"
# https://www.programiz.com/python-programming/datetime/strftime
now2 = now1.strftime("%A %B %m-%d-%y, %H:%M:%S.%f")  # Tuesday December 12-06-22, 19:39:24.135024 <class 'str'>
# ("%m-%d-%YT%H:%M:%S.%f")
print(now2, type(now2))
print(now1.strftime("%d %B"))
print(now1.strftime("%H:%M"))

print("stopped")
time.sleep(0.5)  # "код" будет ждать заданное количество секунд
print("running")
print(datetime.datetime.now().strftime("%m-%d-%y, %H:%M:%S"))


def summator(start_value: int, stop_value: int) -> int:
    sum_value = 0
    for i in range(start_value, stop_value + 1, 1):
        sum_value += i
    return sum_value


point1 = time.perf_counter()  # 6161.9708401 <class 'float'>
print(point1, type(point1))
# ДО ФУНКЦИИ
res = summator(1, 1000000)
print(res)
# ПОСЛЕ ФУНКЦИИ
time_elapsed = round(time.perf_counter() - point1, 5)
print(time_elapsed)




# 5! = 1 * 2 * 3 * 4 * 5 = 120
