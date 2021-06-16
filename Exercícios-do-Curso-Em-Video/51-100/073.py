times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional','Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 
        'Grêmio', 'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama', 'Cruzeiro', 'Fluminense', 'Chapecoence', 
        'CSA', 'Avaí')

cha = times.index('Chapecoence') + 1

# print(times[0:5])
for pri in range(0, 5):
    print(times[pri], end=', ')

print()

# print(f'\n{times[-4:]}')
for i in range(len(times) - 4, len(times)):
    print(times[i], end=', ')
    
print(f'\n\n{sorted(times)}')
print(f'A Chapecoence aparece em {cha}° posição')