from flask import Flask
from routes.api import api
from routes.auth import auth
from routes.blog import blog
from routes.others import others
import time
import config
app = Flask(__name__)

app.config['LOG_FILE'] = 'logs/'+time.strftime("%Y_%m_%d_%H.%M.%S")+'.log'
app.config['LOG_LEVEL'] = 'INFO'
app.register_blueprint(api,url_prefix="/")
app.register_blueprint(auth,url_prefix="/")
app.register_blueprint(blog,url_prefix='/')
app.register_blueprint(others,url_prefix="/")
app.run(
    debug=config.debug,
    host=config.host,
    port=config.port0
)