peso = float( input('Qual seu peso em kg? ') )
altura = float( input('Qual sua altura? ') )
imc = peso / ((altura / 100)**2)

print(imc)
if imc < 18.5:
    print( 'Abaixo do peso' )
elif imc < 25:
    print( 'Ideal' )
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
