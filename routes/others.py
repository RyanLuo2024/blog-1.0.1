import models,os,hashlib,flask,datetime,sqlite3
from fakes import*
from better_profanity import profanity
import json
import config,addheimindan
from includes.dbget import db
from bs4 import BeautifulSoup
from flaskext.markdown import Markdown
others = flask.Blueprint('others', __name__)
def get_db_connection():
    db_,conn = db().return_cursour()
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

@others.route("/mepost/<user>/search",methods=['GET'])
def post3(user):
    from includes.dbget import db
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['/'] == False: 
        return "您已被封禁，无法经行该操作"
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    users = sql.get_return()
    sql.close()
    lists = models.getblog()
    userid=""
    image=""
    for i in users:
        if i[1] == user:
            userid=i[0]
            image=i[3]
            break
    
    if userid == "":
        return flask.render_template(config.htmls.error)
    posts = []
    for i in lists:
        if (i[3] == user):
            posts.append(i)
    # print(posts)
    blog_list = posts
    for i in range(len(blog_list)):
        # print(json.loads(blog_list[i][4])["list"])
        # print(flask.request.form["search"] in json.loads(blog_list[i][4])["list"])
        if str(flask.request.form["search"]) in json.loads(blog_list[i][4])["list"]:
            lists.append(blog_list[i])
    import models
    cookie = flask.request.cookies.get("cookieid")
    flag=True
    image = "/static/image/touxiang.png"
    if (cookie==None) :flag = False
    blog =lists
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    users = sql.get_return()
    sql.close()
    if (flag):
        for i in list:
            if cookie == i[1]:
                if(i[3] != None) :image = i[3]
    # print(lists)
    # return flask.render_template(config.htmls.blog.blog, posts=lists, username=cookie)

    return flask.render_template(config.htmls.blog.blog, posts=lists, username=flask.request.cookies.get("cookieid"))

"""http://host:port/ 主页"""
@others.route("/")
def index():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['/'] == False: 
        return "您已被封禁，无法经行该操作"
    page = 1
    wordonepage = 4
    try:
        page = flask.request.form["page"]
    except:
        pass
    import models
    cookie = flask.request.cookies.get("cookieid")
    blog = models.getblog()
    # blog = blog[((page - 1) * 4):(page * 4 - 1)]
    return flask.render_template(config.htmls.blog.blog, posts=blog, username=cookie, search_show=True)

"""http://host:port/uplaod 上传文件"""
hash_object = hashlib.md5()
@others.route('/upload', methods=['POST', 'GET'])
def upload():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['upload'] == False: 
        return "您已被封禁，无法经行该操作"
    basepath = os.path.dirname(__file__)
    if flask.request.method == 'POST':
        flag = False
        id = None
        try:
            id = flask.request.form["id"]
        except:
            pass
        f = flask.request.files['file']
        hash_object.update(b"11451411010103920829567876543234567898767865432345678765434567876543456")
        hash_object.update(b"13437r047jgfuri5tky5hjtgr8f9io4kt5thjue985iko4htu8i9knjuh98tkihgjrgnhjg")
        hash_object.update(b"13437r047jgfuri5tky5hjtgr8f9io4kt5thjue985iko4htu8i9knjuh98tkihgjrgnhjg")

        if not os.path.exists(os.path.join(basepath, '../static/uploads', flask.request.cookies.get("cookieid"))): 
            os.mkdir(os.path.join(basepath, '../static/uploads', flask.request.cookies.get("cookieid")))
        upload_path = os.path.join(basepath, '../static/uploads',flask.request.cookies.get("cookieid"),hash_object.hexdigest()+f.filename)
        f.save(upload_path)
        if flag == False:
            return """
            <h1>上传成功</h1>
            文件路径：/static/uploads/"""+flask.request.cookies.get("cookieid")+"/"+hash_object.hexdigest()+f.filename+"   请注意复制"
        else:
            data = {
                "moding":"200",
                "data":{
                    "url": "/static/uploads/"+hash_object.hexdigest()+f.filename
                }
            }
    files = os.listdir(os.path.join(basepath, '../static/uploads', 
                     flask.request.cookies.get("cookieid")
                    ),)
    return flask.render_template(config.htmls.upload,username=flask.request.cookies.get("cookieid"), files=files)
 
"""http://host:port/me/<user> 我的 ###cookie###"""
@others.route("/me/<user>")
def me(user):
    if (user=="None" or user == "") :return flask.redirect(flask.url_for("user_login"))
    import models
    cookie = flask.request.cookies.get("cookieid")
    isme = False
    if (cookie == user) :isme = True
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    users = sql.get_return()
    sql.close()
    lists = models.getblog()
    userid=""
    for i in users:
        if i[1] == user:
            userid=i[0]
            break
    
    if userid == "":
        return flask.render_template(config.htmls.error)
    posts = []
    for i in lists:
        if (i[3] == user):
            posts.append(i)
    # print(posts)
    cenghu = "Ta"
    fengjing=""
    x =  flask.request.cookies.get("cookieid")
    a = models.getuser()
    if (user == x):
        cenghu = "您"
    if (addheimindan.get(user) != False):
        fengjing = cenghu+"已被加入黑名单！"
    # print(x)
    for i in a:
        if (i[1]==x):
            return flask.render_template(config.htmls.blog.me,userid=i[0], username_show=i[1],
                                         cenghu=cenghu, fengjing=fengjing,posts=posts,
                                         username=flask.request.cookies.get("cookieid"),
                                         isme = isme)
    return ""

@others.route("/search",methods=['GET'])
def search():
    if (flask.request.method == 'GET'):
        import models
        blog_list=models.getblog()
        user_ = flask.request.cookies.get("cookieid")
        a=""
        lists = []
        import jieba
        search_query = flask.request.args.get("search")
        if search_query:
            cut = jieba.lcut(search_query)
            for i in range(len(blog_list)):
                if search_query in json.loads(blog_list[i][4])["list"]:
                    lists.append(blog_list[i])
        import models
        cookie = flask.request.cookies.get("cookieid")
        flag=True
        image = "/static/image/touxiang.png"
        if (cookie==None) :flag = False
        blog =lists
        sql = db()
        sql.execute("SELECT userid,username,usertype,image FROM user")
        list = sql.get_return()
        sql.close()
        if (flag):
            for i in list:
                if cookie == i[1]:
                        if(i[3] != None) :image = i[3]
        # print(lists)
        return flask.render_template(config.htmls.blog.blog, posts=lists, username=cookie, search_show=True)

@others.route("/about")
def about():
    return flask.render_template(config.htmls.about,yunying=config.RB,beian=config.ICP, username=flask.request.cookies.get("cookieid"))

