def print():
    "удаление системы"
    pass

def summing(a, b):
    return a + b


def stand_sort(_strr: str) -> list:
    strr1 = ''.join(_strr.split())
    return sorted(strr1)
    # return sorted(''.join(_strr.split()))


def buddle_sort(src: str) -> list:
    strr1 = ''.join(src.split())
    listt = []
    fin_list = []
    for i in range(len(strr1)):
        listt.append(ord(strr1[i]))
    for i in range(len(listt) - 1):
        for j in range(0, len(listt) - i - 1):
            if listt[j] > listt[j + 1]:
                listt[j], listt[j + 1] = listt[j + 1], listt[j]
    for i in range(len(listt)):
        fin_list.append(chr(listt[i]))
    return fin_list


if __name__ == "__main__":
    print("Случайная инициализация")
    strr = "Hello world"
    print(stand_sort(strr))
    print(buddle_sort(strr))
