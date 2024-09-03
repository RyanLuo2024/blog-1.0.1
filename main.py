from flask import Flask,render_template
from flask import redirect
from flask import url_for
from flask import request
import fakes
from blueprint.dbget import *
app = Flask(__name__)
from forms import *
