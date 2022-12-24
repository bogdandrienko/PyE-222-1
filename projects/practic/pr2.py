import openpyxl
import requests

# выбрать с сайта json-placeholder данные и записать их в одну папку в разные excel файлы

link = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url=link)

# json_data = response.content  # bytes (image, file...)
# json_data = response.text  # str (str, html...)
json_data = response.json()  # dict (dict, [dict, dict, dict]...)
print(json_data, type(json_data))

# userId - 1 - excel1.xlsx
# userId - 2 - excel2.xlsx

# 1) Получить данные и превращаем объекты в словарь (массив словарей)
# 2) Форматирование и подготовка данных
# 3) Записывать в один excel файл
# 4) Записывать в разные excel файлы

# raw_data = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui'

json_data.sort(key=lambda x: x['id'], reverse=False)
print(json_data)

# list1 = []
# list2 = []
# user_id = 0
# for i in json_data:
#     if i["userId"] == user_id:
#         list2.append(i)
#     else:
#         list1.append(list2)
#         list2 = []
#     user_id = i["userId"]
# print(list1)

# for x in list1:
#     print(x)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1.extend(list2)
# list3 = [*list1, *list2]

dict1 = {}
# print(dict1[1])
# json_data = [{'userId': 1, 'id': 1, '11title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, '11title': 'delectus aut autem', 'completed': False}, {'userId': 2, 'id': 22, 'title': '22delectus aut autem', 'completed': False}, {'userId': 2, 'id': 23, 'title': '22delectus aut autem', 'completed': False}, {'userId': 2, 'id': 24, 'title': '22delectus aut autem', 'completed': False}]
for i in json_data:
    user_id = i["userId"]  # 1, 2, 3... 10
    try:
        current_object = dict1[user_id]  # [i]
        current_object.extend(i)
        dict1[user_id] = current_object
    except Exception as error:
        list5 = []
        list5.append(i)
        dict1[user_id] = list5
print(dict1)

excels = []
for key, value in dict1.items():
    print(value)
    # dict_10 = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    list5 = []
    for key2, value2 in value.items():
        if key2 == "completed":
            if value2 is True:
                list5.append(1)
            else:
                list5.append(0)
        else:
            list5.append(value2)
    excels.append(list5)
print(excels)
# dict1 = {}
#
# for i in json_data:
#     print(i)

# dict2 = {1: [1, 2, 3, 5]}
# print(dict2[1])

excels = \
    [
        [
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed11111111111111"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
        ],
        [
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed2222222222222"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
        ],
        [
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed33333333333"],
            ["userId", "id", "title", "completed"],
            ["userId", "id", "title", "completed"],
        ],
    ]

data1 = [
    ["userId", "id", "title", "completed"],
    ["userId1", "id", "title", "completed1"],
    ["userId2", "id", "title", "completed2"],
    ["userId3", "id", "title", "completed3"],
    ["userId4", "id", "title", "completed4"],
]

# for excel_index, excel in enumerate(excels, 1):
#     new_workbook = openpyxl.Workbook()
#     new_worksheet = new_workbook.active
#
#     index_row = 0
#     for row in excel:
#         index_row = index_row + 1
#         print(row)
#         for index_column, cell in enumerate(row, 1):
#             print(cell)
#             new_worksheet.cell(row=index_row, column=index_column, value=cell)
#
#     new_workbook.save(f"excel_data/new{excel_index}.xlsx")
