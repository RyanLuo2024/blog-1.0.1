import json,config


def get(username):
    USERS = []
    with open(config.json_heimindan,"r") as px:
        USERS = json.loads(px.read())
        px.close()
    for i in USERS["list"]:
        if (i["username"] == username):
            return i
    
    return False

def add(username,unlocktime,qdisk={"post":True,
                                   "add_comment":True,
                                   "writeblog":True,
                                   "handle":True,
                                   "/":True,
                                   "uplaod":True}):
    disk = {"username":username,
            "unlocktime":unlocktime,
            "quanxian":qdisk}
    USERS = {"list":[]}
    with open(config.json_heimindan,"r") as px:
        USERS = json.loads(px.read())
        px.close()
    with open(config.json_heimindan,"w+",encoding="UTF-8") as px:
        for i in USERS["list"]:
            if i["username"] == username:
                i = disk
                break
        else:
            USERS["list"].append(disk)
        px.write(json.dumps(USERS))
        px.close()

def remove(username):
    USERS={"list":[{"username":"a"}]}
    with open(config.json_heimindan,"r") as px:
        USERS = json.loads(px.read())
        px.close()
    x=0
    for i in USERS["list"]:
        if i["username"] == username:
            USERS["list"].pop(x)
        x+=1
    with open(config.json_heimindan,"w") as px:
        px.write(json.dumps(USERS))

remove("b")