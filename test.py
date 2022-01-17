from hSQL import Queryhandler
from hTable import Animes
from hSQL.mysql_connector import create_connection
from Constants.secret import HOST, LOGIN, PASSWORD

connection = create_connection(HOST, LOGIN, PASSWORD, 'arsbot_test')
qh = Queryhandler(connection)

haruhi = Animes(qh, 6)
haruhi.get_names()
print(haruhi.names.names)

qh.close()