la = list()
i = 0

while True:
    n = int(input('Digite um valor '))
    la.append(n)
    i += 1

    cont = int(input('Quer continuar? \n1=sim \n2=nao '))
    if cont == 2: break

print(f'\nForam digitados {i} valores')
la.sort(reverse=True)
print(la)
if 5 in la:
    print(f'O cinco foi digitado')
