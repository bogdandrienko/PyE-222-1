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

fruit = "абрикос1"

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

if (cond1 and cond2) or cond3:
    print("Правда 4")
else:
    print("Ложь 4")

########################################################################################################################
# TODO условный оператор match-case (+ python 3.10)

light = "Жёлтый"
match light:
    case "Красный":
        print("Стоять")
    case "Жёлтый":
        print("Готовьтесь")
    case "Зелёный":
        print("Можно идти")
    case _:
        print("Светофор сломался")

fruit = "абрикос1"
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
cond4 = a < b

res = "Правда" if cond4 else "Ложь"
res2 = a if a < b else b


def print1():
    print("print1")


def print2():
    print("print2")


res3 = print1() if cond4 else print2()
res3 = print1 if cond4 else print2
res3()

a, b = 10, 20
print((b, a)[a < b])

print({True: a, False: b}[a < b])
print((lambda: b, lambda: a)[a < b]())

############################


condition = False

if condition:
    print("Правда 1")
# else:
#     pass


if condition:
    print("Правда 2")
else:
    print("Ложь 2")

value = 40
######################
if value > 100:
    ###############
    print("Правда 3 1")
    ###############
elif value > 50:
    print("Правда 3 2")
elif value > 30:
    print("Правда 3 3")
elif value > 20:
    print("Правда 3 4")
else:
    print("Ложь 3 1")
######################
# exit

# 2/3
# 3.10

word = "banana"
val = 15

match "banana":
    case "fruit":
        print("11111111111")
    case "kivy":
        print("222222222222")
    case "banana":
        print("333333333333333")
    case _:
        print("default")

# + - * / ** ^
# val1 = 10
# val2 = 20
# action = "^"  # захардкоженные

val1 = float(input("Введи первое число: "))  # int == float | float != int
val2 = float(input("Введи второе число: "))
action = input("Введи действие (+ - * / ** ^): ")

# val1 = 10
# val2 = 20
# action = "^"  # захардкоженные
##########################################
if action == "+":
    print(val1 + val2)
elif action == "-":
    print(val1 - val2)

elif action == "*":
    print(val1 * val2)
elif action == "/":
    print(val1 / val2)

elif action == "**":
    print(val1 ** 2)
elif action == "^":
    print(val1 ** 0.5)
else:
    print("Вы ввели некорректное действие")

########################################
match action:
    case "+":
        print(val1 + val2)
    case "-":
        print(val1 - val2)
    case _:
        print("Вы ввели некорректное действие")
##################################
