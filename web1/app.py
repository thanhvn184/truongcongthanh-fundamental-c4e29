from flask import Flask, render_template
app = Flask(__name__)


foods = [
    {
        "Title": "Thịt chó",
        "Description": "Rất ngon",
        "Link": "https://i.ytimg.com/vi/OjKbjN_vfjo/maxresdefault.jpg",
        "Type": "eat"
    },
    {
        "Title": "Bún chả",
        "Description": "Obama rất thích",
        "Link": "https://beptruong.edu.vn/wp-content/uploads/2018/05/bun-cha.jpg",
        "Type": "eat"
    },
    {
        "Title": "Nem rán",
        "Desccription": "Hương vị của mùa xuân",
        "Link": "https://znews-photo.zadn.vn/w860/Uploaded/tmuitg/2018_09_19/_MG_8898.JPG",
        "Type": "eat"
    },
    {
        "Title": "Coke",
        "Description": "Ngọt, có ga",
        "Link": "https://cdn.shopify.com/s/files/1/2432/1939/products/Share_A_Coke_with_Barak_Michelle_1024x1024.jpg?v=1525648384",
        "Type": "drink",
    },    
    {
        "Title": "Nước lọc",
        "Description": "Thanh mát",
        "Link": "https://kangaroovietnam.vn/Uploads/resize_nuoc-loc-de-duoc-bao-20150924091821370.png",
        "Type": "drink",
    }                 
]
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

    return render_template('food.html', foods = foods)   

@app.route('/food/<int:index>')
def detail(index):
    food_detail = foods[index]
    return render_template('food_detail.html', food_detail = food_detail)

if __name__ == '__main__':
  app.run(debug=True)

  


