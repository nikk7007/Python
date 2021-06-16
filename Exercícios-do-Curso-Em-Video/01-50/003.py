verde = '\033[0;32m'
blue = '\033[0;35m'
reset = '\033[0;37m'

n1 = int(input('{1}Digite um numero: {0}'.format(verde, blue)))
n2 = int(input('{1}Digite outro numero: {0}'.format(verde, blue)))

soma = n1 + n2
print(n1,'+', n2, '=', soma, reset)