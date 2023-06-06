def decorator_divide_by_two(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result / 2

    return wrapper


@decorator_divide_by_two
def func1(a, b):
    return a + b


@decorator_divide_by_two
def func2(a, b):
    return a - b


@decorator_divide_by_two
def func3(a, b):
    return a ** b


print(func1(2, 4))
print(func2(2, 4))
print(func3(4, 2))
