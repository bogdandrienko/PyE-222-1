def decor_rounding(function: any) -> any:
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = function(*args, **kwargs)
        result = int(result)
        return result

    return wrapper


@decor_rounding
def square(side1: float | int, side2: float | int) -> float | int:
    return side1 * side2


@decor_rounding
def perimeter(side1: float | int, side2: float | int) -> float | int:
    return (side1 + side2) * 2


def print_name(name: str) -> str:
    return name


print(square(side1=10.5, side2=15.2))  # 159.6  159
print(perimeter(10.02, 15.0))

# print("BoGdan".upper())
