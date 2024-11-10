import main,models,os,hashlib,flask,blueprint,datetime,sqlite3
from fakes import*
from better_profanity import profanity
import json
import config,addheimindan
from bs4 import BeautifulSoup
import PIL.Image as Image
"""wordid: 生成wordid，随机
   ├——wordid() -> class
   |  ├——shengcheng() -> str 生成id
   |  ├——jiexi() -> datetime.datetime() 解析uid
"""
def get_db_connection():
    conn = sqlite3.connect('main.db')
    conn.row_factory = sqlite3.Row
    return conn

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

@main.app.route("/mepost/<user>")
def post2(user):
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['/'] == False: 
        return "您已被封禁，无法经行该操作"
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    cursor.execute("SELECT userid,username,usertype,image FROM user")
    users = cursor.fetchall()
    lists = models.getblog()
    userid=""
    image=""
    for i in users:
        if i[1] == user:
            userid=i[0]
            image=i[3]
            break
    
    if userid == "":
        return flask.render_template("error.html")
    posts = []
    for i in lists:
        if (i[3] == user):
            posts.append(i)
    print(posts)
    return flask.render_template("blog/blog.html", posts=posts, image="/"+image, username=flask.request.cookies.get("cookieid"))

"""http://host:port/post/<postid>: 文章查看"""
@main.app.route("/post/<postid>")
def post(postid):
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['post'] == False: 
        return "您已被封禁，无法经行该操作"
    blog_list=models.getblog()
    user_ = flask.request.cookies.get("cookieid")
    a=""
    print(models.getpinglun())
    for i in range(len(blog_list)):
        if postid == blog_list[i][0] or postid == str(blog_list[i][0]): 
            title=profanity.censor(blog_list[i][1])
            words=profanity.censor(blog_list[i][2])
            user =profanity.censor(blog_list[i][3])
            wordid =profanity.censor(blog_list[i][0])
            if user_ == user or user == "root":
                a ="""<a href="/removeword/"""+ wordid +""""><img src="/static/image/remove.png"></a>"""
            break
    str_ =  """
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
                            <a href="/me/"""+user+""""> by - """+user+"""</a>
                            <p> """+words+"""</p>
                            """+a+"""
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
                        var vm = new Vue({
                        el: '#main-container',
                        data: {
                            textareaContent:'',
                            num: 200,
                        },
                        methods: {
                            monitorInput() {
                            var txtVal = this.textareaContent.length;
                            this.num = 200 - txtVal;
                            }
                        },
                        });
                        
                        </script>
                    </div>
                </div>
                <br>
                <div class="container3">
                    <div class="add">
                        <h1>添加评论</h1>
                        <form action="{{ url_for('add_comment') }}" method="post">
                            <script>
                            $(document).ready(function() {
                            // 设置最大字数限制
                            var maxChars = 400;

                            // 监听textarea的input事件
                            $('#content').on('input', function() {
                                var currentLength = $(this).val().length;
                                var remaining = maxChars - currentLength;
                                $('#remainingChars').text(remaining);
                            });
                            });
                            </script>
                            <input type="text" id="word" name="word" style="display: none;"  value=" """+wordid+""" "><br>
                            <input type="text" id="touser" name="touser" style="display: none;"><br>
                            <div><label for="content">评论:</label></div>
                            <textarea maxlength="400" @input="monitorInput" v-model="textareaContent" id="content" placeholder="写点东西吧..." name="content"></textarea>
                            <div>剩余字数：<span id="remainingChars">400</span></div>
                            <br>
                            <div><input type="submit" class="button" value="提交"></div>
                        </form>
                        <br>
                    </div>
                    <div class="clear"></div>
                </div>
                <br>
                <div class="container3">
                    <div class="list">
                        <h2>评论列表</h2>
                        <br>
                        {% for comment in comments %}
                        
                            <div class="cushy-box2">
                                <br style="font-size: 5px;">
                                <div class="pinguser">
                                    <strong>内容:</strong><br> {{ comment['content'] }}
                                </div>
                                <div class="pingtext" style="width: 700px;text-align: right;font-size:12px;">
                                    <strong>By - </strong> {{ comment['user'] }}
                                </div>
                                <br style="font-size: 5px;">
                            </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </section>
    </body>
</html>
    """
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM pinglun ').fetchall()
    pingl = []
    for i in comments:
        if (i[0]==" "+str(postid)+" "):
            pingl.append(i)
    # conn.close()
    print(pingl)
    return flask.render_template_string(str_, comments=pingl)

