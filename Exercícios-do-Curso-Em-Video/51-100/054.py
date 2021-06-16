ma = 0 
me = 0
 
for i in range(0, 6):
    ano = int(input('Que ano a pessoa nasceu '))
    age = 2021 - ano
    if age < 18:
        me += 1
    else:
        ma += 1
    
print('Tem {} pessoas jovens e {} mais velhas'.format(me, ma))
