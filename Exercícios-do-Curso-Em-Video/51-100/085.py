numbers = []
pares = []
impares = []

for i in range(7):
    number = int(input('Digite um numero: '))
    if number  % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)

pares.sort()
impares.sort()
numbers.append(pares)
numbers.append(impares)

print(f'\nOs numeros foram: ', end='')
for c in numbers:
    for c1 in c:
        print(c1, end=' ')

print('\nOs impares foram ', end='')
for c in impares:
    print(c, end=' ')

print('\ne os pares foram ', end='')
for c in pares:
    print(c, end=' ')
