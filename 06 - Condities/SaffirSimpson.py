# invoer
windsnelheid = int(input('Windsnelheid: '))

#uitvoer
if windsnelheid >= 119 and windsnelheid <= 153:
    print('categorie 1')
elif windsnelheid >= 154 and windsnelheid <= 177:
    print('categorie 2')
elif windsnelheid >= 178 and windsnelheid <= 209:
    print('categorie 3')
elif windsnelheid >= 210 and windsnelheid <= 249:
    print('categorie 4')
elif windsnelheid >= 250:
    print('categorie 5')
else:
    print('geen orkaan')