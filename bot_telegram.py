import config
print(config.BOT_TOKEN)
import telebot

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

user = bot.get_me()
print(user)

bot.polling(none_stop=False, interval=0, timeout=20)