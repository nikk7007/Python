from random import choice
jokenpo = ['pedra', 'papel', 'tesoura']
comp = choice(jokenpo)
usr = input('Pedra, papel ou tesoura? ').strip().lower()

print('O computador escolheu:', comp)
if usr == 'pedra':
    if comp == 'papel':
        print('Vitoria do computador')
    elif comp == 'pedra':
        print('Empate')
    else:
        print('Vitoria do humano')
elif usr == 'papel':
    if comp == 'tesoura':
        print('Vitoria do computador')
    elif comp == 'papel':
        print('Empate')
    else:
        print('Vitoria do humano')
else:
    if comp == 'pedra':
        print('Vitoria do computador')
    elif comp == 'tesoura':
        print('Empate')
    else:
        print('Vitoria do humano')
