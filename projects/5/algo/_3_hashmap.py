import zlib

# https://ru.hexlet.io/courses/python-dicts/lessons/hash-table/theory_unit
# ассоциативный_массив[индекс, ключ(хэшированный), значение]
#        54
dict1 = {"name": "Python"}
# print(dict1["name1"])  # KeyError: 'name1'
print(dict1.get("name", "Dias"))
print(dict1.get("name1", "Dias"))
dict1["age"] = 12
dict1["name1"] = "Айгерим"
dict1[12] = "Айгерим"
dict1[(12,)] = "Айгерим"
print(dict1)

# словарь - ассоциативный массив
# поиск, вставка, удаление занимает O(1)

key_for_dictionary = "Python"
__hash = zlib.crc32(key_for_dictionary.encode(encoding="utf-8"))
print(__hash)  # 2 742 599 054
print(zlib.crc32("Python".encode(encoding="utf-8")))

print(abs(zlib.crc32("Python".encode(encoding="utf-8"))) % 1000)
# 1 свойство - хэш функция "всегда" генерирует одинаковые значения на выходе для одинаковых значений на входе
# 2 свойство - хэш функция "всегда" генерирует ответ одной длины

dict3 = []


def setter(key_for_dictionary2, value):  # dict1["name1"] = "Айгерим"
    # Любые данные, которые мы хотим хэшировать, представляются в виде байтовой строки
    __hash2 = zlib.crc32(key_for_dictionary2.encode(encoding="utf-8"))
    # Это делается для того, чтобы индексы не были слишком большими. От этого зависит потребление памяти.
    __index2 = abs(__hash2) % 1000
    dict3[__index2] = (__hash2, value)


def getter(key_for_dictionary1):  # print(dict1["name1"])
    __hash1 = zlib.crc32(key_for_dictionary1.encode(encoding="utf-8"))
    __index1 = abs(__hash1) % 1000
    return dict3[__index1]

# Ключом в ассоциативном массиве может быть абсолютно любая строка. Но здесь есть одно противоречие:
# Все возможные ключи — это бесконечное множество
# В качестве результата хеш-функция выдает строку фиксированной длины, то есть это конечное множество
# Такую ситуацию принято называть коллизией. Простейший способ разрешения коллизий — это открытая адресация.
# Она предполагает последовательное перемещение по слотам хеш-таблицы в поисках первого свободного слота, куда
# значение будет записано.
