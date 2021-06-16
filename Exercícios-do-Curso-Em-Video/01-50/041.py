from datetime import date
ano = int(input('Qual o ano de nascimento? '))

age = date.today().year - ano

if age <= 9:
    print('Mirim')
elif age <= 14:
    print('Infantil')
elif age <= 19:
    print('Junior')
elif age <= 20:
    print('Senior')
else:
    print('Master')
