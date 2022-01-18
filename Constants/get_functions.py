from Constants import Constants

const = Constants()

def get_type_count(qh, name):
	if const.ANIME_TYPE_COUNT == None:
		row_count = qh.get_rows_count(name)
		const.ANIME_TYPE_COUNT = row_count
	else:
		row_count = const.ANIME_TYPE_COUNT

	return row_count