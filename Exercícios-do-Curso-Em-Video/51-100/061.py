n1 = int(input('Digite um valor para o inicio de uma progressão aritimetica '))
n2 = int(input('Agora digite o valor da razao '))
i = 0

while i != 10:
    if i == 0:
        print(n1, end=' → ')
    else:
        print(n1 + n2, end=' → ')
        n1 += n2

    i += 1
