# pip install colorama
from os import system as sy
from colorama import Fore

cinza    = Fore.LIGHTBLACK_EX
azul     = Fore.CYAN
roxo     = Fore.LIGHTMAGENTA_EX
verde    = Fore.LIGHTGREEN_EX
alert    = Fore.RED
reset    = Fore.RESET

def line(cor):
    print(cor + '#'*30 + reset)


while True:
    sy('cls')
    line(azul)

    # Validação para a, b, c com certeza serem números
    while True:
        a = input(f'{verde}a = {reset}').strip()
        b = input(f'{verde}b = {reset}').strip()
        c = input(f'{verde}c = {reset}').strip()

        if a.isnumeric() == True and b.isnumeric() and c.isnumeric():
            a = float(a)
            b = float(b)
            c = float(c)
            break

        sy('cls')
        line(azul)
        print(f'{alert}ERROR. Por favor, digite apenas NUMEROS')

    line(azul)

    # Calculando delta e raiz de delta
    d  = b**2 - 4*a*c
    rd = d**.5

    print(roxo, end='')
    if d < 0:
        print(f'Delta negativo, resultado VAIZIO')

    else:
        # Calculando x1 e x2
        x1 = (0-b + rd) / (2 * a) 
        x2 = (0-b - rd) / (2 * a) 

        print(f'Valor de delta: {d}')
        print(f'Valor da raiz de delta: {rd}')
        print(f'x1: {x1} ||| x2: {x2}')
        
    while True:
        reuse = input(f'Quer usar o programa novamente? [s/n]:{reset} ').strip().lower()[0]
        if reuse in 'sn':
            break
    
    if reuse == 'n':
        sy('cls')
        break
