from flask import Flask, request, render_template
app = Flask(__name__)

'''
@app.route("/")
def hello_world():
   return 'Hello World'


@app.route("/profile/<username>")
def profile(username):
   return '<h2>Hey there %s</h2>' % username


@app.route("/profile/int:profileID")
def profile1(profileID):
   return '<h2>Hey there %s</h2>' % profileID


@app.route("/bacon")
def bacon():
   return 'this is %s' % request.method


@app.route("/req", methods=['GET','POST'])
def req():
   if request.method == 'POST':
      return "You are using POST"
   else:
      return "You are using GET"
'''


@app.route("/")
@app.route("/<username>")
def index(username=None):
    return render_template("profile.html", name=username)


@app.route("/shopping")
def shopping():
    food_items = ["apple", "cheese" , "icecream"]
    return render_template("shopping.html", food=food_items)


# @app.route('/')
# @app.route('/<username>')
# def index(username=None):
#     return render_template('profile.html', name=username)


# @app.route('/getTime')
# def getTime():
#     print('serverTime : ', time.strftime('%A %B, %d %Y %H:%M:%S'));
#     return 'Done'



if __name__ == '__main__':
    app.run()
