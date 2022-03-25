import string


def set_of_string(s):
    return set(s)


def new_string(s, m):
    ans = ''
    for elem in s:
        if elem not in m:
            ans += elem
    return ans


def list_of_words(s):
    punct = string.punctuation
    s = s.split()
    ans = []
    for elem in s:
        elem = elem.strip(punct)
        ans.append(elem)
    return ans


def set_of_common_words(s1, s2):
    set1 = set(list_of_words(s1))
    set2 = set(list_of_words(s2))
    ans = []
    for elem in set1:
        if elem in set2:
            ans.append(elem)
    return (ans)


def set_of_common_words_2(s1, s2):
    set1 = set(list_of_words(s1.lower()))
    set2 = set(list_of_words(s2.lower()))
    ans = []
    for elem in set1:
        if elem in set2:
            ans.append(elem)
    return ans


with open('text.txt', mode='r', encoding='utf-8') as f:
    str1= f.read()
    print(set_of_string(str1))
    print(new_string(str1, {'я'}))
    print(list_of_words(str1))
    print(set_of_common_words(str1, 'я на солнышке лежу'))
    print(set_of_common_words_2(str1, 'я на солнышке лежу'))
