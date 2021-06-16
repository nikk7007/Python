from os import system
from colorama import Fore

verde = Fore.GREEN
azul  = Fore.CYAN
branco = Fore.WHITE
reset  = Fore.RED

def bhaskara():

    system('cls')
    print('{}{}{}'.format(azul, '#'*30, reset))

    a = float(input('a= {}'.format(azul))) 
    b = float(input('{}b= {}'.format(reset, azul))) 
    c = float(input('{}c= {}'.format(reset, azul))) 

    print('{}{}{}'.format(azul, '#'*30, branco))

    delta  = (b**2 - 4*a*c)
    rdelta = delta**(1/2)
    
    if delta < 0:
        print('Resultado VAZIO, delta é negativo')
    else:
        print('valor de delta:', delta)
        print('valor da raiz de delta:', rdelta)

        x1 = (0-b + rdelta) / (2 * a)
        x2 = (0-b - rdelta) / (2 * a)
        
        print(branco + 'X1: ', x1, end=' ||| ')
        print('X2 {} \n'.format(x2))

    reuse = input('{}Deseja reutilizar o programa? (s/n) {}'.format(azul, reset))
    system('cls')

    if reuse == 's':
        bhaskara()

bhaskara()
