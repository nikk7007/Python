frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')

for palavras in frutas:
    # print('\n' + palavras, end=' -> ')
    print(f'\n{palavras:<7}', end=' -> ')
    for letras in palavras:
        if letras.lower() in 'aáàãâäeéèêëiíìîïoóòôõöuúûùü':print(letras, end=' ')

