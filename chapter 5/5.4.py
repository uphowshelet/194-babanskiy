def f(i, w):
    n = len(i)
    d = [[0] * (w + 1) for _ in range(n + 1)]
    for j in range(1, n + 1):
        for k in range(1, w + 1):
            if i[j - 1][0] <= k:
                d[j][k] = max(d[j - 1][k], d[j - 1][k - i[j - 1][0]] + i[j - 1][1])
            else:
                d[j][k] = d[j - 1][k]
    return d[n][w]

i1 = [(2, 10), (3, 15), (5, 30)]
w1 = 5
i2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
w2 = 10
i3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
w3 = 7
i4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
w4 = 7
i5 = [(6, 10), (8, 15), (12, 30)]
w5 = 5
print(f(i1, w1))
print(f(i2, w2))
print(f(i3, w3))
print(f(i4, w4))
print(f(i5, w5))