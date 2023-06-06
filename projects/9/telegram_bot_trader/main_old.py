import telebot
from telebot import types
import json

bot = telebot.TeleBot('6214461102:AAFlbKZo1UPZbLnZC7pW4XNVTgPeOzZxI0A')


# def logging(user: str, action: str):
#     with

@bot.message_handler(commands=['start'])
def start(message):
    try:
        first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь посмотреть ассортимент товаров?"
        markup = types.InlineKeyboardMarkup()
        with open("data/items.json", mode="r", encoding="utf-8") as file:
            for item in json.load(file):
                markup.add(types.InlineKeyboardButton(text=f"{item['title']} ({item['price']})", callback_data=str(item['id'])))
        bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
    except Exception as error:
        print("error: ", error)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    try:
        if function_call.message:

            with open("data/items.json", mode="r", encoding="utf-8") as file:
                for item in json.load(file):
                    if function_call.data == str(item["id"]):
                        markup = types.InlineKeyboardMarkup()
                        bot.send_message(function_call.message.chat.id, f"[{item['id']}] {item['title']} ({item['price']})\n {item['description']}",
                                         parse_mode='html', reply_markup=markup)

            print(function_call.data, type(function_call.data))
            if function_call.data == "yes":

                with open("data/items.json", mode="r", encoding="utf-8") as file:
                    items = json.load(file)
                    # print(items, type(items))

                second_mess = "<b>Вот список товаров:</b>\n\n"
                for item in items:
                    second_mess += f"[{item['id']}] {item['title']} = {item['price']}\n"
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
                bot.send_message(function_call.message.chat.id, second_mess, parse_mode='html', reply_markup=markup)
                bot.answer_callback_query(function_call.id)
    except Exception as error:
        print("error: ", error)



@bot.message_handler(commands=['start'])
def register(message):
    try:
        first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь посмотреть ассортимент товаров?"
        markup = types.InlineKeyboardMarkup()

        with open("data/items.json", mode="r", encoding="utf-8") as file:
            for item in json.load(file):
                markup.add(types.InlineKeyboardButton(text=f"{item['title']} ({item['price']})", callback_data=item['id']))
        bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
    except Exception as error:
        print("error: ", error)


# @bot.message_handler(commands=['start'])
# def register(message):
#     try:
#         first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь посмотреть ассортимент товаров?"
#         markup = types.InlineKeyboardMarkup()
#         button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#         markup.add(button_yes)
#         bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
#     except Exception as error:
#         print("error: ", error)

@bot.message_handler(commands=['register'])
def register(message):
    bot.send_message(message.chat.id, "Введите Ваше имя пользователя для регистрации: ")
    bot.register_next_step_handler(message, add_user)


def add_user(message: telebot.types.Message):  #
    try:
        print(type(message.text))
        print(message.text)
        with open("data/users.txt", mode="a", encoding="utf-8") as file:
            file.write(message.text + "\n")
    except Exception as error:
        print("error: ", error)

if __name__ == "__main__":
    # import sys
    # str1 = "1686058386"  # 2 tb
    # int1 = 1686058386    # 1 tb
    #
    # print(sys.getsizeof(str1))
    # print(sys.getsizeof(int1))

    print("bot started...")
    try:
        bot.infinity_polling()
    except Exception as error:
        print("error: ", error)
    print("bot stopped...")
