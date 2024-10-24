import random
def f(n):
    if len(n) <= 3:
        return n
    m = list(n[1:-1])
    random.shuffle(m)
    return n[0] + ''.join(m) + n[-1]

def g(t):
    w = t.split()
    s = [f(x) for x in w]
    return ' '.join(s)
print("введите предложение: ")
t = input()
s = g(t)
print(s)