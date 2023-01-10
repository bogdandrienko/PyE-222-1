class Mother:  # (object)
    height = 180
    weight = 70

    def __init__(self):
        self.index = self.height // self.weight

    def hello(self):
        return "испански"


class Child(Mother):  # TODO наследование
    weight = 60  # TODO мутации
    counter_cl = 333  # TODO сокрытие: публичный
    _counter_cl = 333  # TODO сокрытие: защищённый
    __counter_cl = 333  # TODO сокрытие: приватный

    def __init__(self, counter_ex=333):
        super().__init__()

        self.counter_ex = counter_ex  # TODO сокрытие: публичный
        self._counter_ex = counter_ex  # TODO сокрытие: защищённый
        self.__counter_ex = 2023  # TODO сокрытие: приватный  # _Child__counter_ex !!!

    def __eq__(self, other):  # TODO магический метод
        """Алгоритм сравнения"""

    def getter(self) -> int:
        return self.__counter_ex

    def setter(self, new_value: int) -> None:
        self.__counter_ex = new_value

    def hello(self):  # TODO мутации
        return "по итальянски"

    class Books:
        list1 = [1, 2, 3, 4, 5]

# child1 = Child()
# print(child1.height)
# print(child1.weight)
# print(child1.hello())
# print(child1.counter_ex)
# child1.counter_ex = 666
# print(child1.counter_ex)

# print(child1._counter_ex)  # TODO использовать только если понимаем зачем
# print(child1._Child__counter_ex)  # TODO желательно не использовать
# print(child1.getter())
# child1.setter(999)
# print(child1.getter())


class Int1:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


first = Int1(3)
second = Int1(2)

# print(id(first))
# print(id(second))

print(first == second)
print(first.value == second.value)

