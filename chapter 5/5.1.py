s = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
f = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]
a = sorted(s + f, key=lambda x: x.lower())
print(a)