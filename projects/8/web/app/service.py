import openpyxl
import json


def read_excel(filename='data.xlsx', sheetname='', is_have_titles=True) -> list[tuple[any]]:
    # открыли рабочую книгу -> активировали нужный рабочий лист -> прочитали строки
    # -> закрыли рабочую книгу -> вернули массив

    # [('Двигатель', 'V8, в отличном состоянии', 600000, 1, '05.16.2023'),
    # ('Двигатель 2', 'V9, в отличном состоянии', 1600000, 1, '04.16.2023')]

    # Открываем файл Excel
    workbook = openpyxl.load_workbook(f'./static/{filename}')

    if sheetname == '':
        # Получаем активный лист
        sheet = workbook.active
    else:
        # Получаем указанный лист
        sheet = workbook[sheetname]

    # создаём массив, который будем возвращать
    data = []

    # Читаем данные с первого листа
    for index, row in enumerate(sheet.iter_rows(values_only=True), 1):
        if index == 1 and is_have_titles:
            continue
        all_cols = []
        for item in row:
            all_cols.append(item is None)
            # if item is None:
            #     all_cols.append(True)
            # else:
            #     all_cols.append(False)
        if all(all_cols):
            continue
        data.append(row)

    # Закрываем файл Excel
    workbook.close()

    return data


def read_json(filename='data.json') -> list[dict[any]]:
    # открыли файл -> десериализовали (json -> object)
    # -> закрыли файл -> вернули массив

    # [
    #     {
    #       "id": 1,
    #       "title": "Клавиатура",
    #       "description": "б/у",
    #       "price": 1600.6,
    #       "count": 2,
    #       "date": "16.05.2023"
    #     },
    #     {
    #       "id": 2,
    #       "title": "Мышь",
    #       "description": "новая",
    #       "price": 2600.6,
    #       "count": 1,
    #       "date": "14.05.2023"
    #     },
    # ]
    with open(f'./static/{filename}', mode='r', encoding="utf-8") as file:
        data = json.load(file)
    return data
