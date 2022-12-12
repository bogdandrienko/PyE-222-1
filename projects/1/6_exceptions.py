# TODO исключения (try-except)

# операции: транзакции, арифметические (деление на ноль), работа с папками (которых не существует) ...
# print(1/0)  # division by zero
# print("" * "")
# умножение строки на строку
# чтение файла или папки, которых нет
# dict1 = {"name": "Bogdan"}
# print(dict1["name1"])
# KeyError - ключа нет в словаре

print("12")
print(1 / 0)  # падение потока (кода)
print("13")

try:
    print("опасные операции 1")
    print(1 / 0)
    print("опасные операции 2")
except ZeroDivisionError as error:  # ошибка деления на 0
    print(error)
except Exception as error:
    print("неизвестная ошибка в операциях")
    print(error)

# все виды: https://www.tutorialspoint.com/object_oriented_python/images/custom_exception_class.jpg

try:
    print("Сняли деньги с моего счёта")
    print("опасные операции 1")
    print(1 / 0)
    print("опасные операции 2")
    print("Перевели деньги на счёт друга")
except Exception as error:
    print("Перевели деньги назад на мой счёт")
    print(error)
else:
    print("Перевод денег успешно завершён!")
finally:
    print("Уведомление пользователя о статусе перевода (успешный / не успешный)")

try:
    # вызов исключения
    def div2(a, b):
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        if result <= 0:
            raise ArithmeticError
        return result
except Exception as error:
    print(error)


########################################################################################################################
# TODO собственный класс исключений (try-except)

class MyException(Exception):
    def __init__(self, message: str):
        self.message = message

    def get_error_message(self) -> str:
        return f"состояние: {self.message}"

    def __str__(self) -> str:
        return self.get_error_message()


try:
    print("открытие соединения с базой")

    print("опасные операции 1")
    print(1 / 0)
    print("опасные операции 2")
except MyException as error:
    print(f"Наш код упал! {error.get_error_message()}")
except Exception as error:
    print(f"неизвестная ошибка в операциях!")
    print(error)
else:
    print("ошибки не было!")
finally:
    print("Закрытие соединения с базой")

############################################


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
