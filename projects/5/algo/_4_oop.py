print(type(1))  # <class 'int'> / object
print(type("1"))  # <class 'str'> / object


def summing():
    pass


print(type(summing))  # <class 'function'> / object


# OOP
# Наследование - брать свойства от родителя/ей
#

# объявление класса
class Mother(object):
    color_eyes = "brown"  # атрибут класса (есть всегда)
    age = 30

    def __init__(self, name: str, age: int | float):  # инициализатор - магический метод
        self.name = name  # атрибут экземпляра класса (на лету)
        self.age = age

    # def __new__(cls, *args, **kwargs):  # конструктор

    def get_your_name(self):  # метод - функция, но внутри класса
        return self.name


mt1 = Mother()
print(Mother.color_eyes)
print(Mother.name)


class Father(object):
    color_eyes = "red"  # атрибут класса
    age = 30


class Child(Mother, Father):  # множественное наследование
    age = 10

    def __init__(self, name, age):  # инициализатор - магический метод
        super().__init__(name, age)


mother1 = Mother("Эрика", 31)  # создание экземпляра(инстанса) класса
print(mother1, type(mother1))  # <__main__.Mother object at 0x0000013794237670> <class '__main__.Mother'>
# print(mother1.color_eyes)  # brown
print(mother1.age)  # 30
print(mother1.get_your_name())

child1 = Child(1, 2)  # создание экземпляра(инстанса) класса
print(child1, type(child1))  # <__main__.Child object at 0x0000026C918E7010> <class '__main__.Child'>
print(child1.color_eyes)  # brown
print(child1.age)  # 10


# процедурный стиль (много багов, сложные взаимодействия)
# ООП стиль (взаимодействие сущностей)

# функциональный стиль(мало багов, долго разрабатывать)


class Workbook:
    pass


class Worksheet:
    pass


class Row:
    pass


class Column:
    pass


class Cell:
    pass
