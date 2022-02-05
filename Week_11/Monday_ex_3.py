# File Name: Monday Ex 3
# hello_flask.py
# Description: Creating a home page + 'welcome' page + 'mytemplate' page
##############################################################################
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# create an instance of Flask
app = Flask(__name__) 

boostrap = Bootstrap(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

#hello_flask.py
@app.route('/mytemplate')
def t_test():
    return render_template('template.html')