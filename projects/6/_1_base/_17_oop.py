########################################################################################################################
# TODO ООП
import asyncio
import datetime


# Объектно-ориентированное программирование: способ представления взаимодействий сущностей как в реальной жизни

# Процедурное программирование Паскаль
# Функциональное программирование F#
# Объектно-ориентированное программирование  C#, Делфи, Python, С++

#                     объект - видимость, рендеринг, коллизии (физики)
#                     техника - скорость, масса, может с ними взаимодействовать
#         сухопутные водоплавающие - точки, где можно перемещаться
#  Велосипед Машина Мотоцикл гидро скутер Лодка - текстуры, цвет

# TODO простой пример
class Mother1:  # (object)
    eyes = "blue"  # Атрибут класса - только самые частые свойства
    Pi = 3.14
    e = 3.0


class Child1(Mother1):
    height = 1.8  # Атрибут класса


print(Mother1.eyes)
m1 = Mother1()
print(m1.eyes)

ch1 = Child1()
print(ch1.eyes)
print(ch1.height)


# TODO пример сложнее
class MyClass:
    name = "Abulkhair"

    def __init__(self, name, age):  # initializate
        self.name = name  # Атрибут экземпляра класса
        self.age = age  # Атрибут экземпляра класса

    def say_hello(self):  # метод (функция внутри класса)
        print("hello!")


print(MyClass.name)
my1 = MyClass(name="Bogdan", age=25)  # initializate
my1.say_hello()
print(my1.name)
print(my1.age)


class MyClass2:
    def __init__(self, a, b, name='квадрат'):
        self.name = name
        self.a = a
        self.b = b

    def get_perimeter(self):  # метод внутри класса, который работает с внутренними параметрами
        return (self.a + self.b) + (self.a + self.b)

    @staticmethod
    def get_perimeter_static(a, b):  # метод внутри класса, который не работает с внутренними атрибутами
        return (a + b) + (a + b)

    def get_square(self):  # метод внутри класса, который работает с внутренними параметрами
        return self.a * self.b

    @staticmethod
    def get_square_static(a, b):  # метод внутри класса, который работает с внутренними параметрами
        return a * b


print(MyClass2)
myclass = MyClass2(name="Прямоугольник", b=15, a=16)  # создание экземпляра класса
print(myclass)
print(myclass.get_perimeter())

print(MyClass2.get_perimeter_static(15, 17))


# TODO ещё пример
class Calc:
    def __init__(self, value1: float, value2: float):
        self.value1 = value1
        self.value2 = value2

        self.sum_val = value1 + value2  # логика "на лету" - тяжёлая или может не понадобиться
        # self.dif = value1 - value2          # логика "на лету" - тяжёлая или может не понадобиться
        # self.multiply = value1 * value2     # логика "на лету" - тяжёлая или может не понадобиться

    def sum(self):
        return self.value1 + self.value2

    def dif(self):
        return self.value1 - self.value2

    def multiply(self):
        return self.value1 * self.value2

    @staticmethod
    def static_mul(value1, value2):
        return value1 * value2


c1 = Calc(1, 3)
print(c1.sum_val)
print(c1.sum())
print(c1.dif())
print(c1.multiply())
print(c1.static_mul(2, 3))
print(Calc.static_mul(2, 3))

print("\n\n\n\n *************  \n\n\n\n")


# TODO ещё пример
class Obj:
    is_start_rendering1 = True
    visible = False  # публичное свойство атрибута класса
    _visible = False  # защищённое свойство атрибута класса
    __visible = False  # приватное свойство атрибута класса

    def __init__(self, mass, is_start_rendering=True):  # магический метод(функция)
        self.mass = mass
        self.is_start_rendering1 = True
        self.is_start_rendering = is_start_rendering
        self.mass2 = 12
        self.__mass3 = 12

    def get_mass(self):
        return self.mass

    def get_visibility(self) -> bool:  # метод
        """
        Return state of is visibile obj
        :return: bool
        """
        return self._visible

    def set_visibility(self, is_checked: bool) -> None:
        self._visible = is_checked

    def switch_visibility(self) -> None:  # метод
        """
        Этот метод должен переключать видимость
        :return: None
        """
        self._visible = not self._visible


