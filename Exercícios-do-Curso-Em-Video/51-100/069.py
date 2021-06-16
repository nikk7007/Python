more18 = m20 = man = 0
while True:
    print('='*30)
    
    while True:
        sexo = continuar = ' '
        age  = input('Quantos anos? ').strip()
        if age.isnumeric() == True:
            age = int(age)
            break
        
    while sexo not in 'mf':
        sexo = input('Qual o sexo? [M/F] ').lower().strip()[0]

    print('='*30)

    if age > 18: more18 += 1
    if sexo == 'm': man += 1
    if sexo == 'f' and age < 20: m20 += 1

    while continuar not in 'sn':
        continuar = input('Quer continuar? [s/n] ').strip().lower()[0]

    if continuar == 'n': break

print(f'Tem {man} homens, {more18} pessoas com mais de 18 anos e {m20} mulheres com menos de 20')

