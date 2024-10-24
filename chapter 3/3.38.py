print("Введите номер карты:")
n = str(input())
n = n.replace(" ", "")
if len(n) == 16:
    print("True")
else:
    print("False")