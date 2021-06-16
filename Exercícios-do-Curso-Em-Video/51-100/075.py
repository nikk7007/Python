numbers = ( int( input('Digite um numero ')),
            int( input('Digite um numero ')),
            int( input('Digite um numero ')),
            int( input('Digite um numero ')))
               
print(numbers)

print(f'O numero 9 aparece {numbers.count(9)} vezes')

if 3 in numbers:
    print(f'O numero 3 aparece na {numbers.index(3) + 1}ª posição')
else: 
    print('O numero 3 nao aparece em nenhum lugar')

print(f'Os numeros pares digitados foram: ', end='')
for q in numbers:
    if q % 2 == 0:
        print(q, end=' ')
