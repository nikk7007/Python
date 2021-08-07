jogadores = []

while True:
    jogador = {}
    jogador['name']  = input('Qual o nome do jogador? ').strip().title()
    jogador['jogos'] = int(input(f'Quantos jogos {jogador["name"]} jogou? ').strip())
    jogador['gols'] = []
    jogador['totalg'] = 0

    for i in range(1, jogador['jogos'] + 1):
        g = int(input(f'Quantos gols {jogador["name"]} fez no jogo {i}? ').strip())

        jogador['gols'].append(g)
        jogador['totalg'] += g

    jogadores.append(jogador.copy())
    jogador.clear()

    con = input('Quer continuar? [s/n] ').strip().lower()[0]
    if con == 'n':
        break

print('='*25)
print("{:<5}{:^10}{}".format('cod', 'nome', 'total'))
print('='*25)
for cod, person in enumerate(jogadores):
    print('{:<5}{:^10}{:^5}'.format(cod, person['name'], person['totalg']))

while True:
    who = int(input(f'Digite o codigo do jogador que deseja ver: ').strip())

    if who < len(jogadores):
        print(f'Jogador {jogadores[who]["name"]} selecionado')
        for k, v in enumerate(jogadores[who]['gols']):
            print(f'  No jogo {k+1} ele fez {v}')
        
    elif who == 999:
        break
    else:
        print('ERRO jogador inesistente')
