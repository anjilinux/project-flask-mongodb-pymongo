from flask import Blueprint
from mongo.mongo import mongo 
import json
from bson import json_util
from bson.objectid import ObjectId
getbyid = Blueprint("getbyid",__name__)

@getbyid.route("/details/<string:id>")
def home(id):
	query = mongo.db.colpizza.find_one({"_id":ObjectId(id)})
	return json.dumps(query,default=json_util.default)