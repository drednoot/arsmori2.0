class Names:
	def __init__(self, type_count):
		self.type_name = {}
		self.id_name = {}
		self.names = []

		self.id_type_index = {}
		self.id_names_index = {}

		for i in range(1, int(type_count) + 1):
			self.type_name[i] = []


	def add_row(self, id_, type_, name):
		self.type_name[type_].append(name)
		app_ind = len(self.type_name[type_]) - 1
		self.id_type_index[id_] = (type_, app_ind)

		self.id_name[id_] = name

		self.names.append(name)
		app_ind = len(self.names) - 1
		self.id_names_index[id_] = app_ind