a = input().strip()
b = input().strip()
a = a.lower()
b = b.lower()
if a < b:
    c = -1
elif a > b:
    c = 1
else:
    c = 0
print(c)