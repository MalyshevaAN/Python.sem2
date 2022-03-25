import string


def replace(dictionary, s):
    l = [dictionary[elem] if elem in dictionary.keys() else elem for elem in s]
    ans = ''
    for elem in l:
        ans += elem
    return ans


def number_of_symbolls(s):
    a = {elem: 0 for elem in s}
    for elem in s:
        a[elem] += 1
    return a


def list_of_words(s):
    punct = string.punctuation
    helper = list(s.split())
    ans = []
    for elem in helper:
        for i in elem:
            if i in punct:
                elem = elem.strip(i)
        ans.append(elem)
    return ans


def number_of_words(s):
    a = list_of_words(s)
    ans = {word: 0 for word in a}
    for word in a:
        ans[word] += 1
    return ans


with open('text.txt', 'r', encoding='utf-8') as f, open('new.csv', 'w', encoding='Windows-1251') as g:
    s = f.read()
    s = s.lower()
    d = number_of_words(s)
    for key in d.keys():
        print(key, d[key], file=g, sep=';')
    print(number_of_symbolls(s))
    print(number_of_words(s))

d = {'a': 'xyz', 'b': '123'}
print(replace(d, 'abc'))
