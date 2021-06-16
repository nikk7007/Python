nameVelho = 0
ageVelho = 0
sexoVelho = 0

mediaAge = 0
cont = 0
# ==============

for i in range(1, 5):
    print(f'===== {i}ª Pessoa =====')
    name = input('Nome: ').strip().title()
    age = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip().lower()

    mediaAge += age

    if sexo == 'm' and age > ageVelho:
        nameVelho = name
        ageVelho = age

    if sexo == 'f' and age <= 20:
        cont += 1


print(f'\nA media das idades é de {mediaAge / 4}')
print(f'O homem mais velho é {nameVelho} que tem {ageVelho} anos')
print(f'Tem {cont} mulheres mais novas que 20 anos')
