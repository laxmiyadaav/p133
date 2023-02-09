# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def index():

    name = "laxmi" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def father():

    name = "alex" # write your name
    age = "44" # write your age

    return render_template('father.html' , new_name = name , new_age = age)

# define the route to mother webpage
@app.route("/")
def mothet():

    name = "jenefar" # write your name
    age = "34" # write your age

    return render_template('mothet.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/")
def friend():

    name = "lax" # write your name
    age = "14" # write your age

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
