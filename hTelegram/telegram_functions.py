from hTable import Animes

def get_anime_names_from_id(qh, id_):
	anime = Animes(qh, id_)
	names = anime.get_names().names
	output = '\n'.join(names)

	return output