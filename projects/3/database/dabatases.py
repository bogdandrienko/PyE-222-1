import psycopg2

# CRUD

# TODO Read ############################################################################################################
# connection = psycopg2.connect(
#     user="test2",
#     password="12345Qwerty!",
#     host="127.0.0.1",  # localhost - 192.168.1.100
#     port="5432",
#     dbname="abonents",
# )
# connection.autocommit = False
# cursor = connection.cursor()
# query_string1 = """SELECT * FROM public.tarifs"""
# query_string2 = """SELECT * FROM public.tarifs WHERE fio != 'Bogdan' order by salary desc"""
# query_string3 = """SELECT sum(salary), 1 kol FROM public.tarifs group by kol"""
# cursor.execute(query_string3)
# rows = cursor.fetchall()
# print(rows)
# cursor.close()
# connection.close()
# TODO Read ############################################################################################################

# TODO Insert ##########################################################################################################
# connection = psycopg2.connect(
#     user="test2",
#     password="12345Qwerty!",
#     host="127.0.0.1",  # localhost - 192.168.1.100
#     port="5432",
#     dbname="abonents",
# )
# connection.autocommit = False
# cursor = connection.cursor()
# try:
#     for i in range(3000, 4000):
#         query_string1 = f"""INSERT INTO public.tarifs(iin, fio, type, active, salary) VALUES ('{i}', 'Dias', 'c', 'true', '50000');"""
#         cursor.execute(query_string1)
#     # print(1/0)
# except Exception as error:
#     print(error)
#     connection.rollback()
# else:
#     connection.commit()
# finally:
#     cursor.close()
#     connection.close()
# TODO Insert ##########################################################################################################

# TODO Update ##########################################################################################################
# connection = psycopg2.connect(
#     user="test2",
#     password="12345Qwerty!",
#     host="127.0.0.1",  # localhost - 192.168.1.100
#     port="5432",
#     dbname="abonents",
# )
# connection.autocommit = False
# cursor = connection.cursor()
# try:
#     query_string1 = f"""
# UPDATE public.tarifs
# SET fio = 'BOSS'
# WHERE salary != '50000';
# """
#     cursor.execute(query_string1)
#     # print(1/0)
# except Exception as error:
#     print(error)
#     connection.rollback()
# else:
#     connection.commit()
# finally:
#     cursor.close()
#     connection.close()
# TODO Update ##########################################################################################################

# TODO Delete ##########################################################################################################
# connection = psycopg2.connect(
#     user="test2",
#     password="12345Qwerty!",
#     host="127.0.0.1",  # localhost - 192.168.1.100
#     port="5432",
#     dbname="abonents",
# )
# connection.autocommit = False
# cursor = connection.cursor()
# try:
#     query_string1 = f"""DELETE FROM public.tarifs WHERE fio = 'Dias'"""
#     cursor.execute(query_string1)
#     print(1/0)
# except Exception as error:
#     print(f"ERROR!!!!! {error}")
#     connection.rollback()
# else:
#     connection.commit()
# finally:
#     cursor.close()
#     connection.close()
# TODO Delete ##########################################################################################################

import tkinter
from tkinter import ttk


def ui():
    tk_window = tkinter.Tk()
    tk_window.title("Example of tkinter UI desktop app")
    tk_window.geometry('640x480')
    tk_window.minsize(320, 240)
    tk_window.maxsize(1920, 1080)

    # iin, fio, type, active, salary

    ttk_label_iin = tkinter.Label(tk_window, text="iin")
    ttk_label_iin.grid(row=0, column=0)

    ttk_entry_iin = tkinter.Entry(tk_window)
    ttk_entry_iin.grid(row=1, column=0)
    ttk_entry_iin.insert(0, "970801")

    ttk_label_fio = tkinter.Label(tk_window, text="fio")
    ttk_label_fio.grid(row=0, column=1)

    ttk_entry_fio = tkinter.Entry(tk_window)
    ttk_entry_fio.grid(row=1, column=1)
    ttk_entry_fio.insert(0, "Иванов Иван")

    ttk_label_type = tkinter.Label(tk_window, text="type")
    ttk_label_type.grid(row=0, column=2)

    ttk_combo_type = ttk.Combobox(tk_window)
    ttk_combo_type['values'] = ("b", "c", "o")
    ttk_combo_type.current(1)
    ttk_combo_type.grid(row=1, column=2, sticky=tkinter.W)

    ttk_label_type = tkinter.Label(tk_window, text="active")
    ttk_label_type.grid(row=0, column=3)

    tk_chk_value_active = tkinter.BooleanVar(value=False)
    ttk_check_active = tkinter.Checkbutton(tk_window, text="активный/не активный", variable=tk_chk_value_active)
    ttk_check_active.grid(row=1, column=3)

    ttk_label_salary = tkinter.Label(tk_window, text="salary")
    ttk_label_salary.grid(row=0, column=4)

    tk_slider_salary = tkinter.Scale(tk_window, from_=1, to=1000000, orient=tkinter.HORIZONTAL)
    tk_slider_salary.grid(row=1, column=4)

    def click_button():
        iin = int(ttk_entry_iin.get())
        fio = str(ttk_entry_fio.get())
        type_ = str(ttk_combo_type.get())
        active = str(tk_chk_value_active.get()).lower()  # false / true
        salary = int(tk_slider_salary.get())

        # print("data:\n")
        # print(iin, fio, type_, active, salary)

        connection = psycopg2.connect(
            user="test2",
            password="12345Qwerty!",
            host="127.0.0.1",  # localhost - 192.168.1.100
            port="5432",
            dbname="abonents",
        )
        connection.autocommit = False
        cursor = connection.cursor()
        try:
            query_string1 = f"""INSERT INTO public.tarifs(iin, fio, type, active, salary) VALUES
            ('{iin}', '{fio}', '{type_}', '{active}', '{salary}');"""
            cursor.execute(query_string1)
            # print(1/0)
        except Exception as error:
            print(error)
            connection.rollback()
        else:
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    tk_btn = tkinter.Button(
        tk_window, text="Push data to database",  # текст кнопки
        background="#555",  # фоновый цвет кнопки
        foreground="#ccc",  # цвет текста
        padx="20",  # отступ от границ до содержимого по горизонтали
        pady="8",  # отступ от границ до содержимого по вертикали
        font="16",  # высота шрифта
        command=click_button,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
    )
    tk_btn.grid(row=2, column=0)

    tk_window.mainloop()


if __name__ == '__main__':
    ui()
