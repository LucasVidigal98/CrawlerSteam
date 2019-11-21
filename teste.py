from bs4 import BeautifulSoup as BS
import requests
import json

req = requests.get('https://steamcommunity.com/app/730/reviews/?filterLanguage=default')
soup = BS(req.text, 'html.parser')
file = open('init.html', 'w')
file.write(req.text)
file.close()