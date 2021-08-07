jogador = {}

jogador['name'] = input('Qual o nome do jogador? ').strip().title()
p = int(input(f'Quantos jogos {jogador["name"]} jogou? ').strip())

jogador['gols'] = []
jogador['total'] = 0

for i in range(1, p + 1):
    g = int(input(f'Quantos gols {jogador["name"]} fez no jogo {i}? ').strip())

    jogador['gols'].append(g)
    jogador['total'] += g

print(f'O jogador {jogador["name"]} fez {jogador["total"]} gols em {len(jogador["gols"])} jogos')

for k, v in enumerate(jogador['gols']):
    print(f'    No jogo {k + 1} fez {v} gols')
