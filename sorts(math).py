def partition(h, p, r):
    q = p
    for i in range(p, r):
        if h[i] <= h[r]:
            h[q], h[i] = h[i], h[q]
            q += 1
    h[q], h[r] = h[r], h[q]
    return q


def quicksort(a, p, r):
    if p >= r:
        return a
    else:
        s = partition(a, p, r)
        quicksort(a, p, s - 1)
        quicksort(a, s + 1, r)
        return (a)


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c = c + a[i:] + b[j:]
    return c


def merge_sort(a):
    if len(a) == 1:
        return a
    m = len(a) // 2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])
    return merge(l, r)


def selection_sort(a, n):
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        z = a[i]
        j = i
        while j > 0 and z < a[j - 1]:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = z
    return a


def counting_kol(li, lenght, maximum):
    ans = [0] * maximum
    for i in range(lenght):
        ans[li[i]] += 1
    return ans


def counting_sort(a):
    m = max(a) + 1
    n = len(a)
    kol = counting_kol(a, n, m)
    j = 0
    for i in range(m):
        index = kol[i]
        while index != 0:
            a[j] = i
            index -= 1
            j += 1
    return a


l = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print(quicksort(l, 0, 9))
l = [6, 5, 4, 1, 8, 2, 4, 3]
print(merge_sort(l))
l = [1, 2, 3, 6, 7, 8, 4, 5, 4]
print(selection_sort(l, 9))
l = [7, 10, 2, 8, 3]
print(insertion_sort(l))
l = [4, 3, 0, 2, 3, 1, 4, 2]
print(counting_sort(l))
