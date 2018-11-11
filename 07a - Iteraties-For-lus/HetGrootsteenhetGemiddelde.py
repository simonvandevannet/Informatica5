# invoer
aantal_getallen = int(input('aantal getallen: '))
max = float(input('getal: '))
som = max

# berekening
for _ in range(aantal_getallen - 1):
    a = float(input('getal: '))
    if a > max:
        max = a
    som += a

gemiddelde = som / aantal_getallen

# uitvoer
print('Het grootste getal is {:.0f} en het gemiddelde is {:.2f}'.format(max, gemiddelde))