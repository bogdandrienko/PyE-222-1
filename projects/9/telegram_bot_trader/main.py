import telebot
from telebot import types
import json
import datetime

bot = telebot.TeleBot('6214461102:AAFlbKZo1UPZbLnZC7pW4XNVTgPeOzZxI0A')
ERROR_TEXT = "Произошла ошибка, попробуйте ещё раз или обратитесь к администратору"
DEBUG = False  # TODO debug == true - идёт разработка


def decorator_exception_1(func):
    def wrapper(*args, **kwargs):
        message: telebot.types.Message = args[0]
        try:
            func(*args, **kwargs)
        except Exception as error:
            _error = f"error: {error}"
            print(_error)
            with open("logs/errors.txt", mode="a", encoding="utf-8") as file:
                file.write(f"[{datetime.datetime.now()}] {error}\n")
            if DEBUG:
                bot.send_message(message.chat.id, _error, parse_mode='html')
            else:
                bot.send_message(message.chat.id, ERROR_TEXT, parse_mode='html')

    return wrapper


# todo КОМАНДА - 'start' - telegram - '/start'
@decorator_exception_1
@bot.message_handler(commands=['start'])
def f_start(message):
    commands = """
<strong>Я могу помочь тебе купить себе что-нибудь свеженькое!</strong>

<b>Ниже список команда с описанием:</b>

<i>Базовые:</i>
/start - начальное меню

<i>Работа с товаром:</i>
/sale - создание нового товара

"""
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, commands, parse_mode='html', reply_markup=markup)


@decorator_exception_1
@bot.message_handler(commands=['sale'])
def f_sale(message):
    bot.send_message(message.chat.id, """<b>Введите через запятую название, количество и цену публикуемого товара:</b>""", parse_mode='html')
    bot.register_next_step_handler(message, f_sale_step1)


@decorator_exception_1
def f_sale_step1(message: telebot.types.Message):
    data = message.text.split(",")

    title: str = data[0].strip().capitalize()
    count: int = int(data[1].strip())
    price: float = float(data[2].strip())
    # print(title, count, price)

    with open("data/items.json", mode="r", encoding="utf-8") as file:
        items: list[dict] = json.load(file)
        items.append({"id": int(items[-1]["id"]) + 1, "title": title, "count": count, "price": price})

    with open("data/items.json", mode="w", encoding="utf-8") as file:
        json.dump(items, file)


if __name__ == "__main__":
    print("bot started...")
    try:
        bot.infinity_polling()
    except Exception as error:
        print("error: ", error)
    print("bot stopped...")

    # Практика - написать и запустить бота, который при команде старт принимает
    # сообщение и возвращает его "в обратном порядке"
