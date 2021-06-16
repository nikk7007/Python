frase = input('Digite uma frase qualquer ').strip().lower()
print('A letra a aparece', frase.count('a'), 'vezes')
print('A letra a aprece pela primeira vez como a', frase.find('a') + 1, 'letra')
print('A letra a aprece pela urtima vez como a', frase.rfind('a') + 1, 'letra')