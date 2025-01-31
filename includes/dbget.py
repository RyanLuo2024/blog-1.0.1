import sqlite3
from config import *

class db:
    def __getcursor(self):
        try:
            db = sqlite3.connect(dbfile, check_same_thread=False)
            cursor = db.cursor()
        except:
            raise Exception("db connet error")
        return db, cursor

    def __init__(self):
        (self.db, self.cursor) = self.__getcursor()

    def execute(self, sql, import_=()):
        self.cursor.execute(sql, import_)
        self.db.commit()

    def get_return(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()
    def return_cursour(self):
        return (self.db, self.cursor)