import blueprint.dbget as db
import blueprint.user as user
import blueprint.admin as admins
import blueprint.user as user
import blueprint.admin as admin 
import random
import datetime
import models as db
import main,flask
import fakes
port = 8080
ip = "0.0.0.0"
rootpass = "ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAQCtnTHro5CYzJBtGzgt2WTClwJ/RgAVRCp6N0QrZvZ8ROwD+eDwYJqp+bp7xdklli4Sg04vx7GMim6B0ieAQSuINE7uo7Ge24X/yrY/OABl5yFTcOe3OVZJoUO6rPT/v90m6LgD+Dbge++Zxi77YAXVL4IrTykCj8aJ1Q8JAX9M7TGSxIZDtdIu4ZnwgeWygTDLuIIVtVQJ30W7dVLTX1/559YZDbYt5bDoPvjaXtdtSWQ3ChjmSnJ0hCL5O2KTWJ1CZUNUvkMbsd1lSO2g2040v4QtBp4ZKSDniQkZYTgGc9r5eCyMxXoMa/MAq1KpN/kVnL9/1nFbBVff1d0unHRXrsa-key-20240713"
email = "xiaoxuanwangwin102@outlook.com"
# import blueprint.dbget as db
# word = db.word
# users = db.user
# pinglun=db.pinglun
def getblog():
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
    sql2= "SELECT userid,username,usertype FROM user"
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
    cursor.close()
    db.close()
    new_table = []
    for i in range(len(word)):
        new_table.append([])
        for j in word[i]:
            new_table[i].append(j)
            
    print("sql say --- Get db blogs in words , return :",new_table)
    return new_table
def getuser():
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
    sql2= "SELECT userid,username,usertype FROM user"
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
    users = get()[1]
    pinglun = get()[2]
    new_table = []
    for i in range(len(users)):
        new_table.append([])
        for j in users[i-1]:
            new_table[i-1].append(j)
    new_table = []
    for i in range(len(users)):
        new_table.append([])
        for j in users[i]:
            new_table[i].append(j)
    print("sql say --- Get db userlist in users , return :",new_table)
    return new_table
def getpinglun():
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
    sql2= "SELECT userid,username,usertype FROM user"
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
    new_table=[]
    for i in range(len(pinglun)):
        new_table.append([])
        for j in pinglun[i-1]:
            new_table[i-1].append(j)
            
    print("sql say --- Get db 评论 in pinglun , return :",new_table)
    return new_table
def setpinglun(from_,to,text,word):
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    sql4 = "INSERT into pinglun word,touser,user,content values (?, ?, ?, ?)"
    sql4_a=(word,to,from_,text)
    cursor.execute(sql4,sql4_a)
    db.commit()
# word = db.word
# users = db.users
# pinglun=db.pinglun
class userid():
    def __init__(self):
        pass

    def shengzheng(self):
        time = datetime.datetime.now()
        self.uid = time.strftime("%Y%m%d%H%M%S")
        self.uid += str(random.randint(0,10))
        self.uid += str(random.randint(0,10))
        return self.uid
    
    def jiexi(self,uid):
        uid = uid[0:-2]
        return datetime.datetime.strptime(uid,"%Y%m%d%H%M%S") 
class wordid():
    def __init__(self):
        pass

    def shengzheng(self):
        time = datetime.datetime.now()
        self.uid = time.strftime("%Y%m%d%H%M%S")
        self.uid += str(random.randint(0,10))
        self.uid += str(random.randint(0,10))
        return self.uid
    
    def jiexi(self,uid):
        uid = uid[0:-2]
        return datetime.datetime.strptime(uid,"%Y%m%d%H%M%S") 
def is_null(username,password):
	if(username==''or password==''):
		return True
	else:
		return False
def is_existed(username,password):
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
    sql2= "SELECT userid,username,usertype FROM user"
    sql3= "SELECT word,touser,user,content FROM pinglun"
    sql="SELECT * FROM user WHERE username ='%s' and password ='%s'" %(username,password)
    cursor.execute(sql)
    db.commit()
    
    result = cursor.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True
def exist_user(username):
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    sql = "SELECT * FROM user WHERE username ='%s'" % (username)
    cursor.execute(sql)
    db.commit()
    
    result = cursor.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True
def add_user(username, password):
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    a=userid()
    sql = "INSERT INTO user(username, password, userid) VALUES ('%s','%s','%s')" %(username, password,a.shengzheng())
    print(sql)
    # execute(sql)
    cursor.execute(sql)
    # commit
    db.commit()  # 对数据库内容有改变，需要commit()