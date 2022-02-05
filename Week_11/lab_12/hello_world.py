# Lab 12
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
# Note: create a “Hello World” Flask application (without templates)
#######################################################################
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# create an instance of Flask
app = Flask(__name__) 

########################################################################
# Task 4
########################################################################
bootstrap = Bootstrap(app)

########################################################################
# Task 2
########################################################################
# route decorator binds a function to a URL
#@app.route('/')
#def intro():
#    return '<p>Roshan M.A. : CDC (Centers for Disease Control and Prevention)</p>'

########################################################################
# Task 3
########################################################################
#@app.route('/roshan') 
#def t_test():
#    return render_template('template.html')

########################################################################
# Task 4
########################################################################
@app.route('/roshan') 
def t_test():
    return render_template('template1.html')