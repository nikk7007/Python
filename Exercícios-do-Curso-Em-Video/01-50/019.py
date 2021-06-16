import random

name1 = input('Qual o nome do primeiro aluno? ')
name2 = input('Qual o nome do segundo aluno? ')
name3 = input('Qual o nome do terceiro aluno? ')
name4 = input('Qual o nome do quarto aluno? ')

Nomes = [
    name1,
    name2,
    name3,
    name4
]

sorteado = random.choice(Nomes)
print('E o sorteado foi o {}'.format(sorteado))
