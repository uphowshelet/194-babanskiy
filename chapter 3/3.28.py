import math
a = 6378137.0
c = 6356752.314245
e2= 1 - (c**2 / a**2)
e = math.sqrt(e2)
b = 2 * math.pi * a**2 * (1 + ((1 - e2) / e) * math.atanh(e))

r = 6371000
s= 4 * math.pi * r**2

print(b - s)