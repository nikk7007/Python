aluno = {}
aluno['name'] = input('Nome: ').strip().title()
aluno['media'] = float(input(f'Média de {aluno["name"]}: '))

if aluno['media'] < 7:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'aprovado'
    
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


