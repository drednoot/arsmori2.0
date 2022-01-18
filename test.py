from hSQL import Queryhandler
from hTelegram import hTelegram
from hSQL.mysql_connector import create_connection
from Constants.secret import HOST, LOGIN, PASSWORD

connection = create_connection(HOST, LOGIN, PASSWORD, 'arsbot_test')
qh = Queryhandler(connection)

hT = hTelegram(qh)
hT.run()

# haruhi = Animes(qh, 6)
# haruhi.get_names()
# print(haruhi.names.names)

qh.close()