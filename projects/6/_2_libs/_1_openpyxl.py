
########################################################################################################################

#Нужно прочитать все(от 0 до 10) листы и записать на один вертикально
import openpyxl
from openpyxl.reader.excel import load_workbook

# Import `load_workbook` module from `openpyxl`
from openpyxl import load_workbook

# Load in the workbook
wb = load_workbook('data.xlsx')
# sheet = wb.get_sheet_by_name('Лист1')
#
# for name in wb.sheetnames:
#     print(name)
sheet = wb['Лист1']
a1 = sheet['A1'].value
b1 = sheet['B1'].value
c1 = sheet['C1'].value
sheet = wb['Лист2']
d1 = sheet['A1'].value
e1 = sheet['B1'].value
f1 = sheet['C1'].value
sheet = wb['Лист3']
g1 = sheet['A1'].value
h1 = sheet['B1'].value
j1 = sheet['C1'].value
list1 = [[a1,b1,c1],[d1,e1,f1],[g1,h1,j1]]
print(list1)
#Нету динамичности(если имя рабочего листа или количества  то логика сломается)
#Нету записи в новый файл


