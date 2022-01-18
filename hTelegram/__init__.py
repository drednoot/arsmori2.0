import telebot
from Constants.secret import SECRET
from hTable import Animes

class hTelegram:
	def __init__(self, qh):
		self.bot = telebot.TeleBot(SECRET)
		self.qh = qh

		@self.bot.message_handler(commands=['start'])
		def start(message):
			self.bot.send_message(message.chat.id, "test")


		@self.bot.message_handler(commands=['anime'])
		def anime(message):
			haruhi = Animes(qh, 6)
			names = haruhi.get_names().names
			output = '\n'.join(names)
			self.bot.send_message(message.chat.id, output)


	def run(self):
		print("bot is running!")
		self.bot.polling()