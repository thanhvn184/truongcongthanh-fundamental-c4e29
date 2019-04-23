from flask import Flask, render_template, request

app = Flask(__name__)

bike =[]
@app.route('/new-bike', methods=["GET","POST"])
def new_bike():
    form = request.form
    # return render_template('newbike.html')
    if request.method == 'GET':
        return render_template('newbike.html')
    elif request.method == 'POST':
        form = request.form
        new_bike = {
            "model" : form['model'],
            "fee" : form['fee'],
            "image" : form['image'],
            "year" : form['year']

        }
    bike.append(new_bike)
    print(new_bike)
    return "Done"


if __name__ == '__main__':
  app.run(debug=True)