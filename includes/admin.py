import includes.user as user
class Admin(user.User):
    def   __init__():
        type = "admin"
        admin= True
        quanxian = {
            "delword":1,
            "writeword":1,
            "editword":1,
            "delpinglun":1,
            "writepinglun":1
        }
class Root(user.User):
    def   __init__():
        type = "root"
        root = True
        quanxian = {
            "delword":1,
            "writeword":1,
            "editword":1,
            "delpinglun":1,
            "writepinglun":1,
            "writemsg":1,
            "minecraftserverbackin":1
        }