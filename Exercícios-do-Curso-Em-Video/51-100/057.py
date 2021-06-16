sexo = input('Qual seu sexo [M/F]? ').lower()
veri = sexo in 'mf'
while veri == False:
    sexo = str(input('Qual seu sexo [M/F ]? ')).lower()
    veri = sexo in 'mf'
