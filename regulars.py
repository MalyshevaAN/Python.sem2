import re


def email(s):
    em = re.compile(r'([a-z]|\d|_|-|)*@[a-z]+\.[a-z]{2,}')
    m = re.fullmatch(em, s)
    if m:
        return 'It is correct email'
    else:
        return 'email is not correct'


def email_regex(s):
    em2 = re.compile(
        r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
    m2 = re.fullmatch(em2, s)
    if m2:
        return 'It is correct email'
    else:
        return 'email is not correct'


def phone1(s):
    ans = []
    phone_number = re.compile(r'(\+?\d(|\s|\(|\)|-|){0,4}){7,10}')
    for m in re.finditer(phone_number, s):
        ans.append(m.group())
    return ans


def phone2(s):
    ans = []
    phone_number2 = re.compile(r'(\+?\d\s?-?\s?\(?\s?\)?\s?\s?-?\s?){7,10}')
    for m in re.finditer(phone_number2, s):
        ans.append(m.group())
    return ans


def tab(s):
    pattern = re.compile(r'\s,')
    text = re.split(pattern, s)
    ans = ','.join(map(str, text))
    return ans


def reverse(s):
    special_words = re.compile(r'([a-zA-Z]+)-([a-zA-Z]+)')
    for m in re.finditer(special_words, s):
        m1 = m.group(1) + '-'
        m2 = m.group(2)
        s = s.replace(m.group(2), m.group(1))
        s = s.replace(m.group(1), m.group(2), 1)
    return (s)


def change_plus_1(s):
    for m in re.findall(r'-?\d+', s):
        k = int(m) + 1
        s = s.replace(m, str(k))
    return s


print(email('_12 - anaste44s @ mail.com'))
print(phone1('my number is +4913 - (206) - 90, my second number is 94(128)130'))
print(phone2('my number is +4913 - (206) - 90, my second number is 94(128)130'))
print(tab('Это строка , у которой зачем-то написаны два пробела перед запятой'))
print(reverse('Kind-of green-blue grass'))
print(change_plus_1('У меня 2 яблока и -4 банана'))
