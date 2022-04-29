import numpy as np


def task10_10(a=1, b=0):
    ans = np.array([[(a if j == 0 else b) for i in range(10)] for j in range(10)])
    return ans


def border(a=1, b=0):
    ans = np.array([[(a if j == 0 or j == 9 or i == 0 or i == 9 else b) for i in range(10)] for j in range(10)])
    return ans


def task5_5(a=2):
    ans = np.array([[a for i in range(5)] for j in range(5)])
    return ans


def task0_3():
    ans = np.array([[i // 5 if j < 5 else i // 5 + 2 for i in range(10)] for j in range(10)])
    return ans


def chess():
    ans = np.array([[(i + j) % 2 for i in range(10)] for j in range(10)])
    return ans


def lines1_9():
    ans = np.array([[j + 1 for i in range(9)] for j in range(9)])
    return ans


def task1_100():
    ans = np.array([[(10 * j + i + 1) for i in range(10)] for j in range(10)])
    return ans


def multiplication_table():
    ans = np.array([[(i + 1) * (j + 1) for i in range(9)] for j in range(9)])
    return ans


def task_3_diags(n, a, b):
    possible = [a, b]
    ans = np.array([[possible[abs(j - i)] if abs(j - i) <= 1 else 0 for i in range(n)] for j in range(n)])
    return ans


def double_chess():
    ans = np.array(
        [[1 if i % 4 >= 2 and j % 4 < 2 or i % 4 < 2 and j % 4 >= 2 else 0 for i in range(20)] for j in range(20)])
    return ans


def chukh(n):
    possibles = [1, 2]
    diag = [[possibles[i % 2] if i == j else 0 for i in range(n)] for j in range(n)]
    ans = np.array(
        [[possibles[i % 2] if i == j else diag[j][j] if i > j else diag[i][i] for i in range(n)] for j in range(n)])
    return ans