obj1 = Obj(150)
print(obj1.visible)
obj1.visible = True
print(obj1.visible)

print(obj1._visible)
obj1._visible = True
print(obj1._visible)

# print(obj1.__visible)
# obj1.__visible = True
# print(obj1.__visible)

print(obj1._Obj__visible)
obj1._Obj__visible = True
print(obj1._Obj__visible)

print("\n\n\n\n *************  \n\n\n\n")


class Vehicle(Obj):
    def __init__(self, speed: float, mass):
        super().__init__(mass)  # это метод, который позволяет получить доступ к родителю
        self.speed = speed
        # self.mass = mass * 2  # Child  -> Mother -> Grandmother 1

    def get_parent_mass(self):
        return super().get_mass()


vh1 = Vehicle(80, 150)
print(vh1.mass)
print(vh1.get_mass())


# TODO ещё пример
class Parall:
    def __init__(self, side1: int, side2: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side1 / 3 * side2

    def check_is_square(self) -> bool:
        # if self.side1 == self.side2:
        #     return True
        # else:
        #     return False
        return self.side1 == self.side2

    def get_perimeter(self) -> int:
        if self.check_is_square():
            return self.side1 * 4  # квадрат
        else:
            return (self.side1 + self.side2) * 2  # многоугольник

    def get_square(self) -> int:
        if self.check_is_square():
            return self.side1 ** 2  # квадрат
        else:
            return self.side1 * self.side2  # многоугольник

    def add(self, other) -> int:  # '+'
        return self.get_square() + other.get_square()

    def __add__(self, other) -> int:  # '+'
        return self.get_square() + other.get_square()

    def __eq__(self, other):  # equal - '=='
        pass

    def __abs__(self):  # 'abs()'
        print("Privet")
        return "Dina"

    def __gt__(self, other):  # greather than - '>'
        pass


parall1 = Parall(side1=2, side2=3)
parall2 = Parall(side1=3, side2=4)
print(parall1 + parall2)  #
print(parall2.add(parall1))
print(abs(parall1))


# TODO ещё пример
#                 Транспортные средства
#            Сухопутные               Морские
#    машины       мотоциклы    подводные    наводные
# электро

class Transport(object):
    def __init__(self, name, mass, motor, price, speed):
        self.name = name
        self._mass = mass
        self.motor = motor
        self.price = price
        self.speed = speed  # публичная - видна во всех случаях

        self._multiplayer = 12  # защищённая - предупреждает, при попытке её извлечь вне собственного контекста
        self.__multiplayer = 10  # приватная - невидима везде, кроме собственного контекста

    def drive(self):
        return self._mass / self.motor

    def get_speed(self):
        return self.speed


Transport1 = Transport("Трактор", 2000, 400, 5000, 30)

print(Transport1)
print(type(Transport1))
print(Transport1.drive())
print(Transport1.speed)
print(Transport1._mass)
print(Transport1._multiplayer)


class Water(Transport):
    def __init__(self, speed, *args):
        super().__init__(*args)

        self.speed1 = speed

    def drive(self):
        return super().drive() / 0.85

    def get_old_speed(self):
        return super().get_speed()


Transport2 = Water(1000, "Катамаран", 500, 20, 700, 15)

print(Transport2)
print(type(Transport2))
print(Transport2.drive())
print(Transport2.speed)
print(Transport2.speed1)


class SubWater(Water):
    def __init__(self, *args, **kwargs):  # args - позиционные - кортеж, kwargs - именные - словарь
        super().__init__(*args, **kwargs)

    def drive(self):
        return super().drive() * 1.5


Transport3 = SubWater(333333, "Подлодка", 333, 33, 3333, 3)

dict1 = {"speed": 12}
val1 = dict1.get("speed", "")
val2 = dict1["speed"]

print(Transport3)
print(type(Transport3))
print(Transport3.drive())
print(Transport3.speed)
print(Transport3._mass)
print(Transport3.speed1)
print(Transport3.get_speed())


# TODO ещё пример
class MyCalculator:
    def __init__(self, val1: float, val2: float):

        # self.val1 = val1
        # while not isinstance(val1, float):
        #     self.val1 = input('Введите первое значение ещё раз: ')

        try:
            self.val1 = float(val1)
        except Exception as error:
            self.val1 = input('Введите первое значение ещё раз: ')
        self.val2 = val2

    def summ2(self):
        try:
            return float(self.val1) + float(self.val2)
        except Exception as error:
            print(error)
            return 0.0

    def multiply(self):
        return float(self.val1) * float(self.val2)

    @staticmethod
    def multiply_static(val1, val2):
        return float(val1) * float(val2)

    @staticmethod  # декоратор, который делает метод в классе статическим(без параметра селф и инициализации)
    def summ(val1: float, val2: float):  # статический метод
        return val1 + val2


# инициализация калькулятора
summ1 = MyCalculator(12, 16)
print(summ1.summ2())
print(summ1.multiply())
print(MyCalculator.summ(15, 17))
print(MyCalculator.multiply_static(15, 17))


########################################################################################################################

########################################################################################################################
# TODO статические методы

class HelpPython:
    class Time:
        @staticmethod
        def get_current_time(timezone: int, formatting="23:59:59"):
            dat = datetime.datetime.now()

            match formatting:
                case "23:59:59":
                    return dat.strftime('%H:%M:%S')
                case "23:59:59.999":
                    return dat.strftime('%H:%M:%S ...')
                case "23:59":
                    return dat.strftime('%H:%M')
                case _:
                    return dat

        @staticmethod
        def get_different_times_in_seconds(datetime1: datetime.datetime, datetime2: datetime.datetime) -> int:
            # datetime1 - datetime2
            return 0

    class Async:
        @staticmethod
        async def example_async_download_image():
            await asyncio.sleep(1.0)
            print("hello!")

        @staticmethod
        def example1():
            asyncio.run(HelpPython.Async.example_async_download_image())

    class Variable:
        @staticmethod
        def convert_to_string1(value) -> str:
            return f"{value}"

        @staticmethod
        def convert_to_string2(value) -> str:
            return str(value)


# HelpPython.Async.example1()


########################################################################################################################

########################################################################################################################
# TODO множественное наследование


class Mother2:
    val1 = 12
    # eyes = "brown"

    def __init__(self, val1, name="Мама") -> None:
        self.name = name
        self.val = val1
        self._val = val1  # защищённый
        self.__val2 = val1 + 5  # приватный

    def get_value2(self):
        return 10

    def __str__(self):
        return self.name


class Father2:
    val2 = 13
    eyes = "blue"

    def __init__(self, val1) -> None:
        self.val1 = val1

    def get_value(self):
        return 8

    def __str__(self):
        return self.val1


class Child2(Mother2, Father2):

    def __init__(self, val1) -> None:
        super().__init__(val1)

    def get_value1(self):
        return 5


ch2 = Child2(12)
print(ch2.eyes)

########################################################################################################################

########################################################################################################################
# TODO classmethod and staticmethod

from datetime import date


class Person:
    def __init__(self, name: str, age: int | float):
        self.name = name
        self.age = age

    # @classmethod
    # def __new__(cls, *args):
    #     return cls(*args)

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age: int | float) -> bool:
        return age > 18


person1 = Person('Maya', 21)
person2 = Person.from_birth_year('Maya', 1996)

print(person1.age)
print(person2.age)

print(Person.is_adult(22))

########################################################################################################################
