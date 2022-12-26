########################################################################################################################
# TODO 1

# start = int(input("Введите от какого числа: "))
# stop = int(input("Введите до какого числа: "))
#
# result = 0
# for i in range(start, stop+1):
#     result = result + i
# print(result)

########################################################################################################################
# TODO 2

import tkinter

tk_window = tkinter.Tk()
tk_window.title("Example of tkinter UI desktop app")
tk_window.geometry('640x480')

ttk_entry_1 = tkinter.Entry(tk_window)
ttk_entry_1.grid(row=1, column=0)
ttk_entry_1.insert(0, "1")

ttk_entry_2 = tkinter.Entry(tk_window)
ttk_entry_2.grid(row=2, column=0)
ttk_entry_2.insert(0, "1")


def summing():
    start = int(ttk_entry_1.get())
    stop = int(ttk_entry_2.get())
    result = 0
    for i in range(start, stop+1):
        result = result + i
    print(result)


tk_btn = tkinter.Button(
    tk_window, text="Click Me",  # текст кнопки
    background="#555",  # фоновый цвет кнопки
    foreground="#ccc",  # цвет текста
    padx="20",  # отступ от границ до содержимого по горизонтали
    pady="8",  # отступ от границ до содержимого по вертикали
    font="16",  # высота шрифта
    command=summing,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
)
tk_btn.grid(row=3, column=0)

tk_window.mainloop()
