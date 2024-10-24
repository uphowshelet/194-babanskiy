print("введите расстояние в метрах: ")
mm=int(input())
print("введите расстояние в километрах: ")
km=float(input())
print("наименьшее расстояние:")
if (km*1000>mm):
    print("в метрах: ",mm)
else:
    print("в километрах: ",km)