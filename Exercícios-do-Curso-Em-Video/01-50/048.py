n = 0
cont = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        n += c
        cont += 1
print(n, cont)
