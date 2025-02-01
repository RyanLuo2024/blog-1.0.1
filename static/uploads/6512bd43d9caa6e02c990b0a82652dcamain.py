from flask import *
import os
from flask_basicauth import BasicAuth
import sqlite3
from werkzeug.utils import secure_filename
import time
import hashlib
from better_profanity import profanity
hash_object = hashlib.md5()
def connectdb():
	db = sqlite3.connect("word.db")
	cursor = db.cursor()
	return (db,cursor)

def closedb(db,cursor):
	db.close()
	cursor.close()


app = Flask(__name__)
ALLOW_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
app.config['UPLOAD_FOLDER'] = './static/images/'
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = """ssh-rsaAAAAB3NzaC1yc2EAAAADAQABAAABAQCtnTHro5CYzJBtGzgt2WTClwJ/RgAVRCp6N0QrZvZ8ROwD+eDwYJqp+bp7xdklli4Sg04vx7GMim6B0ieAQSuINE7uo7Ge24X/yrY/OABl5yFTcOe3OVZJoUO6rPT/v90m6LgD+Dbge++Zxi77YAXVL4IrTykCj8aJ1Q8JAX9M7TGSxIZDtdIu4ZnwgeWygTDLuIIVtVQJ30W7dVLTX1/559YZDbYt5bDoPvjaXtdtSWQ3ChjmSnJ0hCL5O2KTWJ1CZUNUvkMbsd1lSO2g2040v4QtBp4ZKSDniQkZYTgGc9r5eCyMxXoMa/MAq1KpN/kVnL9/1nFbBVff1d0unHRXrsa-key-20240713"""
basic_auth = BasicAuth(app)



#{
def blog_get():
    db,cursor = connectdb()
    sql = "SELECT id,title,content FROM easy_blog"
    cursor.execute(sql)
    new_table=[]
    p=cursor.fetchall()
    for i in range(len(p)):
        new_table.append([])
        for j in p[i-1]:
            new_table[i-1].append(j)
            
    print(new_table,p)
    return p
#}
#{
@app.route("/")
def blog():
    blog_list=blog_get()
    return render_template("blog.html",posts=blog_list)
#}
#{
@app.route("/post/<postid>")
def post(postid):
    blog_list=blog_get()
    for i in range(len(blog_list)):
        if postid == blog_list[i-1][0] or postid == str(blog_list[i-1][0]): 
            title=profanity.censor(blog_list[i-1][1])
            words=profanity.censor(blog_list[i-1][2])
            break
    n="""
<html>
    <head>
        <link href="/static/css/quill.snow.css" rel="stylesheet">
        <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
        <link rel="stylesheet" href="/static/css/blogcss.css">
        <title>blog文章 - """+title+"""</title>
        <script src="/static/js/quill.js"></script>
    </head>
    <body>
        <header>
    		<a href="/">首页</a>
    		<a href="/admin123" class="banner-link">管理员写文章地址（动不得）</a>
    	</header>
        <h1>"""+title+"""</h1>
        <p>"""+words+"""</p>
    </body>
</html>
    """
    print(n)
    return n
#}
@app.route("/delword/")
@basic_auth.required
def delword(wordid):
    db,cursor=connectdb()
    cursor.execute("DELETE FROM easy_blog WHERE title=?",wordid)
    db.commit()
    return redirect("/")


#{
#"/secret"路由：1号密码的路由

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        print('uploading '+f.filename+'... ')
        hash_object.update(b"1")
        os.system("/static/"+hash_object.hexdigest())
        upload_path = os.path.join(basepath, 'static/uploads',hash_object.hexdigest()+f.filename)
        f.save(upload_path)
        return """
        <h1>上传成功</h1>
        文件路径：/static/uploads/"""+hash_object.hexdigest()+f.filename
    return render_template('upload.html')
 

@app.route("/admin123")
@basic_auth.required
def gift():
    return render_template("admin123.html")
#}
#{
@app.route("/worldedit-mod-7.jar", methods=['GET'])
def download_file():
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file("files/worldedit-mod-7.jar")  
    #}

@app.route('/handle', methods=['POST'])
def handle():
	title = request.form.get("title")
	word = request.form.get("content")
	(db,cursor) = connectdb()
	print(title,word)
	cursor.execute("insert into easy_blog (title, content) values (? , ?)", (title ,word))
	db.commit()
	return redirect("/")

#{
@app.route("/minecraft")
def photo():
    #img = get_img()
    return render_template("minecraft.html")
#}

#"/me"路由
#{   
@app.route("/me")
def me():
    return render_template("me.html")
#}




app.run()