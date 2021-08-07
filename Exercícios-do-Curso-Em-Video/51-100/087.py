matriz = []
soma = 0
soma2 = 0
maior = 0
for l in range(3):
    for c in range(3):
        n = int(input(f'Digite o valor [ {l}, {c} ]'))
        matriz.append(n)
        if c == 2: soma2 += n
        if l == 1:
            if c == 0:
                maior = n
            elif n > maior:
                maior = n

for i in matriz:
    if i == matriz[3] or i == matriz[6]: print('\n')
    if i % 2 == 0: soma += i
    print(f'[ {i:^5} ] ', end='')

print(f'\nA soma dos numeros pares {soma}')
print(f'A soma da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {maior}')
