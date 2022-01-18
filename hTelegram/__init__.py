import telebot
from Constants.secret import SECRET
from hTelegram import telegram_functions as tfunc

class hTelegram:
	def __init__(self, qh):
		self.bot = telebot.TeleBot(SECRET)
		self.qh = qh


		@self.bot.message_handler(commands=['start'])
		def start(message):
			self.bot.send_message(message.chat.id, "test")


		@self.bot.message_handler(commands=['anime'])
		def anime(message):
			output = self.get_args(message.text)
			if output != []:
				id_ = output[0]
				if id_.isnumeric():
					output = tfunc.get_anime_names_from_id(self.qh, id_)
					if output != "":
						self.bot.send_message(message.chat.id, output)
					else:
						self.bot.send_message(message.chat.id, "bruh 404")
				else:
					self.bot.send_message(message.chat.id, "bruh send id and not some stupid bullshit you asshole")
			else:
				self.bot.send_message(message.chat.id, "bruh send smthng")



	def run(self):
		print("bot is running!")
		self.bot.polling()


	def get_args(self, string):
		args = string.split()[1:]

		return args