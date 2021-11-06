from flask import Flask
from routes.home import getdata
from routes.post import adddata
from routes.delete import deletedata
from routes.byid import getbyid
app = Flask(__name__)

app.register_blueprint(getdata)
app.register_blueprint(adddata)
app.register_blueprint(getbyid)
app.register_blueprint(deletedata)
