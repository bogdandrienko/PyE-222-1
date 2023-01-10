import tkinter
from tkinter import ttk
import requests
import aiohttp
from utils import Main


# import PYQT6


class Ui:
    def __init__(self, title: str) -> None:
        self.tk_window = tkinter.Tk()
        self.tk_window.title(str(title))
        self.tk_window.grid_rowconfigure(0, weight=1)
        self.tk_window.grid_columnconfigure(0, weight=1)
        self.tk_window.config(background="black")
        self.tk_window.geometry('640x480')
        self.tk_window.minsize(320, 240)
        self.tk_window.maxsize(1920, 1080)
        # tk_window.destroy

        ttk_frame = ttk.Frame(self.tk_window, padding=10)
        ttk_frame.grid()

        ttk_style = ttk.Style(self.tk_window)
        ttk_style.theme_use('vista')  # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

        ttk_label = ttk.Label(ttk_frame, text="Hello")
        ttk_label.grid(row=0, column=0)
        #  ttk_label.place(x=0, y=300
        ttk_label.config(text="World")

        self.entry1 = self.create_entry_label(frame=ttk_frame, row=1, column=5, default_text="ПРИВЕТ 1")
        self.entry2 = self.create_entry_label(frame=ttk_frame, row=2, column=5, default_text="ПРИВЕТ 2")
        self.entry3 = self.create_entry_label(frame=ttk_frame, row=3, column=5, default_text="ПРИВЕТ 3")
        self.entry4 = self.create_entry_label(frame=ttk_frame, row=4, column=5, default_text="ПРИВЕТ 4")

        tk_btn = tkinter.Button(
            ttk_frame, text="Click Me",  # текст кнопки
            background="#555",  # фоновый цвет кнопки
            foreground="#ccc",  # цвет текста
            padx="20",  # отступ от границ до содержимого по горизонтали
            pady="8",  # отступ от границ до содержимого по вертикали
            font="16",  # высота шрифта
            command=self.click_button,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
        )
        tk_btn.grid(row=2, column=0)

        tk_entry_value = tkinter.StringVar(value='hello!')
        ttk_entry = ttk.Entry(ttk_frame, textvariable=tk_entry_value)
        ttk_entry.grid(row=3, column=0)

        tk_chk_value = tkinter.BooleanVar(value=True)
        ttk_check = tkinter.Checkbutton(ttk_frame, text="Добавлять/не добавлять", variable=tk_chk_value)
        ttk_check.grid(row=4, column=0)

        tk_slider = tkinter.Scale(ttk_frame, from_=1, to=59, orient=tkinter.HORIZONTAL)
        tk_slider.grid(row=5, column=0)

        ttk_combo = ttk.Combobox(ttk_frame)
        ttk_combo['values'] = (1, 2, 3, 4, 5, "Text")
        ttk_combo.current(1)
        ttk_combo.grid(row=6, column=0, sticky=tkinter.W)

        tk_text = tkinter.Text(ttk_frame, font="20", width=10, height=10)
        tk_text.grid(row=0, column=1, sticky=tkinter.W)

        ttk_tree = ttk.Treeview(ttk_frame, columns=('№', 'Фамилия:', 'Имя:', 'Отчество:', 'Дополнительно:'))

        # Set the heading (Attribute Names)
        ttk_tree.heading('#0', text='№')
        ttk_tree.heading('#1', text='Фамилия')
        ttk_tree.heading('#2', text='Имя')
        ttk_tree.heading('#3', text='Отчество')
        ttk_tree.heading('#4', text='Дополнительно')

        # Specify attributes of the columns (We want to stretch it!)
        ttk_tree.column('#0', stretch=tkinter.YES)
        ttk_tree.column('#1', stretch=tkinter.YES)
        ttk_tree.column('#2', stretch=tkinter.YES)
        ttk_tree.column('#3', stretch=tkinter.YES)
        ttk_tree.column('#4', stretch=tkinter.YES)

        ttk_tree.insert('', 'end', iid="1", values=("1", "2", "3", "4", "5"))
        ttk_tree.grid(row=8, columnspan=4, sticky='nsew')

    def create_entry_label(self, frame: ttk.Frame, row: int, column: int, default_text=""):
        _ttk_entry = ttk.Entry(frame)
        _ttk_entry.grid(row=row, column=column)
        _ttk_entry.insert(0, default_text)
        return _ttk_entry

    def show_ui(self):
        self.tk_window.mainloop()

    def click_button(self):
        response = requests.get("https://api.coincap.io/v2/assets")
        if response.status_code != 200:
            print(f"Ошибка: {response.status_code}")
        response_dict = response.json()

        #          0  1  2  3
        # list1 = [1, 2, 3, 4]

        array_cripto = []

        for valute in response_dict["data"]:
            cr1 = Cripto(
                name=valute["id"], rank=valute["rank"], symbol=valute["symbol"],
                price=float(valute["priceUsd"]), change=float(valute["changePercent24Hr"])
            )
            array_cripto.append(cr1)

        print(array_cripto)
        for i in array_cripto:
            i.beatify()

        array_positive_cripto = []
        for i in array_cripto:
            if i.is_upper(multiply=5):
                array_positive_cripto.append(i)
        print(array_positive_cripto)
        for i in array_positive_cripto:
            i.beatify()

        write_to_excel(valutes=array_positive_cripto)


class Cripto:
    """Хочу денег"""

    def __init__(self, name: str, rank: int, symbol: str, price: int | float, change: int | float):
        self.name = name
        self.rank = rank
        self.symbol = symbol
        self.price = price
        self.change = change

    def beatify(self):
        print(f"[{self.symbol}] : {self.price} ({round(self.change, 1)})")

    def is_upper(self, multiply: int | float) -> bool:
        if self.change <= multiply:
            print(f"Валюта упала {round(self.change, 3)}")
            return False
        else:
            print(f"Валюта выросла {round(self.change, 3)}")
            return True

    def get_change(self, multiply=5.0):
        if self.change <= multiply:
            return f"Валюта упала {round(self.change, 3)}"
        else:
            return f"Валюта выросла {round(self.change, 3)}"


def write_to_excel(valutes: list[Cripto]):
    # TODO создание НОВОГО excel-файла
    excel = Main.Excel()

    # TODO формирование матрицы из массива валют
    rows2 = [[valute.name, valute.symbol, valute.price, valute.get_change()] for valute in valutes]

    # TODO запись матрицы в excel-файл
    excel.write_from_coordinates(matrix=rows2)

    # rows = []
    # for valute in valutes:
    #     row = [valute.name, valute.symbol, valute.price, valute.change]
    #     rows.append(row)
    # rows2 = [[valute.name, valute.symbol, valute.price, valute.change] for valute in valutes]
    #
    # # list2 = []
    # # for x in [1, 2, 3]:
    # #     list2.append(x)
    # # list1 = [x for x in [1, 2, 3]]
    #
    # excel.write_from_coordinates(matrix=rows2)


if __name__ == "__main__":
    ui_app = Ui("Парсер криптовалют")
    ui_app.show_ui()
