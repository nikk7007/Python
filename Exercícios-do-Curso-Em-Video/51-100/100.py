from random import randint as ri

nums = []

def sortear(numero):
    for i in range(numero):
        nums.append(ri(1, 10))
    print(f'Numeros sorteados: {nums}')


def somar(lst):
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    print(f'A soma dos numero pares é {s}')


sortear(5)
somar(nums)
 