print("введите число: ")
a=int(input())
print("выберете операцию (1 - килобайты в байты, 2 - байты в килобайты)")
b=str(input())
if b=='1':
    print(a*1024)
elif b=='2':
    print(a/1024)
else:
    print("не туда")