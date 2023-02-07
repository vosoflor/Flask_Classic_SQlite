import sqlite3
from config import DATABASE

class ConnectDatabase:
    def __init__(self, querySQL, dataForQuery = []):
        self.con = sqlite3.connect(DATABASE)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySQL, dataForQuery)