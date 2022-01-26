from Constants import Constants

const = Constants()

def get_anime_type_count(qh, name):
	if const[name] == None:
		row_count = qh.get_rows_count(name)
		const[name] = row_count
	else:
		row_count = const[name]

	return row_count