# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Zac" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
name = "Dad"
age = "60"
# define the route to mother webpage
name = "Mum"
age = "58"
# define the route to friends webpage


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
