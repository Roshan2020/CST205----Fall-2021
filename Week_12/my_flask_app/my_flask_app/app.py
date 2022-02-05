from flask import Flask, render_template
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
  return render_template('index.html', 
                            my_data = my_info)

@app.route('/page2')
def p2():
  return render_template('page2.html')

@app.route('/page3/<mood>')
def p3(mood):
  return render_template('page3.html', mood=mood)
