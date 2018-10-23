# invoer
a = float(input('Getal 1: '))
b = float(input('Getal 2: '))

# uitvoer
resultaat_1 = str('{:>6.0f} + {:<6.0f}'.format(a, b) + ' = ' + str(int(a + b)))
resultaat_2 = str('{:>6.0f} + {:<6.0f}'.format(a * 10, b * 10) + ' = ' + str(int(a * 10 + b * 10)))
resultaat_3 = str('{:>6.0f} + {:<6.0f}'.format(a * 10 ** 2, b * 10 ** 2) + ' = ' + str(int(a * 10 ** 2 + b * 10 ** 2)))
resultaat_4 = str('{:>6.0f} + {:<6.0f}'.format(a * 10 ** 3, b * 10 ** 3) + ' = ' + str(int(a * 10 ** 3 + b * 10 ** 3)))
resultaat_5 = str('{:>6.0f} + {:<6.0f}'.format(a * 10 ** 4, b * 10 ** 4) + ' = ' + str(int(a * 10 ** 4 + b * 10 ** 4)))

print(resultaat_1)
print(resultaat_2)
print(resultaat_3)
print(resultaat_4)
print(resultaat_5)