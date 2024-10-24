import sys
sys.setrecursionlimit(30000)
def f(x, n):
    if n == 0:
        return 1
    return x ** f(x, n - 1)
def c(n):
    return len(str(n))
r1 = f(3, 5)
r2 = f(5, 2)
print("3 5: ",c(r1))
print("5 2: ",c(r2))    