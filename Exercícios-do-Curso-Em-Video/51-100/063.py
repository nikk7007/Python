ant = 0
dep = 1

n = int(input('Quantos numeros quer ver? '))
i = 3
print(ant)
print(dep)
while i <= n:
    soma = ant + dep
    ant = dep
    dep = soma
    print(soma)
    i += 1
