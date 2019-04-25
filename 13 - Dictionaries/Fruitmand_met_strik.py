def fruitmand_maken(lijst):

    fruitmand = {}

    for i in range(len(lijst)):
        fruitmand[len(lijst[i])] = lijst[i]

    return fruitmand

def fruitmand_inpakken(fruitmand):
    lengtes = []
    ingepakt = []
    for key in fruitmand.keys():
        lengtes.append(key)
    lengtes.sort()
    for i in range(len(lengtes)):
        ingepakt.append(fruitmand[lengtes[i]])

    return ingepakt

print(fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))
print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))