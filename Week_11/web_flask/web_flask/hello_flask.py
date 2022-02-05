from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/matthew')
def hello_world():
    print('in hello_world function')
    return 'hi there CST 205, courtesy of Matthew'

@app.route('/welcome') 
def wc():
    s1 = 'Welcome to my page! ' 
    s2 = 'Have a <b>nice</b> day!' 
    return s1 + s2

@app.route('/mytemplate') 
def t_test():
    return render_template('template.html')