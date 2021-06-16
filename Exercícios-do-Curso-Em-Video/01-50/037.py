n = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão
[0]Converter para Binario
[1]Converter para Octal
[2]Converter para Hexadecimal
[3]Converter para todas
''')

option = int(input('Sua opção: '))

if option == 0:
    print('{} em binario é: {}'.format(n, bin(n)))
elif option == 1:
    print('{} em octal é: {}'.format(n, oct(n)))
elif option == 2:
    print('{} em hexadecimal é: {}'.format(n, hex(n)[2:]))
elif option == 3:
    print('{} em binario é: {}'.format(n, bin(n)[2:]))
    print('{} em octal é: {}'.format(n, oct(n)))
    print('{} em hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!')


