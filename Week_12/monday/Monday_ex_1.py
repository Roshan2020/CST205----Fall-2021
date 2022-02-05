# File Name: Monday Ex 1
# hello_flask.py
# Description: Creating a home page + 'page2' page + 'pg3 & mood' page
##############################################################################
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

my_info = {
  'days': ['sun', 'mon', 'tues'],
  'flavors': ['sweet', 'sour'],
  'colors': ['blue', 'green', 'brown']
}

@app.route('/')
def home():
  return render_template('index.html', v1='1', v2='2')

@app.route('/page2')
def page2func():
  return render_template('page2.html', my_list=my_info)

@app.route('/page3/<mood>')
def page3func(mood):
  return render_template('page3.html', mood=mood)