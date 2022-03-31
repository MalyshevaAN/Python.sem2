def graph(f, m=1, n=10):
    for i in range(m, n + 1):
        print(f"f({i}) = {f(i)}")


def funct(x):
    return 5 * x


def eat(*a):
    for elem in a:
        if type(elem) is int and elem % 2 == 0:
            return 'ok'
    return ('I like evens')



def repeat(**a):
    ans = []
    for elem in list(a):
        for i in range(a[elem]):
            ans.append(elem)
    return ans


if __name__ == '__main__':
    function1 = lambda x: x ** 2
    graph(function1, 10, 20)
    print()
    graph(funct)


    print(eat(11, 33, 55, 10, 77, 99))
    print(eat(11, 33, 55, 77, 99, '12'))


    print(repeat(hello = 2, I = 3, am = 2, Nastia = 4))