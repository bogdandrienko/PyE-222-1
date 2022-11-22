# Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.
# Пользователь с клавиатуры вводит длину двух его диагоналей.

d1 = float(input('Введите первую диагональ: '))
d2 = float(input('Введите вторую диагональ: '))
# print(d1 * d2 * 0.5)
# d1_type = type(d1)  # <class 'str'>
# print(d1_type)
print(type(d1))


def squeare_for_romb(side1: float, side2: float) -> float:
    return side1 * side2 * 0.5  # side1 * side2 / 2


# result = squeare_for_romb(d1, d2)  # позиционные
result = squeare_for_romb(side1=d1, side2=d2)  # именованные
print(result)
# 0.5 * d1 * d2
