from random import randint as ri

comp = ri(0,10)
usr = ''
cont = 1

while usr != comp:
    usr = int(input('Qual numero o comp pensou? '))
    cont += 1
    if usr < comp:
        print('Mais... tente novamente')
    elif usr > comp:
        print('Menos... tente novamente')


print('\nPara beins')
print(f'Voce acertou em {cont} tentaivas')
