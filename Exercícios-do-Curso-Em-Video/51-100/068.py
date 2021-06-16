from random import randint

comp = randint(1,10)
cont = 0

print('='*30)
print('Vamos jogar par ou impar')
print('='*30)

while True:
    usr1 = input('Voce escolhe par ou impar [P/I]').lower()
    usr2 = int(input('Qual numero voce escolhe? '))
    soma = comp + usr2
    if usr1 == 'p':
        if soma % 2 == 0:
            print(f'Voce venceu! o computador escolheu {comp} e a soma foi {soma}')
            cont += 1
        else:
            print(f'Voce perdeu! o computador escolheu {comp} e a soma foi {soma}')
            break

    elif usr1 == 'i':
        if soma % 2 != 0:
            print(f'Voce venceu! o computador escolheu {comp} e a soma foi {soma}')
            cont += 1
        else:
            print(f'Voce perdeu! o computador escolheu {comp} e a soma foi {soma}')
            break


print(f'Voce perdeu com {cont} vitorias consecutivas')