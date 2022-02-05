# File Name: Monday Ex 2
# hello_flask.py
# Description: Creating a home page + 'welcome' page
###########################################################
from flask import Flask
# create an instance of Flask
app = Flask(__name__) 
# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2