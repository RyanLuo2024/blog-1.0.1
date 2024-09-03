import main,models,os,hashlib,flask,blueprint,datetime
from fakes import*
from better_profanity import profanity
import json
import config
from bs4 import BeautifulSoup

"""wordid: 生成wordid，随机
   ├——wordid() -> class
   |  ├——shengcheng() -> str 生成id
   |  ├——jiexi() -> datetime.datetime() 解析uid
"""
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

"""http://host:port/post/<postid>: 文章查看"""
@main.app.route("/post/<postid>")
def post(postid):
    blog_list=models.getblog()
    for i in range(len(blog_list)):
        if postid == blog_list[i][0] or postid == str(blog_list[i][0]): 
            title=profanity.censor(blog_list[i][1])
            words=profanity.censor(blog_list[i][2])
            user =profanity.censor(blog_list[i][3])
            wordid =profanity.censor(blog_list[i][0])
            break
    return """
<html>
    <head>
        <link href="/static/css/quill.snow.css" rel="stylesheet">
        <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
        <link rel="stylesheet" href="/static/css/blogcss.css">
        <title>blog文章 - """+title+"""</title>
        <script src="/static/js/quill.js"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <header>
    		<a href="/">首页</a>
            <a href="/about">关于本站</a>
    	</header>
        <section>
            <!-- 背景颜色 -->
            <div class="color"></div>
            <div class="color"></div>
            <div class="color"></div>
            <div class="box">
                <!-- 背景圆 -->
                <div class="circle" style="--x:0"></div>
                <div class="circle" style="--x:1"></div>
                <div class="circle" style="--x:2"></div>
                <div class="circle" style="--x:3"></div>
                <div class="circle" style="--x:4"></div>
                <div class="container2">
                    <div class="form">
                        <div id="editor2">
                            <h1> """+title+"""</h1>
                            <h5> by - """+user+"""</h5>
                            <p> """+words+"""</p>
                            <a href="/removeword/"""+ wordid +""""><img src="/static/image/remove.png"></a>
                            <h6>本文id(wordid): """+ wordid +""" </h6>
                        </div>
                       <script>
                       var toolbarOptions = []
                       const quill = new Quill('#editor2', {
                        readOnly:true,
                        theme: 'snow',
                        modules: {
                            toolbar: toolbarOptions
                        },
                        });
                        </script>
                    </div>
                </div>
            </div>
        </section>
    </body>
</html>
    """

"""http://host:port/writeblog 写文章 ###cookie###"""
@main.app.route("/writeblog")
def writeblog():
    if (main.request.cookies.get("cookieid") == None): flask.redirect(flask.url_for("login"))
    return main.render_template("auth/blogwrite.html")

"""http://host:port/handle 处理文章 ###cookie###"""
@main.app.route('/handle', methods=['POST'])
def handle():
    title = main.request.form.get("title")
    word = main.request.form.get("content")
    print(title,word)
    id = wordid()
    import jieba
    word_search_list = jieba.cut_for_search(BeautifulSoup(word,"html").get_text())
    word_search_list = {"list":str(word_search_list)}
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    cursor.execute("insert into articles (title, word, id, userid,search) values (? , ?, ?, ?, ?)", (title ,word, id.shengzheng(), main.request.cookies.get('cookieid'), json.dumps(word_search_list)))
    db.commit()
    
    return main.render_template("index.html")

"""http://host:port/ 主页"""
@main.app.route("/")
def index():
    blog = models.getblog()
    return flask.render_template("blog/blog.html", posts=blog)

"""http://host:port/logout 退出登录 ###cookie###"""
@main.app.route("/logout")
def logout():
    response = flask.make_response(main.redirect(main.url_for('user_login')))
    response.delete_cookie('cookieid')
    return response

"""http://host:port/removeword/<wordid> 删除文章 ###cookie###"""
@main.app.route("/removeword/<wordid>")
def removeword(wordid):
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    response = main.request.cookies.get("cookieid")
    blog_list=models.getblog()
    if (response=="root"):
        cursor.execute("DELETE FROM articles WHERE id=?", (int(wordid),))
        db.commit()
        return main.render_template("index.html")
    for i in range(len(blog_list)):
        if response == blog_list[i][3] or response == str(blog_list[i][3]): 
            cursor.execute("DELETE FROM articles WHERE id=?", (int(wordid),))
            db.commit()
            return main.render_template("index.html")
    
    return """
<h1>你无权删除该文章！</h1>
"""

