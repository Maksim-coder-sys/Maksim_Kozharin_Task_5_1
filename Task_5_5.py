
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

rez = set()
for i in src:
    if src.count(i) == 1:
        rez.add(i)



rezult = [x for x in src if x in rez]
print(rezult)