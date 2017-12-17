l = list(range(10))
for x in l[:]:
    print(x)
    if x == 8:
        l.remove(8)
