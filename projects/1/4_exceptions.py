# исключение

try:  # попытка (что-то сделать)
    print("Деньги снялись с моего счёта")

    # print(1/0)  # division by zero
    # print("" * "")
    # умножение строки на строку
    # чтение файла или папки, которых нет
    # dict1 = {"name": "Bogdan"}
    # print(dict1["name1"])
    # KeyError - ключа нет в словаре

    print("Деньги пополнили счёт друга")
except Exception as error:
    print(error)
    print("Деньги вернулись на мой счёт")
finally:
    pass


try:
    # попытка (что-то сделать)
    pass
except ZeroDivisionError as error:  # ошибка деления на 0
    print(error)
    # совпадение исключения
    pass
except KeyError as error:  # ошибка словаря
    print(error)
    # совпадение исключения
    pass
except Exception as error:
    print(error)
    # совпадение исключения
    pass

try:
    # попытка (что-то сделать)
    pass
except Exception as error:
    print(error)
    # совпадение исключения
    pass

file = open("new.txt", "r")  # прочитал в оперативную память - утечка памяти
try:
    data = file.read()
    1 / 0
    # попытка (что-то сделать)
    
    pass
except Exception as error:
    print(error)
    # совпадение исключения
    pass
else:  # редко
    # если try отработал успешно
    pass
finally:
    file.close()  # высвобождение оперативной памяти
    # сделать в любом случае (и при ошибке, и при успешном выполнении)
    pass


