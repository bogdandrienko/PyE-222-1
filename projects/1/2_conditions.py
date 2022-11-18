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
