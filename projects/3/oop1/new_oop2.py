import datetime
from utils import Main


class People:
    def __init__(self, fio: str, iin: int, data_birth: datetime.datetime, status_register: str):
        fio = fio.split(" ")
        self.name = fio[1]
        self.surname = fio[0]
        self.patronomyc = fio[2]
        self.iin = iin
        self.data_birth = data_birth
        self.status_register = True if str(status_register).strip() == "+" else False

    def get_full_name(self):
        return f"[{self.iin}] - {self.name} {self.patronomyc}"

    def check_register(self):
        return "Регистрация есть" if self.status_register else "Регистрации нет"


if __name__ == "__main__":
    rows = Main.Excel(filename="data2.xlsx").read_all()

    # list1 = [1, 2, 3, 4]
    # list2 = "Python"
    # print(list2[2:4])

    # peoples = []
    # for row in rows[1:]:
    #     new_people = People(
    #         fio=row[0],
    #         iin=row[1],
    #         data_birth=row[2],
    #         status_register=row[3],
    #     )
    #     peoples.append(new_people)

    peoples = [People(fio=row[0], iin=row[1], data_birth=row[2], status_register=row[3]) for row in rows[1:]]
    for people in peoples:
        print(people.get_full_name(), people.check_register())

    print('\n\n\n\n\n**********\n\n\n\n')

    peoples_with_reg = [people for people in peoples if people.status_register]
    for people in peoples_with_reg:
        print(people.get_full_name(), people.check_register())

    # list6 = [1, 2, 3, 4, 5, 6, 7, 8]
    # list7 = []
    # for i in list6:
    #     if i % 2 == 0:
    #         list7.append(i)
    #
    # list8 = [i for i in list6 if i % 2 == 0]

    # list1 = []
    # for i in range(1, 10)[1:]:
    #     list1.append(i)
    #
    # list2 = [i for i in range(1, 10)[1:]]
