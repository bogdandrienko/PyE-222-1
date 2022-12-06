# todo объявление функции
def print_hello():
    print("Hello world11111!")
# todo объявление функции

# todo вызов функции
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# todo вызов функции

# DRY - don't repeat yourself
# action > 2 (>=2)

input_from_user = 12  # замодокументируемый код


def multiply_two_values(val1, val2):  # замодокументируемый код
    # эта функция умножает два значения
    result = val1 / val2
    print(result)


# multiply_two_values(10, 20)  # позиционные аргументы
# multiply_two_values(val2=20, val1=10)  # именные аргументы


def multiply_two_values_clear(val1, val2):
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 / val2
    return result  # clear function


res = multiply_two_values_clear(val2=20, val1=10)


# print(res)

def multiply_two_values_default(val1=10, val2=10):
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 / val2
    return result  # default function


res2 = multiply_two_values_default()
print(res2)


# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++ - статическая типизация (- скорость разработки + скорость работы - к багам)

def multiply_two_values_typing(val1: float, val2=12) -> float:
    # расчёты не влияющие на контекст (файлы, оперативная внешняя память, удаление)
    result = val1 * val2
    # return "result"  # typing function
    return result  # typing function


res2 = multiply_two_values_typing(val1=12, val2=15) / 10
print(res2)
print("Продолжение")


def multiply(a: float, b: float) -> float:
    return a * b


def calculate(a: float, b: float, action="+") -> float:
    match action:
        case "+":
            return a + b
        case "-":
            return a - b
        case _:
            print("Вы ввели некорректное действие")
            return None
    return None


val1 = float(input("Введи первое число: "))  # int == float | float != int
val2 = float(input("Введи второе число: "))
action = input("Введи действие (+ - * / ** ^): ")
res3 = calculate(val1, val2, action)
print(res3)
