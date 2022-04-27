import json
import requests
from bs4 import BeautifulSoup
import re
from hazm import *

url = f"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%86%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%DB%8C"
f = requests.get(url)
soup = BeautifulSoup(f.content, 'html5lib')
divs_tags = soup.findAll('div', {'class': 'column-count-۶'})
first_names_list = list()
for k in range(len(divs_tags)):
    for j in divs_tags[k].findAll('li'):
        first_names_list.append(re.sub("[\(\[].*?[\)\]]", "", j.getText()))

ln_url = "https://fa.wikipedia.org/w/index.php?title=%D8%B1%D8%AF%D9%87:%D9%86%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%AE%D8%A7%D9%86%D9%88%D8%A7%D8%AF%DA%AF%DB%8C&pageuntil=%D8%AA%D8%B1%DB%8C%D8%A7%D9%86#mw-pages"
last_names_list = list()
while True:
    f1 = requests.get(ln_url)
    soup1 = BeautifulSoup(f1.content, 'html5lib')
    last_name_part = soup1.find_all('div', {'id': 'mw-pages'})[0]
    last_names = last_name_part.find_all('li')
    for last_name in last_names:
        text = last_name.find("a").get_text()
        if not "(نام)" in text:
            last_names_list.append(last_name.find("a").get_text().split(" (")[0])
    all_links = last_name_part.find_all("a", href=True)
    end = True
    for link in all_links:
        if link.get_text() == 'صفحهٔ بعدی':
            ln_url = "https://fa.wikipedia.org" + link['href']
            end = False
            break
    if end:
        break
del last_names_list[-1]
normalized_first_name = list()
normalized_last_name = list()
normalizer = Normalizer()

for first_name in first_names_list:
    normalized_first_name.append(normalizer.normalize(first_name))

for last_name in last_names_list:
    normalized_last_name.append(normalizer.normalize(last_name))

file = open('../data/first_names.json', 'w')
json.dump(normalized_first_name, file, indent=3)
file.close()

file = open('../data/last_names.json', 'w')
json.dump(normalized_last_name, file, indent=3)
file.close()
