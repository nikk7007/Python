salario1 = float(input('Qual seu salario atual? R$'))
aumento  = float(input('Quanto foi seu aumento? ')) / 100

salario2 = salario1 + (salario1 * aumento)
print('Seu salario era R${:.2f}, mas com o aumento de {:.0f}%, agora e: R${:.2f}'.format(salario1, (aumento * 100), salario2))
