########################################################################################################################
# TODO поиск

import base64
import chardet

#        0  1  2     3         4               5                   6
list1 = [1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5]
tuple1 = (1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5)
str1 = "Banana"

print("value: ", list1[2])
print("index: ", list1.index(5))

search1 = list1.index(5)  # поиск индекса в массиве по элементу
print(search1, " : ", list1[search1])
search2 = str1.index('a')
print(search2, " : ", str1[search2])

search3 = list1.index(5, 3, 7)  # поиск индекса в массиве по элементу, с указанием откуда и до куда искать
print(search3, " : ", list1[search3])

text1 = 'Идейные соображения высшего порядка, а также сложившаяся структура организации представляет собой интересный' \
        ' эксперимент проверки форм развития. '
substring = 'структура'
find1 = text1.find(substring)
print(find1)
print(text1[find1:find1 + len(substring):1])

list2 = [1, 2, 5, 10, 4, 2]
list2_1 = [1, 2, 5, 10, 4, 2]
list2.sort()
print(list2)
print(sorted(list2_1))

list5 = [1, 2, 5, 10, 4, 2]
print(list5)
list5.sort(reverse=True)
print(list5)

#       01
str1 = "Award"
print(str1.index("w"))
print("".join(sorted(str1)))

char1 = ord("A")  # получаем индекс(число) строчного элемента
print(char1)
print(type(char1))
print(ord("a"))

number1 = chr(35)  # получаем элемент(символ) из индекса
print(number1)
print(type(number1))
print(chr(98))
print(ord("1"))

########################################################################################################################

########################################################################################################################
# TODO кодировки

# utf-8 win-1251 win-1252 ascii

str1 = b'123BNO'
print(str1)

rList = [1, 2, 3, 4, 12]
arr = bytes(rList)
print(arr)

print(base64.b64encode("Admin Admin".encode()))  # b'QWRtaW4gQWRtaW4='
print(base64.b64encode("Admin".encode()))  # b'QWRtaW4gQWRtaW4='

source = "Р—Р°РєР°Р· Р·РІРѕРЅРєР° С‚РµС…РЅРёС‡РµСЃРєРѕР№ РїРѕРґРґРµСЂР¶РєРё"
print(f"source: {source}")

encode = chardet.detect(source.encode(encoding="cp1251"))['encoding']
print(encode)
source2 = source.encode(encoding="cp1251")
source3 = source2.decode(encoding="utf-8")
print(source3)

########################################################################################################################

########################################################################################################################
# TODO хэширование - одностороннее (нельзя вытащить назад)

import hashlib
import uuid

# hash_object = hashlib.md5("12345".encode())  # danger ! too simple
hash_object = hashlib.sha256("key1".encode('utf-8'))
print(hash_object)
print(hash_object.digest())
print(hash_object.hexdigest())

# if hashlib.sha256(input("введите пароль").encode(
#         'utf-8')).hexdigest() == "8174099687a26621f4e2cdd7cc03b3dacedb3fb962255b1aafd033cabe831530":
#     print("пароли совпали")

########################################################################################################################

########################################################################################################################
# TODO хэширование - одностороннее (нельзя вытащить назад)

alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(2)
message = "Dias12345!".upper()
itog = ''
lang = "Eng"
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
print(itog)


def encypt_func(txt, s):
    result = ""
    # transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt
        if char.isupper():
            result += chr((ord(char) + s - 64) % 26 + 65)
            # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result


# check the above function
txt = "Python is awesome"
s = 4

print("Plain txt : " + txt)
print("Shift pattern : " + str(s))
print("Cipher: " + encypt_func(txt, s))

# https://pythonpip.ru/examples/shifr-tsezarya-python
########################################################################################################################
