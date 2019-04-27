import config
from bot import Bot


print(config.BOT_TOKEN)
import telebot

bot = telebot.TeleBot(config.BOT_TOKEN)

def get_user(message):
	return message.chat.id

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot_wrap.got_command("start",get_user(message),"")

@bot.message_handler(content_types=["location"])
def location_sent(message):
    print(message.location)
    location = message.location
    bot_wrap.got_location(location)

@bot.message_handler(content_types=["text"])
def text_sent(message):
    text = message.text
    bot_wrap.got_text_message(text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def send_message(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

bot_wrap = Bot({'send_message' : send_message})
bot.polling(none_stop=False, interval=0, timeout=20)
