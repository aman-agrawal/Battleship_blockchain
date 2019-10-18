from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/amandb"
mongo = PyMongo(app)

@app.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert({'name' : 'Cristina'})
    user_collection.insert({'name' : 'Derek'})