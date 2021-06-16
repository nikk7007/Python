a = float(input('Digite o primeiro lado do triangulo '))
b = float(input('Digite o segundo lado do triangulo '))
c = float(input('Digite o terceiro lado do triangulo '))

# Definido e identificando
menor = a
meio  = b
maior = c

# Definido quem é o menor
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Definindo quem é o manior
if b > a and b > c:
    maior = b
elif a > b and a > c:
    maior = a

# Definindo quem é o do meio
if a > menor and a < maior:
    meio = a
elif c > menor and c < maior:
    meio = c

# Printando se as retas formam um triangulo
if meio + menor > maior:
    print('Forma triangulo')
else:
    print('NÃO forma trianguo')

print(maior)
print(meio)
print(menor)
