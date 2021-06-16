lista = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Caneta', 22.30,
            'Livros', 34.90)

for produtos in lista:
    ind = lista.index(produtos)
    if ind % 2 == 0 or ind == 0:
        print(f'{produtos:_<20}R$', end='')
    else:
        print(f'{produtos:0>6.2f}')


        