prijs = float(input('prijs artikel: '))
totaalprijs = 0

while prijs > 0:
    totaalprijs += prijs
    prijs = float(input('prijs artikel: '))

print('De totale prijs is € {:.2f}'.format(totaalprijs))