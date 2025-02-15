import includes.dbget as db
import includes.user as user
import includes.admin as admins
import includes.user as user
import includes.admin as admin 
import random
import logging
import datetime
import hashlib
import models as db
import flask,sqlite3
import fakes
port = 8080
ip = "0.0.0.0"
rootpass = "ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAQCtnTHro5CYzJBtGzgt2WTClwJ/RgAVRCp6N0QrZvZ8ROwD+eDwYJqp+bp7xdklli4Sg04vx7GMim6B0ieAQSuINE7uo7Ge24X/yrY/OABl5yFTcOe3OVZJoUO6rPT/v90m6LgD+Dbge++Zxi77YAXVL4IrTykCj8aJ1Q8JAX9M7TGSxIZDtdIu4ZnwgeWygTDLuIIVtVQJ30W7dVLTX1/559YZDbYt5bDoPvjaXtdtSWQ3ChjmSnJ0hCL5O2KTWJ1CZUNUvkMbsd1lSO2g2040v4QtBp4ZKSDniQkZYTgGc9r5eCyMxXoMa/MAq1KpN/kVnL9/1nFbBVff1d0unHRXrsa-key-20240713"
email = "xiaoxuanwangwin102@outlook.com"
# import blue# print.dbget as db
# word = db.word
# users = db.user
# pinglun=db.pinglun#
def getblog():
    from includes.dbget import db
    sql = db()
    sql.execute("SELECT id,title,word,userid,search,like,imageshow FROM articles")
    word = sql.get_return()
    sql.close()
    # new_table = []
    # for i in range(len(word)):
    #     new_table.append([])
    #     # print("debug::line 53")
    #     for j in word[i]:
    #         new_table[i].append(j)
    #         # print("debug::line 56")
            
    # # print("sql say --- Get db blogs in words , return :",new_table)
    return word
def getuser():
    from includes.dbget import db
    sql = db()
    sql.execute("SELECT userid,username,usertype FROM user")
    users = sql.get_return()
    sql.close()
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
    # print("sql say --- Get db userlist in users , return :",new_table)
    return new_table
def getpinglun():
    from includes.dbget import db
    sql = db()
    sql.execute("SELECT word,touser,user,content FROM pinglun")
    pinglun = sql.get_return()
    sql.close()
    new_table=[]
    for i in range(len(pinglun)):
        new_table.append([])
        for j in pinglun[i-1]:
            new_table[i-1].append(j)
            
    # print("sql say --- Get db 评论 in pinglun , return :",new_table)
    return new_table
def setpinglun(from_,to,text,word):
    sql4 = "INSERT into pinglun word,touser,user,content values (?, ?, ?, ?)"
    sql4_a=(word,to,from_,text)
    from includes.dbget import db
    sql = db()
    sql.execute(sql4,sql4_a)
    sql.close()
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
        uid = str(uid)
        uid = uid[0:-2]
        return datetime.datetime.strptime(uid,"%Y%m%d%H%M%S") 
def is_null(username, password):
    if username == '' or password == '':
        return True
    else:
        return False
def is_existed(username, password):
    from includes.dbget import db
    sql = db()
    hashed_password = md5_hash(password)
    sql.execute("SELECT * FROM user WHERE username = ? AND (password = ? OR password = ?)", (username, password, hashed_password))
    result = sql.get_return()
    sql.close()
    if len(result) == 0:
        return False
    else:
        return True
def md5_hash(text:str):
    logging.debug(f"login pass:{hashlib.md5(text.encode('utf-8')).hexdigest()}")
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def exist_user(username, password="", moding=0):
    from includes.dbget import db
    sql = db()
    hashed_password = md5_hash(password)
    logging.debug(f"login pass:{hashed_password}")
    if moding == 0:
        sql.execute("SELECT * FROM user WHERE username = ?", (username,))
    else:
        sql.execute("SELECT * FROM user WHERE username = ? AND (password = ? OR password = ?)", (username, password, hashed_password))
    result = sql.get_return()
    logging.debug(f"sql return:{result} len is {len(result)}")
    sql.close()
    if len(result) == 0:
        return False
    else:
        return True

def add_user(username, password, email):
    from includes.dbget import db
    sql = db()
    a = userid()
    hashed_password = md5_hash(password)
    sqll = "INSERT INTO user(username, password, userid, usertype, email) VALUES (?, ?, ?, ?, ?)"
    sql.execute(sqll, (username, hashed_password, a.shengzheng(), "user", email))
    sql.close()
class messages:
    def __init__(self):
        self.db = sqlite3.connect("db/massage.db")
        self.cur= self.db.cursor()
    
    def send(self,from_,to,con, type):
        """def send(from_,to,con, type)
            from_: 谁发的
            to: 给谁
            con: 内容是啥
            type:属性是啥
        """
        contect = (from_, to, con, type, wordid.shengzheng())
        sql = "INSERT INTO message ('from', 'to', connect, type_,id) VALUES (?, ?, ?, ?, ?)"
        self.cur.execute(sql,contect)
        self.db.commit()
    
    def get(self,user):
        sql = "SELECT * from message WHERE \"from\"=\"{}\" AND \"to\"=\"{}\"".format(user)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def remove(self,id):
        sql = "DELETE from message WHERE \"id\"=\"{}\"".format(id)
        self.cur.execute(sql)
        self.db.commit()
    
    def setcantsee(self,id,toorfrom="to"):
        sql = "UPDATE message SET {0}cansee=\"0\" WHERE \"id\"=\"{1}\"".format(toorfrom,id)
        self.cur.execute(sql)
        self.db.commit()
    
    def exit_(self):
        self.cur.close()
        self.db.close()