"""http://host:port/login 登录 ###cookie###"""
@main.app.route('/user_login',methods=['GET','POST'])
def user_login():
    if main.request.method=='POST':  # 注册发送的请求为POST请求
        username = main.request.form['username']
        password = main.request.form['password']
        if models.is_null(username,password):
            login_massage = "温馨提示：账号和密码是必填"
            return main.render_template('login.html', message=login_massage)
        elif models.is_existed(username, password):
            response = flask.make_response(main.render_template('index.html', username=username)) # 发出cookie
            username = flask.request.form["username"]
            response.set_cookie('cookieid', username, max_age=60*60*24*30)
            return response
        elif models.exist_user(username):
            login_massage = "温馨提示：密码错误，请输入正确密码"
            return main.render_template('login.html', message=login_massage)
        else:
            login_massage = "温馨提示：不存在该用户，请先注册"
            return main.render_template('login.html', message=login_massage)
    return main.render_template('login.html')

"""http://host:port/regiser 注册 ###cookie###"""
@main.app.route("/regiser",methods=["GET", 'POST'])
def register():
    if main.request.method == 'POST':
        username = main.request.form['username']
        password = main.request.form['password']
        if models.is_null(username,password):
            login_massage = "温馨提示：账号和密码是必填"
            return main.render_template('register.html', message=login_massage)
        elif models.exist_user(username):
            login_massage = "温馨提示：用户已存在，请直接登录"
            return flask.redirect(flask.url_for('user_login'))
            # return main.render_template('register.html', message=login_massage)
        else:
            models.add_user(main.request.form['username'], main.request.form['password'] )
            return flask.redirect(flask.url_for("/login"))
    return main.render_template('register.html')

"""http://host:port/uplaod 上传文件"""
hash_object = hashlib.md5()
@main.app.route('/upload', methods=['POST', 'GET'])
def upload():
    if main.request.method == 'POST':
        f = main.request.files['file']
        basepath = os.path.dirname(__file__)
        print('uploading '+f.filename+'... ')
        hash_object.update(b"1")
        upload_path = os.path.join(basepath, 'static/uploads',hash_object.hexdigest()+f.filename)
        f.save(upload_path)
        return """
        <h1>上传成功</h1>
        文件路径：/static/uploads/"""+hash_object.hexdigest()+f.filename+"   请注意复制"
    return main.render_template('upload.html')
 
"""http://host:port/change_password 改密码 ###cookie###"""
@main.app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if flask.request.method == 'POST':
        username = main.request.cookies.get('cookieid')
        old_password = flask.request.form['old_password']
        new_password = flask.request.form['new_password']
        import sqlite3
        try:
            db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
            cursor = db.cursor()
        except :
            try :
                db = sqlite3.connect("main.db", check_same_thread=False)
                cursor = db.cursor()
            except:raise Exception("db connet error")
        user = cursor.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()

        if user and user['password'] == old_password:
            cursor.execute('UPDATE user SET password = ? WHERE username = ?', (new_password, username))
            cursor.close()
            flask.flash('密码更新成功！')
        else:
            flask.flash('用户名或旧密码错误！')
        return flask.redirect(flask.url_for('change_password'))

    if (main.request.cookies.get('cookieid')!=""):
        return flask.render_template('change_password.html', users=main.request.cookies.get('cookieid'))
    else:
        return flask.render_template("login.html",message="请先登录")

"""http://host:port/change_password 我的 ###cookie###"""
@main.app.route("/me")
def me():
    x =  main.request.cookies.get("cookieid")
    a = models.getuser()
    print(x)
    if (x==None) :return flask.redirect(flask.url_for("user_login"))
    for i in a:
        if (i[1]==x):
            return main.render_template("blog/me.html",userid=i[0], username=i[1])
    return ""

""""""
@main.app.route("/about")
def about():
    a = ""
    return flask.render_template("about.html",yunying=config.RB,beian=config.ICP)

main.app.run(
    debug=config.debug,
    host=config.host,
    port=config.port1
)