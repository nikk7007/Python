a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
c = int(input('Digite um numero '))

menor = a
meio  = c
maior = b

# Verificando qual numero é menor
if a > b and c > b:
    menor = b
elif a > c and b > c:
    menor = c

# Verificando qual numero é maior
if b < a and c < a:
    maior = a
elif b < c and a < c:
    maior = c

# Vericando o numero do meio
if b < maior and b > menor:
    meio = b
elif a < maior and a > menor:
    meio = a

# Printando os numeros
print('O menor numero é:',  menor)
print('O numero do meio é:',  meio)
print('O maior numero é:',  maior)

