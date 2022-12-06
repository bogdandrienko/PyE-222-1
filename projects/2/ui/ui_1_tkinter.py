#####################
# сборка в exe

# pip install pyinstaller # обязательно внутри нужного виртуального окружения
# pyinstaller --onefile --windowed ui_1_tkinter.py
# pyinstaller --onedir --windowed ui_1_tkinter.py

#####################





# 1) ссылка, количество, название - программа для скачки картинок (Tkinter)
# 2) Парсер погоды (PySide2)
# 3) Парсер валюты (Pyqt6)

# from tkinter import *  # коллизии имён
from tkinter import ttk
import tkinter
import requests


root = tkinter.Tk()
root.geometry("640x480")
frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="Ссылка: ").grid(column=0, row=0)
url = ttk.Entry(frm)
url.grid(column=1, row=0)

ttk.Label(frm, text="Количество: ").grid(column=0, row=1)
count = ttk.Entry(frm)
count.grid(column=1, row=1)

ttk.Label(frm, text="Имя: ").grid(column=0, row=2)
name = ttk.Entry(frm)
name.grid(column=1, row=2)


def start():
    print("start")
    # print(url, type(url))
    # print(url.get(), type(url.get()))
    # url_for_download = str(url.get())   # https://picsum.photos/320/240/
    # count_for_download = int(count.get())
    # name_for_download = str(name.get())
    val1 = int(url.get())
    val2 = int(count.get())

    def summator(start_value: int, stop_value: int) -> int:
        sum_value = 0
        for i in range(start_value, stop_value + 1, 1):
            sum_value += i
        return sum_value

    value = summator(start_value=val1, stop_value=val2)
    print(value)
    # print(url_for_download)
    # print(count_for_download)
    # print(name_for_download)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    # data = b"hello"
    # "hello".encode() => b"hello" | b"hello".decode() => "hello"

    # for i in range(1, count_for_download + 1):  # 1 2 3 ... 7
    #     data = requests.get(url=url_for_download, headers=headers).content
    #     with open(f"{name_for_download}({i}).jpg", "wb") as opened_file:
    #         opened_file.write(data)

    print("stop")


ttk.Button(frm, text="Старт", command=start).grid(column=1, row=3)

root.mainloop()
