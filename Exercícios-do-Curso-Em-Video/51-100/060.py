n = int(input('Qual numero quer saber o fatorial? '))
# for i in range(n-1, 0, -1):
#     n *= i
# print(n)

i = n - 1
while i != 0:
    n *= i
    i -= 1
print(n)   
