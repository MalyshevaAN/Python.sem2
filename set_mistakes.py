import string

from set1 import set_of_correct_words, list_of_words, wrong_words


def set_of_possible_words(s):
    ans = set()
    for i in range(len(s)):
        help1 = s[:i] + s[i + 1::]
        ans.add(help1)
    return ans


def plus_one_symbol(s):
    letters = string.ascii_lowercase
    ans = set()
    for i in range(len(s) + 1):
        for elem in letters:
            help2 = s[:i] + elem + s[i::]
            ans.add(help2)
    return ans


def transposition(s):
    ans = set()
    for i in range(len(s) - 1):
        help3 = s[:i] + s[i + 1] + s[i] + s[i + 2::]
        ans.add(help3)
    return ans


def correct_new_words(s):
    ans = set()
    l1 = set_of_possible_words(s)
    l2 = plus_one_symbol(s)
    l3 = transposition(s)
    dictionary = set_of_correct_words()
    l1 = l1 | l2 | l3
    for elem in l1:
        if elem in dictionary:
            ans.add(elem)
    return ans


def correct_mistakes():
    with open('text2.txt', mode='r', encoding='utf-8') as f, open('correct_mistakes.txt', mode='w',
                                                                  encoding='utf-8') as j:
        s = f.read().split()
        dictionary = set_of_correct_words()
        text = list_of_words()
        ww = wrong_words(dictionary, text)
        for elem in s:
            if elem in ww:
                print('!', elem, correct_new_words(elem), file=j)


print(set_of_possible_words('ccat'))
print(plus_one_symbol('at'))
print(transposition('hello'))
print(correct_new_words('at'))
correct_mistakes()
