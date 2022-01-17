from Constants import *

def get_type_count(qh, name):
	if ANIME_TYPE_COUNT == None:
		row_count = qh.get_rows_count(name)
	else:
		row_count = ANIME_TYPE_COUNT

	return row_count