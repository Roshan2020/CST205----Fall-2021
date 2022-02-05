# Homework 4
# Course: CST205
# Time: Fall 2021
# Date: 15-Nov.-2021
# School: CSUMB
# Team: 795
# Team Members: Arthur, Daniel & Dylan
# Author: Roshan Indika Menik Arachchi Menik Arachchige
# Description: Using Flask and Bootstrap Flask, create a web application for a small, random image gallery.
#################################################################################################################
import sys
import random

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from PIL import Image
from image_info import image_info

app = Flask(__name__, static_folder="static")
bootstrap = Bootstrap(app)


@app.route('/')
# def home():
#   choices = []
#   random.shuffle(image_info)
#   choices.append(image_info[:3])
#   return render_template('hw4_main.html', my_data=choices)
def home():  
	list = []
	for i in range(0, 3):
		random_image = (random.choice(image_info))
		if(i > 0):
			for selected in list:
				if(selected['id'] == random_image['id']):
					while(selected['id'] == random_image['id']):
						random_image = (random.choice(image_info))
		list.append(random_image)

	return render_template('hw4_main.html', images=list)

@app.route('/pictures')
@app.route('/pictures/<id>')
def pic(id):
  loc = "static/images/" + id + ".jpg"
  img = Image.open(loc)

  title = request.args.get('title')
  user = request.args.get('user')
  mode = img.mode
  form = img.format
  width, height = img.size
  return render_template('hw4_pg1.html', id=id, title=title, user=user, mode=mode, form=form, width=width, height=height)
