from abc import abstractproperty

tempdados = []
dados = []
maior = []
menor = []

while True:
    name = input('Nome: ').strip().title()
    peso = float(input('Peso: '))

    tempdados.append(name)
    tempdados.append(peso)
    dados.append(tempdados[:])

    if len(dados) == 1: 
        maior.append(tempdados[:])
        menor.append(tempdados[:])
    else:
        if peso > maior[0][1]:
            maior.clear()
            maior.append(tempdados[:])
        elif peso < menor[0][1]:
            menor.clear()
            menor.append(tempdados[:])

        elif peso == maior[0][1]:
            maior.append(tempdados[:])
        if peso == menor[0][1]:
            menor.append(tempdados[:])


    tempdados.clear()
    reuse = input('Quer continuar? s/n ').strip().lower()[0]
    if reuse == 'n':
        break

print(f'O programa rodou {len(dados)} vezes')
print('Os mais pesados são:')
for p in maior:
    print(f'{p[0]} com {p[1]}Kg')

print('E os mais leves:')
for p in menor:
    print(f'{p[0]} com {p[1]}Kg')
