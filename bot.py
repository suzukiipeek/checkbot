from telebot import TeleBot, types

TOKEN = 'BOT_TOKEN'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    first_mess = (
        f"<b>{message.from_user.first_name} {message.from_user.last_name or ''}</b>, "
        "Здарова, ты думаешь попал на крутого бота?"
    )
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Конечно', callback_data='yes')
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_mess, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(call):
    bot.answer_callback_query(call.id)

    if not call.message:
        return

    chat_id = call.message.chat.id

    print(f"Нажата кнопка: callback_data={call.data}")

    if call.data == 'yes':
        second_mess = "Ха-ха, да нихуя ты не попал на крутого бота, ты лишь был обоссан мною by @oapku:"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Хочешь увидеть список твоих родителей?", callback_data='more'))
        bot.send_message(chat_id, second_mess, reply_markup=markup)

    elif call.data == 'more':
        bot.send_message(chat_id, "— Зайди на сайт на который ты обычно заходишь пока мама не видит)")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
