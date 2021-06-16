n1 = int(input('Digite um valor para o inicio de uma progressão aritimetica '))
n2 = int(input('Agora digite o valor da razao '))
cont = 0
c = 10
i = -1

while i != c and c != 0:
    
    if i == 1: print(n1, end=' -> ')
    else: 
        print(n1 + n2, end=' -> ')
        n1 += n2
    
    cont += 1
    i += 1
    if i == c - 1:
        c = int(input('\nGostaria de ver quantos termos? '))
        i = -1
    
print(f'Voce viu no total {cont} termos da PA')
