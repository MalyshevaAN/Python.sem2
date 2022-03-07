def compute_lcs_table(x, y):
    m = len(x)
    n = len(y)
    l = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])

    return l


def assemble_lcs(x,y,l,i,j):
    if l[i][j] == 0:
        return ''
    elif  l[i][j] > 0 and x[i-1] == y[j-1]:
        return assemble_lcs(x,y,l,i-1,j-1) + x[i-1]
    elif  x[i-1] != y[j-1] and l[i-1][j] > l[i][j-1]:
        return assemble_lcs(x,y,l,i-1,j)
    elif x[i-1] != y[j-1] and l[i-1][j] <= l[i][j-1]:
        return assemble_lcs(x,y,l,i,j-1)


x = 'ABACDE'
y = 'EBDCE'
length = compute_lcs_table(x, y)
print(length)
m = len(x)
n = len(y)
print(length[m][n])
print(assemble_lcs(x, y, length, m, n))
