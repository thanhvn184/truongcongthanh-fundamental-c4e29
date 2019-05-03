from flask import Flask, render_template, request, redirect
from bson.objectid import ObjectId
from food_db import Foods

app = Flask(__name__)

@app.route('/')
def index():
    return "hello c4e"

@app.route('/say-hi')
def say_hi():
    return "yo bitch"

@app.route('/say-hi/<name>')
def hi_thanh(name):
    return "xin chào {}".format(name)

@app.route('/add/<int:x>/<int:y>')
def add(x, y):  
    return str(x+y)

@app.route('/food')
def food():
    foods = Foods.find()
    return render_template('food.html', foods = foods)   

@app.route('/food/<id>')
def detail(id):
    food_detail = Foods.find_one({"_id": ObjectId(id)})
    return render_template('food_detail.html', food_detail = food_detail)
@app.route('/food/add_food', methods = ['GET', 'POST'])
def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        new_food = {
            "Title": form['title'],
            "Description": form['description'],
            "Link": form['Link'],
            "Type": form['Type'],
        }                 
        Foods.insert_one(new_food)
        print
        return redirect('/food')

@app.route('/food/edit/<id>', methods = ["GET", "POST"])
def edit_food(id):
    food = Foods.find_one({'_id': ObjectId(id)}) 
    if request.method == "GET": 
        return render_template('edit_food.html', food = food)
    elif request.method == "POST":
        form = request.form
        new_value = { "$set": {
            "Title": form["title"],
            "Description": form["description"],
            "Link": form["Link"],
            "Type": form["Type"]
        }}
        Foods.update_one(food, new_value)
        return redirect('/food')


@app.route('/food/delete/<id>')
def delete(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    Foods.delete_one(food)
    return redirect('/food')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        taikhoan ={
            "account": "c4e",
            "password": "c4e",
        }    
    form = request.form
    acc = form["acc"]
    pas = form["pass"]
    if acc != "c4e" and pas != "c4e":

        return "Wrong Accont and Password"
    elif acc == "c4e" and pas != "c4e":
        return "Wrong"    




    
if __name__ == '__main__':
  app.run(debug=True)

  


