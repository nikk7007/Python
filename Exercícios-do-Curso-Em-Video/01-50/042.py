a = float(input('Digite o primeiro lado do triangulo '))
b = float(input('Digite o segundo lado do triangulo '))
c = float(input('Digite o terceiro lado do triangulo '))

# Printando se as retas formam um triangulo
if a + b > c and a + c > b and b + c > a:
    print('Forma triangulo')
 
    if a == b == c:
        print('Equilatero')
    elif a == b != c or a == c != b or b == c != a:
        print('Isoceles')
    elif a != b != c != a:
        print('Escaleno')

else:
    print('NÃO forma trianguo')
