soma = 0
for i in range(0, 6):
    n = int(input('Digite um valor '))
    if n % 2 != 0:
        n = 0 
    soma += n
print(soma)
