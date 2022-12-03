from decimal import Decimal

bool1 = True
bool2 = False

int1 = 12

float1 = 12.0
decimal1 = Decimal(12.0)

str1 = "Bogdan"
str2 = "B"

list1 = ["B", "o", "g"]
list2 = [12.0, 5, 0]
print(list2)  # [12.0, 5, True]
list2.append(666)
print(list2)  # [12.0, 5, True, '666']
reverse = False
list2.sort(reverse=reverse)
list2[0] = 1000
print(list2)  # [1000, 5, 12.0, 666]

tuple1 = ("admin", "admin")
# tuple2 = (12,)
print(tuple1)

# tuple1[0] = "Admin"

set1 = {12, 15, 12}
print(set1)  # {12, 15}
set1.add(16)
print(set1)  # {16, 12, 15}

list3 = [12.0, 5, True, '666', 5]
print(list3)  # [12.0, 5, True, '666', 5]
list3 = list(set(list3))
print(list3)  # [True, 12.0, 5, '666']

dict1 = {"key": "value", "name": 'Bogdan', "age": 25, "teacher": True,
         "subject": ["Python", "Django"],
         "param": {"key": "value", "name": 'Bogdan', "age": 25, "teacher": True,
                   "subject": ["Python", "Django"]}}


# print() - выводит на экран
# len() - считает длину элементов и возврает это число
# type() - возвращает тип данных в виде строки
# int() - превращает в int
# list() - превращает в list
# bool() - превращает в bool
# set() - превращает в set

class Man:

    def eat(self):
        pass

    def sleep(self):
        print("i go to sleep")


man1 = Man()

# man1.sleep()

bool1 = True
bool2 = False

if 12 > 10:
    print("Больше")

a = 12
b = 12

if a > b:
    print("Больше")
else:
    if a == b:
        print("Равны")
    else:
        print("Меньше")

if a > b:
    print("Больше")
elif a == b:
    print("Равны")
else:
    print("Меньше")

c = 12
if c == 20:
    print("20")
elif c == 25:
    print("25")
elif c == 30:
    print("25")
elif c == 25:
    print("25")
elif c == 25:
    print("25")
else:
    print("Не совпадений")


def sleep():
    print("i go to sleep")


def double_dirty(val):
    print(val * 2)


def double_clean(val=25):
    return val * 2


# double_dirty(12)
print(double_clean())

# age = float(input("Введите свой возвраст: "))
age = 24
is_full_age = age >= 18

health = "Здоровый"

exam = True

teacher = False

if (is_full_age and health == "Здоровый" and exam) or teacher:
    print("дать права")
else:
    print("не дать права")

sobes1 = False
sobes2 = True

if sobes1 or not sobes2:
    print("у меня есть работа")
else:
    print("у меня нет работы")
