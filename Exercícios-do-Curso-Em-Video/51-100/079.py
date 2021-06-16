la = list()

while True:
    n = int(input('\nDigite um valor '))
    if n not in la:
        la.append(n)
        print(f'O valor {n} foi adicionado com sucesso')
    else:
        print(f'O valor {n} ja existe')

    r = int(input('Quer continuar? 1=sim 2=nao '))
    if r == 2: break

la.sort()
print(f'Voce digitou os seguintes valores {la}')
