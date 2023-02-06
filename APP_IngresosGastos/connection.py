import sqlite3
from config import DATABASE

class ConnectDatabase:
    def __init__(self, querySQL, dataForQuery):
        self.con = sqlite3.connect(DATABASE)
        self.cur = self.con.cursor()
        if dataForQuery:
            self.res = self.cur.execute(querySQL, dataForQuery)
        else:
            self.res = self.cur.execute(querySQL)