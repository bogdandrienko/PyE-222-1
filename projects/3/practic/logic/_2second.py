# 2) Форматирование и подготовка данных


def second(raw_data: list[dict], is_logging=False) -> list[list[any]]:
    def for_sort(item: dict):
        return item["id"]

    # def <lambda> (item):
    #     return item['id']
    # raw_data.sort(key=lambda item: item['id'], reverse=False)

    raw_data.sort(key=for_sort, reverse=True)

    if is_logging:
        print(raw_data)
    rows = []
    for dict_obj in raw_data:
        val1 = dict_obj["userId"]
        val2 = dict_obj["id"]
        val3 = dict_obj["title"]
        val4 = dict_obj["completed"]
        if val4 is False:
            val4 = 0
        else:
            val4 = 1
        row = [val1, val2, val3, val4]
        rows.append([row])
    if is_logging:
        print(rows)
    return rows


def example():
    dict1 = {'userId': 10, 'id': 200, 'title': 'ipsam aperiam voluptates qui', 'completed': True}
    list1 = [10, 200, 'ipsam aperiam voluptates qui', 1]
    #       [10, 200, 'ipsam aperiam voluptates qui', 1]
    val1 = dict1["userId"]
    val2 = dict1["id"]
    val3 = dict1["title"]
    val4 = dict1["completed"]
    if val4 is False:
        val4 = 0
    else:
        val4 = 1
    list2 = [val1, val2, val3, val4]
    print(list2)
