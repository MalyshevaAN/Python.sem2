import string

def set_of_correct_words():
    with open('words_alpha.txt', mode = 'r', encoding = 'utf-8') as f:
        s = set(f.read().split())
    return s

def list_of_words():
    punct = string.punctuation
    with open('text2.txt', mode= 'r', encoding = 'utf-8') as j:
        s = j.read().split()
        helper = list(s)
        ans = []
        for elem in helper:
            for i in elem:
                if i in punct:
                    elem = elem.strip(i)
            ans.append(elem)
        return ans

def wrong_words(dictionary,text):
    with open('wrong_words.txt',mode = 'w',encoding = 'utf-8') as m:
        ans = []
        for elem in text:
            if elem.lower() not in dictionary:
                ans.append(elem)
                print(elem, file = m)
        return ans

a = set_of_correct_words()
b = list_of_words()
print(' '.join(map(str,wrong_words(a,b))))
