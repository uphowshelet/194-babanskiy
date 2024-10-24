a=[1,2,3]
p=[]
b=1
for i in a:
    b*=i
for i in a:
    p.append(b//i)
print(p)