# Lab 11
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
# Note: Find a web page which contains at least one image. Use Beautiful Soup to grab the image URL
#####################################################################################################
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

my_site = 'https://www.nytimes.com/section/magazine'
page = requests.get(my_site)
soup = BeautifulSoup(page.text, 'lxml')
images = soup.findAll('img')
for image in images:
    print(image['src'])