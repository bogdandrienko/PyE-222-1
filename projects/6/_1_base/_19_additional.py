# TODO каскадное присваивание
a1 = b1 = c1 = 12  # все "переменные" имеют ссылку на один объект
print(a1, b1, c1)

# TODO множественное присваивание
a2, b2, c2 = 1, 2, 3
print(a2, b2, c2)
# username, password = input(), input()

# TODO смена ссылок
x1 = 12
print(x1)
x1 = 13  # redeclared  # имя переменной начинает ссылаться на другой объект,
# предыдущий объект остаётся прежним (т.к. integer неизменяемый тип) и без ссылки "убивается" сборщиком мусора

# TODO "неизменяемость" строк
y1 = "Python"
print(y1[1])
# y1[1] = "x"
y1 = "Python 1"

# TODO обмен переменных
a3 = 12
b3 = 13
c3 = None

# 0   1     0   1
(a3, b3) = (b3, a3)

# c3 = a3
# a3 = b3
# b3 = c3
# print(a3, b3)

# TODO "множественное" возведение в степень
# a4 = 2 ** 3 ** 2

a4_1 = 3 ** 2
a4 = 2 ** a4_1
print(a4_1, a4)

# TODO else в цикле while
index = 1
while index < 10:
    print(index)
    index += 1
    # break
else:
    # блок только если цикл успешно завершён (без break)
    print(index)

# todo корутины
import asyncio


async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)


coroutine_counter = count_to_three()
print(coroutine_counter)  # <coroutine object count_to_three at 0x000002063E2E2E30>
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 1"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 2"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 3"
# coroutine_counter.send(None)  # Выбросит ошибку StopIteration

# todo отладчик python
import pdb


def make_bread():
    pdb.set_trace()
    return "У меня нет времени"


# print(make_bread())

# todo распаковка
def profile():
    name = "Danny"
    age = 30
    return name, age, 666


res = profile()
print(res)
profile_name, profile_age, a = profile()
print(profile_name, profile_age, a)

# todo enumerate
my_list = ['apple', 'banana', 'grapes', 'pear']
index1 = 2
for value in my_list:
    print(index1, value)
    index1 += 1

for index2, value in enumerate(my_list, 2):
    print(index2, value)

# todo map
items = [1, 2, 3, 4, 5]


def multiply(x):
    return x * x


def add(x):
    return x + x


list3 = []
for i in items:
    list3.append(multiply(i))
print(list3)

squared = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(squared)

# todo filter
list4 = [1, 2, 3, 4, 5, 6, 7, 8]
list5 = []
for i in list4:
    if i % 2 == 0:
        list5.append(i)
print(list5)

filtered1 = list(filter(lambda i: i % 2 != 0, list4))
print(filtered1)


from functools import reduce
list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x + y, list8)
print(product)

res = 0
for i in list8:
    res = res + i
print(res)
