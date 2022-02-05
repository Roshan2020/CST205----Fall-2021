import requests
from bs4 import BeautifulSoup

my_site='https://www.airnow.gov/?city=Monterey&state=CA&country=USA'
page = requests.get(my_site)
soup = BeautifulSoup(page.text, 'lxml')

my_ps = soup.find_all('p')

for p in my_ps:
   if p.text != '':
       print(p.text, '\n---\n')