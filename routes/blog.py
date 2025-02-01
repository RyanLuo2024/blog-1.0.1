import models,os,hashlib,flask,datetime,sqlite3
from fakes import*
from better_profanity import profanity
import json
import config,addheimindan
from includes.dbget import db
from bs4 import BeautifulSoup
from flaskext.markdown import Markdown
blog = flask.Blueprint('blog', __name__)
def get_db_connection():
    db_,conn = db().return_cursour()
    conn.row_factory = sqlite3.Row
    return conn
"""http://host:port/post/<postid>: 文章查看"""
@blog.route("/post/<postid>")
def post(postid):
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['post'] == False: 
        return "您已被封禁，无法经行该操作"
    blog_list=models.getblog()
    user_ = flask.request.cookies.get("cookieid")
    a=""
    # print(models.getpinglun())
    for i in range(len(blog_list)):
        if postid == blog_list[i][0] or postid == str(blog_list[i][0]): 
            title=profanity.censor(blog_list[i][1])
            words=md2html(profanity.censor(blog_list[i][2]))
            user =profanity.censor(blog_list[i][3])
            wordid =profanity.censor(blog_list[i][0])
            img =profanity.censor(blog_list[i][6])
            if user_ == user or user == "root":
                a ="""<a href="/removeword/"""+ wordid +""""><img src="/static/image/remove.png"></a>"""
            break
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM pinglun ').fetchall()
    pingl = []
    for i in comments:
        if (i[0]==" "+str(postid)+" "):
            pingl.append(i)
    # conn.close()
    # print(pingl)
    return flask.render_template(config.htmls.blog.word, comments=pingl, title=title, 
                                 words=words, user=user, a=a, wordid=wordid, 
                                 username=flask.request.cookies.get("cookieid"), img=img)

@blog.route('/add_comment', methods=['POST'])
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
    conn.execute('INSERT INTO pinglun (word, touser, user, content, like, dislike) VALUES (?, ?, ?, ?, ?, ?)',
                 (word, touser, user, content, "[]", "[]"))
    conn.commit()
    conn.close()
    return flask.redirect('/post/'+str(word.replace(" ","")))

"""http://host:port/writeblog 写文章 ###cookie###"""
@blog.route("/writeblog")
def writeblog():
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['writeblog'] == False: 
        return "您已被封禁，无法经行该操作"
    if (flask.request.cookies.get("cookieid") == None): flask.redirect(flask.url_for("user_login"))
    return flask.render_template(config.htmls.blog.blogwrite, username=flask.request.cookies.get("cookieid"))

"""http://host:port/handle 处理文章 ###cookie###"""
@blog.route('/handle', methods=['POST'])
def handle(): 
    if addheimindan.get(flask.request.cookies.get("cookieid")) != False and \
       addheimindan.get(flask.request.cookies.get("cookieid"))['quanxian']['handle'] == False: 
        return "您已被封禁，无法经行该操作"
    title = flask.request.form.get("title")
    word = flask.request.form.get("html")
    markdown = flask.request.form.get("markdown")
    dislike = like = "[]"
    id = wordid()
    import jieba
    word_search_list = jieba.lcut(BeautifulSoup(word,"html").get_text())
    # print(word_search_list)
    word_search_list = {"list":str(word_search_list)}
    sql = db()
    sql.execute(
"insert into articles (title,word,id,userid,search,markdown,like,dislike,imageshow) values (?,?,?,?,?,?,?,?,?)", 
    (title ,word, id.shengzheng(), flask.request.cookies.get('cookieid'), json.dumps(word_search_list), 
     markdown, like, dislike, "/static/image/blogtitilebg.png"))
    users = sql.get_return()
    sql.close()
    return flask.render_template(config.htmls.index, username=flask.request.cookies.get("cookieid"))

"""http://host:port/removeword/<wordid> 删除文章 ###cookie###"""
@blog.route("/removeword/<wordid>")
def removeword(wordid):
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    response = flask.request.cookies.get("cookieid")
    blog_list=models.getblog()
    if (response=="root"):
        sql.execute("DELETE FROM articles WHERE id=?", (int(wordid),))
        return flask.render_template(config.htmls.index,username=flask.request.cookies.get("cookieid"))
    for i in range(len(blog_list)):
        if response == blog_list[i][3] or response == str(blog_list[i][3]): 
            sql.execute("DELETE FROM articles WHERE id=?", (int(wordid),))
            return flask.render_template(config.htmls.index, username=flask.request.cookies.get("cookieid"))
    sql.close()
    return """
<h1>你无权删除该文章！</h1>
"""
