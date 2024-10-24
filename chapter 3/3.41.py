def n(pos, dir, word):
    row = ord(pos[0]) - ord('A')
    col = int(pos[1:]) - 1
    if dir == 'horizontal':
        return col + len(word) <= 15
    elif dir == 'vertical':
        return row + len(word) <= 15
print("Введите слово")
word = str(input())
print("координата")
poss = str(input())
print('horizontal or vertical')
dirr = str(input())
print(n(poss, dirr, word))