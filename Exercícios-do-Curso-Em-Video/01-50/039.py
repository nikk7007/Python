from datetime import date
ano = int(input('Que ano voce nasceu? '))
age = date.today().year - ano

if age < 18:
    print('Falta {} anos para voce se alistar, sera no ano {}'.format(18 - age, (18 - age) + (age + ano)))
elif age == 18:
    print('Esta na hora de voce se alistar')
else:
    print('Voce ja se alistou faz {} anos'.format(age - 18))
  