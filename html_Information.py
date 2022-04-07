import requests

import re

from bs4 import BeautifulSoup


def name_of_course(link, year, season):
    l = link + '/' + str(year) + season + '/'
    response = requests.get(l).text
    document = BeautifulSoup(response)
    section = document.find('section', {'class': 'main-content'})
    ul = section.find('ul')
    ul_in_ul = ul.find_all('ul')
    list = []
    for i in range(len(ul_in_ul)):
        list.extend(ul_in_ul[i].find_all('li'))
    names = []
    for i in range(len(list)):
        names.append(list[i].find('a').text)
    return names


def class_of_animal(link, animal):
    l = link + '/' + animal
    response = requests.get(l).text
    document = BeautifulSoup(response)
    table = document.find('table')
    td = table.find('td', {'class': 'plainlist'})
    div = td.find_all('div', {'class': 'ts-Taxonomy-rang-row'})
    for i in range(len(div)):
        d = div[i].find_all('div')
        if d[0].text == 'Класс:':
            return d[1].text


def link_from_wikipedia(link):
    global s

    ans = ''
    while len(s) != 100 and link not in s:
        response = requests.get(link).text
        document = BeautifulSoup(response)
        p = document.find('p')
        span = p.find('span')
        a2 = []
        if span:
            a2 = span.find_all('a')
        a = p.find_all('a')
        reg = re.compile(r'\(.*\)')
        languages = []
        if re.findall(reg, str(p)):
            for elem in re.findall(reg, str(p)):
                x = BeautifulSoup(elem[1: len(elem) - 1])
                languages.extend(x.find_all('a'))
        for elem in a:
            if elem not in a2 and elem not in languages:
                reg2 = re.compile(r'/wiki/.[^\s]*')
                ans = 'https://ru.wikipedia.org' + re.findall(reg2, str(elem))[0]
                s.add(link)
                s.add(ans)
                link_from_wikipedia(ans)
    return ans


link = 'http://students.iposov.spb.ru'
year = 20
season = 'spring'
print(name_of_course(link, year, season))
wiki = 'https://ru.wikipedia.org/wiki'
animal = 'Зебры'
print(class_of_animal(wiki, animal))
s = set()
link_wiki = 'https://ru.wikipedia.org/wiki/%D0%9E%D1%81%D1%8C%D0%BC%D0%B8%D0%BD%D0%BE%D0%B3%D0%B8'
print(link_from_wikipedia((link_wiki)))

