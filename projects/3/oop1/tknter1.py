import tkinter
from tkinter import ttk

tk_window = tkinter.Tk()
tk_window.title("Example of tkinter UI desktop app")
tk_window.grid_rowconfigure(0, weight=1)
tk_window.grid_columnconfigure(0, weight=1)
tk_window.config(background="black")
tk_window.geometry('640x480')
tk_window.minsize(320, 240)
tk_window.maxsize(1920, 1080)
# tk_window.destroy

ttk_frame = ttk.Frame(tk_window, padding=10)
ttk_frame.grid()

ttk_style = ttk.Style(tk_window)
ttk_style.theme_use('vista')  # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

ttk_label = ttk.Label(ttk_frame, text="Hello")
ttk_label.grid(row=0, column=0)
#  ttk_label.place(x=0, y=300
ttk_label.config(text="World")

ttk_entry = ttk.Entry(ttk_frame)
ttk_entry.grid(row=1, column=0)
ttk_entry.insert(0, "Hello World")

tk_btn = tkinter.Button(
    ttk_frame, text="Click Me",  # текст кнопки
    background="#555",  # фоновый цвет кнопки
    foreground="#ccc",  # цвет текста
    padx="20",  # отступ от границ до содержимого по горизонтали
    pady="8",  # отступ от границ до содержимого по вертикали
    font="16",  # высота шрифта
    command=lambda: print("val1"),  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
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

tk_window.mainloop()
