from random import randint
from os import system

def program():

    system('cls')

    n = randint(1, 100)
    print('='*35)
    print('Um numero entre 1 e 100 foi gerado')
    print('descubra qual é o numero')
    print('='*35)

    def quest():
        global resp
        resp = int(input('Qual numero voce acha que é? '))

        if resp > n:
            print('Um pouco menos')
            quest()

        elif resp < n:
            print('Um pouco mais')
            quest()

        elif resp == n:
            print('Parabens, voce acertou')
        
    def reuse():
        reuse = input('Deseja reutilisar o programa? (s/n)').lower()
        if reuse == 's':
            program()
    
    
    quest()
    reuse()

program()
