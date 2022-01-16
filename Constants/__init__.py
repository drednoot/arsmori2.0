SEARCH_PAGE_SIZE = 5
DATABASE_NAME = 'arsbot_test'


ANIME_TYPE_NAMES_DICT = {
    1: 'main_english',
    2: 'main_origin',
    3: 'main_russian',
    4: 'english',
    5: 'origin',
    6: 'russian',
    7: 'other'
}
ANIME_NAME_TYPES_DICT = {value : key for (key, value) in ANIME_TYPE_NAMES_DICT.items()}


SETTINGS_TYPE_NAMES_DICT = {
    1: '1',
    2: '2',
    3: '3'
}
SETTINGS_NAME_TYPES_DICT = {value : key for (key, value) in SETTINGS_TYPE_NAMES_DICT.items()}


DISTRIBUTIONS_TYPE_NAMES_DICT = {
    1: 'sub',
    2: 'dub',
    3: 'raw'
}
DISTRIBUTIONS_NAME_TYPES_DICT = {value : key for (key, value) in DISTRIBUTIONS_TYPE_NAMES_DICT.items()}



# command callback query's prefixes
SEARCH_PREFIX = "search"
DISTS_TYPE_PREFIX = "dists_type"