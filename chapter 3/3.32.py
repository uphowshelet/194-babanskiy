def h(string_1, string_2):
    d = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            d += 1
    return d
print(h("hello", "hoiir"))
