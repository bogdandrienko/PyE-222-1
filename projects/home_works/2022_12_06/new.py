########################################################################################################################
# TODO 1

import tkinter

tk_window = tkinter.Tk()
tk_window.title("Example of tkinter UI desktop app")
tk_window.geometry('640x480')

ttk_entry_1 = tkinter.Entry(tk_window)
ttk_entry_1.grid(row=1, column=0)
ttk_entry_1.insert(0, "data.txt")


def summing():
    filename = str(ttk_entry_1.get())
    with open(filename, mode="r") as file:
        data = file.readlines()
        print(data)
        list1 = []
        for i in data:
            val = int(i.strip())
            if val % 2 != 0:
                if val not in list1:
                    list1.append(val)
        data = list1
        data.sort(reverse=True)
        print(data)

    with open("new.txt", mode="w") as file:
        list2 = []
        for i in data:
            list2.append(str(i) + "\n")
        file.writelines(list2)


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
