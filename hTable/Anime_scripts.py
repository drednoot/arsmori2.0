class Names:
	def __init__(self, row_count):
		self.type_name = {}
		self.id_name = {}
		self.names = []


	def add_row(self, id, type, name):
		try:
			self.id_name[id].append(name)
		except KeyError:
			# self.id_name[id] = 
			pass