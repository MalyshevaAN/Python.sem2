import string


def set_of_correct_words():
    with open('words_alpha.txt', mode='r', encoding='utf-8') as f:
        s = set(f.read().split())
    return s


def list_of_words():
    punct = string.punctuation
    with open('text2.txt', mode='r', encoding='utf-8') as j:
        s = j.read().split()
        ans = []
        for elem in s:
            for i in elem:
                if i in punct:
                    elem = elem.strip(punct)
            ans.append(elem)
        return ans


def wrong_words(dictionary, text):
    ans = []
    for elem in text:
        if elem.lower() not in dictionary:
            ans.append(elem)
    return ans

if __name__ == "__main__":

    a = set_of_correct_words()
    b = list_of_words()
    print(' '.join(map(str, wrong_words(a, b))))
    print(b)
    with open('wrong_words.txt', mode='w', encoding='utf-8') as m:
        print(' '.join(map(str, wrong_words(a, b))), file=m)
