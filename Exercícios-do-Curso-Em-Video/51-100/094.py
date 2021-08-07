from os import system as sy
sy('cls')
people = []
mulheres = []
totalAge = 0

# Cadastrando pessoas
while True:
    person = {}
    person['name'] = input(f'Nome: ').strip().title()
    while True:
        person['sexo'] = input(f'Sexo [M/F]: ').strip().lower()[0]
        if person['sexo'] in 'mf':
            break
        print(f'ERRO, "{person["sexo"]}" não é um sexo valido. Tente novamente')
    
    if person['sexo'] == 'f':
        mulheres.append(person['name'])
    
    person['age' ] = int(input(f'Idade: ').strip())
    totalAge += person['age']

    people.append(person.copy())
    person.clear()

    while True:
        con = input(f'Deseja continuar? [S/N] ').strip().lower()[0]
        if con in 'sn':
            break
        print(f'ERRO, "{con}" não é valido, por favor digite apenas "s" ou "n". Tente novamente')
    if con == 'n':
        sy('cls')
        break

# Printando informações
print(f'\n- O grupo tem {len(people)} pessoas')

print(f'- A media de idade é de {totalAge / len(people)}')

print(f'- As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m, end=', ')

print(f'\nLista das pessoas acima da media de idade:')
for person in people:
    if person['age'] > totalAge / len(people):
        print('\n  ', end='')
        for k, v in person.items():
            print(f'{k} => {v}; ', end='')
