def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def f(r, w):
    n = len(w)
    p = [1] * n
    for _ in range(r - max(w)):
        s = sum(w) + n
        for i in range(n):
            p[i] *= (w[i] + 1) / s
    f = [round(p[i] * 10000) for i in range(n)]
    g = f[0]
    for x in f[1:]:
        g = gcd(g, x)
    return [x // g for x in f]

print(f(3, [2, 1]))
print(f(5, [1, 1, 2]))