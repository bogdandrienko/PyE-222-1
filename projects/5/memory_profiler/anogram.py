def clear_method(source: str, equal: str) -> bool:
    if len(source) < 1 or len(equal) < 1:
        return False
    if len(source.split(" ")) != len(equal.split(" ")):
        return False
    return sorted(source) == sorted(equal)  # O(log(n)) * 2


def dirty_method1(source: str, equal: str) -> bool:
    for i in equal:  # O(N)
        if i not in source:
            return False
    return True


def dirty_method2(source: str, equal: str) -> bool:
    source_dict = {}
    for i in source:
        # if source_dict.get(i, "не существует") == "не существует":
        #     source_dict[i] = 1
        # else:
        #     source_dict[i] += 1
        source_dict[i] = source_dict.get(i, 0) + 1
    # print(source_dict)
    for j in equal:
        elem = source_dict.get(j, None)
        if elem is None or elem < 1:
            return False
        else:
            source_dict[j] -= 1
            if source_dict[j] == 0:
                del source_dict[j]
    # print(source_dict)  # {'t': 0, 'e': 0, 'a': 0} == {}
    return source_dict == {}


def check_arrays():
    # Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
    # Надо вернуть [1, 2, 2, 3] (порядок неважен)

    # set1 = set()
    # set2 = set()
    #
    # set1.intersection()
    # set1.difference()

    src1: list[int] = [1, 2, 3, 2, 0]
    src2: list[int] = [5, 1, 2, 7, 3, 2]
    # output = [1, 2, 2, 3]

    source_dict = {}
    for i in src1:
        source_dict[i] = source_dict.get(i, 0) + 1
    print(source_dict)
    result = []
    for j in src2:
        if source_dict.get(j, 0) > 0:
            result.append(j)
            source_dict[j] -= 1
    return result

if __name__ == "__main__":
    a = "tea"  # "ватерполистка"
    b = "eat"  # "австралопитек"
    # print(clear_method(a, b))
    # print(dirty_method1(a, b))
    # print(dirty_method2(a, b))

    print(check_arrays())

    # c = "Python is awesome"
    # print("P" in c)

    # print("".join(c.split(" ")))



