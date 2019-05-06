from flask import *
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
uri = "mongodb+srv://admin:admin@thanhvn184-l6olc.mongodb.net/test?retryWrites=true"


client = MongoClient(uri)
newbike_db = client.newbike_database
newbike_coll = newbike_db["new_bike"]



@app.route('/new-bike', methods=["GET","POST"])
def new_bike():
    form = request.form

    if request.method == 'GET':
        return render_template('new_bike.html')
    elif request.method == 'POST':
        form = request.form

        
        new_bike = {
            "model" : form["model"],
            "fee" : form["dailyfee"],
            "image" : form["image"],
            "year" : form["year"]

        }
        newbike_coll.insert_one(new_bike)
        return redirect("/new-bike")
    



if __name__ == '__main__':
  app.run(debug=True)