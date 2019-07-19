import telebot

TOKEN =  "747223213:AAHtvTdTcF-0Vvw4bWAxDGxU9hg2Yrg2sMo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)

bot.polling( none_stop = True )
