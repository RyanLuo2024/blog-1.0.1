import sqlite3

try :
    db = sqlite3.connect("main.db", check_same_thread=False)
    cursor = db.cursor()
except:raise Exception("db connet error")

sql = "UPDATE user SET usertype=\"admin\" WHERE username='%s';" % (input("username:"))
cursor.execute(sql)
db.commit()
cursor.close()
db.close()