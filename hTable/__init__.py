from hTable.Anime_scripts import Names
from Constants import get_functions as getf

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

		self.names = None


	def get_names(self):
		anime_names = Anime_names(self.qh, self.id)
		self.names = anime_names.get()

		return self.names



class Anime_names(Table):
	def __init__(self, qh, anime_id):
		super().__init__(qh)
		self.id = Row("name_id")
		self.anime_id = anime_id
		self.type_id = Row("type_id")
		self.anime_name = Row("anime_name")

		tn = Anime_type_names(self.qh)
		self.names = Names(tn.get_type_count())


	def get(self):
		rows = self.qh.select((self.id.key, self.type_id.key, self.anime_name.key),
			self.name,
			f'{self.anime_id.key} = {self.anime_id.val}')

		print(rows)
		

		for i in rows:
			id_ = i[0]
			type_ = i[1]
			name = i[2]
			self.names.add_row(id_, type_, name)

		return self.names



class Anime_type_names(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("type_id")
		self.type_name = Row("type_name")


	def get_type_count(self):
		row_count = getf.get_type_count(self.qh, self.name)

		return row_count



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



################################    distributors and such    ############################



class Distributors(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("distributor_id")
		self.name = Row("distributor_name")



class Distributions(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("distribution_id")
		self.distributor_id = Row("distributor_id")
		self.anime_id = Row("anime_id")
		self.distribution_type = Row("distribution_type")



class Distribution_types(Table):
	def __init__(self, qh):
		super().__init__(qh)
		self.id = Row("type_id")
		self.type_name = Row("type_name")
