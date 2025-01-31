import models,os,hashlib,flask,datetime,sqlite3
from fakes import*
from better_profanity import profanity
import json
import config,addheimindan
from includes.dbget import db
from bs4 import BeautifulSoup
from flaskext.markdown import Markdown

