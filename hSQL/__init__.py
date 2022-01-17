# from tables.Tables import *
from mysql.connector.connection import MySQLConnection
from hSQL.mysql_connector import create_connection

from Constants.secret import HOST, LOGIN, PASSWORD

from Exceptions import *
from Constants import *



class Queryhandler:    
    def __init__(self, conn):

        self.conn = conn
        self.cur = self.conn.cursor()
        

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def fetch(self, q, multi = False):
        self.cur.execute(q, multi = multi)
        rows = self.cur.fetchall()

        return rows

    def exec(self, q):
        self.cur.execute(q)
        self.conn.commit()


    def get_last_insert_id(self):
            rows = self.select(('LAST_INSERT_ID()',))[0][0]

            return rows

        
    def get_rows_count(self, tab, cond = None):        
        self.select(('*',), tab, cond)

        return self.cur.rowcount


    # UPDATE
    def update(self, row_list, tab, cond_list = None):
        if cond_list == None:
            cond = ''
        elif type(cond_list) is list:
            cond = ' AND '.join(cond_list)
        elif type(cond_list) is str:
            cond = cond_list
        else:
            raise wrong_type(f"'cond_list' class must include either 'str' or 'list', but it includes {type(cond_list)}")

        # upd_dict = ', '.join([' = '.join([str(i), f'"{str(upd_dict[i])}"']) for i in upd_dict])

        query = f'UPDATE {tab} SET {row_list.get_update_str()}'
        if cond:
            query += f' WHERE {cond};'
        else:
            query += ';'
            
        print(query)
        self.exec(query)

        return self


    # INSERT
    def insert(self, rows, tab):
        ins = ''
        for row in rows.get_rows_respectivly():
            temp = [f'"{str(i)}"' for i in row]
            ins += f", ({', '.join(temp)})"
        ins = ins[2:]

        # print(rows)
        # print(rows.rows)

        query = f'INSERT INTO {tab} ({", ".join(rows.names)}) '
        query += f'VALUES {ins}'

        print(query)
        self.exec(query)

        return self


    # DELETE
    def delete(self, tab, cond_list):
        if type(cond_list) is list:
            cond = ' AND '.join(cond_list)
        elif type(cond_list) is str:
            cond = cond_list
        else:
            raise wrong_type(f"'cond_list' class must include either 'str' or 'list', but it includes {type(cond_list)}")

        query = f'DELETE FROM {tab} WHERE {cond};'

        print(query)
        self.exec(query)

        return self


    # SELECT
    def select(self, sel_tup, tab = None, cond_list = None, g_b = None, o_b = None, limit = None):
        cond = ''
        if cond_list:
            if type(cond_list) is list:
                cond = ' AND '.join(cond_list)
            elif type(cond_list) is str:
                cond = cond_list
            else:
                raise wrong_type(f"'cond_list' must be either str list or just string with condition but it's '{type(cond_list)}'")
        # multi = False
            
        query = f"SELECT {', '.join(sel_tup)}"
        if tab:
            query += f" FROM {tab}"
        if cond:
            query += f" WHERE {cond}"
        if g_b:
            query += f" GROUP BY {g_b}"  
        if o_b:
            query += f" ORDER BY {o_b}"
        if limit:
            query += f" LIMIT {limit[0]}, {limit[1]}"
        
        query += ";"

        print(query)
        rows = self.fetch(query)

        # print(rows)
        # row_list = Row_list(qh_rows=rows, qh_sel_tup=sel_tup)

        return rows