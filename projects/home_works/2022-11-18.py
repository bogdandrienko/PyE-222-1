# values = input("Введите три числа через запятую: ")
values = "5, 5, 5"
print(values, type(values))

values1 = values.split(sep=", ")
print(values1, type(values1))

# ['1', '2', '3']
summary = 1
for i in values1:
    int_value = int(i)
    summary = summary * int_value
    print(int_value, type(int_value))
print(summary)

print("#####################################")

# val1 = int(input("Введите зарплата за месяц  "))
# val2 = int(input("Введите сумма месячного платежа по кредиту в банке  "))
# val3 = int(input("Введите задолженность за коммунальные услуги  "))

# result = val1 - val2 - val3
# print(result)  # 55000

print("#####################################")

# side1 = int(input("Введите первую сторону  "))
# side2 = int(input("Введите вторую сторону  "))
#
# P = (side1 + side2) * 2
# S = side1 * side2
# print(P)  # 50
# print(S)  # 150

print("#####################################")

print("“Life is what happens\nwhen\nyou’re busy making other plans”\nJohn Lennon.")

str1 = """
“Life is what happens
        when
                you’re busy making other plans”
                                                                John Lennon.
"""
print(str1)

print("#####################################")
Pi = 3.14

R = 5

L = 2 * Pi * R
# L = round(2 * Pi * R, 1)
print(L)  # 75.36

S = round(Pi * (R ** 2), 1)
print(S)  # 452.16

import decimal


print(3.14 * 5 * 2)
print(round(decimal.Decimal(3.14 * 5 * 2), 2))
