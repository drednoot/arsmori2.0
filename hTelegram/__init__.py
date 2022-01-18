import telebot
from Constants.secret import SECRET

bot = telebot.TeleBot(SECRET)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "test")

def run():
	print("bot is running!")
	bot.polling()