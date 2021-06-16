c = 0
s = 0
maior = 0
menor = 0
usr = ''


while usr != 'n':
    n = int(input('Digite um valor '))
    if c == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    c += 1
    s += n
    usr = input('Deseja continuar? [S/N] ').strip().lower()

print(f'A media dos numeros digitados foi {s / c}')
print(f'O maior numero foi {maior} e o menor {menor}')
