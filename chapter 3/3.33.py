def fac(n):
    r = 1
    for i in range(n, 0, -2):
        r *= i
    return r
num = [7, 8]
for i in num:
    res =fac(i)
    print(i,"!!=", res)