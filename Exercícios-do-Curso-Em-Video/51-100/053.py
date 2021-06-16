frase = input('Digite um frase ').strip().lower()
junto = frase.replace(' ', '')
inverso = junto[::-1]
# inverso = ''
# for l in range(len(junto) -1, -1, -1):
#     inverso += junto[l]

if junto != inverso:
    print('Nhe')
else:
    print('Isso é um palindromo!!!')

print('Normal: ', junto)
print('Inverso:', inverso)
# print(inverso)