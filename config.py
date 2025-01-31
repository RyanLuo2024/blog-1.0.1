port0=5000
port1=8081
debug=True
host="0.0.0.0"
Root_Password="""ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAQCtnTHro5CYzJBtGzgt2WTClwJ/RgAVRCp6N0QrZvZ8ROwD+eDwYJqp+bp7xdklli4Sg04vx7GMim6B0ieAQSuINE7uo7Ge24X/yrY/OABl5yFTcOe3OVZJoUO6rPT/v90m6LgD+Dbge++Zxi77YAXVL4IrTykCj8aJ1Q8JAX9M7TGSxIZDtdIu4ZnwgeWygTDLuIIVtVQJ30W7dVLTX1/559YZDbYt5bDoPvjaXtdtSWQ3ChjmSnJ0hCL5O2KTWJ1CZUNUvkMbsd1lSO2g2040v4QtBp4ZKSDniQkZYTgGc9r5eCyMxXoMa/MAq1KpN/kVnL9/1nFbBVff1d0unHRXrsa-key-20240713"""
Root_UserName="xiaoxuanwangwin102@outlook.com"
ICP="null"
RB ="null"
dbfile = "db/main.db"
json_heimindan = "static/jsons/heimindan.json"
class auth:
    setimage  = "auth/setimage.html"
    login     = "auth/login.html"
    register  = "auth/register.html"
class blog:
    blogwrite = "blog/blogwrite.html"
    blog = "blog/blog.html"
    me   = "blog/me.html"
    word = "blog/word.html"

class htmls:
    auth  = auth()
    blog  = blog()
    about = "about.html"
    base  = "base.html"
    change_password = "change_password.html"
    error = "error.html"
    index = "index.html"
    settings="settings.html"
    upload= "upload.html"
    web   = "web.html"
