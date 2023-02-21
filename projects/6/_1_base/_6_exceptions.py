########################################################################################################################
# TODO исключения (try-except) | try-catch

# операции: транзакции, арифметические (деление на ноль), работа с папками (которых не существует) ...
# print(1/0)  # division by zero
# print("" * "")
# умножение строки на строку
# чтение файла или папки, которых нет
# dict1 = {"name": "Bogdan"}
# print(dict1["name1"])
# KeyError - ключа нет в словаре

# print("12")
# print(1 / 0)  # падение (runtime error) потока (кода)
# # Process finished with exit code 1
# print("13")


# try:
#     print("опасные операции 1")
#     dict1 = {"name": "Bogdan"}
#     print(dict1["name1"])
#     # print(1 / 0)
#     print("опасные операции 2")
# except ZeroDivisionError as error:
#     print("Ошибка при делении на нуль, НЕ надо так!")
# except KeyError as error:
#     print("Имени нет!")
# except Exception as error:
#     print("неизвестная ошибка в операциях")


# все виды: https://www.tutorialspoint.com/object_oriented_python/images/custom_exception_class.jpg

try:
    print("Сняли деньги с моего счёта")
    print("попытка определить счёт получателя", 1 / 0)  # synthetic
    print("Перевели деньги на счёт друга")
except Exception as error:
    print("неизвестная ошибка в операциях")
    print("Перевели деньги назад на мой счёт")
else:
    print("Перевод денег успешно завершён!")
finally:
    print("Уведомление пользователя о статусе перевода (успешный / не успешный)")

# вызов исключения
try:
    def div2(a, b):
        if b == 0:
            raise ZeroDivisionError  # вызов исключения
        result = a / b
        if result <= 0:
            raise ArithmeticError  # вызов исключения
        return result
except Exception as error:
    print(error)

a = "Bogdan"
if a != "Bogdan":
    raise Exception("Вы не админ!")
else:
    print("Добро пожаловать")

print('\n\n\n\n\n********\n\n\n')


########################################################################################################################

########################################################################################################################
# TODO собственный класс исключений (try-except)

class MyException(Exception):
    def __init__(self, message="error"):
        self.message = message


try:
    print("открытие соединения с базой")

    print("опасные операции 1")
    raise MyException("Сеть не работает")
    print(1 / 0)
    print("опасные операции 2")
except MyException as error:
    print(f"Наш код упал! {error}")
except Exception as error:
    print(f"неизвестная ошибка в операциях!")
    print(f"не наша ошибка: {error}")
else:
    print("ошибки не было!")
finally:
    print("Закрытие соединения с базой")

########################################################################################################################
