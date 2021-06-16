
totpreco = cmmil = i = 0
print('='*40)
print('Carrinho de compras inteligente')
while True:
    print('='*40)
    name = input('Nome do produto ')
    preco = float(input('Preço do produto '))
    totpreco += preco
    if preco > 1000:
        cmmil += 1
    if i == 0 or menorp > preco:
        menorp = preco
        menorn = name

    while True:
        continuar = input('Deseja continuar? [s/n] ').lower().strip()[0]
        if continuar in 'sn':
            break
    if continuar == 'n':
        break
    i += 1
    
print('\n' + '='*50)
print(f'O produto mais barato foi o {menorn} custando R${menorp}')
print(f'Tiveram {cmmil} que custaram mais que R$1000')
print(f'Tudo ficou por R${totpreco}')
