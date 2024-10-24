import math
def w(n):
    a = 1.0
    for i in range(1, n + 1):
        a *= (4 * i**2) / (4 * i**2 - 1)
    return 2 * a

n = 100000
pi = w(n)
print("приближенное значение pi с использованием", n ,"членов:" ,pi)