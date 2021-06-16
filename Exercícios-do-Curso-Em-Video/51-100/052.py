n = int(input('Digite um valor: '))
p = 0

for i in range(1, n+1):
    if n % i == 0:
        p += 1
        print(i, end=' ')

if p > 2:
    print('\n{} não é primo!\nele é divisivel {} vezes'.format(n, p))
else:
    print('{} é primo!'.format(n))