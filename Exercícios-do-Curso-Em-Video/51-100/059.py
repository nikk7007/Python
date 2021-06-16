usr = ''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('[1] Somar \n[2] Multiplicar\n[3] Maior \n[4] Novos numeros \n[5] Sair do programa\n')

while usr != 5:
    usr = int(input('\nQual ação deseja fazer? '))

    if usr == 1:
        print(n1 + n2)
    elif usr == 2:
        print(n1 * n2)
    elif usr == 3:
        if n1 < n2:
            print(n2)
        elif n1 > n2:
            print(n1)
        else:
            print('Sao iguais')
    elif usr == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
            
