def f(k1):
    k2 = k1 + 1
    n = 1
    while True:
        a = n * k1
        b = n * k2
        if sorted(str(a)) == sorted(str(b)):
            return n
        n += 1
print(f(100))
print(f(325))  