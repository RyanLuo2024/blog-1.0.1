import blueprint.user as user
import blueprint.admin as admin 
import random
import datetime
import models as db
import main,flask,markdown
from flaskext.markdown import Markdown
from jinja2.utils import markupsafe
# word = db.word
# users = db.users
# pinglun=db.pinglun

class userid():
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

def md2html(mdcontent):
	exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
	
	# with open(filename,'r',encoding='utf-8') as f:
	# 	mdcontent = f.read()
	# 	pass	
	html = markdown.markdown(mdcontent,extensions=exts)
	content = markupsafe.Markup(html)
	return content

