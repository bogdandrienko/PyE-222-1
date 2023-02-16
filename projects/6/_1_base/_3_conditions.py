########################################################################################################################
# TODO условный оператор if-else

bool_condition1 = False

if bool_condition1:
    print("Правда 1")
# else:
#     pass

if bool_condition1:
    print("Правда 2")
else:
    print("Ложь 2")

value = 40

if value > 100:
    print("Правда 3 1")
else:
    if value > 50:
        print("Правда 3 2")
    else:
        if value > 30:
            print("Правда 3 3")
        else:
            if value > 20:
                print("Правда 3 4")
            else:
                print("Ложь 3 1")

if value > 100:
    print("Правда 3 1")
elif value > 50:
    print("Правда 3 2")
elif value > 30:
    print("Правда 3 3")
elif value > 20:
    print("Правда 3 4")
else:
    print("Ложь 3 1")

fruit = "абрикос"
if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")
elif fruit == "банан":
    print("Всё в норме")
else:
    print("Неизвестный фрукт")

# таблица истинности
# https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D0%B8%D1%81%D1%82%D0%B8%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8
cond1 = 12 > 5
cond2 = 12 == 12
cond3 = 12 < 7

# and - оба значения должны быть True, только тогда True
# or - одно из значений должно быть True, тогда True

#       True
if (cond1 and cond2) or cond3:
    print("Правда 4")
else:
    print("Ложь 4")

########################################################################################################################
# TODO условный оператор match-case (+ python 3.10)

light = "Жёлтый"

# match (exp)
# случай "Красный":
# случай "Красный":
# случай _:

match light:
    case "Красный":
        print("Стоять")
    case "Жёлтый":
        print("Готовьтесь")
    case "Зелёный":
        print("Можно идти")
    case _:
        print("Светофор сломался")

fruit = "абрикос"
match fruit:
    case "абрикос":
        print("У Вас аллергия, будьте осторожны")
    case "банан":
        print("Всё в норме")
    case _:
        print("Неизвестный фрукт")

########################################################################################################################
# TODO тернарный оператор

a = 10
b = 20

# res = True if cond() else False
res = "Правда" if a < b else "Ложь"

res1 = ""
if (a < b) and 17 > 15:
    res1 = "Меньше"
else:
    res1 = "Больше"

res2 = "Меньше" if (a < b) and 17 > 15 else "Больше"


# вызов функций
def print1():
    print("print1")


def print2():
    print("print2")


res3 = print1() if a < b else print2()
