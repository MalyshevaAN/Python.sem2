import requests


from bs4.element import Tag

from bs4 import BeautifulSoup


def name_of_course(link, year, season):
    l = link + '/' + str(year) + season + '/'
    response = requests.get(l).text
    document = BeautifulSoup(response, features = 'html.parser')
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
    document = BeautifulSoup(response, features = 'html.parser')
    table = document.find('table')
    td = table.find('td', {'class': 'plainlist'})
    div = td.find_all('div', {'class': 'ts-Taxonomy-rang-row'})
    for i in range(len(div)):
        d = div[i].find_all('div')
        if d[0].text == 'Класс:':
            return d[1].text




def link_from_wikipedia(link, s,names):
    l = link
    if len(s) == 100 or l in s:
        return l
    else:

        response = requests.get(link).text
        document = BeautifulSoup(response, features='html.parser')
        div = document.find('div', {'class': 'mw-parser-output'})
        if not div:
            return l
        p = div.find('p', recursive=False)
        if not p:
            return l
        flag = 1
        for child in p.children:
            if '(' in str(child):
                flag = 0
            if ')' in str(child):
                flag = 1
            if flag == 1 and isinstance(child, Tag) and str(child).startswith('<a'):
                s.append(link)
                new = 'https://ru.wikipedia.org' + str(child.get('href'))
                names.append(str(child.get('title')))
                link_from_wikipedia(new, s, names)
                break
        return s[-1]



link = 'http://students.iposov.spb.ru'
year = 20
season = 'spring'
print(name_of_course(link, year, season))
wiki = 'https://ru.wikipedia.org/wiki'
animal = 'Зебры'
print(class_of_animal(wiki, animal))
s = []
names = []
link_wiki = 'https://ru.wikipedia.org/wiki/%D0%9E%D1%81%D1%8C%D0%BC%D0%B8%D0%BD%D0%BE%D0%B3%D0%B8'
print(link_from_wikipedia(link_wiki, s, names))
