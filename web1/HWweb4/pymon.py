from flask import *
from pymongo import MongoClient
from bson.objectid import ObjectId


uri = "mongodb+srv://admin:admin@thanhvn184-l6olc.mongodb.net/test?retryWrites=true"


client = MongoClient(uri)
newbike_db = client.newbike_database
newbike_coll = newbike_db["new_bike"]