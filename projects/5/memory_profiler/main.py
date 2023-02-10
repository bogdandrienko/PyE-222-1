import random
import sys
import time


# import memory_profiler
# pip install matplotlib memory_profiler

# 0 - диспетчер задач
# 1 - memory_profiler
# 2 - profiling by pycharm
# 3 - matplotlib

# mprof run --include-children python main.py
# mprof plot --output memory-profile_bad.png

# @memory_profiler.profile
def start():
    car_names = ["Audi", "Mers", "BMW", "Nissan", "Toyota"]
    car_colors = ["Black", "White", "Red", "Yellow"]
    car_count = 10000000

    # 10 000 000

    def start_bad():
        cars = []
        for i in range(1, car_count + 1):
            car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            cars.append(car)
        return cars

    def start_good():
        for i in range(1, car_count + 1):
            car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            yield car

    # todo full list
    # cars1 = start_bad()  # 15.977  #  89 095 160

    # todo generator
    cars1 = start_good()  # 14.964  # 104
    print(sys.getsizeof(cars1))  #

    # for i in cars1:
    #     print(i["name"])
    # todo WORK
    with open("log.txt", "a") as file:
        for i in cars1:
            file.write(i["name"] + "\n")


if __name__ == "__main__":
    t_start = time.perf_counter()

    # start()

    print("Elapsed time: ", round(time.perf_counter() - t_start, 3))

    # a = 12  # dynamic typing
    # a = "12"
    # a: int = 12  # static typing
    # b = a
    # del b

    # компиляция(native - binary file) или интерпретация - C++, Rust, C, Assembler, C#, Go | Python, JavaScript, Php
    # статическая (быстрее) или динамическая типизация - C++, Rust, C, Assembler, C#, Go, TypeScript | Python, JavaScript, Php
    # наличие или отсутствие(быстрее) сборщика мусора - C++, Rust, C, Assembler | C#, Go, TypeScript Python, JavaScript, Php

    # a = 12  # 28 bytes
    # b = 12.756785  # 24
    # c = "Python"  # 55
    # c1 = "Python is awesome"  # 66
    # d = {"name": "Python"}  # 232 * 1000 * 1000
    # e = True  # 28
    # list1 = [1, 2, 3]  # 88 * 100000
    # tuple1 = (1, 2, 3)  # 64 * 100000
    #
    # print(sys.getsizeof(tuple1))

    list1 = []
    for i in range(1, 1000 + 1):
        if i % 2 != 0:
            list1.append(i)
    print(list1)

    # list comprehension(expression)
    list2 = [i for i in range(1, 1000 + 1) if i % 2 != 0]
    list3 = [i ** 2 for i in range(1, 1000 + 1) if i % 2 != 0]
    list4 = [{"id": i, "name": f"name {i}"} for i in range(1, 1000 + 1) if i % 2 != 0]

    # for i in list2:
    #     print(i)
    print(list2)
    print(list3)

    # generator comprehension
    gen1 = (i for i in range(1, 1000 + 1) if i % 2 != 0)
    print(gen1)


    # for i in gen1:
    #     print(i)

    def file_read_write():
        # file = None
        # try:
        #     file = open("log.txt", "a")  # r w rb wb a
        #     file.write("Python is awesome!")
        # except Exception as error:
        #     pass
        # finally:
        #     file.close()  # утечка памяти

        with open("log.txt", "a") as file:  # менеджер контекста - закрывает файл в любом случае
            file.write("Python is awesome!")
