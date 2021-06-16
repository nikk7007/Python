c = s = 0

while True:
    n = int(input('Digite um valor [0 para parar]: '))
    if n == 0:
        break
    c += 1
    s += n

print(f'Foram digitados {c} valores e a soma entre eles foi {s}')