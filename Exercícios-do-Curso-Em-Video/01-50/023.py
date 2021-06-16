num = int(input('Digite uma numero até 9999 '))
num1 = str(num / 10000)

print('unidade: {}'.format(num1[5]))
print('dezena: {}'.format(num1[4]))
print('centena: {}'.format(num1[3]))
print('milhar: {}'.format(num1[2]))