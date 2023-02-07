import random
import time


def sort_sorted(_source: list[int], _reverse=False) -> list[int]:
    # _source.sort(reverse=_reverse)  # сортирует прям этот массив, но ничего не возвращает
    new_sorted_array = sorted(_source, reverse=_reverse)  # сортирует и возвращает отсортированный массив
    return new_sorted_array


def sort_bubble(_src: list[int], _reverse=False) -> list[int]:
    # https://vk.com/@bookflow-naglyadnaya-vizualizacii-algoritmov-sortirovki
    length = len(_src)
    for i in range(0, length - 1):
        already_sorted = True
        for j in range(0, length - 1 - i):
            if _reverse:
                if _src[j] < _src[j + 1]:
                    # a = 15
                    # b = 17

                    # c = b
                    # b = a
                    # a = c

                    # a, b = b, a
                    # print(a, b)

                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
                    already_sorted = False
            else:
                if _src[j] > _src[j + 1]:
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
                    already_sorted = False
        if already_sorted:
            break
    return _src


def sort_insertion(_src: list[int], _reverse=False) -> list[int]:
    length = len(_src)
    for i in range(1, length):
        key_item = _src[i]
        j = i - 1
        if _reverse:
            while j >= 0 and _src[j] < key_item:
                _src[j + 1] = _src[j]
                # j -= 1  # decrement
                j = j - 1  # decrement
        else:
            while j >= 0 and _src[j] > key_item:
                _src[j + 1] = _src[j]
                j = j - 1
        _src[j + 1] = key_item

    return _src


def sort_quicksort(_src: list[int], is_reversed=False) -> list[int]:
    def start_quicksort(__src: list[int], _is_reversed=False) -> list[int]:
        length = len(__src)
        if length < 2:
            return __src
        low, same, high = [], [], []
        pivot = __src[random.randint(0, length - 1)]
        for item in __src:
            if _is_reversed:
                if item > pivot:
                    low.append(item)
                elif item == pivot:
                    same.append(item)
                elif item < pivot:
                    high.append(item)
            else:
                if item < pivot:
                    low.append(item)
                elif item == pivot:
                    same.append(item)
                elif item > pivot:
                    high.append(item)
        return start_quicksort(low, is_reversed) + same + start_quicksort(high, is_reversed)

    return start_quicksort(_src, is_reversed)


def sort_merge(_src: list[int], is_reversed=False) -> list[int]:
    def start_merge(__src: list[int], _is_reversed=False) -> list[int]:
        def merge(left, right):
            if len(left) == 0:
                return right
            if len(right) == 0:
                return left
            result = []
            index_left = index_right = 0
            if _is_reversed:
                while len(result) < len(left) + len(right):
                    if left[index_left] >= right[index_right]:
                        result.append(left[index_left])
                        index_left += 1
                    else:
                        result.append(right[index_right])
                        index_right += 1
                    if index_right == len(right):
                        result += left[index_left:]
                        break
                    if index_left == len(left):
                        result += right[index_right:]
                        break
            else:
                while len(result) < len(left) + len(right):
                    if left[index_left] <= right[index_right]:
                        result.append(left[index_left])
                        index_left += 1
                    else:
                        result.append(right[index_right])
                        index_right += 1
                    if index_right == len(right):
                        result += left[index_left:]
                        break
                    if index_left == len(left):
                        result += right[index_right:]
                        break

            return result

        if len(__src) < 2:
            return __src
        midpoint = len(__src) // 2
        return merge(
            left=start_merge(__src[:midpoint], _is_reversed),
            right=start_merge(__src[midpoint:], _is_reversed)
        )

    return start_merge(__src=_src, _is_reversed=is_reversed)


if __name__ == "__main__":  # этот блок исполняется, только если файл запустить напрямую
    #          0  1  2   3                         9
    # list1 = [4, 5, 1, 333, 2, 3, 100, 42, 6, 60, 7]
    list1 = []
    for _ in range(1, 1000 + 1):
        list1.append(random.randint(1, 1000 + 1))
    is_reverse = False

    print("Оригинальный массив: ", list1)
    t_start = time.perf_counter()

    print("Стандартная сортировка: ", sort_sorted(list1, is_reverse))  # 0.00143
    print("Пузырьковая сортировка: ", sort_bubble(list1, is_reverse))  # 0.05709
    # print("Сортировка вставками: ", sort_insertion(list1, is_reverse))    # 0.02701
    # print("Сортировка быстрая: ", sort_quicksort(list1, is_reverse))      # 0.00699
    # print("Сортировка слиянием: ", sort_merge(list1, is_reverse))           # 0.00698

    t_stop = time.perf_counter()
    print("Заняло времени: ", round(t_stop - t_start, 5), " секунд")
