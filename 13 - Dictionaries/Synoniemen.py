def synoniemen(zin, synoniemen):

    zin = zin.split()

    for i in range(len(zin)):

        if zin[i] in synoniemen:
            zin[i] = synoniemen.get(zin[i])

    zin = ' '.join(zin)

    return zin

print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))