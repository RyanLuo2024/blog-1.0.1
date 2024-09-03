from flask import Flask, render_template, request
from flask_basicauth import BasicAuth
from flask_socketio import SocketIO
import paramiko
import config
app = Flask(import_name=__name__,
            static_url_path='/static',    # 配置静态文件的访问url前缀
            static_folder='static',       # 配置静态文件的文件夹
            template_folder='templates')  # 配置模板文件的文件夹
basic_auth = BasicAuth(app)
app.config['SECRET_KEY'] = "abcdef"
app.config['BASIC_AUTH_USERNAME'] = config.Root_UserName
app.config['BASIC_AUTH_PASSWORD'] = config.Root_Password
socketio = SocketIO(app)


def ssh_cmd():
    tran = paramiko.Transport(('127.0.0.1', 22,))
    tran.start_client()
    tran.auth_password('ryan', '12345678')
    chan = tran.open_session()
    chan.get_pty(height=492, width=1312)
    chan.invoke_shell()
    return chan


sessions = ssh_cmd()


@app.route("/")
@basic_auth.required
def index():
    return render_template("web.htm")


@socketio.on("message", namespace="/ws")
def socket(message):
    """接收到前端message消息，执行此方法"""
    print(f"接收到消息: {message}")
    sessions.send(message)  # 传到服务器上执行
    ret = sessions.recv(4096)
    socketio.emit(
        "response",
        {"data": ret.decode("utf-8")},
        namespace="/ws"
    )


@socketio.on("connect", namespace="/ws")
def connect():
    """当websocket连接成功时,自动触发connect默认方法"""
    ret = sessions.recv(4096)
    socketio.emit(
        "response",
        {"data": ret.decode("utf-8")},
        namespace="/ws")
    print("链接建立成功..")


@socketio.on("disconnect", namespace="/ws")
def disconnect():
    """当websocket连接失败时,触发disconnect默认方法"""
    print("链接建立失败..")


if __name__ == '__main__':
    socketio.run(
        app,
        debug=config.debug,
        host=config.host,
        port=config.port1,
        allow_unsafe_werkzeug=True
    )

