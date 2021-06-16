# num = int(input('Digite um numero '))
# num = str(num)
# len = len(num) - 1

# if num[len] == '2':
#     print('par') 
# elif num[len] == '4':
#     print('par') 
# elif num[len] == '6':
#     print('par') 
# elif num[len] == '8':
#     print('par') 
# elif num[len] == '0':
#     print('par') 
# else:
#     print('impar')

#   OU 

num = int(input('Digite um numero '))
ide = num % 2 # ToDO NUMERO IMPAR DIVIDIDO POR 2 RESTA 1 

if ide == 0:
    print('Par')

else:
    print('Impar')
