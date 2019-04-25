def woord_frequentie(zin):
    dictionary = {}
    zin = zin.split()
    for i in range(len(zin)):
        zin[i] = zin[i].lower()
        if '.' in zin[i] or ',' in zin:
            zin[i] = zin[i][0: -1]
    for i in range(len(zin)):
        if zin[i] in dictionary:
            dictionary[zin[i]] += 1
        else:
            dictionary[zin[i]] = 1

    return dictionary

def woorden_per_frequentie(zin):
    dictionary = {}
    frequentie = woord_frequentie(zin)
    for woord in frequentie:
        if woord not in dictionary:
            dictionary[frequentie[woord]] = [woord]
        else:
            dictionary[frequentie[woord]] = dictionary[frequentie[woord]].append(frequentie[woord])

    return dictionary


print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))