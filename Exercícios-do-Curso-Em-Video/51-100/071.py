print('='*30)
print(f'{"Banco do Nik":^30}')
print('='*30)

val = int(input('Quanto dinheiro voce quer retirar? R$'))
tot = val
ced = 50
totced = 0

while True:
    if tot >= ced:
        tot -= ced 
        totced += 1
    else:
        if totced != 0:
            print(f'O tota de cedulas de R${ced} é igual a {totced}')
        totced = 0

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if tot == 0:
            break
