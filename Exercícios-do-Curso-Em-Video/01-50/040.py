notas = input('Digite suas duas notas separando-as por uma virgula ')

nota = notas.split(',')
nota1, nota2 = float(nota[0]), float(nota[1])
# print('Sua primeira nota foi {} e a segunda {}'.format(nota1[0].strip(), nota1[1].strip()))

media = (nota1 + nota2) / 2
print(media)

if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROADO')

