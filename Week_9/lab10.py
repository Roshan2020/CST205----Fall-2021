# Lab 10
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
#################################################################################################################

#################################################################################################################
# Task 1
# API: ExchangeRate-API
# KEY: ea4e971dd6801a0b56602694
# Ex: https://v6.exchangerate-api.com/v6/ea4e971dd6801a0b56602694/latest/USD
# Description: This API contains a JSON object with exchange rates from your base currency. 
#              In other words, given a supplied base currency it will return the whole list of other currencies.
#################################################################################################################

#################################################################################################################
# Task 2
#################################################################################################################
import requests
from pprint import pprint

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/ea4e971dd6801a0b56602694/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)