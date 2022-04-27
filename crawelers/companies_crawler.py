import json
import requests
from bs4 import BeautifulSoup
from hazm import *
from static.enums import Keywords, CrawlUrl, Path


def remove_pre_words(text):
    for keyword in Keywords.COMPANY_PRE_KEYWORDS.value:
        text = text.replace(keyword, '')
    return text


def iranian_companies_crawler(url):
    companies_list = list()
    f_iranian_companies = requests.get(url)
    soup_iranian_companies = BeautifulSoup(f_iranian_companies.content, 'html5lib')
    rows = soup_iranian_companies.findAll("tbody")[0].findAll('tr')
    for i in range(2, len(rows)):
        plain_text = remove_pre_words(rows[i].findAll('td')[1].text)
        companies_list.append(plain_text)
    return companies_list


def other_companies_crawler(url):
    companies_list = list()
    f_other_companies = requests.get(url)
    soup_other_companies = BeautifulSoup(f_other_companies.content, 'html5lib')
    divs = soup_other_companies.findAll('div', {'id': 'mw-content-text'})
    links = divs[0].findAll('ul')[0]
    for i in links.findAll('a'):
        plain_text = remove_pre_words(i.getText())
        companies_list.append(plain_text)
    return companies_list


def normalize_companies_names(names_list):
    normalizer = Normalizer()
    normalized_names_list = list()
    for name in names_list:
        normalized_names_list.append(normalizer.normalize(name))
    return normalized_names_list


def write_to_file(companies_names_list, path):
    file = open(path, 'w')
    json.dump(companies_names_list, file)
    file.close()


normalized_companies_names = normalize_companies_names(
    iranian_companies_crawler(CrawlUrl.IRANIAN_FIRST_COMPANY_URL.value) + iranian_companies_crawler(
        CrawlUrl.IRANIAN_SECOND_COMPANY_URL.value) + other_companies_crawler(CrawlUrl.OTHERS_COMPANY_URL.value))
write_to_file(normalized_companies_names, Path.COMPANIES_PATH_WRITE.value)
