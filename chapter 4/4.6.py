def f(n, k):
    x = 0
    while n >= k:
        n //= k
        x += n
    return x
n = 10
k = 2
r = f(n, k)
print("наибольшая степень",k," на которую делится", n,"!:" ,r)