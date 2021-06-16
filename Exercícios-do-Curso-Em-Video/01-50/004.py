print()
algo = input('Digite qualquer coisa: ')

print()
#print(algo, 'e um numero?', algo.isnumeric())

if algo.isnumeric() == True:
    print(algo, 'é um numero!')

elif algo.isalpha() == True:
    print(algo, 'é uma palavra!')

elif algo.isspace() == True:
    print(algo, 'é espaço!')