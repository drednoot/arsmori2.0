from hSQL import Queryhandler
from hSQL.mysql_connector import create_connection
from Constants.secret import HOST, LOGIN, PASSWORD

connection = create_connection(HOST, LOGIN, PASSWORD, 'arsbot_test')
qh = Queryhandler(connection)
### HEADERS loading test
type_names = qh.select(('type_id', 'type_name'), 'Anime_type_names').get_rows_respectivly()
ANIME_TYPE_NAMES_DICT = dict(type_names)
ANIME_NAME_TYPES_DICT = {value : key for (key, value) in ANIME_TYPE_NAMES_DICT.items()}

setting_names = qh.select(('setting_name_id', 'setting_name'), 'Setting_id_names').get_rows_respectivly()
SETTINGS_TYPE_NAMES_DICT = dict(setting_names)
SETTINGS_NAME_TYPES_DICT = {value : key for (key, value) in SETTINGS_TYPE_NAMES_DICT.items()}

distribution_names = qh.select(('type_id', 'type_name'), 'Distribution_types').get_rows_respectivly()
DISTRIBUTIONS_TYPE_NAMES_DICT = dict(distribution_names)
DISTRIBUTIONS_NAME_TYPES_DICT = {value : key for (key, value) in DISTRIBUTIONS_TYPE_NAMES_DICT.items()}

# print(ANIME_NAME_TYPES_DICT, '\n', SETTINGS_NAME_TYPES_DICT, '\n', DISTRIBUTIONS_NAME_TYPES_DICT)

### SETTINGS test
# settings = Settings(qh, 1)
# settings.get()
# settings.change('3', 'test2')
# print(settings)

### ANIME test 
# anime = Animes(qh, 4)
# anime.append()
# anime.get_names()
# print(anime.names_dict)
# 
# anime.append_name(1, 'Persona 4 the Animation')
# anime.append_name(3, 'Персона 4')
# anime.append_name(7, 'P4A')
# print(anime.names_dict)
# 
# anime.remove_name(list(anime.names_dict['other'].keys())[0]) 

# ANIME'S DISTRIBUTIONS TEST
# haruhi = Animes(qh, 6)
# haruhi.add_name('main_english', 'The Melancholy of Haruhi Suzumiya Season 2')
# haruhi.add_name('main_origin', 'Suzumiya Haruhi no Yuuutsu (2009)')
# haruhi.add_name('main_russian', 'Меланхолия Харухи Судзумии 2')


# reanimedia = Distributors(qh, 'Reanimedia')
# haruhi.load_distributions()
# haruhi.add_distribution('dub', reanimedia)
# haruhi.add_distribution('sub', reanimedia)
# print(haruhi.distributions)
# 
# gits = Animes(qh, 1)
# gits.load_distributions()
# print(gits.distributions)

### USER test
# user = Users(qh, 1)
# try:
#     user.append()
# except table_exists:
#     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
# 
# qh.delete('Anime_names', {'name_id': 8})

### DISTRIBUTION & DISTRIBUTOR test
# gits1 = Animes(qh, 3)
# gits2 = Animes(qh, 1)
# medusa = Distributors(qh, None, 4)
# print(medusa.get_name_by_id())
# dist1 = Distributions(qh, gits1, medusa, 'sub')
# dist2 = Distributions(qh, gits2, medusa, 'sub')
# dist2.append()
# dist1.append()
# medusa.add_distribution(gits1, 'sub')
# medusa.add_distribution(gits2, 'sub')
# 
# medusa.load_distributions()
# print(medusa.distributions)
# print(medusa.distributions_by_id)

### SELECT test
# result = qh.select( ('anime_id', 'anime_name'), 'Anime_names',
#     (f'anime_name REGEXP "[[:<:]]ghost[[:>:]]"',), 'anime_id', 'name_id' )
# print(result.get_rows_respectivly())
# print(qh.cur.rowcount)

### INSERT test
# rows = Row_list(Row('anime_id', [7,7,7]), Row('type_id', [1, 3, 4]), Row('anime_name', ['Grand Blue', 'Необъятный океан', 'Grand Blue Dreaming']))
# qh.insert(rows, 'Anime_names')

### UPDATE test
# rows = Row_list(Row('setting_value', ['aaa']))
# qh.update(rows, 'Settings', ['user_id = 1'])

### DELETE test
# qh.delete('Anime_names', ['anime_id = 7'])

qh.close()