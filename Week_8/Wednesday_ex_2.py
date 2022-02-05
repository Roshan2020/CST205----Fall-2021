##############################################################################################################
# Example for JSON Object
##############################################################################################################
import json

with open('cs_people.json') as f:
    data = json.load(f)

# print(data['people'][0]['firstName'])

for person in data['people']:
  print(f'{person["firstName"]}', end='')
  print(f' {person["lastName"]} ', end='')
  print('is a famous Computer Scientist.')