import sqlite3
try:
    db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
    cursor = db.cursor()
except :
    try :
        db = sqlite3.connect("main.db", check_same_thread=False)
        cursor = db.cursor()
    except:raise Exception("db connet error")

sql = "SELECT id,title,word,userid FROM articles"
sql2= "SELECT userid,username,usertype,image FROM user"
sql3= "SELECT word,touser,user,content FROM pinglun"

def get():
    cursor.execute(sql)
    word=cursor.fetchall()
    cursor.execute(sql2)
    user=cursor.fetchall()
    cursor.execute(sql3)
    pinglun=cursor.fetchall()
    return word,user,pinglun

word = get()[0]
user = get()[1]
pinglun = get()[2]
print(word,user,pinglun)
# cursor.close()
# db.close()