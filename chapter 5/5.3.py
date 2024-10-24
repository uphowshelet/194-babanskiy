def f(p):
    b = 0
    s = 0
    m = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            d = p[j] - p[i]
            if d > m:
                m = d
                b = i
                s = j
    return b, s, m
p1 = [100, 120, 140, 160, 180, 200, 220]
p2 = [200, 180, 220, 160, 240, 260, 210]
p3 = [250, 230, 210, 190, 170, 150, 130]
p4 = [200, 200, 200, 200, 200, 200, 200]
p5 = [150, 160, 155, 170, 180, 175, 165]
print(f(p1))
print(f(p2))
print(f(p3)
print(f(p4))
print(f(p5))