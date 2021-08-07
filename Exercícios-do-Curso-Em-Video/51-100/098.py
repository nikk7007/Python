from time import sleep

def cont(i, f, p):
    if p == 0:
        p = 1
    elif i < f:
        f += 1
        if p < 0:
            p *= -1
        
    elif i > f:
        f -= 1
        if p > 0:
            p *= -1

    print(f'\ncontagem de {i} até {f} de {p} em {p}:')

    for c in range(i, f, p):
        print(c, end=' => ', flush=True)
        sleep(.2)
    

cont(1, 10, 1)
cont(10, 0, 2)

print('\nAgora é sua vez de personalizar!')

ini = int(input('Inicio: ').strip())
fim = int(input('Fim:    ').strip())
pas = int(input('Passo:  ').strip())
cont(ini, fim, pas)

