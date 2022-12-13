# TODO регулярные выражения

import re
import hashlib

txt = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
txt2 = r"^  (?=.*[A-Za-z])    (?=.*\d)    (?=.*[@$!%*#?&])     [A-Za-z\d@$!%*#?&]    {12,16}      $"

input_from_user1 = "qwerty"
input_from_user1.isascii()  # пароль должен быть на английском
input_from_user1.islower()  # только маленькие ли?
input_from_user1.isdigit()  # только цифры?
input_from_user1.isalpha()

# Минимум восемь символов, минимум одна заглавная буква, одна строчная буква и одна цифра, и спец символ:

# Хотя бы одна заглавная английская буква (?=.*?[A-Z])
# Хотя бы одна строчная английская буква (?=.*?[a-z])
# Хотя бы одну цифру (?=.*?[0-9]) \d+
# По крайней мере, один специальный символ,(?=.*?[?!@%^&*-])
# Минимум восемь в длину .{12,16}(с анкерами)

# password check
password1 = "111111111"
password2 = "123456789Qwerty!"

cond1 = re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password2)
print(cond1, type(cond1))

if cond1:
    print("True 1")
else:
    print("False 1")

# email check
email1 = "admin.com"
email2 = "admin@gmail.com"

#               admin        @   gmail       .   edu
if re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", string=email2):
    print("True 2")
else:
    print("False 2")


def check(email: str) -> bool:
    res = re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$', email)
    print(res, type(res))
    if res:
        print("Почта верная")
        return True
    else:
        print("Почта не верная, повторите")
        return False


check('bogdanrienko@gmail.com')

while True:
    a1 = input("Введите новый пароль:  ")  # python
    if not re.search(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$", a1):
        print("\n\nОшибка ввода, повторите ввод!\n")
        continue
    b1 = input("Введите новый пароль ещё раз:  ")  # python
    if a1 != b1:
        print("\n\nОшибка ввода, повторите ввод!\n")
        continue
    print("Пароль успешно применён")
    break

# phone check
#                         8-777-635-76-86
phoneRegex1 = re.compile(r"\d-\d\d\d-\d\d\d-\d\d-\d\d")

#                         777-635-76-86
phoneRegex2 = re.compile(r"\d\d\d-\d\d\d-\d\d-\d\d")
# (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})
