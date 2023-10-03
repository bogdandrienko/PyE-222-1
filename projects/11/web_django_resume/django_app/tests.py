import re

if __name__ == "__main__":
    def check_reg(chars):
        if re.match(r'^(?=.*?[а-я])(?=.*?[А-Я])(?=.*?[0-9]).{4,}$', chars):
            return True
        return False

    print(check_reg("11Zzя"), "11Zzя")
    print(check_reg("11Z"), "11Z")
    print(check_reg("ZяяяяяяяZzЯ"), "ZяяяяяяяZzЯ")
    print(check_reg("Богдан777"), "Богдан777")

