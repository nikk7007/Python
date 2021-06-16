vel = int(input('Qual sua velocidade? '))

if vel > 80:
    print('Sua multa é de: R$' + str(7 * (vel - 80)))

else:
    print('Continue assim')
