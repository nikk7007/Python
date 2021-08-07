matriz = []
maior = 0
for i in range(3):
    for c in range(3):
        n = int(input(f'Digite o valor [ {i}, {c} ]'))
        matriz.append(n)

for i in matriz:
    if i == matriz[3] or i == matriz[6]: print('\n')
    print(f'[ {str(i):^5} ] ', end='')
