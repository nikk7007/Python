from random import randint as ri
from time import sleep
from operator import itemgetter
players = {}

for i in range(1, 5):
    jog = 'Jogador-' + str(i)
    players[jog] = ri(1, 6)

print('Valores sorteados:')
for k, v in players.items():
    print(f'    {k} tirou {v}')
    sleep(.3)

# Ordenando o dicionario
sortp = dict(sorted(players.items(), key=itemgetter(1), reverse=True))

print('Ranking dos jogadores:')
for k, v in sortp.items():
    print(f'    {k} tirou {v}')
