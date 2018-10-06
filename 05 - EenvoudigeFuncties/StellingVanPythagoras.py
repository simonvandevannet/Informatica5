from math import sqrt

# invoer
a = float(input('a: '))
b = float(input('b: '))

# berekening
c = sqrt(a ** 2 + b ** 2)

# uitvoer
resultaat = str('In een rechthoekige driehoek met rechthoekszijden a = ')
resultaat += str('{:.2f}'.format(a))
resultaat += str(' en b = ')
resultaat += str('{:.2f}'.format(b))
resultaat += str(' is de schuine zijde ')
resultaat += str('{:.2f}'.format(c))

print(resultaat)