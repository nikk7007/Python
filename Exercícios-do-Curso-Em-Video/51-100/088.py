from random import randint as ri
from time import sleep

print('-'*30)
print(f'{"Mega sena":^30}')
print('-'*30)

quant = int(input('Quantos jogos voce quer sortear? '))
card = []

for i in range(quant):
    while len(card) != 6:
        number = ri(1, 60)
        if number not in card:
            card.append(number)

    sleep(.5)
    card.sort()
    print(f'O {i+1}° jogo sorteado foi: {card}')
    card.clear()


