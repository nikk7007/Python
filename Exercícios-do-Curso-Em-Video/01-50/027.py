name = input('Qual seu nome ').strip().title()
name1 = name.split()
lenName = len(name1)

print('Seu primeiro nome é: ' + name1[0])
print('Seu ultimo nome é: ' + name1[lenName - 1])
