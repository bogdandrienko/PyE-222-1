"""
Консольные:
- технические команды (сис. админы / программисты)

Графические:
- desktop [c# - wpf / c++ Qt / python PyQt6(PySide2/tkinter)] (windows, linux, mac)
- mobile [swift|objective-c / kotlin/java  / python-kivy] (ios/android)
- web [PHP-laravel, Python-django, JavaScript-Nodejs (много программистов), flask, fastapi... , Java-Spring-(банки-надёжность), Go-Gin (backend-speed), C++ Webassembly ] (сайты в браузере Chrome/Mozila/Safari)
- iot [c/c++ ...java/assembler/] (холодильники, стиралки, пылесосы, комбайны, бульдозеры..)
"""

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# import tkinter as tk
# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
# frame_a.pack()
# frame_b.pack()
# window.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class Ui:
    def __init__(self, title: str, icon="icon.ico", width=640, height=480):
        # todo основное ################################################################################################
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{width}x{height}')
        self.window.iconbitmap(icon)
        # todo основное ################################################################################################

        #

        # todo вёрстка #################################################################################################

        self.label_filename = tk.Label(self.window, text="Введите название excel-файла для чтения")
        self.label_filename.grid(column=0, row=0)

        self.entry_filename = ttk.Entry(self.window)
        self.entry_filename.insert(0, "data.xlsx")
        self.entry_filename.grid(column=1, row=0)

        self.button_start = tk.Button(self.window, text="запустить", command=self.clicked)
        self.button_start.grid(column=0, row=1)

        self.label_result = tk.Label(self.window, text="...")
        self.label_result.grid(column=1, row=1)

        self.select_box_variable = tk.StringVar(self.window)
        self.select_box_variable.set("стекло")  # default value
        self.select_box = tk.OptionMenu(
            self.window, self.select_box_variable, "стекло", "металл", "органика", command=self.change_box
        )
        self.select_box.grid(column=1, row=2)

        # todo вёрстка #################################################################################################

    @staticmethod
    def change_box(event):
        print("ПРИВЕТ")

        from tkinter import messagebox
        answer = messagebox.askokcancel("Вопрос", "Создать новое окно или закрыть приложение?")
        if answer:
            new_ui = Ui(title="My Awesome App 2")
            new_ui.show()

        pass

    def show(self):
        self.window.mainloop()

    def clicked(self):
        filename = self.entry_filename.get()
        workbook: Workbook = openpyxl.load_workbook(filename)
        worksheet: Worksheet = workbook.active
        text = str(worksheet.cell(row=1, column=1).value)
        self.label_result.configure(text=text)


if __name__ == "__main__":
    ui = Ui(title="My Awesome App")
    ui.show()
    pass
