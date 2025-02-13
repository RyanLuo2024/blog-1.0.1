import flask,config,hashlib,os
from includes.dbget import db
hash_object = hashlib.md5()
api = flask.Blueprint('api', __name__)
@api.route("/api/setmineimage",methods=['POST','GET'])
def setmineimage():
    if (flask.request.method == 'POST') :
        im = flask.request.form["image"]
        im = "."+im
        cookie = flask.request.cookies.get("cookieid")
        # image = Image.open(im)
        # resized_image = image.resize((80, 80))
        # resized_image.save(im)
        sql = db()
        sql.execute("UPDATE user SET image = ? WHERE username = ?",(im, cookie, ))
        sql.close()
        return flask.render_template(config.htmls.index)
    return flask.render_template(config.htmls.auth.setimage)
    
@api.route("/api/setadmin",methods=['POST','GET'])
def settings():
    if (flask.request.method == 'POST' and flask.request.cookies.get("cookieid")):
        sql = db()
        sql.execute("UPDATE user SET usertype=\"admin\" WHERE username=?;" , (flask.request.form["username"]))
        sql.close()
        return flask.render_template(config.htmls.index)
    elif flask.request.method=='GET' and flask.request.cookies.get("cookieid"):
        return flask.render_template(config.htmls.settings)
    
@api.route("/api/get/userimage",methods=['GET'])
def api_get_userimage():
    import models
    cookie = flask.request.cookies.get("cookieid")
    flag=True
    image = "static/image/touxiang.png"
    if (cookie==None) :flag = False
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    list = sql.get_return()
    sql.close()
    if (flag):
        for i in list:
            if cookie == i[1]:
                if(i[3] != None) :image = i[3]
    data = {"type":"200","data":{"image":"/"+image}}
    return flask.jsonify(data)

@api.route("/api/get/userimage/<user>",methods=['GET'])
def api_get_userimage_user(user):
    import models
    cookie = user
    flag=True
    image = "static/image/touxiang.png"
    if (cookie==None) :flag = False
    sql = db()
    sql.execute("SELECT userid,username,usertype,image FROM user")
    list = sql.get_return()
    sql.close()
    if (flag):
        for i in list:
            if cookie == i[1]:
                if(i[3] != None) :image = i[3]
    data = {"type":"200","data":{"image":"/"+image}}
    return flask.jsonify(data)

@api.route("/api/post/editormd_uplaodimg",methods=['POST'])
def editormd_uplaodimg():
    f = flask.request.files.get('editormd-image-file')
    if not f:
        result = {
            'success':0,
            'message':'上传失败'
        }
    else:
        basepath = os.path.dirname(__file__)
        # print('uploading '+f.filename+'... ')
        hash_object.update(b"1")
        upload_path = os.path.join(basepath, 'static/uploads',hash_object.hexdigest()+f.filename)
        f.save(upload_path)
        result = {
            'success':1,
            'message':'上传成功!',
            'url':"/static/uploads/"+hash_object.hexdigest()+f.filename
        }
    return result

@api.route("/api/post/massage/setmassage",methods=['POST'])
def api_setmassage():
    from_ = flask.request.cookies.get("cookieid")
    to    = flask.request.form["to"]
    con   = flask.request.form["con"]
    type_ = "other"
    import models
    cls = models.messages()
    cls.send(from_,to,con,type_)
    cls.exit_()
    return flask.jsonify({"type":"200","data":{}})

@api.route("/api/get/massage/getmassage",methods=['GET'])
def api_getmassage():
    user = flask.request.cookies.get("cookieid")
    import models
    cls = models.messages()
    list = cls.get(user)
    cls.exit_()
    newlist = []
    for i in list:
        if (i[0] == user and i[5] == "1"):
            newlist.append(i)
        elif i[1] ==user and i[6] == "1":
            newlist.append(i)
        else:
            pass
    data = {
        "type":"200",
        "data":{
            "list":newlist
        }
    }
    return flask.jsonify(data)

@api.route("/api/post/massage/setmassagecannotsee",methods=['POST'])
def api_setmassagecannotsee():
    user = flask.request.cookies.get("cookieid")
    type_= flask.request.form["who"]
    import models
    cls = models.messages()
    cls.setcantsee(user,type_)
    cls.exit_() 
    data = {
        "type":"200",
        "data":{}
    }
    return flask.jsonify(data)

@api.route('/api/get/download_uplaodfile/<filename>')
def download_file(filename):
    basepath = os.path.dirname(__file__)
    return flask.send_from_directory(
        os.path.join(basepath, '../static/uploads', 
                     flask.request.cookies.get("cookieid")
                    ), 
        filename, as_attachment=True
        )

@api.route('/api/get/delete_uplaodfile/<filename>')
def delete_file(filename):
    basepath = os.path.dirname(__file__)
    try:
        os.remove(os.path.join(os.path.join(basepath, '../static/uploads', 
                        flask.request.cookies.get("cookieid")
                        ), filename))
    except:pass
    return flask.redirect('/upload')