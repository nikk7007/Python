n1 = int(input('Digite um valor para o inicio de uma progressão aritimetica '))
n2 = int(input('Agora digite o valor da razao '))

for i in range(n1, 10 * n2 + 1, n2):
    print(i, end=' → ')
