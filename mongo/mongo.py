from flask_pymongo import PyMongo
import os
from flask import Flask

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)