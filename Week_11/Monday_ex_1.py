# File Name: Monday Ex 1
# hello_flask.py
# Description: Creating a home page
###########################################################
from flask import Flask
# create an instance of Flask
app = Flask(__name__) 
# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'Hello world from Flask!'