# TODO арифметические операторы

import math
import operator

print(10 + 10)  # сложение
print(10 - 10)  # вычитание

print(10 * 10)  # умножение
print(10 / 10)  # деление
print(15 // 10)  # целочисленное деление (отбрасывает дробную часть)

print(15 % 4)  # остаток от деления
print(9 % 2 == 0)  # проверка числа на чётность
print(9 % 2 != 0)  # проверка числа на нечётность

print(2 ** 4)  # возведение в степень
print(16 ** 0.5)  # извлечение из-под корня

print(math.sqrt(16))  # извлечение из-под корня с помощью библиотеки
print(math.exp(2))  # ... другие математические операции

print(15 < 4)  # меньше
print(15 > 4)  # больше
print(15 == 4)  # равно
print(15 != 4)  # не равно
print(15 <= 4)  # меньше или равно
print(15 >= 4)  # больше или равно

###################
seconds = 0
seconds = seconds + 1
seconds += 1  # increment

seconds = seconds - 1
seconds -= 1  # decrement

seconds = seconds * 2
seconds *= 2  # multiply
# ...


a = 5
b = 2
print(operator.truediv(a, b))
print(operator.floordiv(a, b))
print(operator.pow(a, b))

# in
list1 = [1, 2]
val1 = 2
cond3 = val1 in list1  # True
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")

str1 = "Python"
chr1 = "P"  # "P".lower() => "p"
chr2 = "p"
print(chr1 in str1)
print(chr2 in str1)

# is
x = 5
y = 5
print(x is y)

