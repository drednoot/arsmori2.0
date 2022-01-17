class Row:
	def __init__(self, key, value = "NULL"):
		self.key = str(key)
		self.val = value



class Table:
	def __init__(self, qh):
		self.id = Row("")						# pk
		self.name = self.__class__.__name__		# getting table name

		self.qh = qh							# QueryHandler



#####################################    ACTUAL CLASSES    #############################



class Animes(Table):
	def __init__(self, qh, id):
		super().__init__(qh)
		self.id = Row("anime_id", id)


	def get_names(self):
		self.names = Anime_names(self.qh, self.id)
		self.names.get()



class Anime_names(Table):
	def __init__(self, qh, anime_id):
		super().__init__(qh)
		self.id = Row("name_id")
		self.anime_id = anime_id
		self.type_id = Row("type_id")
		self.anime_name = Row("anime_name")

	def get(self):
		result = self.qh.select((self.id.key, self.type_id.key, self.anime_name.key),
			self.name,
			f'{self.anime_id.key} = {self.anime_id.val}')



class Anime_type_names(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("type_id")
		self.type_name = Row("type_name")



class Episodes(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("episode_id")
		self.anime_id = Row("anime_id")
		self.episode_number = Row("episode_number")
		self.name = Row("name")
		self.desc = Row("desc")
		self.link = Row("link")



class Statuses(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("status_id")
		self.user_id = Row("user_id")
		self.anime_id = Row("anime_id")
		self.episode_id = Row("episode_id")
		self.distribution_type = Row("distribution_type")
		self.distributor_id = Row("distributor_id")
		self.watched = Row("watched")