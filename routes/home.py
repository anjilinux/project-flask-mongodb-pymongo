from flask import Blueprint
from mongo.mongo import mongo 
import json
from bson import json_util
getdata = Blueprint("getdata",__name__)

@getdata.route("/")
def home():
	query = mongo.db.colpizza.find()
	data = [d for d in query]

	return json.dumps(data,default=json_util.default)