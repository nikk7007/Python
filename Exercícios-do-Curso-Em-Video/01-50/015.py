dias = int(input('Quantos dias você alugou o carro? R:'))
km = float(input('Quantos km você percorreu com o carro? R:'))

# R$60 por dia e R$0,15 por km
preco = (dias * 60) + (km * 0.15)
print('Você tera de pagar R${}'.format(preco))