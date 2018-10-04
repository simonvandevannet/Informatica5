# invoer
x = float(input('x: '))
y = float(input('y: '))

# uitvoer
linkerlid = abs(abs(x) - abs(y))
rechterlid = abs(x - y)

print('{:.4f} ≤ {:.4f}'.format(linkerlid, rechterlid))