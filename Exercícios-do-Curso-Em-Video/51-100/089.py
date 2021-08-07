from os import system as s
s('cls')
dados = []
tempdados = []
cont = 0
nota = []

while True:
    name = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2 

    nota.append(nota1)
    nota.append(nota2)

    tempdados.append(name)
    tempdados.append(media)
    tempdados.append(nota[:])

    dados.append(tempdados[:])
    tempdados.clear()
    nota.clear()
    
    reuse = input('Quer continuar? [s/n] ').strip().lower()[0]
    if reuse == 'n': 
        s('cls')
        break

print(f'{"N°":<5}{"Nome":<10}{"Media":<5}')
print('-'*20)
for i in dados:
    cont += 1
    print(f'{cont:<5}{i[0]:<10}{i[1]:<5}')

while True:
    person = int(input('\nNota de quem voce quer ver? [0 para sair] '))
    if person == 0:
        break
    # print(f'As notas do {dados[0][0]} são {dados[person - 1][2]}')
    print(f'As notas do {dados[0][0]} são', end=' ')
    for i in dados[person - 1][2]:
        print(i, end=' / ')
    print()

s('cls')
