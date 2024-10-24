print("сколько чисел вы хотите ввести?")
c = int(input())
print("Введи числа")
m=[]
for i in range(c):
    b=int(input())
    m.append(b)
maxx = max(m)
otv = []
for i in range(len(m)):
    otv.append(m[i] / maxx)
print(otv)
