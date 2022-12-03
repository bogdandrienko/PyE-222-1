#####################
# сборка в exe

pip install pyinstaller # обязательно внутри нужного виртуального окружения
pyinstaller --onefile --console withou_ui.py
pyinstaller --onedir --console withou_ui.py

#####################

val1 = int(input("Введите первое число: "))
val2 = int(input("Введите второе число: "))

print(f"Результат: {val1*val2}")

val3 = int(input("введите что-либо для закрытия: "))
