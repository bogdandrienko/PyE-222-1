import time
# pip install pyinstaller
# pyinstaller --onefile fexe.py
# pip install auto-py-to-exe
# auto-py-to-exe

start = int(input("Введи начало: "))
stop = int(input("Введи конец: "))

for i in range(start, stop, 1):
    print(i)
    time.sleep(0.1)
