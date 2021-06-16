from base64 import b64encode, b64decode
from colorama import Fore
from os import system

cor1  = Fore.CYAN
cor2  = Fore.LIGHTGREEN_EX
cor3  = Fore.LIGHTBLACK_EX
alert = Fore.RED
reset = Fore.RESET

while True:
    system('cls')

    print(cor3 + '='*20)
    print('{} [ 1 ] Encriptar\n [ 2 ] Decriptar{}'.format(cor1, cor3))
    print('='*20 + cor2)

    usr = int(input(f'{cor1}O que quer fazer? [1/2] {cor3}'))

    if usr == 1 or usr == 2:
        if usr == 1:
            usrencode = input(f'{cor2}O que quer encriptar? {cor3}').strip().encode()
            code = b64encode(usrencode).decode()
        elif usr == 2:
            usrencode = input(f'{cor2}O que quer encriptar? {cor3}').strip().encode()
            code = b64decode(usrencode).decode()
        print(cor1+code+cor2)
    else:
        print(f'{alert}comando invalido{reset}')
    
    reuse = input(f'{reset}Deseja reutilizar? [S/N]{cor3} ').strip().lower()[0]
    if reuse == 'n': break
    
