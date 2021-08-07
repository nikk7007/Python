from random import randint as ri

def maior(lst):
    snums = lst[:]
    snums.sort()
    print(f' o maior numero entre {lst} é {snums[-1]}')

nums = []
for c in range(0, ri(2, 4)):
    for i in range(ri(2, 10)):
        nums.append(ri(-50, 100))
    maior(nums)
    nums.clear()



