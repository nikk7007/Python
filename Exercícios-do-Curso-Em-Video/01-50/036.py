valCasa = float( input( 'Qual o valor da casa? R$' ) )
salario = float( input( 'Qual seu salario? R$' ) )
anos = float( input( 'Em quantos anos deseja pagar? ' ) )
meses  = anos * 12
valMes = valCasa / meses

if valMes <= (salario * (30 / 100)):
    print('Ok, o valor mensal sera de R$', valMes)
elif valMes > (salario * (30 / 100)):
    print('Negado, a parcela exedaria 30% de seu salario, a parcela seria de R$', valMes)
