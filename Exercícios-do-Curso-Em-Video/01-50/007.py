notam = float(input('Sua nota mensal: '))
notab = float(input('Sua nota bimestral: '))
media = (notam + notab) / 2
print()

if media >= 7:
    print('Parabens voce passou!!!')

else:
    print('Puts, nao foi dessa vez')

print('Media: {}'.format(media))