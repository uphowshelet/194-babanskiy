def f(s):
    n = len(s)
    r = 2 ** n - 1
    return r

s1 = {"rose", "jasmine", "lily"}
s2 = {"orchid", "tulip", "violet", "daisy"}
s3 = {"lavender", "sunflower"}
print(f(s1))
print(f(s2))
print(f(s3))