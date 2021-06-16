from colorama import Fore
from os import system
system('cls')
color = Fore.YELLOW
reset = Fore.RESET

name = input('Qual seu nome inteiro? :'+ color).strip().title()
system('cls')

upper = name.upper()
lower = name.lower()
#numName = len(name.replace(' ', '')) ou
numName = len(name) - name.count(' ')
priName = name.split()

print(reset + 'Analizando seu nome...')

print('Seu nome é: {0}{1}{2}'.format(color, name, reset))
print('Seu nome em maiusculo: {}{}{}'.format(color, upper, reset))
print('Seu nome em minusculo: {}{}{}'.format(color, lower, reset))
print('Seu nome tem {}{}{} letras'.format(color, numName, reset))
print('Seu primeiro nome é: {0}{1}{2} e tem {0}{3}{2} letras'.format(color, priName[0], reset, len(priName[0])))