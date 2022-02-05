# Lab 10
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
#################################################################################################################

#################################################################################################################
# Task 3
#################################################################################################################
import requests, json
from pprint import pprint

my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
  'api_key': my_key,
}

endpoint = 'https://api.nasa.gov/planetary/apod'


try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
except:
    print('please try again')