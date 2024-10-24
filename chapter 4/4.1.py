def s(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def v(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]
def sm(a, b, c):
    return s(a, v(b, c))
def vm(a, b, c):
    return v(a, v(b, c))
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print("скалярное произведение: ",s(a, b))
print("векторное произведение: ",v(a, b))
print("скалярное смешанное произведение: ",sm(a, b, c))
print("векторное смешанное произведение: ",vm(a, b, c))