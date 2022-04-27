import json
import requests
from bs4 import BeautifulSoup
import re
from hazm import *
from static.enums import CrawlUrl, Path


def first_name_crawler(url):
    f_firstname = requests.get(url)
    soup_firstname = BeautifulSoup(f_firstname.content, 'html5lib')
    divs_tags = soup_firstname.findAll('div', {'class': 'column-count-۶'})
    first_names_list = list()
    for i in range(len(divs_tags)):
        for j in divs_tags[i].findAll('li'):
            first_names_list.append(re.sub("[\(\[].*?[\)\]]", "", j.getText()))
    return first_names_list


def last_name_crawler(url):
    last_names_list = list()
    while True:
        f_lastname = requests.get(url)
        soup_lastname = BeautifulSoup(f_lastname.content, 'html5lib')
        last_names_li_tags = soup_lastname.find_all('div', {'id': 'mw-pages'})[0].find_all('li')
        for last_name in last_names_li_tags:
            text = last_name.find("a").get_text()
            if not "(نام)" in text:
                last_names_list.append(last_name.find("a").get_text().split(" (")[0])
        links = soup_lastname.find_all('div', {'id': 'mw-pages'})[0].find_all("a", href=True)
        end = True
        for link in links:
            if link.get_text() == 'صفحهٔ بعدی':
                url = CrawlUrl.BASE_URL.value + link['href']
                end = False
                break
        if end:
            break
    del last_names_list[-1]
    return last_names_list


def normalize_names(names_list):
    normalizer = Normalizer()
    normalized_names_list = list()
    for name in names_list:
        normalized_names_list.append(normalizer.normalize(name))
    return normalized_names_list


def write_to_file(names_list, path):
    file = open(path, 'w')
    json.dump(names_list, file)
    file.close()


write_to_file(normalize_names(first_name_crawler(CrawlUrl.FIRST_NAME_URL.value)), Path.FIRST_NAME_PATH_WRITE.value)
write_to_file(normalize_names(last_name_crawler(CrawlUrl.LAST_NAME_URL.value)), Path.LAST_NAME_PATH_WRITE.value)
