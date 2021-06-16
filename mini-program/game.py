from random import randint
from os import system as sy

while True:

    sy('cls')
    usr = ''
    comp = randint(1, 10)
    print('# ================================= #')
    print('# Um numer entre 1 e 10 foi gerado, #')
    print('# descubra qual é o numero          #')
    print('# ================================= #')

    while usr != comp:
        usr = int(input('# Qual é o numero? '))
        if usr < comp:
            print('# Mais... ')
        elif usr > comp:
            print('# Menos...')
    
    print(f'Parabens vc consegiu, o numero era {comp}')
    program = input('Precione enter para jogar novamente ou q para sair ').lower()
    if program == 'q': 
        sy('cls')
        break
