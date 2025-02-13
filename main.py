import logging
from flask import Flask, render_template, request
from flask_basicauth import BasicAuth
from flask_socketio import SocketIO
import paramiko
from logs import create_app, setup_log
from routes.api import api
from routes.auth import auth
from routes.blog import blog
from routes.others import others
from routes.massage import mail_blueprint
import config

ssh = Flask(
    import_name=__name__,
    static_url_path='/static',    # 配置静态文件的访问url前缀
    static_folder='static',       # 配置静态文件的文件夹
    template_folder='templates'   # 配置模板文件的文件夹
)
app = create_app("development", ssh)
basic_auth = BasicAuth(ssh)
app.config['SECRET_KEY'] = "abcdef"
app.config['BASIC_AUTH_USERNAME'] = config.Root_UserName
app.config['BASIC_AUTH_PASSWORD'] = config.Root_Password
socketio = SocketIO(ssh)
app.register_blueprint(api, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(blog, url_prefix='/')
app.register_blueprint(others, url_prefix="/")
app.register_blueprint(mail_blueprint, url_prefix='/mail')
def ssh_cmd():
    tran = paramiko.Transport(('127.0.0.1', 22,))
    tran.start_client()
    tran.auth_password('ryan', 'Ryan+123')
    chan = tran.open_session()
    chan.get_pty(height=492, width=1312)
    chan.invoke_shell()
    return chan

sessions = {}

@app.route("/ssh")
@basic_auth.required
def index():
    return render_template("web.htm")

@socketio.on("message", namespace="/ssh/ws")
def socket(message):
    """接收到前端message消息，执行此方法"""
    logging.info(f"接收到消息: {message}")
    sid = request.sid
    if sid in sessions:
        if isinstance(message, str):
            sessions[sid].send(message)  # 传到服务器上执行
            ret = sessions[sid].recv(4096)
            socketio.emit(
                "response",
                {"data": ret.decode("utf-8")},
                namespace="/ssh/ws"
            )
        else:
            logging.error("接收到的消息不是字符串类型")

@socketio.on("connect", namespace="/ssh/ws")
def connect():
    """当websocket连接成功时,自动触发connect默认方法"""
    sid = request.sid
    sessions[sid] = ssh_cmd()
    ret = sessions[sid].recv(4096)
    socketio.emit(
        "response",
        {"data": ret.decode("utf-8")},
        namespace="/ssh/ws"
    )
    logging.info("连接成功")

@socketio.on("disconnect", namespace="/ssh/ws")
def disconnect():
    """当websocket连接失败时,触发disconnect默认方法"""
    sid = request.sid
    if sid in sessions:
        sessions[sid].close()
        del sessions[sid]
    logging.debug("链接已断开")

@app.errorhandler(404)
def err404(message):
    return render_template("error.html",message=message)

@app.errorhandler(403)
def err403(message):
    return render_template("error.html",message=message)

@app.errorhandler(401)
def err401(message):
    return render_template("error.html",message=message)

@app.errorhandler(400)
def err400(message):
    return render_template("error.html",message=message)

@app.errorhandler(408)
def err408(message):
    return render_template("error.html",mmessage=message)

@app.errorhandler(429)
def err429(message):
    return render_template("error.html",message=message)


if __name__ == '__main__':
    socketio.run(
        app,
        debug=config.debug,
        host=config.host,
        port=config.port0,
        allow_unsafe_werkzeug=True
    )