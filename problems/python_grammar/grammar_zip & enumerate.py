info1 = [1, 2, 3, 4]
info2 = [4, 3, 2, 1]

for idx, (one, two) in enumerate(zip(info1, info2)):
    print(idx, one, two)