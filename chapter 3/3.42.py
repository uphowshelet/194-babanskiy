for i in range(1,999999):
    s=1
    s1=0
    for b in range(1,i):
       s*=b
    for b in str(s):
        s1+=int(b)
    if s%s1!=0:
        print(i)
        break