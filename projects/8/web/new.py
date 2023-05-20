import openpyxl

# Открываем файл Excel
workbook = openpyxl.load_workbook('./static/data.xlsx')

# Получаем первый лист
sheet = workbook.active

# Читаем данные с первого листа
for index, row in enumerate(sheet.iter_rows(values_only=True), 1):
    if index == 1:
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
    print(row)

# Закрываем файл Excel
workbook.close()
