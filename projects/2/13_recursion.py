def while_factorial(stop_value: int):
    counter = 1
    while stop_value > 0:
        # counter = counter * stop_value
        counter *= stop_value
        print(counter)
        # stop_value = stop_value - 1
        stop_value -= 1
    return counter


def factorial(stop_value: int):
    if stop_value <= 1:
        return 1
    else:
        res = stop_value * factorial(stop_value - 1)
        return res


def summator(stop_value: int) -> int:
    sum_value = 0
    for i in range(1, stop_value + 1, 1):
        sum_value += i
    return sum_value


# res1 = summator(4)
# print(res1)

# num = 5
# print("number : ", num)
# print("Factorial : ", factorial(num))
# res2 = factorial(2)
# print(res2)
# res3 = while_factorial(4)
# print(res3)


def multiply1(a, b):
    return a ** b


multiply2 = lambda a, b: a ** b

res4 = multiply1(6, 2)
res5 = multiply2(6, 2)
# print(res4)
# print(res5)

peoples = [
    {"name": "Bogdan1", "age": 24},  # dict
    {"name": "Bogdan1", "age": 22},  # dict
    {"name": "Bogdan3", "age": 20}
]

peoples2 = [
    [1, 1, 99, 4],  # tuple
    ("Python", 2, 6),  # list
    [99, 1, 3],  # list
]

# print((2,         6,"Python")[-1])

names = [
    # 65 109
    "Amina",
    # 66
    "Bogdan",
    # 65 108
    "Alema",

]

char_f = chr(50)  # 120: x | 50: 2


# print(char_f)
# ord_f1 = ord("A")
# ord_f2 = ord("B")
# print(ord_f1)
# print(ord_f2)
# print(ord("l"))
# print(ord("m"))
# # print(sorted(peoples2, reverse=False))
# print(sorted(names, reverse=False))


# print(sum([1, 2, 98]))


def for_sorted(x):
    x = sum(x)
    return x


# def sorted1(list1: list, key=None):
#     if key is None:
#         return list1.sort()
#     key()  # [1, 2, 3] 6
#     key()  # (1, 1, 99, 4) 105

# print(sorted(peoples, key=lambda x: x["age"], reverse=True))
# print(sorted(peoples2, key=lambda x: sum(x)))

def counter_while(value_from):
    while value_from > 0:
        print(value_from)
        value_from = value_from - 1


def counter_recursion(value_from):
    print(value_from)
    if value_from <= 1:
        return 1
    else:
        counter_recursion(value_from - 1)


# counter_recursion(12)


def non_anonimus_function(a, b, c):
    res = (a ** b) / c
    return res


anonimus_function = lambda a, b, c: (a ** b) / c
# print(anonimus_function(2, 4, 3))
# print(non_anonimus_function(2, 4, 3))

arrays = [
    [99, 1, 3],  # list         3: [99, 1,         3]
    ("Python", 2, 9),  # list         9: ("Python", 2,   9)
    [1, 1, 99, 666],  # tuple    666: [1, 1, 99,      666]
]


def get_last_element(arr: list | tuple):
    return arr[-1]


# for array in arrays:
#     last_element = get_last_element(arr=array)
#     print(last_element)

sorted_array = sorted(arrays, key=lambda arr: arr[-1])
print(sorted_array)
arrays.sort(key=get_last_element, reverse=True)
print(arrays)
