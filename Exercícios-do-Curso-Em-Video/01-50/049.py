n = int(input('Qual numero deseja consultar a tabuada? '))

print('-'*12)
for i in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, i, n*i))
print('-'*12)
