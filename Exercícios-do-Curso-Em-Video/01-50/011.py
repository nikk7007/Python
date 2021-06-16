h = float(input('Qual a altura da sua parede? R:'))
w = float(input('E a largura? R:'))

parede = h * w
tinta = parede / 2

print('Sua parede tem {}m²'.format(parede))
print('Ela vai precisar de {}l de tinta'.format(tinta))