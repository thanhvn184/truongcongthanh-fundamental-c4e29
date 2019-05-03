from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@thanhvn184-l6olc.mongodb.net/test?retryWrites=true"


client = MongoClient(uri)


food_db = client.food_database
Foods = food_db["food_collection"]
