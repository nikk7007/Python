from datetime import date 

ano = date.today().year
person = {}

person['nome'] = input('Nome: ')
person['idade'] = ano - int(input('Ano de nacimento: '))
person['ctps'] = int(input('Carteira de trabalho [ 0 se não tem ]: '))

if person['ctps'] > 0:
    person['contratação'] = int(input('Ano de contratação: '))
    person['salario'] = float(input('Salario: '))
    person['aposentadoria'] = person['idade']+ person['contratação'] + 35 - ano

for k, v in person.items():
    print(f'{k} tem o valor de {v}')
