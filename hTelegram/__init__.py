import telebot
from Constants.secret import SECRET

def run_bot():
	bot = telebot.TeleBot(SECRET)

	bot.polling()