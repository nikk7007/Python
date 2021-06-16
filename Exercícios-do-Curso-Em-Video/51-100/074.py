from random import randint

numbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

# menor = maior = numbers[0]
# for i in numbers:
#     print(i, end=' ')
#     if   i > maior: maior = i
#     elif i < menor : menor = i
# maior = sorted(numbers)[4]
# menor = sorted(numbers)[0]
maior = max(numbers)
menor = min(numbers)

print(numbers)
print(f'\nO maior numero é {maior} e o menor {menor}')

