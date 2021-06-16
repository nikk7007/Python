while True:
    n = int(input('Qual numer quer consultar a tabuada? '))

    if n < 0: break
    print('='*40)
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('='*40)