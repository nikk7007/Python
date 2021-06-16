salario = int(input('Qual o seu salario? R$'))

if salario <= 1250:
    salarioAumento = salario + (salario * (15 / 100))

else:
    salarioAumento = salario + (salario * (10 / 100))

print('Novo Salario: R${}'.format(salarioAumento))
