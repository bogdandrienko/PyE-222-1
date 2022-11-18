# for - по итераторам
# for i in range(20, 10, -1):
#     print(i)
# for i in range(2, 10+1, 2):
#     print(i)
# arr = range(1, 10+1)
# print(arr, type(arr))  # range(1, 11) <class 'range'>
# for i in range(1, 10+1):  # [1, 2, 3, ... 10]
#     print(i)
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:  # [1, 2, 3, ... 10]
#     print(i)
# while - c постусловием / с предусловием
# do while

# index = 0
# for i in range(1, 1000+1):
#     for j in range(1, 1000+1):
#         for x in range(1, 10+1):
#             index += 1
# print(index)

# while (условие):
#     действие

# 1
# index = 1
# while index <= 10:
#     print(index)
#     index = index + 1
#
index = 1
while True:
    if index > 10:
        break  # тормоз

    index = index + 1
    if index % 2 == 0:  # только чётные
        continue  # сбрасывает цикл на начало следующей итерации
    else:
        print(index)

    print("не было сброса")