preco = float(input('Qual o preco da camiseta? R$'))
desconto = int(input('Quanto ela tem de desconto em porcentagem? R:')) / 100

precoFinal = preco - (preco * desconto) 
print('O preco dela com o desconto e: R${}'.format(precoFinal))