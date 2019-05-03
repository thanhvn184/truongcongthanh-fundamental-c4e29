from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb+srv://admin:admin@thanhvn184-l6olc.mongodb.net/test?retryWrites=true"

# 1. Create Collection
client = MongoClient(uri)

# 2. Get / Create database
first_db = client.first_database

# 3. Get / Create collection
first_clt = first_db["first_collection"]

# 4. Create document
first_document = {
    "game": "Dota",
    "description": "moba",

}

game_list = [
    {
        "game": "hung bia",
        "description": "hot",
    },
    {
        "game": "DevilMayCry",
        "description": "hack&slash"
    }

]
# 5. Create
# 5a. Create one

# first_clt.insert_one(first_document)

# 5b. Create nany

# first_clt.insert_many(game_list)


# 6. Read
# 6a. Read all
# all_game = first_clt.find()

# # Lazy loading...
# for game in all_game:
#     print(game)
# 6b. Read one
# dmc_game = first_clt.find_one({'_id': ObjectId('5cc05e794697ba4ce3b0ab29')})
# print(dmc_game)

# 7. Update
dmc_game = first_clt.find_one({'_id': ObjectId('5cc05e794697ba4ce3b0ab29')})
new_value = { "$set": { "game": "AUTO CHESS" } }
first_clt.update_one(dmc_game, new_value)
print(dmc_game)

# 8.Delete
dmc_game = first_clt.find_one({'_id': ObjectId('5cc05e794697ba4ce3b0ab29')})
first_clt.delete_one(dmc_game)
