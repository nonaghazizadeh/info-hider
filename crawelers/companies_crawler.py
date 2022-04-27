import json
import requests
from bs4 import BeautifulSoup
import re
from hazm import *

companies = []
url = "http://ircreative.isti.ir/contents.php?cntid=112"
url2 = "http://ircreative.isti.ir/contents.php?cntid=853"
f = requests.get(url)
soup = BeautifulSoup(f.content, 'html5lib')
rows = soup.findAll("tbody")[0].findAll('tr')
for i in range(2, len(rows)):
    row = rows[i]
    text = row.findAll('td')[1].text
    text = text.replace('شرکت', '')
    text = text.replace('موسسه', '')
    text = text.replace('سازمان', '')
    companies.append(text)
f2 = requests.get(url2)
soup2 = BeautifulSoup(f2.content, 'html5lib')
rows2 = soup2.findAll("tbody")[0].findAll('tr')
for i in range(2, len(rows2)):
    row = rows2[i]
    companies.append(row.findAll('td')[1].text)

international_companies = []
url3 = "https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D8%B1%DA%A9%D8%AA%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%DB%8C%DB%8C"
f3 = requests.get(url3)
soup3 = BeautifulSoup(f3.content, 'html5lib')
divs = soup3.findAll('div', {'id': 'mw-content-text'})
links = divs[0].findAll('ul')[0]
for i in links.findAll('a'):
    text = i.getText()
    text = text.replace('شرکت', '')
    text = text.replace('موسسه', '')
    text = text.replace('سازمان', '')
    international_companies.append(text)

all_companies = companies + international_companies
normalized_companies = list()
normalizer = Normalizer()
for i in all_companies:
    normalized_companies.append(normalizer.normalize(i))

file = open('../data/companies.json', 'w')
json.dump(normalized_companies, file, indent=3)
file.close()
