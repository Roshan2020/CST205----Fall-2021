from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json

app = Flask(__name__)
bootstrap = Bootstrap(app)


# better to replace this with your own key from https://api.nasa.gov/
my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
  'api_key': my_key,
  'start_date': '2019-4-3',
  'end_date': '2019-4-5'
}

endpoint = 'https://api.nasa.gov/planetary/apod'


@app.route('/')
def index():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template('nasa.html', data=data)