from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return "hi this is me"
@app.route('/about-me')
def about_me():
    
    about_me = {
    "Name": "Trương Công Thành",
    "Work": "Student",
    "School": "National Economics University",
    "Hobbies": "play videos game, reading books, listening to music",
    "Crush": "Far from me",
    }
    return render_template('aboutme.html', about_me=about_me)
@app.route('/school')
def school():
  return redirect("http://techkids.vn", code=302)




if __name__ == '__main__':
  app.run(debug=True)