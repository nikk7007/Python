preco = float( input('Qual o valor do produto? ') )
fpagamento = input('Desja pagar em dinheiro ou cartão? ').strip().lower()

if fpagamento == 'dinheiro':
    print('Voce vai pagar: R${}'.format(preco - (preco * 0.1)))
else:
    fpagamento2 = input('Á vista ou em quantas vezes? ')
    if fpagamento2.isnumeric() == True:
        fpagamento2 = int(fpagamento2)
        if fpagamento2 == 2:
            print('Voce vai pagar: R${}'.format(preco))
        elif fpagamento2 >= 3:
            print('Voce vai pagar: R${}'.format(preco + (preco * 0.2)))
    
    else:
        print('Voce vai pagar: R${}'.format(preco - (preco * 0.05)))

