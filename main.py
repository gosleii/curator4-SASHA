import telebot

bot = telebot.TeleBot('6642050787:AAFxDO7QfD1mekRNLlGK_YrsDrd8_8Wur34')


@bot.message_handler(commands=['name'])
def main(message):
    bot.send_message(message.chat.id, "Максимакс")


@bot.message_handler(commands=['love'])
def main(message):
    bot.send_message(message.chat.id, '*BURGER KING*', parse_mode='Markdown')


bot.infinity_polling()