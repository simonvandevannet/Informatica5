from math import sqrt

# invoer
x = float(input('x: '))

# uitvoer
if x == 2:
    print('2.00 is nulpunt van f')
elif x > 2:
    print('f(' + '{:.2f}'.format(x) + ') = ' + '{:.2f}'.format(sqrt(x - 2)))
else:
    print('{:.2f}'.format(x) + ' ∉ dom(f)')
