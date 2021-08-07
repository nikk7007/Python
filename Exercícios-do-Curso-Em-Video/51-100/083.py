expr = input('Digite sua expreção: ')
cont = 0 
for e in expr:
    if e == '(':
        cont += 1
    elif e == ')':
        cont -= 1

if cont > 0:
    print(f'Expreção errada, tem {cont} ")" faltando')
elif cont < 0:
    print(f'Expreção errada, tem {cont + (cont * -2)} "(" faltando')
else:
    print('Expreção valida!')

