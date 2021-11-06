from flask import Blueprint
from mongo.mongo import mongo 
import json
from bson import json_util
adddata = Blueprint("adddata",__name__)

@adddata.route("/add")
def add():
	query = mongo.db.colpizza.insert_one({"name":"pizza beef","price":12000,"like":2})

	return "data success add "