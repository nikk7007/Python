from datetime import date

ano = int(input('Que ano quer analizar? ou digite 0 para o ano atual '))

if ano == 0:
    print(date.today().year)
    ano = int(date.today().year)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não bissexto')
