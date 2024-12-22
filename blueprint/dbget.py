import sqlite3
class db:
    def __getcursor(self,file):
        try:
            db = sqlite3.connect(file, check_same_thread=False)
            cursor = db.cursor()
        except :
            raise Exception("db connet error")
        return db,cursor
    def __init__(self,file):
        self.file = file
        (self.db, self.cursor) = self.__getcursor()
    def execute(self,sql,import_=()):
        self.cursor.execute(sql,import_)
        self.db.commit()
    def get_return(self):
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.db.close()
