import math
deg = math.radians(float(input('Quntos graus tem o angulo? ')))

seno = math.sin(deg)
coss = math.cos(deg)
tang = math.tan(deg)

print('O seno do angulo é {}, o cosseno {} e a tangente {}'.format(seno, coss, tang))
