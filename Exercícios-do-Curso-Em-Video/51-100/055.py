maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é de {maior}Kg e o menor de {menor}Kg')
