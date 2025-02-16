import flask,models,config,re
auth = flask.Blueprint('auth', __name__)
"""http://host:port/login 登录 ###cookie###"""
@auth.route('/user_login',methods=['GET','POST'])
def user_login():
    if flask.request.method=='POST':  # 注册发送的请求为POST请求
        username = flask.request.form['username']
        password = flask.request.form['password']
        if models.is_null(username,password):
            login_massage = "温馨提示：账号和密码是必填"
            return flask.render_template(config.htmls.auth.login, message=login_massage)
        elif models.is_existed(username, password):
            response = flask.make_response(flask.render_template('index.html', username=username)) # 发出cookie
            username = flask.request.form["username"]
            response.set_cookie('cookieid', username, max_age=60*60*24*30)
            return response
        elif models.exist_user(username,password,moding=1):
            login_massage = "温馨提示：密码错误，请输入正确密码"
            return flask.render_template(config.htmls.auth.login, message=login_massage)
        else:
            login_massage = "温馨提示：不存在该用户，请先注册"
            return flask.render_template(config.htmls.auth.login, message=login_massage)
    return flask.render_template(config.htmls.auth.login)

"""http://host:port/regiser 注册 ###cookie###"""
@auth.route("/regiser",methods=["GET", 'POST'])
def register():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        email = flask.request.form['email']
        if models.is_null(username,password) or email == "":
            login_massage = "温馨提示：邮件、账号和密码是必填"
            return flask.render_template(config.htmls.auth.register, message=login_massage)
        elif models.exist_user(username):
            login_massage = "温馨提示：用户名已存在"
            return flask.render_template(config.htmls.auth.register, message=login_massage)
        elif re.compile('^.*@.*\.[a-zA-Z][a-zA-Z0-9_]{1,3}$').match(email) == False:
            login_massage = "温馨提示：邮件地址不合法"
            return flask.render_template(config.htmls.auth.register, message=login_massage)
        else:
            models.add_user(flask.request.form['username'], flask.request.form['password'], email)
            return flask.redirect(flask.url_for('auth.user_login'))
    return flask.render_template(config.htmls.auth.register)

"""http://host:port/logout 退出登录 ###cookie###"""
@auth.route("/logout")
def logout():
    if (flask.request.cookies.get("cookieid") == None): return flask.redirect(flask.url_for("auth.user_login"))
    response = flask.make_response(flask.redirect(flask.url_for('auth.user_login')))
    response.delete_cookie('cookieid')
    return response