@main.app.route('/add_comment', methods=['POST'])
def add_comment():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['add_comment'] == False: 
        return "您已被封禁，无法经行该操作"
    conn = get_db_connection()
    word = flask.request.form['word']
    touser = flask.request.form['touser']
    user = flask.request.cookies.get("cookieid")
    if user=="" or user==None : return flask.redirect(flask.url_for('user_login'))
    content = flask.request.form['content']
    conn.execute('INSERT INTO pinglun (word, touser, user, content) VALUES (?, ?, ?, ?)',
                 (word, touser, user, content))
    conn.commit()
    conn.close()
    return flask.redirect(flask.url_for('index'))

"""http://host:port/writeblog 写文章 ###cookie###"""
@main.app.route("/writeblog")
def writeblog():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['writeblog'] == False: 
        return "您已被封禁，无法经行该操作"
    if (main.request.cookies.get("cookieid") == None): flask.redirect(flask.url_for("login"))
    return main.render_template("auth/blogwrite.html")

"""http://host:port/handle 处理文章 ###cookie###"""
@main.app.route('/handle', methods=['POST'])
def handle():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['handle'] == False: 
        return "您已被封禁，无法经行该操作"
    title = main.request.form.get("title")
    word = main.request.form.get("content")
    print(title,word)
    id = wordid()
    import jieba
    word_search_list = jieba.lcut(BeautifulSoup(word,"html").get_text())
    print(word_search_list)
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
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['/'] == False: 
        return "您已被封禁，无法经行该操作"
    import models
    cookie = flask.request.cookies.get("cookieid")
    flag=True
    image = "/static/image/touxiang.png"
    if (cookie==None) :flag = False
    blog = models.getblog()
    import sqlite3
    try:
        db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
        cursor = db.cursor()
    except :
        try :
            db = sqlite3.connect("main.db", check_same_thread=False)
            cursor = db.cursor()
        except:raise Exception("db connet error")
    cursor.execute("SELECT userid,username,usertype,image FROM user")
    list = cursor.fetchall()
    if (flag):
        for i in list:
            if cookie == i[1]:
                    if(i[3] != None) :image = i[3]
    return flask.render_template("blog/blog.html", posts=blog, image=image, username=cookie)

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
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['upload'] == False: 
        return "您已被封禁，无法经行该操作"
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
 
"""http://host:port/me/<user> 我的 ###cookie###"""
@main.app.route("/me/<user>")
def me(user):
    cenghu = "Ta"
    fengjing=""
    x =  main.request.cookies.get("cookieid")
    a = models.getuser()
    if (user == x):
        cenghu = "您"
    if (addheimindan.get(user) != False):
        fengjing = cenghu+"已被加入黑名单！"
    print(x)
    if (x==None) :return flask.redirect(flask.url_for("user_login"))
    for i in a:
        if (i[1]==x):
            return main.render_template("blog/me.html",userid=i[0], username=i[1],cenghu=cenghu, fengjing=fengjing)
    return ""

@main.app.route("/about")
def about():
    a = ""
    return flask.render_template("about.html",yunying=config.RB,beian=config.ICP)

@main.app.route("/setmineimage",methods=['POST','GET'])
def setmineimage():
    if (flask.request.method == 'POST') :
        im = flask.request.form["image"]
        im = "."+im
        cookie = flask.request.cookies.get("cookieid")
        image = Image.open(im)
        resized_image = image.resize((80, 80))
        resized_image.save(im)
        import sqlite3
        try:
            db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
            cursor = db.cursor()
        except :
            try :
                db = sqlite3.connect("main.db", check_same_thread=False)
                cursor = db.cursor()
            except:raise Exception("db connet error")
        cursor.execute("UPDATE user SET image = ? WHERE username = ?",(im, cookie, ))
        db.commit()
        return flask.render_template("index.html")
    return flask.render_template("auth/setimage.html")
    
@main.app.route("/setadmin",methods=['POST','GET'])
def settings():
    if (flask.request.method == 'POST' and flask.request.cookies.get("cookieid")):
        import sqlite3
        try:
            db = sqlite3.connect("/blueprint/main.db", check_same_thread=False)
            cursor = db.cursor()
        except :
            try :
                db = sqlite3.connect("main.db", check_same_thread=False)
                cursor = db.cursor()
            except:raise Exception("db connet error")
        sql = "UPDATE user SET usertype=\"admin\" WHERE username='%s';" % (flask.request.form["username"])
        cursor.execute(sql)
        db.commit()
        return flask.render_template("index.html")
    elif flask.request.method=='GET' and flask.request.cookies.get("cookieid"):
        return flask.render_template("settings.html")



main.app.run(
    debug=config.debug,
    host=config.host,
    port=config.port0
)