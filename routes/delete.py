from flask import Blueprint
from mongo.mongo import mongo 
import json
from bson.objectid import ObjectId
from bson import json_util
deletedata = Blueprint("deletedata",__name__)

@deletedata.route("/delete/<string:id>",methods=["DELETE"])
def add(id):
	query = mongo.db.colpizza.delete_one({"_id":ObjectId(id)})
	return "success delete id : " + id