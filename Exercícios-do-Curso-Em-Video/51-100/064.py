n = 0
c = 0
s = 0


while n != 999:
    n = int(input('Digite um valor[999 para parar] '))
    if n != 999:
        c += 1
        s += n

print('vc saiu do loop')
print(f'vc enviou {c} numeros e a soma entre eles é {s}')
