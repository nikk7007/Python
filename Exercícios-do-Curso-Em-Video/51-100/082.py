la = list()
li = list()
lp = list()

while True:
    n = int(input('Digite um valor '))
    la.append(n)
    continuar = input('Deseja continuar? [s/n] ').strip().lower()
    if continuar == 'n': break

for i in la:
    if i % 2 == 0:
        lp.append(i)
    else:
        li.append(i)

print(f'A lista normal: {la}')
print(f'A lista com os pares: {lp}')
print(f'A lista com os impares: {li}')
