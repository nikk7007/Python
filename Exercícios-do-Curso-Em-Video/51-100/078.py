numbers = list()

for cont1 in range(0, 3):
    numbers.append(int(input(f'Digite o valor para a posiçao {cont1}: ')))

print(f'Os valores digitados foram {numbers}')

maior = max(numbers)
menor = min(numbers)

print(f'O menor numero foi {menor} nas posições', end=' ')
for i1, val1 in enumerate(numbers):
    if val1 == menor:
        print(f'{i1}...', end=' ')

print(f'\nO maior numero foi {maior} nas posições', end=' ')
for i2, val2 in enumerate(numbers):
    if val2 == maior:
        print(f'{i2}...', end=' ')
