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



# oplossing
aantal = int(input('aantal'))

grootste = int(input('getal: '))
som = grootste

for i in range(aantal - 1):
    getal = int(input('getal: '))
    som += getal
    if(getal > grootste):
        grootste = getal

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste, som / aantal))

# bij grootste of kleinste steeds een getal voor de lus inlezen
