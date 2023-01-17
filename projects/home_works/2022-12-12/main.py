# print("Hello")
# a = abs(int(input("команда a: ")))
# b = abs(int(input("команда b: ")))
#
# print(a, b)


def max_mnozh(c, d):
    while d > 0:
        temp = c
        c = d
        d = temp % d
        # c, d = d, c % d
    return c


print(max_mnozh(12, 17))

a1 = 12
b1 = 17
print(a1, b1)  # 12 17
a1, b1 = b1, a1
print(a1, b1)  # 17 12

print(15 % 4)  # 7,5 - остаток от деления
print(3 % 2)  # 3-2 = 1
print(5 % 2)  # 5-2=3-2=1


def recur_factorial(n):
    if n < 1:
        raise Exception("число должно быть положительным!")
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


print(recur_factorial(2))
print(recur_factorial(3))
print(recur_factorial(4))
